import requests
import json
import os
import time

global null
null = 'shit'

date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
dir_path='d:\\shit\\beian\\'
batch_api = "http://apidata.chinaz.com/BatchAPI/Domain"

api_key = "0c48c62fb1494090b39d9255c00bbbc2"

#domain_dict = {'baidu':'baidu.com|','isimu':'isimu123.com|'}

dataload = {'key':api_key,'domainNames':'baidu.com|isimu123.com|testtt.com|asdas.cn|'}

batch_response = requests.post(batch_api,data=dataload)
print (batch_response.text)

batch_json = json.loads(batch_response.text)
task_api = "http://apidata.chinaz.com/batchapi/GetApiData"

dataset = {'TaskID':batch_json['TaskID']}
print (task_api+'?'+'taskid='+batch_json['TaskID'])

final_result = requests.post(task_api,data=dataset)
print (final_result.text)

reason_json = json.loads(final_result.text)
return_status = reason_json['StateCode']

def get_return(reason_json1):
    print(reason_json['StateCode'])
    if reason_json1['StateCode'] == 0:
        time.sleep(5)
        global final_result1
        final_result1 = requests.post(task_api,data=dataset)
        print (final_result1.text)
        print("1")
        reason_json1 = json.loads(final_result1.text)
        print(reason_json1['StateCode'])
        get_return(reason_json1)
    #else:
     #   final_result1 = requests.post(task_api,data=dataset)
      #  reason_json1 = json.loads(final_result1.text)
    return '1'

get_return(reason_json)


final_result = requests.post(task_api,data=dataset)
reason_json = json.loads(final_result.text)
print(reason_json)

result_dict=reason_json['Result']['Data']
dict_len=len(result_dict)

result = {}
i=0

while i < dict_len:
    result[result_dict[i]['Domain']]=result_dict[i]['StateCode']
    i=i+1
print(result)

for key in result:
    if result[key] == 0:
        log_file = open(dir_path+'\\'+date+'.log','a')
        log_file.write(key+'\n')
        print(key)
        log_file.close()


