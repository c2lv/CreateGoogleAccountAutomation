# selenium의 webdriver를 이용한다.
# 키보드 조작을 위해 Keys를 이용한다.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 다음 페이지 로딩을 기다리기 위해 이용한다.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# webdriver의 경로를 입력한다.
path = "chromedriver_win32/chromedriver.exe"

# 크롬 브라우저로 해당하는 주소에 접속한다.
driver = webdriver.Chrome(path)
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3DOGB%26tab%3Drk%26utm_medium%3Dapp&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')

# 입력할 내용을 미리 변수에 할당한다.
lastName = ""
firstName = ""
Username = ""
Passwd = ""

# find_element_by_name(), find_element_by_id(): 해당하는 element에 커서를 올린다.
# send_keys(): 커서가 위치한 곳에 해당 값을 입력한다.
lastName_box = driver.find_element_by_name("lastName")
lastName_box.send_keys(lastName)
firstName_box = driver.find_element_by_name("firstName")
firstName_box.send_keys(firstName)
Username_box = driver.find_element_by_name("Username")
Username_box.send_keys(Username)
Passwd_box = driver.find_element_by_name("Passwd")
Passwd_box.send_keys(Passwd)
ConfirmPasswd_box = driver.find_element_by_name("ConfirmPasswd")
ConfirmPasswd_box.send_keys(Passwd)

# Retrun key(Enter)를 입력한다.
ConfirmPasswd_box.send_keys(Keys.RETURN)

# 새 창이 로딩되어 전화번호 입력이 가능할 때까지 기다린다.
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'phoneNumberId')))

phoneNumberId = driver.find_element_by_id("phoneNumberId")
phoneNumberId.send_keys("") # 미리 변수 할당하면 안 돼서 직접 입력했음.
phoneNumberId.send_keys(Keys.RETURN)

# Google 인증 코드는 직접 입력하고 Enter 입력 후 현재 창에서 다음 파일 실행하면 되는데 방법을 몰라서 일단 여기까지.