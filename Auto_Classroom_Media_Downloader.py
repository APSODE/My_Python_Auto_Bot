import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import datetime


chromedriver_dir = "C:\\Users\\Administrator\\Desktop\\py\\driver\\chromedriver.exe" #크롬드라이버 디렉토리
onlineClass_url = "https://classroom.google.com/u/1/h"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chromedriver_dir, options = options)

testArray = []
unFinAssign_Array = [] #미완료과제 저장파일에서 변수화 진행할때 저장할 공간

sido_X_path = "/html[@class=' -webkit-']/body/div[@id='modal']/div[@id='modal-popup']/div[@class='modal-wrapper']/div[@class='modal-container']/div[@id='softBoardListLayer']/div[@class='layerContentsWrap']/div[@class='layerSchoolSelectWrap']/table[@class='layerSchoolTable']/tbody/tr[1]/td/select[@id='sidolabel']/option[@value='10']"
grade_X_path = "/html[@class=' -webkit-']/body/div[@id='modal']/div[@id='modal-popup']/div[@class='modal-wrapper']/div[@class='modal-container']/div[@id='softBoardListLayer']/div[@class='layerContentsWrap']/div[@class='layerSchoolSelectWrap']/table[@class='layerSchoolTable']/tbody/tr[2]/td/select[@id='crseScCode']/option[@value='4']"
search_X_path = "/html[@class=' -webkit-']/body/div[@id='modal']/div[@id='modal-popup']/div[@class='modal-wrapper']/div[@class='modal-container']/div[@id='softBoardListLayer']/div[@class='layerContentsWrap']/div[@class='layerSchoolSelectWrap']/table[@class='layerSchoolTable']/tbody/tr[3]/td[1]/input[@id='orgname']"
search_School_X_path = "/html[@class=' -webkit-']/body/div[@id='modal']/div[@id='modal-popup']/div[@class='modal-wrapper']/div[@class='modal-container']/div[@id='softBoardListLayer']/div[@class='layerContentsWrap']/div[@class='layerSchoolSelectWrap']/table[@class='layerSchoolTable']/tbody/tr[3]/td[2]/button[@class='searchBtn']"
select_mySchool_X_path = "/html[@class=' -webkit-']/body/div[@id='modal']/div[@id='modal-popup']/div[@class='modal-wrapper']/div[@class='modal-container']/div[@id='softBoardListLayer']/div[@class='layerContentsWrap']/div[@class='layerSchoolSelectWrap']/ul[@class='layerSchoolArea']/li/a/p/a/em"
select_mySchool_finBtn_X_path = "/html[@class=' -webkit-']/body/div[@id='modal']/div[@id='modal-popup']/div[@class='modal-wrapper']/div[@class='modal-container']/div[@id='softBoardListLayer']/div[@class='layerContentsWrap']/div[@class='layerBtnWrap']/input[@class='layerFullBtn']"
input_myName_Space_X_path = "/html[@class=' -webkit-']/body/app-root/div/div[1]/div[@id='container']/div[@class='subpage']/div[@class='contents']/div/div[@id='WriteInfoForm']/table/tbody/tr[2]/td/input[@id='user_name_input']"
input_myBirth_Space_X_path = "/html[@class=' -webkit-']/body/app-root/div/div[1]/div[@id='container']/div[@class='subpage']/div[@class='contents']/div/div[@id='WriteInfoForm']/table/tbody/tr[3]/td/input[@id='birthday_input']"
input_myPassward_X_path = "/html[@class=' -webkit-']/body/app-root/div/div[1]/div[@id='container']/div[@class='subpage']/div[@class='contents']/div/div[@id='WriteInfoForm']/table/tbody/tr/td/input[@class='input_text_common']"




click_nextBtn_Fin_X_path = "/html[@class=' -webkit-']/body/app-root/div/div[1]/div[@id='container']/div[@class='subpage']/div[@class='contents']/div[2]/input[@id='btnConfirm']"
click_nextBtn_X_path = "/html[@class=' -webkit-']/body/app-root/div/div[1]/div[@id='container']/div[@class='subpage']/div[@class='contents']/div/input[@id='btnConfirm']"
click_myProfile_X_path = "/html[@class=' -webkit-']/body/app-root/div/div[1]/div[@id='container']/div/section[@class='memberWrap']/div[2]/ul/li/a/span[@class='name']"
click_myProfile_Checked_X_path = "/html[@class=' -webkit-']/body/app-root/div/div[1]/div[@id='container']/div/section[@class='memberWrap']/div[2]/ul/li[@class='active']/a/span[@class='name']"

selfCheck_url_First = "https://hcs.eduro.go.kr/#/loginHome"
selfCheck_url_Second = "https://hcs.eduro.go.kr/#/loginWithUserInfo" 
selfCheck_Search_School_Class = "input_text_common.input_text_search"
selfCheck_My_School = "사우고등학교"
selfCheck_myName = "이건보"
selfCheck_myBirth = "040212"
selfCheck_myPassward = "0212"


