from selenium import webdriver

driver = webdriver.Chrome()
# driver = webdriver.Firefox()  


driver.get('https://login.taobao.com/member/login.jhtml')

driver.find_element_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]').click()
driver.find_element_by_id("TPL_username_1").clear()
driver.find_element_by_id("TPL_password_1").clear()
driver.find_element_by_id("TPL_username_1").send_keys('unt1tan')
driver.find_element_by_id("TPL_password_1").send_keys('T1t@no518')

driver.find_element_by_id("J_SubmitStatic").click()

# driver.get_cookies()取得cookie  
cookie = "; ".join([item["name"] + "=" + item["value"] + "\n" for item in driver.get_cookies()])
print(cookie)
