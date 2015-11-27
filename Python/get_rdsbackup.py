import urllib
import urllib2
import time
import json
import os

rds = {'ygg_rds':'' , 'jy_a_rds':'' , 'qs_a_rds':'' , 'cx1_a_rds':'' , 'cx2_a_rds':'' , 'jy_b_rds':'' , 'qs_b_rds':'' , 'cx1_b_rds':'' , 'cx2_b_rds':''}

date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
start_time='T00:00Z'
end_time='T23:59Z'
url_head = 'http://%IP%/api/device/rds/aliyun/?username=%work_code%&api_key=%API_KEY%&account=%aliyun_account%&Action=DescribeBackups&RegionId=cn-hangzhou&DBInstanceId='
url=url_head+rds['ygg_rds']+'&StartTime='+'2015-09-22'+start_time+'&EndTime='+'2015-09-22'+end_time
#print url
print "downloading with urllib"
ygg_rds_url=''
jy_a_rds_url=''
qs_a_rds_url=''
cx1_a_rds_url=''
cx2_a_rds_url=''
jy_b_rds_url=''
qs_b_rds_url=''
cx1_b_rds_url=''
cx2_b_rds_url=''

ygg_rds_path=''
jy_a_rds_path=''
qs_a_rds_path=''
cx1_a_rds_path=''
cx2_a_rds_path=''
jy_b_rds_path=''
qs_b_rds_path=''
cx1_b_rds_path=''
cx2_b_rds_path=''

dir_path='d:\\rds_backup_log\\' + date
os.mkdir(dir_path)


url = {'ygg_rds':ygg_rds_url , 'jy_a_rds':jy_a_rds_url , 'qs_a_rds':qs_a_rds_url , 'cx1_a_rds':cx1_a_rds_url , 'cx2_a_rds':cx2_a_rds_url , 'jy_b_rds':jy_b_rds_url , 'qs_b_rds':qs_b_rds_url , 'cx1_b_rds':cx1_b_rds_url , 'cx2_b_rds':cx2_b_rds_url}

for key in url.keys():
 url[key]=url_head+rds[key]+'&StartTime='+ date +start_time+'&EndTime='+ date +end_time
 print url[key]
	
json_path={'ygg_rds':ygg_rds_path , 'jy_a_rds':jy_a_rds_path , 'qs_a_rds':qs_a_rds_path , 'cx1_a_rds':cx1_a_rds_path , 'cx2_a_rds':cx2_a_rds_path , 'jy_b_rds':jy_b_rds_path , 'qs_b_rds':qs_b_rds_path , 'cx1_b_rds':cx1_b_rds_path , 'cx2_b_rds':cx2_b_rds_path}
download_path = dir_path + '\\' + date

os.mkdir(download_path)

for key in json_path.keys():
	json_path[key]=dir_path + '\\' + key + '_' + date + '.json'
	print json_path[key]

#local = 'd:\\' + 'ygg_rds' + date + '.json'

for key in url.keys():
	urllib.urlretrieve(url[key],json_path[key])
#urllib.urlretrieve(url,local)

for key in json_path.keys():
	url_tmp = open(json_path[key],'r')#json to str
	print url_tmp
	url_json=json.loads(url_tmp.read())#son_str to dict
	BackupStatus = url_json['Items']['Backup'][0]['BackupStatus']
	print BackupStatus
	BackupDownloadURL = url_json['Items']['Backup'][0]['BackupDownloadURL']
	print BackupDownloadURL
	BackupStartTime = url_json['Items']['Backup'][0]['BackupStartTime']
	print BackupStartTime
	BackupEndTime = url_json['Items']['Backup'][0]['BackupEndTime']
	print BackupEndTime
	BackupId = url_json['Items']['Backup'][0]['BackupId']
	print BackupId
	BackupMethod = url_json['Items']['Backup'][0]['BackupMethod']
	print BackupMethod
	BackupMode = url_json['Items']['Backup'][0]['BackupMode']
	print BackupMode
	BackupSize = url_json['Items']['Backup'][0]['BackupSize']
	print BackupSize
	BackupType = url_json['Items']['Backup'][0]['BackupType']
	print BackupType
	DBInstanceId = url_json['Items']['Backup'][0]['DBInstanceId']
	print DBInstanceId
	url_tmp.close()
	backup_log=open(dir_path + '\\' + date + '.log','a')
	backup_log.write('BackupStatus = '+BackupStatus+'\n')
	backup_log.write('DB_NAME = '+key+'\n')
	backup_log.write('DBInstanceId = '+DBInstanceId+'\n')
	backup_log.write('BackupStartTime = '+BackupStartTime+'\n')
	backup_log.write('BackupEndTime = '+BackupEndTime+'\n')
	backup_log.write('BackupId = '+BackupId+'\n')
	backup_log.write('BackupMethod = '+BackupMethod+'\n')
	backup_log.write('BackupMode = '+BackupMode+'\n')
	backup_log.write('BackupSize = '+str(BackupSize)+'\n')
	backup_log.write('BackupType = '+BackupType+'\n')
	backup_log.write('BackupDownloadURL = '+BackupDownloadURL+'\n')
	backup_log.write('RequestUrl = '+ url[key]+'\n')
	backup_log.write('\n' + '-----------------------------------------------' + '\n\n')
	backup_log.close()
	urllib.urlretrieve(BackupDownloadURL,download_path + '\\' + key + '_' + DBInstanceId + '_' + date + '.tar')
 