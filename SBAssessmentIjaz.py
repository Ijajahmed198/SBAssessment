# python
import requests
import json
app_id='447EFC04-C90C-4791-9A34-60C4C7B53D33'
user='sendbird_desk_agent_id_dd55be86-f095-47d5-b1b7-3c7a89ea3fa0'
moderator='785964'
api_headers = {
  'Api-Token': '883d2f13a6ae931340b1cdc6993341c55c250667',
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}
#assessment1 printing the exisiting group channels
try:
    res = requests.get('https://api-'+app_id+'.sendbird.com/v3/group_channels',headers=api_headers)
    #print (res.content)
    channel_list = json.loads(res.content)
    all_channels = channel_list["channels"]
    for i in range(len(all_channels)):
        channel_name = all_channels[i]["name"]
        print (channel_name)
except:
    print ("exception while calling the list group api")
#get the channel count before
try:
    res = requests.get('https://api-'+app_id+'.sendbird.com/v3/users/'+moderator+'/group_channel_count',headers=api_headers)
    #print (res.content.name)
except:
    print ("exception while calling the count group api")
#assessment 2 create a group channel and adding users
group_name = input("please enter groupname:")
channel_url = input("please enter Channel url:")
custom_type = input("please enter custom type:")
user_ids = input("please enter user ids seperated by space to be added to group channel:")
user_list = list(user_ids.split(" "))
user_list_to_pass = json.dumps(user_list)
create_group_1 = {
    'name': group_name,
    'channel_url': channel_url,
    'cover_url': 'https://sendbird.com/main/img/cover/cover_08.jpg',
    'custom_type': custom_type,
    'is_distinct': "false",
    'user_ids': user_list,
    'operator_ids': ["Ijaz"]
}

create_group_to_pass = json.dumps(create_group_1)
try:
    result_create = requests.post('https://api-'+app_id+'.sendbird.com/v3/group_channels',headers=api_headers,data=create_group_to_pass)
    print (result_create.content)
    print (result_create)
    print (group_name+" group channel created successfully")
except:
    print ("exception while calling the create group api")
#check custom_type and return the channel name and custom type value
try:
    custom_type=requests.get('https://api-'+app_id+'.sendbird.com/v3/group_channels?custom_types=Ijajahmed',headers=api_headers)
    custom_data_dict=json.loads(custom_type.content)
    custom_data_list=custom_data_dict["channels"]
    for i in range(len(custom_data_list)):
        print (custom_data_list[i]["name"]+"("+(custom_data_list[i]["custom_type"])+")")
except:
    print ("failed to get the channel and custom type")
#sending message to newly created channels,we can customise to take user input
message_text = {
    "message_type": "MESG",
    "user_id": "user1",
    "message": "Assessment2" 
}
try:
    for channel in ('assessment2','assessment_2'):
        send_message = requests.post('https://api-'+app_id+'.sendbird.com/v3/group_channels/'+channel+'/messages',headers=api_headers,data=json.dumps(message_text))
        print ("message successfully sent")
except:
    print ("couldnt send message")
#assessment3 finding the channels with custom_type value
custom_type=requests.get('https://api-'+app_id+'.sendbird.com/v3/group_channels',headers=api_headers)
custom_data_dict=json.loads(custom_type.content)
custom_data_list=custom_data_dict["channels"]
print ("listing the group channels having custom_type values")
for custom in range(len(custom_data_list)):
    if custom_data_list[custom]["custom_type"]:
        custom_type_exist=requests.get('https://api-'+app_id+'.sendbird.com/v3/group_channels?custom_types='+custom_data_list[custom]["custom_type"]+'',headers=api_headers)
        custom_data_dict_exist=json.loads(custom_type_exist.content)
        custom_data_list_exist=custom_data_dict_exist["channels"]
        for exist in range(len(custom_data_list_exist)):
            print (custom_data_list_exist[exist]["name"])
#assessment4 sending push notification upon receiving message on channel
channel_list=requests.get('https://api-'+app_id+'.sendbird.com/v3/group_channels',headers=api_headers)
channel_list_dict=json.loads(channel_list.content)
channels=channel_list_dict["channels"]
print ("looking for any new unread messages")
for channel in range(len(channels)):
    channel_name = channels[channel]["name"]
    channel_url = channels[channel]["channel_url"]
    unread_messages = channels[channel]["unread_message_count"]
    print (channel_name+" "+channel_url+" "+str(unread_messages))
    if unread_messages > 0:
        print("Send push notification")
    