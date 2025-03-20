import requests
import json

# ⚠️ Thay thế ACCESS_TOKEN mới để tránh lộ dữ liệu
ACCESS_TOKEN = "y00DGA000009JzOD!ARgAQOsAs1IKn4bCcqv.y9oVAWgn7yP.oJPQtci5MmWD9M74xvIOBLOIf.FWiP2biJy7RxLqOhSwHPSWfhTmfh3XIG1ClhJ2"
INSTANCE_URL = "https://pre-prod-manabie.my.salesforce.com"

# Danh sách Event_Master ID cần cập nhật
event_master_ids = [
    "a32GA000002ZoheYAC",
  "a32GA000002ZohfYAC",
  "a32GA000002ZohgYAC",
  "a32GA000002ZohhYAC",
  "a32GA000002ZohiYAC",
  "a32GA000002ZohjYAC",
  "a32GA000002ZohkYAC",
  "a32GA000002ZohlYAC",
  "a32GA000002ZohmYAC",
  "a32GA000002ZohnYAC",
  "a32GA000002ZohoYAC",
  "a32GA000002ZohpYAC",
  "a32GA000002ZohqYAC",
  "a32GA000002ZohrYAC",
  "a32GA000002ZohsYAC",
  "a32GA000002ZohtYAC",
  "a32GA000002ZohuYAC",
  "a32GA000002ZohvYAC",
  "a32GA000002ZohwYAC",
  "a32GA000002ZohxYAC",
  "a32GA000002ZohyYAC",
  "a32GA000002ZohzYAC",
  "a32GA000002Zoi0YAC",
  "a32GA000002Zoi1YAC",
  "a32GA000002Zoi2YAC",
  "a32GA000002Zoi3YAC",
  "a32GA000002Zoi4YAC",
  "a32GA000002Zoi5YAC",
  "a32GA000002Zoi6YAC",
  "a32GA000002Zoi7YAC",
  "a32GA000002Zoi8YAC",
  "a32GA000002Zoi9YAC",
  "a32GA000002ZoiAYAS",
  "a32GA000002ZoiBYAS",
  "a32GA000002ZoiCYAS",
  "a32GA000002ZoiDYAS",
  "a32GA000002ZoiEYAS",
  "a32GA000002ZoiFYAS",
  "a32GA000002ZoiGYAS",
  "a32GA000002ZoiHYAS",
  "a32GA000002ZoiIYAS",
  "a32GA000002ZoiJYAS",
  "a32GA000002ZoiKYAS",
  "a32GA000002ZoiLYAS",
  "a32GA000002ZoiMYAS",
  "a32GA000002ZoiNYAS",
  "a32GA000002ZoiOYAS",
  "a32GA000002ZoiPYAS",
  "a32GA000002ZoiQYAS",
  "a32GA000002ZoiRYAS",
  "a32GA000002ZoiSYAS",
  "a32GA000002ZoiTYAS",
  "a32GA000002ZoiUYAS",
  "a32GA000002ZoiVYAS",
  "a32GA000002ZoiWYAS",
  "a32GA000002ZoiXYAS",
  "a32GA000002ZoiYYAS",
  "a32GA000002ZoiZYAS",
  "a32GA000002ZoiaYAC",
  "a32GA000002ZoibYAC",
  "a32GA000002ZoicYAC",
  "a32GA000002ZoidYAC",
  "a32GA000002ZoieYAC",
  "a32GA000002ZoifYAC",
  "a32GA000002ZoigYAC",
  "a32GA000002ZoihYAC",
  "a32GA000002ZoiiYAC",
  "a32GA000002ZoijYAC",
  "a32GA000002ZoikYAC",
  "a32GA000002ZoilYAC",
  "a32GA000002ZoimYAC",
  "a32GA000002ZoinYAC",
  "a32GA000002ZoioYAC",
  "a32GA000002ZoipYAC",
  "a32GA000002ZoiqYAC",
  "a32GA000002ZoirYAC",
  "a32GA000002ZoisYAC",
  "a32GA000002ZoitYAC",
  "a32GA000002ZoiuYAC",
  "a32GA000002ZoivYAC",
  "a32GA000002ZoiwYAC",
  "a32GA000002ZoixYAC",
  "a32GA000002ZoiyYAC",
  "a32GA000002ZoizYAC",
  "a32GA000002Zoj0YAC",
  "a32GA000002Zoj1YAC",
  "a32GA000002Zoj2YAC",
  "a32GA000002Zoj3YAC",
  "a32GA000002Zoj4YAC",
  "a32GA000002Zoj5YAC",
  "a32GA000002Zoj6YAC",
  "a32GA000002Zoj7YAC",
  "a32GA000002Zoj8YAC",
  "a32GA000002Zoj9YAC",
  "a32GA000002ZojAYAS",
  "a32GA000002ZojBYAS",
  "a32GA000002ZojCYAS",
  "a32GA000002ZojDYAS",
  "a32GA000002ZojEYAS",
  "a32GA000002ZojFYAS",
  "a32GA000002ZojGYAS",
  "a32GA000002ZojHYAS",
  "a32GA000002ZojIYAS",
  "a32GA000002ZojJYAS",
  "a32GA000002ZojKYAS",
  "a32GA000002ZojLYAS",
  "a32GA000002ZojMYAS",
  "a32GA000002ZojNYAS",
  "a32GA000002ZojOYAS",
  "a32GA000002ZojPYAS",
  "a32GA000002ZojQYAS",
  "a32GA000002ZojRYAS",
  "a32GA000002ZojSYAS",
  "a32GA000002ZojTYAS",
  "a32GA000002ZojUYAS",
  "a32GA000002ZojVYAS",
  "a32GA000002ZojWYAS",
  "a32GA000002ZojXYAS",
  "a32GA000002ZojYYAS",
  "a32GA000002ZojZYAS",
  "a32GA000002ZojaYAC",
  "a32GA000002ZojbYAC",
  "a32GA000002ZojcYAC",
  "a32GA000002ZojdYAC",
  "a32GA000002ZojeYAC",
  "a32GA000002ZojfYAC",
  "a32GA000002ZojgYAC",
  "a32GA000002ZojhYAC",
  "a32GA000002ZojiYAC",
  "a32GA000002ZojjYAC",
  "a32GA000002ZojkYAC",
  "a32GA000002ZojlYAC",
  "a32GA000002ZojmYAC",
  "a32GA000002ZojnYAC",
  "a32GA000002ZojoYAC",
  "a32GA000002ZojpYAC",
  "a32GA000002ZojqYAC",
  "a32GA000002ZojrYAC",
  "a32GA000002ZojsYAC",
  "a32GA000002ZojtYAC",
  "a32GA000002ZojuYAC",
  "a32GA000002ZojvYAC",
  "a32GA000002ZojwYAC",
  "a32GA000002ZojxYAC",
  "a32GA000002ZojyYAC",
  "a32GA000002ZojzYAC",
  "a32GA000002Zok0YAC",
  "a32GA000002Zok1YAC",
  "a32GA000002Zok2YAC",
  "a32GA000002Zok3YAC",
  "a32GA000002Zok4YAC",
  "a32GA000002Zok5YAC",
  "a32GA000002Zok6YAC",
  "a32GA000002Zok7YAC",
  "a32GA000002Zok8YAC",
  "a32GA000002Zok9YAC",
  "a32GA000002ZokAYAS",
  "a32GA000002ZokBYAS",
  "a32GA000002ZokCYAS",
  "a32GA000002ZokDYAS",
  "a32GA000002ZokEYAS",
  "a32GA000002ZokFYAS",
  "a32GA000002ZokGYAS",
  "a32GA000002ZokHYAS",
  "a32GA000002ZokIYAS",
  "a32GA000002ZokJYAS",
  "a32GA000002ZokKYAS",
  "a32GA000002ZokLYAS",
  "a32GA000002ZokMYAS",
  "a32GA000002ZokNYAS",
  "a32GA000002ZokOYAS",
  "a32GA000002ZokPYAS",
  "a32GA000002ZokQYAS",
  "a32GA000002ZokRYAS",
  "a32GA000002ZokSYAS",
  "a32GA000002ZokTYAS",
  "a32GA000002ZokUYAS",
  "a32GA000002ZokVYAS",
  "a32GA000002ZokWYAS",
  "a32GA000002ZokXYAS",
  "a32GA000002ZokYYAS",
  "a32GA000002ZokZYAS",
  "a32GA000002ZokaYAC",
  "a32GA000002ZokbYAC",
  "a32GA000002ZokcYAC",
  "a32GA000002ZokdYAC",
  "a32GA000002ZokeYAC",
  "a32GA000002ZokfYAC",
  "a32GA000002ZokgYAC",
  "a32GA000002ZokhYAC",
  "a32GA000002ZokiYAC",
  "a32GA000002ZokjYAC",
  "a32GA000002ZokkYAC",
  "a32GA000002ZoklYAC",
  "a32GA000002ZokmYAC",
  "a32GA000002ZoknYAC",
  "a32GA000002ZokoYAC",
  "a32GA000002ZokpYAC",
  "a32GA000002ZokqYAC",
  "a32GA000002ZokrYAC"
]
location_ids = [
    '001GA00004vWx3KYAS',
    '001GA0000539lkFYAQ',
    '001GA00004y0OGxYAM',
    '001GA00004y1ACMYA2',
    '001GA00004vWx25YAC',
    '001GA00004vWx22YAC',
    '001GA00004vWx23YAC',
    '001GA00004vWx24YAC',
    '001GA00004vyKCkYAM',
    '001GA000053WEVdYAO',
    '001GA000053XZ7BYAW',
    '001GA000053A6cWYAS',
    '001GA0000539SKkYAM',
    '001GA000050ufjvYAA',
    '001GA000052IqRYYA0',
    '001GA0000539lkKYAQ',
    '001GA000053X3Q4YAK',
    '001GA000050xNclYAE',
    '001GA00004vWx3JYAS',
    '001GA000052IBgrYAG',
    '001GA0000539bohYAA',
    '001GA000050xix4YAA',
    '001GA000050ufjqYAA',
    '001GA000052HWrqYAG',
    '001GA000052HWnPYAW',
    '001GA00004vDugNYAS',
    '001GA000050xYvBYAU',
    '001GA000053WEVxYAO',
    '001GA000052IqRZYA0',
    '001GA00004vB4peYAC',
    '001GA000053WXURYA4'
]


# Headers của Salesforce API
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Tạo danh sách cập nhật với location_id được gán vòng tròn
update_data = []
for index, event_master_id in enumerate(event_master_ids):
    location_id = location_ids[index % len(location_ids)]  # Xoay vòng location_id
    update_data.append({
        "attributes": {"type": "MANAERP__Event_Master_Target_Location__c"},
        "MANAERP__Event_Master__c": event_master_id,
        "MANAERP__Location__c": location_id
    })

# Gửi batch request để cập nhật hàng loạt
update_url = f"{INSTANCE_URL}/services/data/v63.0/composite/sobjects"
payload = json.dumps({"allOrNone": False, "records": update_data}, indent=2)

update_response = requests.post(update_url, headers=headers, data=payload)

# Kiểm tra phản hồi từ API Salesforce
if update_response.status_code in [200, 201]:
    print("✅ Cập nhật thành công:", update_response.json())
else:
    print("❌ Cập nhật thất bại:", update_response.json())
