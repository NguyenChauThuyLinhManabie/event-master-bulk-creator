API: https://pre-prod-manabie.my.salesforce.com/services/data/v63.0/composite/sobjects
example:
{
   "allOrNone" : true,
   "records" : [{
      "attributes" : {"type" : "MANAERP_Activity_Event__c"},
      "Name" : "Event 1",
      "MANAERP__Location__c": "id",
      "MANAERP__Start_Date_Time__c": "",
      "MANAERP__End_Date_Time__c": "",
      "MANAERP__Event_Master__c": "id",
      "MANAERP__Event_Capacity__c":0,
      "MANAERP__Event_Medium__c":"",
      "MANAERP__Send_To__c":"",
      "MANAERP__Allow_Response__c":"",
      "MANAERP__Allow_Submit_Proposal__c":,
      "MANAERP__Reminder__c":0,
      "MANAERP__Allow_Extra_Participant__c":,
      "MANAERP__Limit_Total_Participants__c":"",
      "Description":""
   }]
}

How to get pre-prod-manabie token by command: 
curl -X POST   https://pre-prod-manabie.my.salesforce.com/services/oauth2/token   -d "grant_type=client_credentials"   -d "client_id=3MVG929eOx29turGJCOlKndaCRQr1PFfcl0dhsG01zKEfMX4KxME_HEM2BX69JgBwyc63KEhmd8Sc_PDRmewe"   -d "client_secret=F5C00B2BCD49F94412422AA64D79C95A77F8BFB1A816530A8D6829240A477F98"

Bulk creation of 500 activity events for each event master across 1,000 event masters:
import 1k event master then use SOQL to get id, name -> create activity event base on event master id list (file import_requests.py)

File update_target_location.py to update target location for each event master by API, because of request limitation so we can post 200 event master id /per time.

SOQL: 
SELECT COUNT_DISTINCT(MANAERP__Event_Master__c)
FROM MANAERP__Event_Master_Target_Location__c
WHERE MANAERP__Event_Master__c IN (
    SELECT Id FROM MANAERP__Event_Master__c 
    WHERE Name LIKE '%Verify epic LT-73558 Part 1 with 1k event master%'
)
Purpose of the Query:
    This query is used to determine how many distinct Event Master records have at least one corresponding Target Location entry.
    The filtering condition ensures that only Event Masters matching a specific name pattern are considered.
    The use of COUNT_DISTINCT ensures that duplicate references to the same Event Master in MANAERP__Event_Master_Target_Location__c are not counted multiple times.

