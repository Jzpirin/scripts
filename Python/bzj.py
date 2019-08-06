from selenium import webdriver
import time
import os
import datetime
import shutil
url='http://www.dce.com.cn/dalianshangpin/yw/fw/ywcs/jycs/tlbzjyhcs/index.html'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
iframe=driver.find_elements_by_tag_name('iframe')[2]
time.sleep(2)
driver.switch_to.frame(iframe)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="marginArbiPerfParaForm"]/div/ul/li[3]/a').click()
time.sleep(20)
driver.quit()
src_path = "C:"+os.sep+"Users"+os.sep+"hspcadmin"+os.sep+"Downloads"
des_path = "D:"+os.sep+"shit"
oldname = src_path+os.sep+"组合保证金优惠参数.txt"
year = datetime.date.today().strftime("%Y")
month = datetime.date.today().strftime("%m")
day = datetime.date.today().strftime("%d")
newname = des_path+os.sep+year+month+day+"_保证金优惠参数表.txt"
shutil.move(oldname,newname)
