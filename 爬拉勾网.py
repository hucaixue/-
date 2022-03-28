from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

web=Chrome()
web.get("https://www.lagou.com/")
el=web.find_element(By.XPATH,"/html/body/div[10]/div[1]/div[2]/div[2]/div[1]/div/p[1]/a")
el.click()
time.sleep(2)

search_el=web.find_element(By.XPATH,"/html/body/div[7]/div[1]/div[1]/div[1]/form/input[1]").send_keys("python",Keys.ENTER)

time.sleep(2)

div_list=web.find_elements(By.XPATH,"//*[@id='jobList']/div[1]/div")

for div in div_list:
    div.find_element(By.XPATH,"./div[1]/div[1]/div[1]/a").click()
    time.sleep(2)
    web.switch_to.window(web.window_handles[-1])
    jobdetails=web.find_element(By.XPATH,"//*[@id='job_detail']/dd[2]/div").text
    company=web.find_element(By.XPATH,"//*[@id='__next']/div[2]/div[1]/div/div[1]/dd/div/span[1]").text
    web.close()
    web.switch_to.window(web.window_handles[0])
    print("---以下是新的职位---")
    print(company)
    print(jobdetails)
    print("------------------")
    time.sleep(2)
