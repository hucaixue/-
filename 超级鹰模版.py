from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By
import time

web = Chrome()
web.get("http://www.chaojiying.com/user/login/")
time.sleep(3)
# 处理验证码
img = web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('15274777477', 'danny1010', '930493')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']
print(verify_code)