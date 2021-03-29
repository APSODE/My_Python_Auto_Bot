## selenium을 이용한 온라인 클래스 자동 과제 수집 프로그램
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime

unfinAssign_Save_dir = "Your_dir" #미완료과제의 리스트를 저장할 파일의 디렉토리
chromedriver_dir = "Your_dir" #크롬드라이버 디렉토리
onlineClass_url = "https://classroom.google.com/u/1/h"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chromedriver_dir, options = options)

testArray = []
unFinAssign_Array = [] #미완료과제 저장파일에서 변수화 진행할때 저장할 공간

loginSpace = "whsOnd.zHQkBf"
nextButton = "VfPpkd-RLmnJb"
manuBar = "XuQwKc"
unFinAssign = "R06fGe"
unlimAssign_Bar = "e2urcc"
unlimAssign_Period = "ppMo6b.iiWxqc"
my_google_id = "Your_id"
my_google_pw = "Your_pw"

del_sec = 1.5

def Driver_Get_Class(ClassName):
    try:
        dgc = driver.find_element_by_class_name(ClassName)
        return dgc
    except:
        time.sleep(del_sec + 5.5) #로딩이 느려 예외가 발생했을 경우 5초 delay를 주어 대기후 다시 코드 시작
        dgc = driver.find_element_by_class_name(ClassName)
        return dgc

def Drive_Google_Login(ClassName, Button, Infor):
    findElem_ins = Driver_Get_Class(ClassName)
    findElem_ins.send_keys(Infor)
    findElem_ins = Driver_Get_Class(Button).click()
    return findElem_ins


driver.get(onlineClass_url)


#==================================================================== 로그인 구문
findElem = Drive_Google_Login(loginSpace, nextButton, my_google_id)

time.sleep(del_sec)

findElem = Drive_Google_Login(loginSpace, nextButton, my_google_pw)
#==================================================================== 로그인 구문


time.sleep(del_sec + 1)


#==================================================================== 미완료 과제 클릭
findElem = Driver_Get_Class(unFinAssign).click()
#==================================================================== 미완료 과제 클릭


time.sleep(del_sec)


#==================================================================== 
findElem = Driver_Get_Class(unlimAssign_Bar).text

unFinAssign_Save_Before = open(unfinAssign_Save_dir)
unFinAssign_Save_After = unFinAssign_Save_Before.read()
unFinAssign_Save_Before.close()



unfinAssign_list = open(unfinAssign_Save_dir, 'w') #unfinAssign_Save_dir을 'w'(쓰기모드)로 연다
unfinAssign_list.write(findElem) #unfinAssign_list에 findElem을 작성한다.
unfinAssign_list.close()

##아직 미완##
