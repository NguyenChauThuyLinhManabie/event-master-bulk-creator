import requests
import concurrent.futures

# Salesforce API Credentials
ACCESS_TOKEN = "00DGA000009JzOD!ARgAQBGal2HUJjg5intwmSBKjgKwfWLsc9NFtqKc7.ACd.XFllbVi86UxUtjUKTIayYfTnpSciVqo_fFr_zgDT7QeWxmWIRK"
INSTANCE_URL = "https://pre-prod-manabie.my.salesforce.com"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Function to fetch paginated data
def fetch_data(query):
    records = []
    url = f"{INSTANCE_URL}/services/data/v63.0/query/?q={query}"
    
    while url:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Kiểm tra lỗi HTTP
            data = response.json()

            if isinstance(data, list):  # Nếu data là list, lấy phần tử đầu tiên
                data = data[0]

            if "records" in data:
                records.extend(data["records"])

            url = data.get("nextRecordsUrl")
            if url:
                url = f"{INSTANCE_URL}{url}"

        except Exception as e:
            print(f"Error fetching data: {e}")
            break

    return records

# Fetch students from Contact
def fetch_students():
    query = "SELECT Id FROM Contact WHERE MANAERP__Record_Type_Name__c = 'Student' AND IsDeleted = false"
    return fetch_data(query)

# Fetch enrollments with Student and Location
def fetch_enrollments():
    query = "SELECT MANAERP__Student__c, MANAERP__Location__c FROM MANAERP__Enrollment__c WHERE IsDeleted = false"
    return fetch_data(query)

# Fetch event master target locations
def fetch_event_locations():
    query = """
    SELECT MANAERP__Location__c FROM MANAERP__Event_Master_Target_Location__c
    WHERE MANAERP__Event_Master__c IN (
        SELECT Id FROM MANAERP__Event_Master__c
        WHERE Name LIKE '%Verify epic LT-73558 Part 1 with 1k event master%'
    )
    """
    return fetch_data(query)

# Multi-thread execution
with concurrent.futures.ThreadPoolExecutor() as executor:
    future_students = executor.submit(fetch_students)
    future_enrollments = executor.submit(fetch_enrollments)
    future_event_locations = executor.submit(fetch_event_locations)
    
    students = future_students.result()
    enrollments = future_enrollments.result()
    event_locations = {rec["MANAERP__Location__c"] for rec in future_event_locations.result() if "MANAERP__Location__c" in rec}

# Store Student ID and corresponding Locations
student_location_pairs = {(rec["MANAERP__Student__c"], rec["MANAERP__Location__c"]) for rec in enrollments if "MANAERP__Student__c" in rec and "MANAERP__Location__c" in rec}

# Check which students can see the event
students_with_access = [s_id for s_id, loc in student_location_pairs if loc in event_locations]

# Print results
print(f"Total Students: {len(students)}")
print(f"Total Enrollments: {len(enrollments)}")
print(f"Unique Student-Location Pairs: {len(student_location_pairs)}")
print(f"Students who can see the event: {len(students_with_access)}")