my_google_id = "20sw1014@sawoo.hs.kr"
my_google_pw = "kunbolee0212@"


del_sec = 1.5

def Del(deltime):
    time.sleep(deltime)

def Driver_Get_Class(ClassName):
    try:
        dgc = driver.find_element_by_class_name(ClassName)
        return dgc
    except:
        time.sleep(del_sec + 5.5) #로딩이 느려 예외가 발생했을 경우 5초 delay를 주어 대기후 다시 코드 시작
        dgc = driver.find_element_by_class_name(ClassName)
        return dgc


def Driver_Get_Id(IdName):
    try:
        dgi = driver.find_elements_by_id(IdName)
        return dgi
    except:
        time.sleep(del_sec)
        dgi = driver.find_elements_by_id(IdName)
        return dgi


def Drive_Google_Login(ClassName, Button, Infor):
    findElem_ins = Driver_Get_Class(ClassName)
    findElem_ins.send_keys(Infor)
    findElem_ins = Driver_Get_Class(Button).click()
    return findElem_ins

def Driver_Get_X_Path(XPath):
    try:

        Del(1)
        dgxp = driver.find_element_by_xpath(XPath)
    except(Exception == Nosy)
    return dgxp


driver.get(selfCheck_url_First)

Del(5)

driver.get(selfCheck_url_Second)

Del(3)

Driver_Get_Class(selfCheck_Search_School_Class).click()

LeeguArray = [sido_X_path, grade_X_path, search_X_path, search_School_X_path, select_mySchool_X_path, select_mySchool_finBtn_X_path, input_myName_Space_X_path, input_myBirth_Space_X_path, click_nextBtn_X_path, input_myPassward_X_path, click_nextBtn_X_path, click_myProfile_Checked_X_path, click_nextBtn_Fin_X_path]
#                  0             1              2                     3                       4                              5                          6                           7                     8                        9                     10                              11                        12                         
list_Count = len(LeeguArray)
for Count in range(0,list_Count):
    Del(1)
    findElem = Driver_Get_X_Path(LeeguArray[Count])

    if Count == 2:
        Del(1)
        findElem.send_keys(selfCheck_My_School)
        #Driver_Get_X_Path(search_X_path).send_keys(selfCheck_My_School)
        

    elif Count == 6:
        Del(1)
        findElem.send_keys(selfCheck_myName)
        

    elif Count == 7:
        Del(1)
        findElem.send_keys(selfCheck_myBirth)
        

    elif Count == 9:
        Del(1)
        findElem.send_keys(selfCheck_myPassward)
        

    elif Count == 13 or 14 or 15:
        Del(1)
        Num = 0
        
        if Count == 13:
            Num = 1
            pass

        elif Count == 14:
            Num = 2
            pass

        elif Count == 14:
            Num = 3    
            pass
                
        check_selfCheck_list_X_path = f"/html[@class=' -webkit-']/body/app-root/div/div[1]/div[@id='container']/div[@class='subpage']/div[@class='contents']/div[2]/div[@class='survey_question']/dl[{Num}]/dd/ul[@class='radioList']/li[1]/label"
        Driver_Get_X_Path(check_selfCheck_list_X_path).click()
        Del(1)


    else:
        Del(1)
        findElem.click()
        

    
"""    
    Del(1)
    Driver_Get_X_Path(sido_X_path).click()

    Del(1)
    Driver_Get_X_Path(grade_X_path).click()

    Del(1)
    Driver_Get_X_Path(search_X_path).send_keys(selfCheck_My_School)

    Del(1)
    Driver_Get_X_Path(search_School_X_path).click()

    Del(1)
    Driver_Get_X_Path(select_mySchool_X_path).click()

    Del(1)
    Driver_Get_X_Path(select_mySchool_finBtn_X_path).click()

    Del(1)
    Driver_Get_X_Path(input_myName_Space_X_path).send_keys(selfCheck_myName)

    Del(1)
    Driver_Get_X_Path(input_myBirth_Space_X_path).send_keys(selfCheck_myBirth)

    Del(1)
    Driver_Get_X_Path(click_nextBtn_X_path).click()

    Del(1)
    Driver_Get_X_Path(input_myPassward_X_path).send_keys(selfCheck_myPassward)

    Del(1)
    Driver_Get_X_Path(click_nextBtn_X_path).click()

    Del(1)
    #Driver_Get_X_Path(click_myProfile_X_path).click()
    Driver_Get_X_Path(click_myProfile_Checked_X_path).click()
    Del(1)
        
Del(1)
for Num in range(1,4):
    check_selfCheck_list_X_path = f"/html[@class=' -webkit-']/body/app-root/div/div[1]/div[@id='container']/div[@class='subpage']/div[@class='contents']/div[2]/div[@class='survey_question']/dl[{Num}]/dd/ul[@class='radioList']/li[1]/label"
    Driver_Get_X_Path(check_selfCheck_list_X_path).click()
    Del(1)


Driver_Get_X_Path(click_nextBtn_Fin_X_path).click()
        """

print("test")
