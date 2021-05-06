import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
from discord.ext import commands # from discord.ext import tasks, commands
from discord.ext import tasks #
import discord #
import asyncio #
import time #
import nacl
import sys
sys.path.append("C:\\Users\\leegu\\AppData\\Local\\Programs\\Python\\Python38\\Scripts")
from youtube_dl import YoutubeDL
import random
import datetime #
import os
import re
from dotenv import load_dotenv
import json
import csv

images_file_dir = "D:\\건보\\동기화\\Naver MYBOX\\C언어반 예습\\매크로\\디스코드 봇 만들기\\images_file\\" #"D:\\images_file" #
yunh_image_dir = images_file_dir + "yunh\\"
kimki_image_dir = images_file_dir + "kimki\\"
juns_image_dir = images_file_dir + "juns\\"
han_image_dir = images_file_dir + "han\\"
leesae_image_dir = images_file_dir + "leesae\\"
bot = commands.Bot(command_prefix='!')
TEST_BOT_TOKEN = 'YOUR_BOT_TOKEN'
WASHER_BOT_TOKEN = 'YOUR_BOT_TOKEN'
BOT_TOKEN = WASHER_BOT_TOKEN





#=========================================변수============================================
user = []
musictitle = []
song_queue = []
musicnow = []


stop_loop = 1
DelContent_List = ["윤탈", "씨발", "윤탈난발", "윤발탈난", "윤난탈발"]
Gather_Evidence_List = ["동규"]
#Gather_Evidence_List = ["돼지", "뚱", "통통", "뚠뚠", "살찐", "건보", "꿀꿀"]
Gathered_Evidence_dir = "D:\\건보\\프로그램 관련\\Gathered_Evidence.txt"
User_Data_dir = "D:\\건보\\동기화\\Naver MYBOX\\C언어반 예습\\매크로\\통돌이\\"
SHOW_CURRENT_STOCK_LIST = ['롤', '마크', '발로란트', '배그', '오버워치', '나무위키', '산와머니', '순무코인', '히토미', '샘숭전자', '애풀', '세빈왕국', '테수라']

subUrl_List = [] #각 과목의 클래스룸 링크를 받아오는 배열

#=========================================제일고============================================ 
monSub_206_B = ["선택과목 A","선택과목 C","영어","수학","선택과목 D","문학","자율"] #월요일
tusSub_206_B = ["수학","미창","영어","선택과목 B","스생","문학","선택과목 D"] #화요일
wenSub_206_B = ["선택과목 A","일본어 / 중국어","선택과목 C","선택과목 B","창특","동아리"] #수요일
thrSub_206_B = ["진로","선택과목 D","문학","영어","선택과목 A","일본어 / 중국어","수학"] #목요일
friSub_206_B = ["문학","미창","선택과목 B","선택과목 C","일본어 / 중국어","수학","영어"] #금요일
#=========================================제일고============================================


#=========================================운양고============================================  #화요일 6교시
monSub_205_Y = ["운건", "선택과목 A", "수학", "선택과목 A", "선택과목 B", "문학", "선택과목 B"]
tusSub_205_Y = ["선택과목 A", "수학", "창주", "문학", "자율", "창체"]
wenSub_205_Y = ["선택과목 A", "선택과목 C", "수학", "음악", "일본어", "문학", "선택과목 B"]
thrSub_205_Y = ["일본어", "선택과목 B", "기하", "선택과목 A", "선택과목 C", "운건", "수학"]
firSub_205_Y = ["기하", "진활", "선택과목 C", "수학", "음악", "선택과목 A", "문학"]
#=========================================운양고============================================


#=========================================김포고============================================ #수요일 6교시
monSub_206_K = ["선택과목 A","선택과목 C","영어","수학","선택과목 D","문학","자율"] #월요일
tusSub_206_K = ["수학","미창","영어","선택과목 B","스생","문학","선택과목 D"] #화요일
wenSub_206_K = ["선택과목 A","일본어 / 중국어","선택과목 C","선택과목 B","창특","동아리"] #수요일
thrSub_206_K = ["진로","선택과목 D","문학","영어","선택과목 A","일본어 / 중국어","수학"] #목요일
friSub_206_K = ["문학","미창","선택과목 B","선택과목 C","일본어 / 중국어","수학","영어"] #금요일
#=========================================김포고============================================


#=========================================사우고============================================
monSub_205 = ["선택과목 A","영어","운건","선택과목 B","문학","수학","창체"] #월요일
tusSub_205 = ["수학","일본어","선택과목 A","영어","음감","선택과목 C","문학"] #화요일
wenSub_205 = ["운건","한문 / 정보","선택과목 C","문학","창체","창체"] #수요일
thrSub_205 = ["진로","일본어","선택과목 B","문학","영어","선택과목 A","수학"] #목요일
friSub_205 = ["영어","한문 / 정보","선택과목 C","일본어","음감","선택과목 B","수학"] #금요일

monSub_204 = ["선택과목 A","음감","문학","선택과목 B","정보","일본어","창체"] #월요일
tusSub_204 = ["영어","수학","선택과목 A","문학","운건","선택과목 C","진로"] #화요일
wenSub_204 = ["영어","일본어","선택과목 C","수학","창체","창체"] #수요일
thrSub_204 = ["영어","음감","선택과목 B","문학","수학","선택과목 A","정보"] #목요일
friSub_204 = ["문학","일본어","선택과목 C","영어","수학","선택과목 B","운건"] #금요일

monSub_202 = ["선택과목 A","영어","일본어","선택과목 B","운건","문학","창체"] #월요일
tusSub_202 = ["음감","문학","선택과목 A","정보","영어","선택과목 C","수학"] #화요일
wenSub_202 = ["진로","수학","선택과목 C","문학","창체","창체"] #수요일
thrSub_202 = ["운건","수학","선택과목 B","영어","음감","선택과목 A","일본어"] #목요일
friSub_202 = ["정보","문학","선택과목 C","수학","일본어","선택과목 B","영어"] #금요일
#=========================================사우고============================================

#=========================================클래스룸 변수============================================

ClsRoom_URL = "https://classroom.google.com/u/0/h"
MyClsRoom_ID = "20sw1014@sawoo.hs.kr"
MyClsRoom_PW = "kunbolee0212@"

Google_Login_ID_Space = "/html[@class='CMgTXc']/body[@id='yDmH0d']/div[@class='H2SoFe LZgQXe TFhTPc']/div[@id='initialView']/div[@class='xkfVF']/div[@class='Aa1VU']/div[@id='view_container']/div[@class='zWl5kd']/div[@class='DRS7Fe bxPAYd k6Zj8d']/div[@class='pwWryf bxPAYd']/div[@class='Wxwduf Us7fWe JhUD8d']/div[@class='WEQkZc']/div[@class='bCAAsb']/form/span/section[@class='aTzEhb ']/div[@class='CxRgyd']/div/div[@class='d2CFce cDSmF cxMOTc']/div[@class='rFrNMe N3Hzgf jjwyfe QBQrY zKHdkd sdJrJc Tyc9J u3bW4e']/div[@class='aCsJod oJeWuf']/div[@class='aXBtI Wic03c']/div[@class='Xb9hP']/input[@id='identifierId']"
Google_Login_PW_Space = "/html[@class='CMgTXc']/body[@id='yDmH0d']/div[@class='H2SoFe LZgQXe TFhTPc']/div[@id='initialView']/div[@class='xkfVF']/div[@class='Aa1VU']/div[@id='view_container']/div[@class='zWl5kd']/div[@class='DRS7Fe bxPAYd k6Zj8d']/div[@class='pwWryf bxPAYd']/div[@class='Wxwduf Us7fWe JhUD8d']/div[@class='WEQkZc']/div[@class='bCAAsb']/form/span/section[@class='aTzEhb ']/div[@class='CxRgyd']/div/div[@class='SdBahf VxoKGd']/div[@class='eEgeR']/div[@class='W498nc']/div[@class='fdWl7b']/div[@class='hDp5Db']/div[@id='password']/div[@class='aCsJod oJeWuf']/div[@class='aXBtI Wic03c']/div[@class='Xb9hP']/input[@class='whsOnd zHQkBf']"
Google_Login_NextBtn = "/html[@class='CMgTXc']/body[@id='yDmH0d']/div[@class='H2SoFe LZgQXe TFhTPc']/div[@id='initialView']/div[@class='xkfVF']/div[@class='Aa1VU']/div[@id='view_container']/div[@class='zWl5kd']/div[@class='DRS7Fe bxPAYd k6Zj8d']/div[@class='pwWryf bxPAYd']/div[@class='Wxwduf Us7fWe JhUD8d']/div[@class='zQJV3']/div[@class='dG5hZc']/div[@class='qhFLie']/div[@id='identifierNext']/div[@class='VfPpkd-dgl2Hf-ppHlrf-sM5MNb']/button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b']/div[@class='VfPpkd-RLmnJb']"
Google_Login_FinBtn = "/html[@class='CMgTXc']/body[@id='yDmH0d']/div[@class='H2SoFe LZgQXe TFhTPc']/div[@id='initialView']/div[@class='xkfVF']/div[@class='Aa1VU']/div[@id='view_container']/div[@class='zWl5kd']/div[@class='DRS7Fe bxPAYd k6Zj8d']/div[@class='pwWryf bxPAYd']/div[@class='Wxwduf Us7fWe JhUD8d']/div[@class='zQJV3']/div[@class='dG5hZc']/div[@class='qhFLie']/div[@id='passwordNext']/div[@class='VfPpkd-dgl2Hf-ppHlrf-sM5MNb']/button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b']/div[@class='VfPpkd-RLmnJb']"


ClsRoom204 = "/html[@class='zIKt9b W0dUmf']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[@class='kdAl3b']/div[2]/div/ol[@class='JwPp0e']/li[@class='gHz6xd Aopndd rZXyy'][13]/div[@class='Tc9hUd DShyMc-MjgyNDEyNjgwOTU2']/div[@class='R4EiSb']/a[@class='onkcGd ZmqAt']"
KRLang_Sub = "/html[@class='zIKt9b W0dUmf']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[@class='kdAl3b']/div[2]/div/ol[@class='JwPp0e']/li[@class='gHz6xd Aopndd rZXyy'][9]/div[@class='Tc9hUd DShyMc-MjgyNTI1MjMzODY3']/div[@class='R4EiSb']/a[@class='onkcGd ZmqAt']"
JPLang_Sub = "/html[@class='zIKt9b W0dUmf']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[@class='kdAl3b']/div[2]/div/ol[@class='JwPp0e']/li[@class='gHz6xd Aopndd rZXyy'][4]/div[@class='Tc9hUd DShyMc-MjgyNDQyNzUwOTkz']/div[@class='R4EiSb']/a[@class='onkcGd ZmqAt']"
USLang_Sub = "/html[@class='zIKt9b W0dUmf']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[@class='kdAl3b']/div[2]/div/ol[@class='JwPp0e']/li[@class='gHz6xd Aopndd rZXyy'][7]/div[@class='Tc9hUd DShyMc-MjgyNTA4OTIzNTk0']/div[@class='R4EiSb']/a[@class='onkcGd ZmqAt']"
Math_Sub = "/html[@class='zIKt9b W0dUmf']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[@class='kdAl3b']/div[2]/div/ol[@class='JwPp0e']/li[@class='gHz6xd Aopndd rZXyy'][8]/div[@class='Tc9hUd DShyMc-MjgyNDg2NTI2MjM1']/div[@class='R4EiSb']/a[@class='onkcGd ZmqAt']"
Chemistry_Sub = "/html[@class='zIKt9b W0dUmf']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[@class='kdAl3b']/div[2]/div/ol[@class='JwPp0e']/li[@class='gHz6xd Aopndd rZXyy'][12]/div[@class='Tc9hUd DShyMc-MjgyNTEwODI5MDk2']/div[@class='R4EiSb']/a[@class='onkcGd ZmqAt']"
Physics_Sub = "/html[@class='zIKt9b W0dUmf']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[@class='kdAl3b']/div[2]/div/ol[@class='JwPp0e']/li[@class='gHz6xd Aopndd rZXyy'][11]/div[@class='Tc9hUd DShyMc-MjgyNTAyODM4MzU3']/div[@class='R4EiSb']/a[@class='onkcGd ZmqAt']"
Earth_Sub = "/html[@class='zIKt9b W0dUmf']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[@class='kdAl3b']/div[2]/div/ol[@class='JwPp0e']/li[@class='gHz6xd Aopndd rZXyy'][10]/div[@class='Tc9hUd DShyMc-MjgyNDg0MzE5NDMx']/div[@class='R4EiSb']/a[@class='onkcGd ZmqAt']"
Exercise_Sub = "/html[@class='zIKt9b W0dUmf']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[@class='kdAl3b']/div[2]/div/ol[@class='JwPp0e']/li[@class='gHz6xd Aopndd rZXyy'][3]/div[@class='Tc9hUd DShyMc-MjgyNTM2OTUzNzE2']/div[@class='R4EiSb']/a[@class='onkcGd ZmqAt']"
Music_Sub = "/html[@class='zIKt9b W0dUmf']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[@class='kdAl3b']/div[2]/div/ol[@class='JwPp0e']/li[@class='gHz6xd Aopndd rZXyy'][2]/div[@class='Tc9hUd DShyMc-MjgyNDU3MzM1Njk0']/div[@class='R4EiSb']/a[@class='onkcGd ZmqAt']"
Career_sub = "/html[@class='zIKt9b W0dUmf']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[@class='kdAl3b']/div[2]/div/ol[@class='JwPp0e']/li[@class='gHz6xd Aopndd rZXyy'][6]/div[@class='Tc9hUd DShyMc-MjgzNTQ3MjQ0NTE3']/div[@class='R4EiSb']/a[@class='onkcGd ZmqAt']"
Infor_Sub = "/html[@class='zIKt9b W0dUmf']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[@class='kdAl3b']/div[2]/div/ol[@class='JwPp0e']/li[@class='gHz6xd Aopndd rZXyy'][5]/div[@class='Tc9hUd DShyMc-MjgyNTMzOTcxMDAy']/div[@class='R4EiSb']/a[@class='onkcGd ZmqAt']"

#ClsRoom_Attendance_Check_X_Path = "/html[@class='zIKt9b W0dUmf mwJvDe']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[4]/div[@class='dbEQNc']/div[@class='v9TZ3c bFjUmb-Tvm9db']/div[@class='qyN25']/div[@class='T4tcpe n0p5v']/div[@class='vraZ7e QRiHXd tLDEHd']/div[@class='QRiHXd']/span/a[@class='tnRfhc etFl5b']/div[@class='QRiHXd']"
ClsRoom_Attendance_Check_X_Path = "/html[@class='zIKt9b W0dUmf mwJvDe']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div/div[@class='dbEQNc']/div[@class='v9TZ3c bFjUmb-Tvm9db']/div[@class='qyN25']/div[@class='T4tcpe n0p5v']/div[@class='vraZ7e QRiHXd tLDEHd']/div[@class='QRiHXd']/span/a[@class='tnRfhc etFl5b']/div[@class='QRiHXd']"

#=========================================클래스룸 변수============================================

#=========================================자가진단 변수============================================

sido_X_path = "/html[@class=' -webkit-']/body/div[@id='modal']/div[@id='modal-popup']/div[@class='modal-wrapper']/div[@class='modal-container']/div[@id='softBoardListLayer']/div[@class='layerContentsWrap']/div[@class='layerSchoolSelectWrap']/table[@class='layerSchoolTable']/tbody/tr[1]/td/select[@id='sidolabel']/option[@value='10']"
grade_X_path = "/html[@class=' -webkit-']/body/div[@id='modal']/div[@id='modal-popup']/div[@class='modal-wrapper']/div[@class='modal-container']/div[@id='softBoardListLayer']/div[@class='layerContentsWrap']/div[@class='layerSchoolSelectWrap']/table[@class='layerSchoolTable']/tbody/tr[2]/td/select[@id='crseScCode']/option[@value='4']"
search_X_path = "/html[@class=' -webkit-']/body/div[@id='modal']/div[@id='modal-popup']/div[@class='modal-wrapper']/div[@class='modal-container']/div[@id='softBoardListLayer']/div[@class='layerContentsWrap']/div[@class='layerSchoolSelectWrap']/table[@class='layerSchoolTable']/tbody/tr[3]/td[1]/input[@id='orgname']"
search_mySchool_input_space_X_path = "/html[@class=' -webkit-']/body/app-root/div/div[1]/div[@id='container']/div[@class='subpage']/div[@class='contents']/div/div[@id='WriteInfoForm']/table/tbody/tr[1]/td/input[@id='schul_name_input']"

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
click_menuBtn_X_path = "/html[@class='-webkit-']/body/app-root/div/div[1]/header[@id='header']/button[@id='topMenuBtn']"
click_logoutBtn_X_path = "/html[@class='-webkit-']/body/app-root/div/div[1]/header[@id='header']/div[@id='topMenuWrap']/ul/li[4]/button[@class='topmenu07']"

selfCheck_url_First = "https://hcs.eduro.go.kr/#/loginHome"
selfCheck_url_Second = "https://hcs.eduro.go.kr/#/loginWithUserInfo" 
selfCheck_Search_School_Class = "input_text_common.input_text_search"

chromedriver_dir = "D:\\Chrome_Search_Engine\\chromedriver_win32\\chromedriver.exe"

User1_data = ["이윤행", "040912", "1234"]
User2_data = ["김기정", "040907", "1234"]
User3_data = ["종다훈", "040617", "1438"]
User4_data = ["고준혁", "040308", "1224"]
User5_data = ["정윤호", "040808", "0408"]
User6_data = ["이건보", "040212", "0212"]
User7_data = ["두동규", "040216", "2675"]
User8_data = ["임원경", "040311", "9938"]
User9_data = ["최은준", "040824", "1234"]
User10_data = ["이세윤", "040830", "1225"]
User11_data = ["김성민", "041016", "1016"]
User12_data = ["김도영", "041122", "6549"]

dotwName = ["토요일", "일요일"]

holiSub = ["주말이당"]
txtchId = 714475326708908133 #744199524138090501 
#=========================================변수============================================

def Get_All_User_List(guild):
    for guild in ctx.guilds:
        for member in guild.members:
            yield member.id

            return member

def Checking_Money(USER):
    with open(f"{User_Data_dir}\\User_Data\\{USER}.json", "r", encoding = "utf-8") as READ_USER_PROFILE:
        READ_USER_DATA = json.load(READ_USER_PROFILE)
        MONEY = int(READ_USER_DATA['USERMONEY'])
        READ_USER_PROFILE.close()

        return MONEY

def Checking_Stock(USER, STOCK_NAME):
    with open(f"{User_Data_dir}\\User_Data\\{USER}.json", "r", encoding = "utf-8") as READ_USER_PROFILE:
        READ_USER_DATA = json.load(READ_USER_PROFILE)
        STOCK = READ_USER_DATA[f'STOCK_{STOCK_NAME}']
        READ_USER_PROFILE.close()

        return STOCK

def Checking_Stock_Price(STOCK_NAME):
    with open(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json", "r", encoding = "utf-8") as READ_STOCK_LIST_PROFILE:
        READ_STOCK_LIST_DATA = json.load(READ_STOCK_LIST_PROFILE)
        STOCK = READ_STOCK_LIST_DATA['STOCK_PRICE']
        READ_STOCK_LIST_PROFILE.close()

        return STOCK

def Driver_Get_Class(ClassName):
    try:
        dgc = driver.find_element_by_class_name(ClassName)
        return dgc
    except:
        time.sleep(del_sec + 5.5) #로딩이 느려 예외가 발생했을 경우 5초 delay를 주어 대기후 다시 코드 시작
        dgc = driver.find_element_by_class_name(ClassName)
        return dgc

def Driver_Get_X_Path(XPath):
    Del(1)
    dgxp = driver.find_element_by_xpath(XPath)
    return dgxp

def Del(Second):
    time.sleep(Second)
    return Second

def User_Data_Check(UserName):
    
    if UserName in User1_data:
        Checked_User_Data = User1_data
        return Checked_User_Data

    elif UserName in User2_data:
        Checked_User_Data = User2_data
        return Checked_User_Data

    elif UserName in User3_data:
        Checked_User_Data = User3_data
        return Checked_User_Data

    elif UserName in User4_data:
        Checked_User_Data = User4_data
        return Checked_User_Data

    elif UserName in User5_data:
        Checked_User_Data = User5_data
        return Checked_User_Data

    elif UserName in User6_data:
        Checked_User_Data = User6_data
        return Checked_User_Data

    elif UserName in User7_data:
        Checked_User_Data = User7_data
        return Checked_User_Data
    
    elif UserName in User8_data:
        Checked_User_Data = User8_data
        return Checked_User_Data
    
    elif UserName in User9_data:
        Checked_User_Data = User9_data
        return Checked_User_Data

    elif UserName in User10_data:
        Checked_User_Data = User10_data
        return Checked_User_Data

    elif UserName in User11_data:
        Checked_User_Data = User11_data
        return Checked_User_Data

    elif UserName in User12_data:
        Checked_User_Data = User12_data
        return Checked_User_Data
    else:
        return None

def myHealthy_SelfCheck(UserName):


    global driver 
    #options = webdriver.ChromeOptions()
    #options.add_argument("headless")
    #driver = webdriver.Chrome(chromedriver_dir, options = options)
    driver = webdriver.Chrome(chromedriver_dir)

    selfCheck_User_School = ""
    selfCheck_userName = ""
    selfCheck_userBirth = ""
    selfCheck_userPassward = ""

    BestHighSchool = ["고준혁", "이세윤"]
    UnyangHighschool = ["두동규"]
    
    User_Data = User_Data_Check(UserName) #User_Data[0] : UserName / User_Data[1] : UserBirth / User_Data[2] : UserPassward
    if User_Data == None:
        finish = 2
        pass
    selfCheck_userName = User_Data[0]
    selfCheck_userBirth = User_Data[1]
    selfCheck_userPassward = User_Data[2]

    driver.get(selfCheck_url_First)
    Del(3)
    driver.get(selfCheck_url_Second)
    Del(2)

    if UserName in UnyangHighschool:
        selfCheck_User_School = "운양고등학교"
        pass
    elif UserName in BestHighSchool:
        selfCheck_User_School = "김포제일고등학교"
        pass
    else:
        selfCheck_User_School = "사우고등학교"
        pass
    
    
    #LeeguArray = [sido_X_path, grade_X_path, search_X_path, search_School_X_path, select_mySchool_X_path, select_mySchool_finBtn_X_path, input_myName_Space_X_path, input_myBirth_Space_X_path, click_nextBtn_X_path, input_myPassward_X_path, click_nextBtn_X_path, click_myProfile_Checked_X_path, click_nextBtn_Fin_X_path]
    ##                  0             1              2                     3                       4                              5                          6                           7                     8                        9                     10                              11                        12     
    Del(2)
    Driver_Get_X_Path(search_mySchool_input_space_X_path).click()
    Driver_Get_X_Path(sido_X_path).click()
    Driver_Get_X_Path(grade_X_path).click()
    Driver_Get_X_Path(search_X_path).send_keys(selfCheck_User_School)
    Driver_Get_X_Path(search_School_X_path).click()
    Driver_Get_X_Path(select_mySchool_X_path).click()
    Driver_Get_X_Path(select_mySchool_finBtn_X_path).click()
    Driver_Get_X_Path(input_myName_Space_X_path).send_keys(selfCheck_userName)
    Driver_Get_X_Path(input_myBirth_Space_X_path).send_keys(selfCheck_userBirth)
    Driver_Get_X_Path(click_nextBtn_X_path).click()
    Driver_Get_X_Path(input_myPassward_X_path).send_keys(selfCheck_userPassward)
    Driver_Get_X_Path(click_nextBtn_X_path).click()
    
    try:
        Driver_Get_X_Path(click_myProfile_X_path).click()
    except:
        Driver_Get_X_Path(click_myProfile_Checked_X_path).click()

    Del(3)
    check_selfCheck_list_X_path = f"/html[@class=' -webkit-']/body/app-root/div/div[1]/div[@id='container']/div[@class='subpage']/div[@class='contents']/div[2]/div[@class='survey_question']/dl[1]/dd/ul[@class='radioList']/li[1]/label"
    Driver_Get_X_Path(check_selfCheck_list_X_path).click()
    Del(3)
    check_selfCheck_list_X_path = f"/html[@class=' -webkit-']/body/app-root/div/div[1]/div[@id='container']/div[@class='subpage']/div[@class='contents']/div[2]/div[@class='survey_question']/dl[2]/dd/ul[@class='radioList']/li[1]/label"
    Driver_Get_X_Path(check_selfCheck_list_X_path).click()
    Del(3)
    check_selfCheck_list_X_path = f"/html[@class=' -webkit-']/body/app-root/div/div[1]/div[@id='container']/div[@class='subpage']/div[@class='contents']/div[2]/div[@class='survey_question']/dl[3]/dd/ul[@class='radioList']/li[1]/label"
    Driver_Get_X_Path(check_selfCheck_list_X_path).click()

    Del(1)
    Driver_Get_X_Path(click_nextBtn_Fin_X_path).click()
    driver.quit()
    
    if User_Data != None:
        finish = 1
        pass

    return finish

def Subject_Checker(subName):
    if subName == "문학":
        Sub_X_Path = KRLang_Sub
        SubNum = 9
        return Sub_X_Path, SubNum

    elif subName == "수학":
        Sub_X_Path = Math_Sub
        SubNum = 8
        return Sub_X_Path, SubNum

    elif subName == "영어":
        Sub_X_Path = USLang_Sub
        SubNum = 7
        return Sub_X_Path, SubNum

    elif subName == "일본어":
        Sub_X_Path = JPLang_Sub
        SubNum = 4
        return Sub_X_Path, SubNum

    elif subName == "선택과목 A":
        Sub_X_Path = Chemistry_Sub
        SubNum = 12
        return Sub_X_Path, SubNum

    elif subName == "선택과목 B":
        Sub_X_Path = Physics_Sub
        SubNum = 11
        return Sub_X_Path, SubNum

    elif subName == "선택과목 C":
        Sub_X_Path = Earth_Sub
        SubNum = 10
        return Sub_X_Path, SubNum

    elif subName == "음감":
        Sub_X_Path = Music_Sub
        SubNum = 2
        return Sub_X_Path, SubNum

    elif subName == "운건":
        Sub_X_Path = Exercise_Sub
        SubNum = 3
        return Sub_X_Path, SubNum

    elif subName == "진로":
        Sub_X_Path = Career_sub
        SubNum = 6
        return Sub_X_Path, SubNum

    elif subName == "정보":
        Sub_X_Path = Infor_Sub
        SubNum = 5
        return Sub_X_Path, SubNum
    
    elif subName == "창체":
        Sub_X_Path = ClsRoom204
        SubNum = 13
        return Sub_X_Path, SubNum

    else:
        pass
    
def Auto_ClsRoom_Loader(Today_Sub, nowPeriod):
    
    First_time = time.perf_counter()

    TodSub = []
    TodSub = Today_Sub

    Period_Use_Array = Period_Changer(nowPeriod)

    nowSub = TodSub[Period_Use_Array]
    nowSub_X_Path = Subject_Checker(nowSub)[0]
    SubNum = Subject_Checker(nowSub)[1]

    Normal_Sub_X_Path = f"/html[@class='zIKt9b W0dUmf']/body[@id='yDmH0d']/div[@class='v7wOcf ZGnOx']/div[@class='kdAl3b']/div[2]/div/ol[@class='JwPp0e']/li[@class='gHz6xd Aopndd rZXyy'][{SubNum}]/div[@class='Tc9hUd DShyMc-MjgyNTMzOTcxMDAy']/div[@class='R4EiSb']/a[@class='onkcGd ZmqAt']"

    global driver
    driver = webdriver.Chrome(chromedriver_dir)
    
    driver.get(ClsRoom_URL)
    Del(1)
    Driver_Get_X_Path(Google_Login_ID_Space).send_keys(MyClsRoom_ID)
    Del(1)
    Driver_Get_X_Path(Google_Login_NextBtn).click()
    Del(1)
    Driver_Get_X_Path(Google_Login_PW_Space).send_keys(MyClsRoom_PW)
    Del(1)
    Driver_Get_X_Path(Google_Login_FinBtn).click()
    Del(8)
    Driver_Get_X_Path(nowSub_X_Path).click()
    Del(1)
    #Driver_Get_X_Path(Normal_Sub_X_Path).click() #현재 교시에 해당하는 과목을 클래스룸으로 접속
    Driver_Get_X_Path(ClsRoom_Attendance_Check_X_Path).click() #행아웃 링크 클릭

    Second_time = time.perf_counter()

    Del_Sec = round(Second_time - First_time, 2)

    return nowSub, Del_Sec

def Today_Dotw_Checker(Date_Of_The_Week1): #오늘의 Dotw값을 받아서 해당 요일의 과목 배열을 각 반의 순서대로 2차원 배열의 형식으로 과목을 리턴

    Second_todSub_205 = [] #위의 시간표에서 해당요일 시간표 저장하는 배열
    Second_todSub_204 = [] #위의 시간표에서 해당요일 시간표 저장하는 배열
    Second_todSub_202 = [] #위의 시간표에서 해당요일 시간표 저장하는 배열
    #Second_todSub_206_K= [] #위의 시간표에서 해당요일 시간표 저장하는 배열

    if Date_Of_The_Week1 >= 5: #Date_Of_The_Week1의 값이 5보다 크거나 같다면 주말이므로 밑의 if문 안의 코드 실행
        #테스트용 코드
        Rnd_mix = random.randint(0, 4)
        Date_Of_The_Week1 = Rnd_mix
        pass
    
    else: #위의 경우를 제외한 모든 경우에는 바로 밑의 코드를 실행한다.
        pass

    if Date_Of_The_Week1 == 0:
        #print("월요일")
        Second_todSub_205 = monSub_205
        Second_todSub_204 = monSub_204
        Second_todSub_202 = monSub_202
        #Second_todSub_206_K = monSub_206_K
        #Second_todSub_205_Y
        #monSub_205_Y tusSub_205_Y wenSub_205_Y thrSub_205_Y firSub_205_Y


        return Second_todSub_202, Second_todSub_204, Second_todSub_205 #, Second_todSub_206_K

    elif Date_Of_The_Week1 == 1:
        #print("화요일")
        Second_todSub_205 = tusSub_205
        Second_todSub_204 = tusSub_204
        Second_todSub_202 = tusSub_202
        #Second_todSub_206_K = tusSub_206_K



        return Second_todSub_202, Second_todSub_204, Second_todSub_205 #, Second_todSub_206_K

    elif Date_Of_The_Week1 == 2:
        #print("수요일")
        Second_todSub_205 = wenSub_205
        Second_todSub_204 = wenSub_204
        Second_todSub_202 = wenSub_202
        #Second_todSub_206_K = wenSub_206_K



        return Second_todSub_202, Second_todSub_204, Second_todSub_205 #, Second_todSub_206_K

    elif Date_Of_The_Week1 == 3:
        #print("목요일")
        Second_todSub_205 = thrSub_205
        Second_todSub_204 = thrSub_204
        Second_todSub_202 = thrSub_202
        #Second_todSub_206_K = thrSub_206_K



        return Second_todSub_202, Second_todSub_204, Second_todSub_205 #, Second_todSub_206_K

    elif Date_Of_The_Week1 == 4:
        #print("금요일")
        Second_todSub_205 = friSub_205
        Second_todSub_204 = friSub_204
        Second_todSub_202 = friSub_202
        #Second_todSub_206_K = friSub_206_K



        return Second_todSub_202, Second_todSub_204, Second_todSub_205 #, Second_todSub_206_K

def Get_Dotw(Date_Of_The_Week2):
    
    todDotw = 0

    if Date_Of_The_Week2 == 0:
        todDotw = "월요일"
        return todDotw

    elif Date_Of_The_Week2 == 1:
        todDotw = "화요일"
        return todDotw

    elif Date_Of_The_Week2 == 2:
        todDotw = "수요일"
        return todDotw

    elif Date_Of_The_Week2 == 3:
        todDotw = "목요일"
        return todDotw

    elif Date_Of_The_Week2 == 4:
        todDotw = "금요일"
        return todDotw

def Get_Now_Period(td_hour, td_min, td_sec): #Td_hour, Td_min의 값을 기준으로 현재의 교시를 받아오는 Get_period 배열을 리턴
    
    Get_period = 0

    if td_hour == 9:
        if td_min == 10 or 9:
            if td_sec == 0:
                Get_period = 1 #Get_period에 현재 교시를 추가
                return Get_period

    elif td_hour == 10:
        if td_min == 10 or 9:
            if td_sec == 0:
                Get_period = 2 #Get_period에 현재 교시를 추가
                return Get_period

    elif td_hour == 11:
        if td_min == 10 or 9:
            if td_sec == 0:
                Get_period = 3 #Get_period에 현재 교시를 추가
                return Get_period

    elif td_hour == 12:
        if td_min == 10 or 9:
            if td_sec == 0:
                Get_period = 4 #Get_period에 현재 교시를 추가
                return Get_period

    elif td_hour == 13 or 14:
        if td_hour == 13:
            if td_min == 59:
                if td_sec == 0:
                    Get_period = 5
                    return Get_period
        elif td_hour == 14:
            if td_min == 0 :
                if td_sec == 0:
                    Get_period = 5 #Get_period에 현재 교시를 추가
                    return Get_period

    elif td_hour == 14 or 15:
        if td_hour == 14:
            if td_min == 59:
                if td_sec == 0:
                    Get_period = 6
                    return Get_period
        elif td_hour == 15:
            if td_min == 0:
                if td_sec == 0:
                    Get_period = 6 #Get_period에 현재 교시를 추가
                    return Get_period

    elif td_hour == 15 or 16:
        if td_hour == 15:
            if td_min == 59:
                if td_sec == 0:
                    Get_period = 7
                    return Get_period
        elif td_hour == 16:
            if td_min == 0:
                if td_sec == 0:
                    Get_period = 7 #Get_period에 현재 교시를 추가
                    return Get_period
    else: #테스트용 코드
        pass
        #Rnd_period = random.randint(1,7)
        #Get_period = Rnd_period
        #return Get_period

def Period_Changer(Current_Period):
    
    nowPeriod = Current_Period 
    Cached_nowPeriod_fin = 0

    if nowPeriod == 1:
        Cached_nowPeriod_fin = 0
        return Cached_nowPeriod_fin

    elif nowPeriod == 2:
        Cached_nowPeriod_fin = 1
        return Cached_nowPeriod_fin

    elif nowPeriod == 3:
        Cached_nowPeriod_fin = 2
        return Cached_nowPeriod_fin

    elif nowPeriod == 4:
        Cached_nowPeriod_fin = 3
        return Cached_nowPeriod_fin

    elif nowPeriod == 5:
        Cached_nowPeriod_fin = 4
        return Cached_nowPeriod_fin

    elif nowPeriod == 6:
        Cached_nowPeriod_fin = 5
        return Cached_nowPeriod_fin

    elif nowPeriod == 7:
        Cached_nowPeriod_fin = 6
        return Cached_nowPeriod_fin

def Period_Checker(td_hour, td_min):
    
    td_hour_chk = td_hour
    td_min_chk = td_min
    Td_Date = datetime.datetime.today()
    Td_Dotw = Td_Date.weekday()

    get_nowPeriod = []

    if td_hour_chk == 9:
        if td_min_chk >= 10:
            get_nowPeriod.append(1)
            print(type(get_nowPeriod[0]))
            return get_nowPeriod[0]
        
    elif td_hour_chk == 10:
        if td_min_chk >= 10:
            get_nowPeriod.append(2)
            print(type(get_nowPeriod[0]))
            return get_nowPeriod[0]

    elif td_hour_chk == 11:
        if td_min_chk >= 10:
            get_nowPeriod.append(3)
            print(type(get_nowPeriod[0]))
            return get_nowPeriod[0]

    elif td_hour_chk == 12:
        if td_min_chk >= 10:
            get_nowPeriod.append(10)
            print(type(get_nowPeriod[0]))
            return get_nowPeriod[0]

    elif td_hour_chk ==  13 or 14:
        if td_hour_chk == 13:
            if td_min_chk >= 0:
                get_nowPeriod.append(4)
                print(type(get_nowPeriod[0]))
                return get_nowPeriod[0]

        elif td_hour_chk == 14:
            if td_min_chk >= 0:
                get_nowPeriod.append(5)
                print(type(get_nowPeriod[0]))
                return get_nowPeriod[0]

    elif td_hour_chk == 15:
        if td_min_chk >= 0:
            if Td_Dotw == 2:
                get_nowPeriod.append(7) #get_nowPeriod의 값이 7보다 크면 마지막 교시의 알람이 반환
                print(type(get_nowPeriod[0]))
                return get_nowPeriod[0]
                
            elif Td_Dotw != 2:
                get_nowPeriod.append(6)
                print(type(get_nowPeriod[0]))
                return get_nowPeriod[0]

    elif td_hour_chk == 16:
        if td_min_chk >= 0:
            get_nowPeriod.append(7)
            print(type(get_nowPeriod[0]))
            return get_nowPeriod[0]

def Get_Period_Sub(classNum, td_dotw): #완성, #td_dotw의 값에 따라 해당 과목을 받아옴
    
    
    
    Get_Period_Sub_List = []
    Get_Next_Period_Sub_List = []
    Class_Chk = classNum 
    

    Get_Period_Sub_List = Today_Dotw_Checker(td_dotw)
    
    if Class_Chk == 2:
        Class_Chk = 0
        pass

    elif Class_Chk == 4:
        Class_Chk = 1
        pass

    elif Class_Chk == 5:
        Class_Chk = 2
        pass
    
    
    Get_Next_Period_Sub_List = Get_Period_Sub_List[Class_Chk]
    print(f"Get_Period_Sub 값 = {Class_Chk}, \nGet_Period_Sub_List 값 = {Get_Next_Period_Sub_List}")  #[[과목들](2반), [과목들](4반), [과목들](5반)] ##출력 형태##
    return Get_Next_Period_Sub_List

def Next_Period_Sub_Send(classNum):
    
    
    ClassName = f"2학년 {classNum}반"




    Td_Date = datetime.datetime.today()
    Td_Dotw = Td_Date.weekday()
    Td_hour = Td_Date.hour
    Td_min = Td_Date.minute
  
    

    nowPeriod_chk = Period_Checker(Td_hour, Td_min) #6교시 이후에 NoneType 오류
     #현재 교시를 받아옴
    


    nextSub = Get_Period_Sub(classNum, Td_Dotw) #nowPeriod_chk에대한 nextSub가 반환

    
    print(type(nowPeriod_chk))



    
   

    if nowPeriod_chk <= 6: 
    
    
        embed=discord.Embed(title = f'[##다음교시##]', description = f'##다음교시는?##', color=0x00ff00)
        embed.add_field(name=f'[사우고 {ClassName}]', value=f'[{nextSub[nowPeriod_chk]}]', inline=False)
        return embed

    elif nowPeriod_chk == 10:

        embed=discord.Embed(title = f"[##다음교시##]", description = f"##다음교시는?##", color=0x00ff00)
        embed.add_field(name = f"[사우고{ClassName}]", value = f"[점심시간]", inline=False)
        return embed

    elif nowPeriod_chk >= 7:
    
        embed=discord.Embed(title = f'[##다음교시##]', description = f'##다음교시는?##', color=0x00ff00)
        embed.add_field(name=f'[사우고 {ClassName}]', value=f'[끝]', inline=False)
        return embed
              
def load_chrome_driver(): ##나중에 호스팅 서버에 봇을 올리게 되면 사용
      
    options = webdriver.ChromeOptions()

    options.binary_location = os.getenv('GOOGLE_CHROME_BIN')

    options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    return webdriver.Chrome(executable_path=str(os.environ.get('CHROME_EXECUTABLE_PATH')), chrome_options=options)

def title(msg):
    global music

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    chromedriver_dir = "D:\\Chrome_Search_Engine\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver_dir, options = options) #driver = load_chrome_driver()
    driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
    source = driver.page_source
    bs = bs4.BeautifulSoup(source, 'lxml')
    entire = bs.find_all('a', {'id': 'video-title'})
    entireNum = entire[0]
    music = entireNum.text.strip()
    
    musictitle.append(music)
    musicnow.append(music)
    test1 = entireNum.get('href')
    url = 'https://www.youtube.com'+test1
    with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']

    driver.quit()
    
    return music, URL

def play(ctx):
    global vc
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    URL = song_queue[0]
    del user[0]
    del musictitle[0]
    del song_queue[0]
    vc = get(bot.voice_clients, guild=ctx.guild)
    if not vc.is_playing():
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx)) 

def play_next(ctx):
    if len(musicnow) - len(user) >= 2:
        for i in range(len(musicnow) - len(user) - 1):
            del musicnow[0]
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if len(user) >= 1:
        if not vc.is_playing():
            del musicnow[0]
            URL = song_queue[0]
            del user[0]
            del musictitle[0]
            del song_queue[0]
            vc.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS), after=lambda e: play_next(ctx))

def Send_Del_Embed(Del_Message):
    
    UserTypingText = Del_Message

    embed = discord.Embed(title = f"##금칙어 감지##", description = f"##{UserTypingText}에는 금칙어가 포함되어 있습니다. 수정하여주세요##")
    embed.add_field(name = f"##이 메세지는 3초 후에 자동으로 삭제됩니다##", value = f"세윤이 바보", inline = False)

    return embed




@bot.event
async def on_ready():
    print("=============")
    print(" 실 행 완 료 ")
    print("=============")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("노래"))
    #Sawoo_Period_Check.start(txtchId)
    #Stock_Change_Cycle.start(839531082986422292) #test server
    Stock_Change_Cycle.start(817688404631617546)
    #Auto_Check.start(txtchId)

    
    global unlimit_ch
    global unlimit_ch2
    unlimit_ch = bot.get_channel(817688404631617546)
    unlimit_ch2 = bot.get_channel(753557373725179928)


    #kimkijung.start(txtchId)

    #if not discord.opus.is_loaded():
    #    discord.opus.load_opus('opus')
"""
    @bot.event
    async def on_message(message):
        Gather_Evidence_List_Count = len(Gather_Evidence_List)
        DelContent_List_Count = len(DelContent_List) 
        UserTypingText = message.content
        UserTypingText1 = message.content
        channel = bot.get_channel(txtchId)
        
        if message.author != bot.user:
            for Count in range(0, Gather_Evidence_List_Count):
                if Gather_Evidence_List[Count] in UserTypingText:
                    Evidence_Chk = datetime.datetime.today()
                    Writer = message.author
                    Gathered_Evidence_list = open(Gathered_Evidence_dir, 'a') #unfinAssign_Save_dir을 'w'(쓰기모드)로 연다
                    Gathered_Evidence_list.write(f"작성내용 : {UserTypingText}\n일시 : {Evidence_Chk}\n작성자 : {Writer}\n\n") #unfinAssign_list에 findElem을 작성한다.
                    Gathered_Evidence_list.close()
                else:
                    break

            for Count in range(0, DelContent_List_Count):
                if DelContent_List[Count] in UserTypingText1:
                
                    await message.delete()
                    msg = await channel.send(embed = Send_Del_Embed(UserTypingText1))
                    time.sleep(3)
                    await msg.delete()
                
                else:
                    break
    

    @bot.event
    async def on_message(message):
        
        
        DelContent_List_Count = len(DelContent_List) 
        channel = bot.get_channel(txtchId)
        UserTypingText1 = message.content

        if message.author != bot.user:
            for Count in range(0, DelContent_List_Count):
                if DelContent_List[Count] in UserTypingText1:
                
                    await message.delete()
                    msg = await channel.send(embed = Send_Del_Embed(UserTypingText1))
                    time.sleep(3)
                    await msg.delete()
    """           


@bot.command()
async def 금칙어(ctx):
    Embed_List_Count = len(DelContent_List)
    
    embed = discord.Embed(title = f"##금칙어 리스트##", description = f"##금칙어 리스트 입니다.##")
    for count in range(0, Embed_List_Count):
        embed.add_field(name = f"{count + 1}번 금칙어", value = f"{DelContent_List[count]}")

    await ctx.send(embed = embed)
    
@bot.command()
async def 명령어(ctx):
    embed=discord.Embed(title='[이통돌의 기능들]', description='##이통돌 Ver 1.0의 기능##', color=0x00ff00)
    embed.add_field(name=f'[!들어와]', value='[통돌이를 음성채널로 불러옵니다]', inline=False)
    embed.add_field(name=f'[!꺼져]', value='[통돌이를 음성채널에서 쫓아냅니다]', inline=False)
    embed.add_field(name=f'[!URL재생 <URL>]', value='[URL으로 노래를 재생합니다.]', inline=False)
    embed.add_field(name=f'[!재생 <제목>]', value='[유튜브에서 [제목]을 검색해 노래를 재생합니다.]', inline=False)
    embed.add_field(name=f'[!멜론차트]', value='[유튜브에서 최신 멜론차트를 검색하여 재생합니다.]', inline=False)
    embed.add_field(name=f'[!지금노래]', value='[현재 재생중인 노래를 보여줍니다.]', inline=False)
    embed.add_field(name=f'[!일시정지]', value='[현재 재생죽인 노래를 일시정지 합니다.]', inline=False)
    embed.add_field(name=f'[!다시재생]', value='[일시정지한 노래를 다시 재생합니다.]', inline=False)
    embed.add_field(name=f'[!정지]', value='[노래기능을 정지시킵니다.(다시 재생명령어를 사용하면 노래를 들을수 있습니다)]', inline=False)
    embed.add_field(name=f'[!재생목록]', value='[현재 재생중인 재생목록을 보여줍니다.]', inline=False)
    embed.add_field(name=f'[!목록재생]', value='[재생목록에 추가된 노래를 재생합니다.]', inline=False)
    embed.add_field(name=f'[!목록초기화]', value='[재생목록을 초기화 합니다.]', inline=False)
    embed.add_field(name=f'[!대기열추가 <노래>]', value='[노래를 대기열에 추가합니다.]', inline=False)
    embed.add_field(name=f'[!대기열삭제 <숫자>]', value='[대기열의 숫자와 매칭되는 노래를 삭제합니다.]', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 들어와(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
        channel = ctx.author.voice.channel
        embed=discord.Embed(title='[## 입장 알림 ##]', description='## 음성 채널 입장 알림입니다 ##', color=0x00ff00)
        embed.add_field(name=f'[현재 입장 채널]', value=f'[## {channel} ##]', inline=True)
        await ctx.send(embed=embed)

    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
            channel = ctx.author.voice.channel
            embed=discord.Embed(title='[## 입장 알림 ##]', description='## 음성 채널 입장 알림입니다 ##', color=0x00ff00)
            embed.add_field(name=f'[현재 입장 채널]', value=f'[## {channel} ##]', inline=True)
            await ctx.send(embed=embed)

        except:
            await ctx.send("채널에 접속하고 불러주세요...")

@bot.command()
async def 꺼져(ctx):
    try:
        await vc.disconnect()
        channel = ctx.author.voice.channel
        embed=discord.Embed(title='[## 퇴장 알림 ##]', description='## 음성 채널 퇴장 알림입니다 ##', color=0x00ff00)
        embed.add_field(name=f'[현재 퇴장 채널]', value=f'[## {channel} ##]', inline=True)
        await ctx.send(embed=embed)
    

    except:
        await ctx.send("이미 그 채널에 입장한 상태가 아니에요....")

@bot.command()
async def 멜론차트(ctx):
    if not vc.is_playing():
        
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromedriver_dir = "D:\\Chrome_Search_Engine\\chromedriver_win32\\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver_dir, options = options)#driver = load_chrome_driver()
        driver.get("https://www.youtube.com/results?search_query=멜론차트")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")

@bot.command()
async def URL재생(ctx, *, url):
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + url + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    else:
        await ctx.send("노래가 이미 재생되고 있습니다!")

@bot.command()
async def 멈춰(ctx):
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    url = "https://www.youtube.com/watch?v=l3kRNd4obwc" 
    title = "멈춰 리믹스"
    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + title + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    else:
        await ctx.send("노래가 이미 재생되고 있습니다!")

@bot.command()
async def plum(ctx):
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    url1 = "https://www.youtube.com/watch?v=PojjikO8zb4&list=PLYW5J-00fLS3_H4gK0tMwaswoaQ6hEwji&index=3"
    url2 = "https://www.youtube.com/watch?v=PojjikO8zb4&list=PLYW5J-00fLS3_H4gK0tMwaswoaQ6hEwji&index=3"
    url3 = "https://www.youtube.com/watch?v=zGmK9WFnQhg"
    url4 = "https://www.youtube.com/watch?v=aH-uM4I5hq8" 
    url5 = "https://www.youtube.com/watch?v=P_xlimP0MTw"

    url_list = [url1, url2, url3, url4, url5]

    title = "plum"
    Rnd_plum = random.randint(0, 4)

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url_list[Rnd_plum], download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + title + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    else:
        await ctx.send("노래가 이미 재생되고 있습니다!")

@bot.command()
async def 재생(ctx, *, msg):
    if not vc.is_playing():
        
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        
        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromedriver_dir = "D:\\Chrome_Search_Engine\\chromedriver_win32\\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver_dir, options = options)#driver = load_chrome_driver()
        driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()
        musicnow.insert(0, entireText)

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download = False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after = lambda e: play_next(ctx))
    else:
        await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")

@bot.command()
async def 지금노래(ctx):
    if not vc.is_playing():
        await ctx.send("지금은 노래가 재생되지 않네요..")
    else:
        await ctx.send(embed = discord.Embed(title = "지금노래", description = "현재 " + musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))

@bot.command()
async def 일시정지(ctx):
    if vc.is_playing():
        vc.pause()
        await ctx.send(embed = discord.Embed(title= "일시정지", description = musicnow[0] + "을(를) 일시정지 했습니다.", color = 0x00ff00))
    else:
        await ctx.send("지금 노래가 재생되지 않네요.")

@bot.command()
async def 다시재생(ctx):
    try:
        vc.resume()
    except:
         await ctx.send("지금 노래가 재생되지 않네요.")
    else:
         await ctx.send(embed = discord.Embed(title= "다시재생", description = musicnow[0] + "을(를) 다시 재생했습니다.", color = 0x00ff00))

@bot.command()
async def 정지(ctx):
    if vc.is_playing():
        vc.stop()
        await ctx.send(embed = discord.Embed(title= "노래끄기", description = musicnow[0] + "을(를) 종료했습니다.", color = 0x00ff00))
    else:
        await ctx.send("지금 노래가 재생되지 않네요.")

@bot.command()
async def 대기열추가(ctx, *, msg):
    user.append(msg)
    result, URLTEST = title(msg)
    song_queue.append(URLTEST)
    await ctx.send(result + "를 재생목록에 추가했어요!")

@bot.command()
async def 대기열삭제(ctx, *, number):
    try:
        ex = len(musicnow) - len(user)
        del user[int(number) - 1]
        del musictitle[int(number) - 1]
        del song_queue[int(number)-1]
        del musicnow[int(number)-1+ex]
            
        await ctx.send("대기열이 정상적으로 삭제되었습니다.")
    except:
        if len(list) == 0:
            await ctx.send("대기열에 노래가 없어 삭제할 수 없어요!")
        else:
            if len(list) < int(number):
                await ctx.send("숫자의 범위가 목록개수를 벗어났습니다!")
            else:
                await ctx.send("숫자를 입력해주세요!")

@bot.command()
async def 재생목록(ctx):
    if len(musictitle) == 0:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")
    else:
        global Text
        Text = ""
        for i in range(len(musictitle)):
            Text = Text + "\n" + str(i + 1) + ". " + str(musictitle[i])
            
        await ctx.send(embed = discord.Embed(title= "노래목록", description = Text.strip(), color = 0x00ff00))

@bot.command()
async def 목록초기화(ctx):
    try:
        ex = len(musicnow) - len(user)
        del user[:]
        del musictitle[:]
        del song_queue[:]
        while True:
            try:
                del musicnow[ex]
            except:
                break
        await ctx.send(embed = discord.Embed(title= "목록초기화", description = """목록이 정상적으로 초기화되었습니다. 이제 노래를 등록해볼까요?""", color = 0x00ff00))
    except:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")

@bot.command()
async def 목록재생(ctx):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    if len(user) == 0:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")
    else:
        if len(musicnow) - len(user) >= 1:
            for i in range(len(musicnow) - len(user)):
                del musicnow[0]
        if not vc.is_playing():
            play(ctx)
        else:
            await ctx.send("노래가 이미 재생되고 있어요!")

@bot.command()
async def 대화목록(ctx): 
    embed=discord.Embed(title = f'[##대화 가능 목록##]', description = f'##사용방법 : !통돌아 <인자>##', color=0x00ff00)
    embed.add_field(name=f'[기정이는]', value=f'[기정이의 태그를 보여줍니다]', inline=False)
    embed.add_field(name=f'[윤행이는]', value=f'[윤행이의 태그를 보여줍니다]', inline=False)
    embed.add_field(name=f'[기정]', value=f'[기정이의 엽사를 보여줍니다]', inline=False)
    embed.add_field(name=f'[윤행]', value=f'[윤행이의 엽사를 보여줍니다]', inline=False)
    embed.add_field(name=f'[유빈]', value=f'[의뢰받은 사진첩입니다.]', inline=False)

    await ctx.send(embed = embed)

@bot.command()
async def 시험범위(ctx):
    embed = discord.Embed(title = f"[##시험범위##]", description = f"##다른 과목 시험범위 제보 받아영##", color=0x00ff00)  
    embed.add_field(name = f"[문학]", value = f"공간 부족으로 인한 미작성", inline=False)
    embed.add_field(name = f"[수학]", value = f"삼각함수 활용 전까지", inline=False)
    embed.add_field(name = f"[영어]", value = f"1, 2, 3과 본문 / 2021년 3월 모의고사", inline=False)
    embed.add_field(name = f"[화학]", value = f"몰 농도까지", inline=False)
    embed.add_field(name = f"[물리학]", value = f"열역학 제 2법칙(Maybe 까먹음)", inline=False)
    embed.add_field(name = f"[지구과학]", value = f"교과서 : ~ 66p \n학습지 : ~ 20p \n선택형 : 18문항(90점), 서술형 1문항 : 10점", inline=False)
    await ctx.send(embed = embed)

@bot.command()
async def 사진첩(ctx, *arg):
    
    images_file_dir = "D:\\건보\\동기화\\Naver MYBOX\\C언어반 예습\\매크로\\디스코드 봇 만들기\\images_file\\"
    yunh_image_dir = images_file_dir + "yunh\\"
    kimki_image_dir = images_file_dir + "kimki\\"

    
    picTuple_Conv = list(arg) #<!사진첩 1 2> 입력시 picTuple_Conv[0] = 1, picTuple_Conv[1] = 2 #picTuple_Conv[2]값은 무조건 int형으로 변환 시킬것 str형 들어가면 TypeError발생
    
    unLimit_ch = bot.get_channel(817688404631617546)
    unlimit_ch2 = bot.get_channel(753557373725179928)

    p1 = "윤행이"
    p2 = "기정이"
    
    if ctx.channel == unLimit_ch or unlimit_ch2:
            
        if picTuple_Conv[0] == str(p1):
            
            Images_file_list_yun = list(os.listdir(yunh_image_dir))
            Image_file_count = len(Images_file_list_yun)

            if int(picTuple_Conv[1]) <= Image_file_count:
                
                disgus_warn = await ctx.send(f"이 메세지가 출현한 이후 3초뒤에 혐짤이 나옵니다 주의해주세요")
                time.sleep(1)

                for timeChk in range(1, 3):
                    
                    if timeChk == 1:
                        timeChk_1 = 2
                        
                        await disgus_warn.edit(content=f'이 메세지가 출현한 이후 {timeChk_1}초뒤에 혐짤이 나옵니다 주의해주세요')
                        time.sleep(1)

                        pass

                    elif timeChk == 2:
                        timeChk_1 = 1
                        
                        await disgus_warn.edit(content=f'이 메세지가 출현한 이후 {timeChk_1}초뒤에 혐짤이 나옵니다 주의해주세요')
                        time.sleep(1)
                        
                        pass

                    else:
                        pass

                time.sleep(0.2)
                await disgus_warn.edit(content = "!!주의!!주의!!주의!!주의!!주의!!")

                await ctx.send(file = discord.File(f"{yunh_image_dir}image{int(picTuple_Conv[1])}.jpg"))
            
            elif int(picTuple_Conv[1]) > Image_file_count:
                await ctx.send(f"입력하신 값 {int(picTuple_Conv[1])}은(는) 현재 윤행이 엽사 갯수보다 많습니다. \n번호를 낮춰주세요.")

        elif picTuple_Conv[0] == str(p2):
            
            Images_file_list_kimki = list(os.listdir(kimki_image_dir))
            Image_file_count = len(Images_file_list_kimki)

            if int(picTuple_Conv[1]) <= Image_file_count:

                disgus_warn = await ctx.send(f"이 메세지가 출현한 이후 3초뒤에 혐짤이 나옵니다 주의해주세요")
                time.sleep(1)

                for timeChk in range(1, 3):
                    
                    if timeChk == 1:
                        timeChk_1 = 2
                        
                        await disgus_warn.edit(content=f'이 메세지가 출현한 이후 {timeChk_1}초뒤에 혐짤이 나옵니다 주의해주세요')
                        time.sleep(1)

                        pass

                    elif timeChk == 2:
                        timeChk_1 = 1
                        
                        await disgus_warn.edit(content=f'이 메세지가 출현한 이후 {timeChk_1}초뒤에 혐짤이 나옵니다 주의해주세요')
                        time.sleep(1)
                        
                        pass

                    else:
                        pass

                time.sleep(0.2)
                await disgus_warn.edit(content = "!!주의!!주의!!주의!!주의!!주의!!")

                await ctx.send(file = discord.File(f"{kimki_image_dir}kimimage{int(picTuple_Conv[1])}.jpg"))
            
            elif int(picTuple_Conv[1]) > Image_file_count:
                await ctx.send(f"입력하신 값 {int(picTuple_Conv[1])}은(는) 현재 윤행이 엽사 갯수보다 많습니다. \n번호를 낮춰주세요.")
        
    elif ctx.channel != unLimit_ch:
        await ctx.send("여기는 다훈이에 의해 명령어를 칠 수 없게 변했어요")

@bot.command()
async def 변수테스트(ctx, *arg):
    Command = list(arg)
    CMD_AUTHOR_USER = ctx.author
    LIST_COUNTER = len(Command)

    if LIST_COUNTER == 1:
        BUY_STOCK_NAME = str(Command[0])
        pass

    elif LIST_COUNTER == 2:
        BUY_STOCK_NAME = str(Command[0])
        BUY_STOCK_AMOUNT = int(Command[1])
        pass

    else:
        await ctx.send("너무 많은 인자가 입력되었거나, 인자가 입력되지 않았습니다.")
    
    

    with open(f"{User_Data_dir}\\Stock_List\\{BUY_STOCK_NAME}.json", "r", encoding = "utf-8") as STOCK_LIST_PROFILE:
        STOCK_LIST_DATA = json.load(STOCK_LIST_PROFILE)
        STOCK_LIST_PROFILE.close()

    STOCK_NAME = str(STOCK_LIST_DATA['STOCK_NAME'])

    with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "r", encoding = "utf-8") as USER_PROFILE:
        USER_DATA = json.load(USER_PROFILE)
        USER_PROFILE.close()

    with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "w", encoding = "utf-8") as USER_PROFILE:
        USER_DATA[f'STOCK_{STOCK_NAME}'] = BUY_STOCK_AMOUNT
        json.dump(USER_DATA, USER_PROFILE, indent = 4)
        

    


@bot.command()
async def 통돌아(ctx, arg):
    #await ctx.send("현재 영문 모를 버그가 발생해 수리중입니다.")

    p1 = "놀아줘"
    p2 = "기정이는"
    p3 = "윤행이는"
    p4 = "윤행"
    p5 = "기정"
    p6 = "유빈"
    p7 = "다훈"
    p8 = "승엽"
    p9 = "세윤이는"
    
    
    p10 = "대화목록"

    #p6 = "다음교시"
    
    #Using_image_dir = ""
    ##image_count_list = list(os.listdir(images_file_dir)) 
    ##Image_files_count = len(image_count_list)


    Images_file_list = []
    Image_file_count = 0

    if arg == str(p1):
        await ctx.send("싫어")


    
    elif arg ==str(p2) or str(p3) or str(p4) or str(p5) or str(p6) or str(p7) or str(p9):
        global unlimit_ch
        global unlimit_ch2
        unlimit_ch = bot.get_channel(817688404631617546)
        unlimit_ch2 = bot.get_channel(753557373725179928)
        if ctx.channel == unlimit_ch or unlimit_ch2:
            if arg == str(p4):
                Images_file_list = list(os.listdir(yunh_image_dir))
                Image_file_count = len(Images_file_list)

                disgus_warn = await ctx.send(f"이 메세지가 출현한 이후 3초뒤에 혐짤이 나옵니다 주의해주세요")

                for timeChk in range(1, 3):
                    
                    
                    if timeChk == 1:
                        timeChk_1 = 2
                        
                        await disgus_warn.edit(content=f'이 메세지가 출현한 이후 {timeChk_1}초뒤에 혐짤이 나옵니다 주의해주세요')
                        time.sleep(1)

                        pass

                    elif timeChk == 2:
                        timeChk_1 = 1
                        
                        await disgus_warn.edit(content=f'이 메세지가 출현한 이후 {timeChk_1}초뒤에 혐짤이 나옵니다 주의해주세요')
                        time.sleep(1)
                        
                        pass

                    else:
                        pass

                time.sleep(0.2)
                await disgus_warn.edit(content = "!!주의!!주의!!주의!!주의!!주의!!")
                    

                Rnd_Count = random.randint(0, Image_file_count)
                await ctx.send(file = discord.File(f'{yunh_image_dir}image{Rnd_Count}.jpg'))

            elif arg == str(p5):
                Images_file_list = list(os.listdir(kimki_image_dir))
                Image_file_count = len(Images_file_list)
                
                disgus_warn = await ctx.send(f"이 메세지가 출현한 이후 3초뒤에 혐짤이 나옵니다 주의해주세요")

                for timeChk in range(1, 3):
                    
                    
                    if timeChk == 1:
                        timeChk_1 = 2
                        
                        await disgus_warn.edit(content=f'이 메세지가 출현한 이후 {timeChk_1}초뒤에 혐짤이 나옵니다 주의해주세요')
                        time.sleep(1)

                        pass

                    elif timeChk == 2:
                        timeChk_1 = 1
                        
                        await disgus_warn.edit(content=f'이 메세지가 출현한 이후 {timeChk_1}초뒤에 혐짤이 나옵니다 주의해주세요')
                        time.sleep(1)
                        
                        pass

                    else:
                        pass

                time.sleep(0.2)
                await disgus_warn.edit(content = "!!주의!!주의!!주의!!주의!!주의!!")

                Rnd_Count = random.randint(0, Image_file_count)
                await ctx.send(file = discord.File(f'{kimki_image_dir}kimimage{Rnd_Count}.jpg'))

            elif arg == str(p6):
                Images_file_list = list(os.listdir(juns_image_dir))
                Image_file_count = len(Images_file_list)

                Rnd_Count = random.randint(0, Image_file_count)
                await ctx.send(file = discord.File(f'{juns_image_dir}jimage{Rnd_Count}.jpg'))

            elif arg == str(p8):
                Images_file_list = list(os.listdir(han_image_dir))
                Image_file_count = len(Images_file_list)

                Rnd_Count = random.randint(0, Image_file_count)
                await ctx.send(file = discord.File(f"{han_image_dir}hanimage{Rnd_Count}.jpg"))
            
            elif arg == str(p9):
                Images_file_list = list(os.listdir(leesae_image_dir))
                Image_file_count = len(Images_file_list)

                Rnd_Count = random.randint(0, Image_file_count)
                await ctx.send(file = discord.File(f"{leesae_image_dir}leesaeimage{Rnd_Count}.jpg"))

            elif arg == str(p2) or str(p3):
                Text_1 = ["@승엽이 따까리", "ㄱㅗㅏㅇ ㅁㅗ 남편", "윤슬이 ㄴㅍ", "원숭이", "고급 남창", "개떡장애 새끼", "뒤에서 1등급", "오른쪽 땜빵", "기탈난발", "미란이 남편", "조루새끼"]
                Text_2 = ["@윤행", "원숭이", "틱장애 말기", "개떡장애 새끼", "멀대새끼", "윤 ~ 3", "윤탈난발"]
                Text = []
        
                 
                if arg == str(p2):
                    array_len = len(Text_1)
                    Text = Text_1
                    pass
                
                elif arg == str(p3):
                    array_len = len(Text_2)
                    Text = Text_2
                    pass


                Count_s = 0
                Count_e = array_len #배열 원소 갯수보다 1씩 더한다

                for Count in range(Count_s, Count_e): 
                    await ctx.send(f"{Text[Count]}")
                    time.sleep(0.5)
            
        elif arg == str(p7):
            await ctx.send("너 때문에 내가 격리 당했어...죽일꺼야...")
        
        elif ctx.channel != unlimit_ch:
            await ctx.send("여기는 다훈이에 의해 명령어를 칠 수 없게 변했어요")


#수수료 추가할것


@bot.command()
async def 회원가입(ctx):
    Resister_USER = ctx.author
    Resister_USER_ID = Resister_USER.id
    Welcom_Money = 200000
    #await ctx.send(f"messgae author = {Resister_USER} / message author id = {Resister_USER_ID}")

    DIR_CHECKER = os.path.exists(f"{User_Data_dir}\\User_Data\\{Resister_USER}.json")
    if DIR_CHECKER == True:
        await ctx.send(f"{Resister_USER}님의 데이터는 이미 존재합니다.")

    else:
        with open(f"{User_Data_dir}\\User_Data\\{Resister_USER}.json", 'a') as RESISTER_USER_DATA:
            
            
            USER_DATA = {"USERNAME": f"{Resister_USER}", "USERID": f"{Resister_USER_ID}", "USERMONEY": Welcom_Money}
            """
            USER_DATA = {}
            USER_DATA["USER"] = []
            USER_DATA["USER"].append({"USERNAME": f"{Resister_USER}", "USERID": f"{Resister_USER_ID}", "USERMONEY": f"{Welcom_Money}"})
            """
            USER_PROFILE = json.dump(USER_DATA, RESISTER_USER_DATA, indent = 4)
            
            embed = discord.Embed(title = f"##회원가입 완료##", description = f"회원가입 선물로 20만원이 계좌로 입금되었어요!\n<!자산>으로 확인해보세요!")
            await ctx.send(embed = embed)

@bot.command()
async def 자산(ctx, arg: discord.Member = None):
    #SHOW_CURRENT_STOCK_LIST = ['롤', '마크', '발로란트', '배그', '오버워치']
    CMD_AUTHOR_USER = ctx.author
    USER_NAME = str(arg)
    
    STOCK_LIST_COUNTER = len(SHOW_CURRENT_STOCK_LIST)
    SHOW_STOCK_LIST = []
    #await ctx.send(f"명령어 입력한 사람 : {CMD_AUTHOR_USER}")
    if not arg:
        try:

            with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "r", encoding = "utf-8") as READ_USER_PROFILE:
                READ_USER_DATA = json.load(READ_USER_PROFILE)
                READ_USER_PROFILE.close()

            USER_MONEY = READ_USER_DATA['USERMONEY']
                
            embed = discord.Embed(title = f"[##현재 자산##]", description = f"")
            embed.add_field(name = f"[보유 현금]", value = f"{USER_MONEY}원", inline = False)
            #embed.add_field(indax = "STOCK", name = f"[보유 주식]", value = f"", inline = False)
            for STOCK_COUNT in range(STOCK_LIST_COUNTER):
                STOCK_NAME_BH = SHOW_CURRENT_STOCK_LIST[STOCK_COUNT]
                STOCK_NAME_CHECK = f"STOCK_{STOCK_NAME_BH}"
                if STOCK_NAME_CHECK in READ_USER_DATA:
                    SHOW_STOCK_LIST.append(STOCK_NAME_BH) #뒤에 주식 이름

            
            SHOW_STOCK_LIST_COUNTER = len(SHOW_STOCK_LIST)

            for STOCK_COUNT in range(SHOW_STOCK_LIST_COUNTER):
                STOCK_NAME = SHOW_STOCK_LIST[STOCK_COUNT]
                STOCK_NAME_CHECK = f'STOCK_{STOCK_NAME}'
                if STOCK_NAME_CHECK in READ_USER_DATA:
                    USER_OWN_STOCK_AMOUNT = READ_USER_DATA[STOCK_NAME_CHECK]
                    if USER_OWN_STOCK_AMOUNT != 0:
                        embed.add_field(name = f"{STOCK_NAME}  ", value = f"{USER_OWN_STOCK_AMOUNT}주", inline = True)
                    else:
                        pass
            embed.set_footer(text = f"{CMD_AUTHOR_USER}")
            await ctx.send(embed = embed)
            


            
        
        except:
            await ctx.send(f"[{USER_NAME}]님의 데이터가 존재하지 않습니다.")

    else:
        try:
            with open(f"{User_Data_dir}\\User_Data\\{USER_NAME}.json", "r", encoding = "utf-8") as READ_USER_PROFILE:
                READ_USER_DATA = json.load(READ_USER_PROFILE)
                READ_USER_PROFILE.close()

            USER_MONEY = READ_USER_DATA['USERMONEY']
                
            embed = discord.Embed(title = f"[##현재 자산##]", description = f"")
            embed.add_field(name = f"[보유 현금]", value = f"{USER_MONEY}원", inline = False)
            #embed.add_field(indax = "STOCK", name = f"[보유 주식]", value = f"", inline = False)
            for STOCK_COUNT in range(STOCK_LIST_COUNTER):
                STOCK_NAME_BH = SHOW_CURRENT_STOCK_LIST[STOCK_COUNT]
                STOCK_NAME_CHECK = f"STOCK_{STOCK_NAME_BH}"
                if STOCK_NAME_CHECK in READ_USER_DATA:
                    SHOW_STOCK_LIST.append(STOCK_NAME_BH) #뒤에 주식 이름

            
            SHOW_STOCK_LIST_COUNTER = len(SHOW_STOCK_LIST)

            for STOCK_COUNT in range(SHOW_STOCK_LIST_COUNTER):
                STOCK_NAME = SHOW_STOCK_LIST[STOCK_COUNT]
                STOCK_NAME_CHECK = f'STOCK_{STOCK_NAME}'
                if STOCK_NAME_CHECK in READ_USER_DATA:
                    USER_OWN_STOCK_AMOUNT = READ_USER_DATA[STOCK_NAME_CHECK]
                    if USER_OWN_STOCK_AMOUNT != 0:
                        embed.add_field(name = f"{STOCK_NAME}  ", value = f"{USER_OWN_STOCK_AMOUNT}주", inline = True)
                    else:
                        pass

            embed.set_footer(text = f"{USER_NAME}")
            await ctx.send(embed = embed)
            


            
        
        except:
            await ctx.send(f"[{USER_NAME}]님의 데이터가 존재하지 않습니다.")

@bot.command()
async def 베팅(ctx, arg):
    
    Money = int(arg)
    CMD_AUTHOR_USER = ctx.author
    USER_MONEY = int(Checking_Money(CMD_AUTHOR_USER))
    #await ctx.send(f"USER_MONEY : {USER_MONEY}")
    if Money >= 500:

        if Money <= int(USER_MONEY):
            Rnd = random.randint(1, 10)
            #await ctx.send(f"Rnd : {Rnd}")

            if Rnd == 1:
                Rnd_val = 2
                pass

            elif Rnd == 2:
                Rnd_val = 2
                pass

            elif Rnd == 3:
                Rnd_val = 3
                pass
            
            elif Rnd == 4:
                Rnd_val = 3
                pass

            else:
                Rnd_val = 0
                pass

            if Rnd_val == 2: #2배
            #if Rnd != 0:
                with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "r") as EDIT_USER_PROFILE:
                    EDIT_USER_DATA = json.load(EDIT_USER_PROFILE)
                    EDIT_USER_PROFILE.close()

                EDIT_USER_DATA['USERMONEY'] = USER_MONEY + Money

                with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "w") as EDIT_USER_PROFILE:
                    json.dump(EDIT_USER_DATA, EDIT_USER_PROFILE, indent = 4)
                    EDIT_USER_PROFILE.close()


                await ctx.send("2배! 운이 좋네요!")

                Del(1)

                MONEY = Checking_Money(CMD_AUTHOR_USER)
                embed = discord.Embed(title = f"", descripton = f"")
                embed.add_field(name = f"보유자산 : ", value = f"{MONEY}원", inline = True)
                embed.set_footer(text = CMD_AUTHOR_USER)
        
        
                await ctx.send(embed = embed)

            elif Rnd_val == 3:
                with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "r") as EDIT_USER_PROFILE:
                    EDIT_USER_DATA = json.load(EDIT_USER_PROFILE)
                    EDIT_USER_PROFILE.close()

                EDIT_USER_DATA['USERMONEY'] = USER_MONEY + (Money * 2)

                with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "w") as EDIT_USER_PROFILE:
                    json.dump(EDIT_USER_DATA, EDIT_USER_PROFILE, indent = 4)
                    EDIT_USER_PROFILE.close()

                await ctx.send("3배! 운이 좋네요!")

                Del(1)

                MONEY = Checking_Money(CMD_AUTHOR_USER)
                embed = discord.Embed(title = f"", descripton = f"")
                embed.add_field(name = f"보유자산 : ", value = f"{MONEY}원", inline = True)
                embed.set_footer(text = CMD_AUTHOR_USER)
        
        
                await ctx.send(embed = embed)

            elif Rnd_val == 0:
                with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "r") as EDIT_USER_PROFILE:
                    EDIT_USER_DATA = json.load(EDIT_USER_PROFILE)
                    EDIT_USER_PROFILE.close()

                EDIT_USER_DATA['USERMONEY'] = USER_MONEY - Money

                with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "w") as EDIT_USER_PROFILE:
                    json.dump(EDIT_USER_DATA, EDIT_USER_PROFILE, indent = 4)
                    EDIT_USER_PROFILE.close()

                await ctx.send("아쉽지만 배팅금액은 제가 가져갈께요~")

                Del(1)

                MONEY = Checking_Money(CMD_AUTHOR_USER)
                embed = discord.Embed(title = f"", descripton = f"")
                embed.add_field(name = f"보유자산 : ", value = f"{MONEY}원", inline = True)
                embed.set_footer(text = CMD_AUTHOR_USER)
        
        
                await ctx.send(embed = embed)

        elif Money > int(USER_MONEY):
            await ctx.send(f"보유하고 있는 자산보다 더 많은 돈은 배팅할 수 없어요! \n{USER_MONEY}이하로 배팅해주세요!")
    else:
        await ctx.send("베팅금액은 최소 500원 이상부터 입니다.")   

@bot.command()
async def 지급(ctx, *arg):
    ENTERED_DATA = list(arg)
    CMD_AUTHOR_USER = ctx.author
    CMD_AUTHOR_USER_ID = CMD_AUTHOR_USER.id
    ADMIN_ID = 688705421082361856
    
    BLANK_CHECK = len(ENTERED_DATA)
    #await ctx.send(f"BLANK_CHECK : {BLANK_CHECK}")
    
    if BLANK_CHECK == 2:
        RECIPIENTER = ENTERED_DATA[0]
        SENDMONEY = int(ENTERED_DATA[1])
        pass

    elif BLANK_CHECK == 3:
        RECIPIENTER = str(ENTERED_DATA[0] + " " + ENTERED_DATA[1])
        SENDMONEY = int(ENTERED_DATA[2])
        pass

    USER_FILE_CHECK = os.path.exists(f"{User_Data_dir}\\User_Data\\{RECIPIENTER}.json")

    if ADMIN_ID == CMD_AUTHOR_USER_ID:
        if USER_FILE_CHECK == True:
            with open(f"{User_Data_dir}\\User_Data\\{RECIPIENTER}.json", "r") as RECIPIENT_USER_PROFILE:
                RECIPIENT_USER_DATA = json.load(RECIPIENT_USER_PROFILE)
                RECIPIENT_USER_PROFILE.close()

            EXISITING_USERMONEY = RECIPIENT_USER_DATA['USERMONEY'] 
            RECIPIENT_USER_DATA['USERMONEY'] = int(EXISITING_USERMONEY) + int(SENDMONEY)

            with open(f"{User_Data_dir}\\User_Data\\{RECIPIENTER}.json", "w") as RECIPIENT_USER_PROFILE:
                json.dump(RECIPIENT_USER_DATA, RECIPIENT_USER_PROFILE, indent = 4)
                RECIPIENT_USER_PROFILE.close()

            MONEY = Checking_Money(RECIPIENTER)
            embed = discord.Embed(title = f"", descripton = f"")
            embed.add_field(name = f"보유자산 : ", value = f"{MONEY}원", inline = True)
            embed.set_footer(text = f"{RECIPIENTER}")
    
    
            await ctx.send(embed = embed)

        else:
            await ctx.send(f"[{RECIPIENTER}]님의 데이터를 찾을수 없습니다. ")
    

    else:
        await ctx.send("이 명령어를 사용할 권한이 없습니다.")

@bot.command()
async def 수정(ctx, *arg):
    ENTERED_DATA = list(arg)
    CMD_AUTHOR_USER = ctx.author
    CMD_AUTHOR_USER_ID = CMD_AUTHOR_USER.id
    ADMIN_ID = 688705421082361856
    
    BLANK_CHECK = len(ENTERED_DATA)
    #await ctx.send(f"BLANK_CHECK : {BLANK_CHECK}")
    
    if BLANK_CHECK == 2:
        RECIPIENTER = ENTERED_DATA[0]
        EDITEDMONEY = int(ENTERED_DATA[1])
        pass

    elif BLANK_CHECK == 3:
        RECIPIENTER = str(ENTERED_DATA[0] + " " + ENTERED_DATA[1])
        EDITEDMONEY = int(ENTERED_DATA[2])
        pass

    USER_FILE_CHECK = os.path.exists(f"{User_Data_dir}\\User_Data\\{RECIPIENTER}.json")

    if ADMIN_ID == CMD_AUTHOR_USER_ID:
        if USER_FILE_CHECK == True:
            with open(f"{User_Data_dir}\\User_Data\\{RECIPIENTER}.json", "r") as RECIPIENT_USER_PROFILE:
                RECIPIENT_USER_DATA = json.load(RECIPIENT_USER_PROFILE)
                RECIPIENT_USER_PROFILE.close()

            RECIPIENT_USER_DATA['USERMONEY'] = EDITEDMONEY
            

            with open(f"{User_Data_dir}\\User_Data\\{RECIPIENTER}.json", "w") as RECIPIENT_USER_PROFILE:
                json.dump(RECIPIENT_USER_DATA, RECIPIENT_USER_PROFILE, indent = 4)
                RECIPIENT_USER_PROFILE.close()

            MONEY = Checking_Money(RECIPIENTER)
            embed = discord.Embed(title = f"", descripton = f"")
            embed.add_field(name = f"보유자산 : ", value = f"{MONEY}원", inline = True)
            embed.set_footer(text = f"{RECIPIENTER}")
    
    
            await ctx.send(embed = embed)

        else:
            await ctx.send(f"[{RECIPIENTER}]님의 데이터를 찾을수 없습니다. ")
    

    else:
        await ctx.send("이 명령어를 사용할 권한이 없습니다.")

@bot.command()
async def 송금(ctx, *arg):
    ENTERED_DATA = list(arg)
    CMD_AUTHOR_USER = ctx.author
    CMD_AUTHOR_USER_ID = CMD_AUTHOR_USER.id
    AUTHOR_MONEY = int(Checking_Money(CMD_AUTHOR_USER))
    
    BLANK_CHECK = len(ENTERED_DATA)
    #await ctx.send(f"BLANK_CHECK : {BLANK_CHECK}")
    
    if BLANK_CHECK == 2:
        RECIPIENTER = ENTERED_DATA[0]
        SENDMONEY = int(ENTERED_DATA[1])
        pass

    elif BLANK_CHECK == 3:
        RECIPIENTER = str(ENTERED_DATA[0] + " " + ENTERED_DATA[1])
        SENDMONEY = int(ENTERED_DATA[2])
        pass

    USER_FILE_CHECK = os.path.exists(f"{User_Data_dir}\\User_Data\\{RECIPIENTER}.json")

    
    if SENDMONEY <= AUTHOR_MONEY:

        if USER_FILE_CHECK == True:
            #============================송금인 돈 데이터 수정============================================
            with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "r") as AUTHOR_USER_PROFILE:
                AUTHOR_USER_DATA = json.load(AUTHOR_USER_PROFILE)
                AUTHOR_USER_PROFILE.close()

            EXISITING_USERMONEY = AUTHOR_USER_DATA['USERMONEY']
            AUTHOR_USER_DATA['USERMONEY'] = int(EXISITING_USERMONEY) - int(SENDMONEY)

            with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "w") as AUTHOR_USER_PROFILE:
                json.dump(AUTHOR_USER_DATA, AUTHOR_USER_PROFILE, indent = 4)
                AUTHOR_USER_PROFILE.close()
            #============================송금인 돈 데이터 수정============================================
            #============================수신인 돈 데이터 수정============================================
            with open(f"{User_Data_dir}\\User_Data\\{RECIPIENTER}.json", "r") as RECIPIENT_USER_PROFILE:
                RECIPIENT_USER_DATA = json.load(RECIPIENT_USER_PROFILE)
                RECIPIENT_USER_PROFILE.close()

            EXISITING_USERMONEY = RECIPIENT_USER_DATA['USERMONEY'] 
            RECIPIENT_USER_DATA['USERMONEY'] = int(EXISITING_USERMONEY) + int(SENDMONEY)

            with open(f"{User_Data_dir}\\User_Data\\{RECIPIENTER}.json", "w") as RECIPIENT_USER_PROFILE:
                json.dump(RECIPIENT_USER_DATA, RECIPIENT_USER_PROFILE, indent = 4)
                RECIPIENT_USER_PROFILE.close()
            #============================수신인 돈 데이터 수정============================================

            AUTHOR_MONEY = Checking_Money(CMD_AUTHOR_USER)
            RECIPIENTER_MONEY = Checking_Money(RECIPIENTER)
            embed = discord.Embed(title = f"", descripton = f"")
            embed.add_field(name = f"{CMD_AUTHOR_USER}님의 자산 : ", value = f"{AUTHOR_MONEY}원", inline = False)
            embed.add_field(name = f"{RECIPIENTER}님의 자산 : ", value = f"{RECIPIENTER_MONEY}원", inline = False)
            embed.set_footer(text = f"송금액 : {SENDMONEY}원")


            await ctx.send(embed = embed)

        else:
            await ctx.send(f"[{RECIPIENTER}]님의 데이터를 찾을수 없습니다. ")
    
    elif SENDMONEY > AUTHOR_MONEY:
        await ctx.send(f"[{SENDMONEY}원]은 현재 당신의 자산인 [{AUTHOR_MONEY}원]보다 많습니다.\n송금액을 줄여주세요.")

    else:
        await ctx.send(f"입력이 잘못되었어요. 다시 한 번 입력해주세요!")

@bot.command()
async def 주식(ctx, *arg):
    try:    
        
        Command = list(arg)
        CMD_AUTHOR_USER = ctx.author
        OBJ_COUNT = len(Command)
        FUNC_NAME = Command[0]
        #SHOW_CURRENT_STOCK_LIST = ['롤', '마크', '발로란트', '배그', '오버워치']

        if OBJ_COUNT == 2:
            OBJ_ONE = Command[1]#STOCK_NAME
            pass
        
        elif OBJ_COUNT == 3:
            OBJ_ONE = Command[1]
            OBJ_TWO = Command[2]#BUY_AMOUNT / SELL_AMOUNT
            pass
        
        

        if FUNC_NAME == "목록":
            STOCK_LIST_COUNTER = len(SHOW_CURRENT_STOCK_LIST)
            embed = discord.Embed(title = f"", description = "")
            for STOCK_LIST_COUNT in range(STOCK_LIST_COUNTER):
                STOCK_NAME = str(SHOW_CURRENT_STOCK_LIST[STOCK_LIST_COUNT])
                STOCK_PRICE = Checking_Stock_Price(STOCK_NAME)
                embed.add_field(name = f"{STOCK_NAME}", value = f"{STOCK_PRICE}원", inline = True)
            
            
            embed.set_footer(text = f"현재 구매 가능한 주식 목록입니다.")

            await ctx.send(embed = embed)

        elif FUNC_NAME == "수수료":
            global REAL_SELL_COMMISSION
            SELL_COMMISSION = round(float((int(OBJ_ONE) / 100) * 100), 2)
            REAL_SELL_COMMISSION = round(float(int(OBJ_ONE) / 100), 2)

            await ctx.send(f"수수료 설정 완료\n현재 수수료 : {SELL_COMMISSION}%")



        elif FUNC_NAME == "가격":
            STOCK_NAME = str(OBJ_ONE)
            STOCK_LIST_CHECK = os.path.exists(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json")


            if STOCK_LIST_CHECK == True:
                with open(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json", "r", encoding = "utf-8") as STOCK_LIST_PROFILE:
                    STOCK_LIST_DATA = json.load(STOCK_LIST_PROFILE)
                    STOCK_LIST_PROFILE.close()

                STOCK_PRICE = int(STOCK_LIST_DATA['STOCK_PRICE'])

                await ctx.send(f"{STOCK_NAME}의 가격 : {STOCK_PRICE}원")

        elif FUNC_NAME == "구매":
            try:
                STOCK_NAME = str(OBJ_ONE)
                BUY_AMOUNT = int(OBJ_TWO)

                STOCK_LIST_CHECK = os.path.exists(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json")

                if STOCK_LIST_CHECK == True:
                    with open(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json", "r", encoding = "utf-8") as BUY_STOCK_PROFILE:
                        BUY_STOCK_DATA = json.load(BUY_STOCK_PROFILE)
                        BUY_STOCK_PROFILE.close()

                    STOCK_PRICE = int(BUY_STOCK_DATA['STOCK_PRICE'])
                    TOTAL_PRICE = int(STOCK_PRICE) * int(BUY_AMOUNT)

                    with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "r", encoding = "utf-8") as BUYER_PROFILE:
                        BUYER_DATA = json.load(BUYER_PROFILE)
                        BUYER_PROFILE.close()

                    BUYER_MONEY = BUYER_DATA['USERMONEY']
                    
                    if TOTAL_PRICE <= BUYER_MONEY: #USERDATA의 USERMONEY가 충분하다면 밑의 코드 실행

                        with open(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json", "r", encoding = "utf-8") as BUY_STOCK_PROFILE:
                            BUY_STOCK_DATA = json.load(BUY_STOCK_PROFILE)
                            BUY_STOCK_PROFILE.close()

                        STOCK_NAME = str(BUY_STOCK_DATA['STOCK_NAME'])

                        with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "r", encoding = "utf-8") as BUYER_PROFILE:
                            BUYER_DATA = json.load(BUYER_PROFILE)
                            BUYER_PROFILE.close()

                        USER_OWN_STOCK_CHECK = f'STOCK_{STOCK_NAME}'

                        
                        if USER_OWN_STOCK_CHECK in BUYER_DATA:
                            EXISITING_USER_STOCK = BUYER_DATA[f'STOCK_{str(STOCK_NAME)}']

                        else:
                            EXISITING_USER_STOCK = 0

                        with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "w", encoding = "utf-8") as BUYER_PROFILE:
                            BUYER_DATA['USERMONEY'] = int(BUYER_MONEY) - int(TOTAL_PRICE)
                            BUYER_DATA[f'STOCK_{STOCK_NAME}'] = BUY_AMOUNT + EXISITING_USER_STOCK
                            json.dump(BUYER_DATA, BUYER_PROFILE, indent = 4)

                        
                        CURRENT_USER_MONEY = Checking_Money(CMD_AUTHOR_USER)
                        CURRENT_USER_STOCK = Checking_Stock(CMD_AUTHOR_USER, STOCK_NAME)

                        embed = discord.Embed(title = f"", descripton = f"")
                        embed.add_field(name = f"보유자산 : ", value = f"{CURRENT_USER_MONEY}원", inline = True)
                        embed.add_field(name = f"{STOCK_NAME} 보유 주식 : ", value = f"{CURRENT_USER_STOCK}주", inline = True)
                        embed.set_footer(text = CMD_AUTHOR_USER)                                
                        await ctx.send(embed = embed)

                    else:
                        await ctx.send(f"총 구매 금액[{TOTAL_PRICE}원]은 현재 당신의 소지 금액 [{BUYER_MONEY}원]보다 큽니다")
            except:
                await ctx.send("입력받은 인자의 갯수가 너무 많거나 부족합니다.")       

        elif FUNC_NAME == "판매":
            try:

                STOCK_NAME = str(OBJ_ONE)
                SELL_AMOUNT = int(OBJ_TWO)

                STOCK_LIST_CHECK = os.path.exists(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json")

                if STOCK_LIST_CHECK == True:
                    with open(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json", "r", encoding = "utf-8") as SELL_STOCK_PROFILE:
                        SELL_STOCK_DATA = json.load(SELL_STOCK_PROFILE)
                        SELL_STOCK_PROFILE.close()

                    STOCK_PRICE = int(SELL_STOCK_DATA['STOCK_PRICE'])
                    TOTAL_PRICE = int(STOCK_PRICE) * int(SELL_AMOUNT)

                    SELLER_MONEY = Checking_Money(CMD_AUTHOR_USER)
                    
                    
                    CURRENT_USER_STOCK_CHECK = Checking_Stock(CMD_AUTHOR_USER, STOCK_NAME)
                    
                    if SELL_AMOUNT <= CURRENT_USER_STOCK_CHECK:

                        with open(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json", "r", encoding = "utf-8") as SELL_STOCK_PROFILE:
                            SELL_STOCK_DATA = json.load(SELL_STOCK_PROFILE)
                            SELL_STOCK_PROFILE.close()

                        STOCK_NAME = str(SELL_STOCK_DATA['STOCK_NAME'])

                        with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "r", encoding = "utf-8") as SELLER_PROFILE:
                            SELLER_DATA = json.load(SELLER_PROFILE)
                            SELLER_PROFILE.close()

                        USER_OWN_STOCK_CHECK = f'STOCK_{STOCK_NAME}'

                        
                        if USER_OWN_STOCK_CHECK in SELLER_DATA:
                            EXISITING_USER_STOCK = SELLER_DATA[f'STOCK_{STOCK_NAME}']
                            pass

                        else:
                            EXISITING_USER_STOCK = 0
                            pass


                        with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "w", encoding = "utf-8") as SELLER_PROFILE:
                            SELLER_DATA['USERMONEY'] = int(SELLER_MONEY) + int(TOTAL_PRICE)
                            SELLER_DATA[f'STOCK_{STOCK_NAME}'] = EXISITING_USER_STOCK - SELL_AMOUNT
                            json.dump(SELLER_DATA, SELLER_PROFILE, indent = 4)

                    
                        CURRENT_USER_MONEY = Checking_Money(CMD_AUTHOR_USER)
                        CURRENT_USER_STOCK = Checking_Stock(CMD_AUTHOR_USER, STOCK_NAME)

                        embed = discord.Embed(title = f"", descripton = f"")
                        embed.add_field(name = f"보유자산 : ", value = f"{CURRENT_USER_MONEY}원", inline = True)
                        embed.add_field(name = f"{STOCK_NAME} 보유 주식 : ", value = f"{CURRENT_USER_STOCK}주", inline = True)
                        embed.set_footer(text = CMD_AUTHOR_USER)                                
                        await ctx.send(embed = embed)

                    elif SELL_AMOUNT > CURRENT_USER_STOCK_CHECK:
                        await ctx.send(f"현재 당신이 보유하고 있는 [{CURRENT_USER_STOCK_CHECK}주]보다\n입력된 값이 큽니다. 다시 입력해주세요.")
                else:
                    await ctx.send("해당 주식의 데이터가 없거나 입력된 데이터가 잘못되었습니다.")
            except:
                await ctx.send("입력받은 인자의 갯수가 너무 많거나 부족합니다.")       

    except:
        error_msg = await ctx.send("명령어가 잘못되었습니다. 다시 입력하여주세요")
        Del(5)
        await error_msg.delete()

@bot.command()
async def 구제금융(ctx):
    CMD_AUTHOR_USER = ctx.author
    QUALIFICATION = 0

    with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "r", encoding = "utf-8") as READ_USER_PROFILE:
        READ_USER_DATA = json.load(READ_USER_PROFILE)
        READ_USER_PROFILE.close()

    POOR_OWN_MONEY = READ_USER_DATA["USERMONEY"]
    SHOW_CURRENT_STOCK_LIST_COUNTER = len(SHOW_CURRENT_STOCK_LIST)

    for STOCK_CHECK_COUNT in range(SHOW_CURRENT_STOCK_LIST_COUNTER):
        STOCK_OWN_CHECK = SHOW_CURRENT_STOCK_LIST[STOCK_CHECK_COUNT]
        STOCK_CHECK_NAME = f"STOCK_{STOCK_OWN_CHECK}"

        with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "r", encoding = "utf-8") as READ_USER_PROFILE:
            READ_USER_DATA = json.load(READ_USER_PROFILE)
            READ_USER_PROFILE.close()

        if STOCK_CHECK_NAME in READ_USER_DATA:
            QUALIFICATION = QUALIFICATION + 1
            

        elif STOCK_CHECK_NAME not in READ_USER_DATA:
            QUALIFICATION = QUALIFICATION + 0
            

    if QUALIFICATION <= 0:
        if POOR_OWN_MONEY <= 10000:
            with open(f"{User_Data_dir}\\User_Data\\{CMD_AUTHOR_USER}.json", "w", encoding = "utf-8") as WRITE_USER_PROFILE:
                READ_USER_DATA["USERMONEY"] = POOR_OWN_MONEY + 100000
                if "SAVE_MONEY_APPLICATION_COUNT" in READ_USER_DATA:
                    READ_USER_DATA["SAVE_MONEY_APPLICATION_COUNT"] = int(READ_USER_DATA["SAVE_MONEY_APPLICATION_COUNT"]) + 1
                else:
                    READ_USER_DATA["SAVE_MONEY_APPLICATION_COUNT"] = 1

                json.dump(READ_USER_DATA, WRITE_USER_PROFILE, indent = 4)
        
        else:
            await ctx.send("당신은 구제금융을 받을만한 사람이 아닙니다.")
    else:
        await ctx.send("당신은 구제금융을 받을만한 사람이 아닙니다.")

    MONEY = Checking_Money(CMD_AUTHOR_USER)
    embed = discord.Embed(title = f"", descripton = f"")
    embed.add_field(name = f"보유자산 : ", value = f"{MONEY}원", inline = True)
    embed.set_footer(text = f"{CMD_AUTHOR_USER}")
    
    await ctx.send(embed = embed)

@bot.command()
async def 가격초기화(ctx):
    WIPE_STOCK_LIST = SHOW_CURRENT_STOCK_LIST
    ARRAY_COUNTER = len(WIPE_STOCK_LIST)
    CMD_AUTHOR_USER_ID = ctx.author.id

    if CMD_AUTHOR_USER_ID == 688705421082361856:
        for STOCK in range(ARRAY_COUNTER):
            STOCK_NAME = str(WIPE_STOCK_LIST[STOCK])

            with open(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json", "r", encoding = "utf-8") as WIPE_STOCK_LIST_PROFILE:
                WIPE_STOCK_LIST_DATA = json.load(WIPE_STOCK_LIST_PROFILE)
                WIPE_STOCK_LIST_PROFILE.close()

            STOCK_PRICE = 10000

            with open(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json", "w", encoding = "utf-8") as WIPE_STOCK_LIST_PROFILE:
                WIPE_STOCK_LIST_DATA['STOCK_PRICE'] = STOCK_PRICE
                json.dump(WIPE_STOCK_LIST_DATA, WIPE_STOCK_LIST_PROFILE, indent = 4)

    else:
        await ctx.send("당신은 이 명령어를 사용할 권한이 없습니다.")

@tasks.loop(seconds = 1)
async def Stock_Change_Cycle(self):
    #=========================변수 선언=========================
    STOCK_LIST_COUNTER = len(SHOW_CURRENT_STOCK_LIST)
    SHOW_STOCK_LIST = []
    NowDay = datetime.datetime.today()
    NOW_MIN = NowDay.minute
    NOW_SEC = NowDay.second
    channel = bot.get_channel(817688404631617546)
    global channel_st
    channel_st = bot.get_channel(838936568273043476)
    #channel_st = bot.get_channel(839531082986422292)#test server
    
    CHANGE_PRICE_STOCK_LIST = SHOW_CURRENT_STOCK_LIST
    ARRAY_COUNTER = len(CHANGE_PRICE_STOCK_LIST)
    #주식 거래장 채널 ID = 838936568273043476
    CHANCE_CHECKER = [1, 2, 3, 4, 5]
    CONTROL = 0
    WARNING = 1
    ADMIN = "심심한데놀아줘#2140" #가격 변동 테스트 용 유저 
    #=========================변수 선언=========================
                
    
    MIN_CHECK = NOW_MIN % 5
    if MIN_CHECK == 0:
        if NOW_SEC == 0:
            await channel_st.purge(limit=100)

            
            embed = discord.Embed(title = f"##[주식 목록 & 주식 가격]##\n\n", description = f"")
            embed.add_field(name = f"마크", value = f"가격 수정중...", inline = False)
            embed.add_field(name = f"발로란트", value = f"가격 수정중...", inline = False)
            embed.add_field(name = f"배그", value = f"가격 수정중...", inline = False)
            embed.add_field(name = f"오버워치", value = f"가격 수정중...", inline = False)
            embed.add_field(name = f"롤", value = f"가격 수정중...", inline = False)
            
            DELAY_EMBED = await channel_st.send(embed = embed)

            for STOCK in range(ARRAY_COUNTER):

                with open(f"{User_Data_dir}\\User_Data\\{ADMIN}.json", "r", encoding = "utf-8") as READ_USER_PROFILE:
                    READ_USER_DATA = json.load(READ_USER_PROFILE)
                    READ_USER_PROFILE.close()

                for STOCK_COUNT in range(STOCK_LIST_COUNTER):
                    STOCK_NAME_BH = SHOW_CURRENT_STOCK_LIST[STOCK_COUNT]
                    STOCK_NAME_CHECK = f"STOCK_{STOCK_NAME_BH}"
                    if STOCK_NAME_CHECK in READ_USER_DATA:
                        SHOW_STOCK_LIST.append(STOCK_NAME_BH) #뒤에 주식 이름

    
                SHOW_STOCK_LIST_COUNTER = len(SHOW_STOCK_LIST)

                for STOCK_COUNT in range(SHOW_STOCK_LIST_COUNTER):
                    STOCK_NAME = str(CHANGE_PRICE_STOCK_LIST[STOCK])
                    STOCK_NAME_CHECK = f'STOCK_{STOCK_NAME}'
                    if STOCK_NAME_CHECK in READ_USER_DATA:
                        USER_OWN_STOCK_AMOUNT = READ_USER_DATA[STOCK_NAME_CHECK]
                        if USER_OWN_STOCK_AMOUNT != 0:
                            CONTROL = 1
                        else:
                            CONTROL = 0
                

                PRICE_CHANGE_RANGE = random.randint(1, 30)
                STOCK_NAME = str(CHANGE_PRICE_STOCK_LIST[STOCK])
                print(f"CONTROL = {CONTROL}")
                print(f"STOCK_NAME = {STOCK_NAME}")
                
                
                if CONTROL == 1:
                    if WARNING != 1:
                        PRICE_CHANGE_PL_MI = 1
                    else:
                        PRICE_CHANGE_PL_MI = random.randint(1, 10)
                else:
                    PRICE_CHANGE_PL_MI = random.randint(1, 10)

                CHANCE_TIME = random.randint(1, 1000)
                CHANCE_RANDOM = random.randint(5000, 10000)
                

                with open(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json", "r", encoding = "utf-8") as STOCK_LIST_PROFILE:
                    STOCK_LIST_DATA = json.load(STOCK_LIST_PROFILE)
                    STOCK_LIST_PROFILE.close()

                STOCK_PRICE_BFCH = STOCK_LIST_DATA['STOCK_PRICE']
                STOCK_CHANGE_RANGE = int(STOCK_PRICE_BFCH) * (PRICE_CHANGE_RANGE / 100)
                
                PRICE_UP_CHECK = "PRICE_UP"
                PRICE_DOWN_CHECK = "PRICE_DOWN"
                
                PRICE_UPDOWN_CHECK = []
                PRICE_UPDOWN_CHECK.append(PRICE_UP_CHECK)
                PRICE_UPDOWN_CHECK.append(PRICE_DOWN_CHECK)

                PRICE_UPDOWN_CHECK_COUNTER = len(PRICE_UPDOWN_CHECK)

                if PRICE_CHANGE_PL_MI <= 5:
                    
                    
                    #await channel_st.send(f"STOCK_NAME = {STOCK_NAME}\nPRICE_CHANGE_PL_MI = {PRICE_CHANGE_PL_MI}\nSTOCK_PRICE_AFCH = {STOCK_PRICE_AFCH}\nSTOCK_CHANGE_RANGE = {round(float(STOCK_CHANGE_RANGE), 0)}\nCHANCE_RANDOM = {CHANCE_RANDOM}\n\n")
                    

                    for COUNT in range(PRICE_UPDOWN_CHECK_COUNTER):


                        if PRICE_UPDOWN_CHECK[COUNT] not in STOCK_LIST_DATA:
                            STOCK_LIST_DATA[PRICE_UPDOWN_CHECK[COUNT]] = 0

                            if PRICE_UPDOWN_CHECK[COUNT] == "PRICE_UP":
                                BEFORE_PRICE_UPDOWN = STOCK_LIST_DATA['PRICE_UP']
                                if BEFORE_PRICE_UPDOWN < 2:
                                    STOCK_LIST_DATA['PRICE_UP'] = BEFORE_PRICE_UPDOWN + 1
                                    STOCK_LIST_DATA['PRICE_DOWN'] = 0
                                    pass
                                    
                                else:
                                    STOCK_LIST_DATA['PRICE_UP'] = BEFORE_PRICE_UPDOWN + 0
                                    STOCK_LIST_DATA['PRICE_DOWN'] = 0
                                    pass

                                if CHANCE_TIME in CHANCE_CHECKER:
                                    STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) + int(CHANCE_RANDOM)
                                    pass

                                else:
                                    LAST_PRICE_UPDOWN_CHANCE = random.randint(1, 10)
                                    if STOCK_PRICE_BFCH <= 3500:

                                        if LAST_PRICE_UPDOWN_CHANCE >= 8:
                                            STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) + int(CHANCE_RANDOM)
                                            pass

                                        else:
                                            STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) + round(float(STOCK_CHANGE_RANGE), 0)
                                            pass
                                    else:
                                        STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) + round(float(STOCK_CHANGE_RANGE), 0)
                                        pass
                        
                            else:
                                pass
                        
                        else:
                            BEFORE_PRICE_UPDOWN = STOCK_LIST_DATA[PRICE_UPDOWN_CHECK[COUNT]]

                            if PRICE_UPDOWN_CHECK[COUNT] == "PRICE_UP":
                                BEFORE_PRICE_UPDOWN = STOCK_LIST_DATA['PRICE_UP']
                                if BEFORE_PRICE_UPDOWN < 2:
                                    STOCK_LIST_DATA['PRICE_UP'] = BEFORE_PRICE_UPDOWN + 1
                                    STOCK_LIST_DATA['PRICE_DOWN'] = 0
                                    pass
                                    
                                else:
                                    STOCK_LIST_DATA['PRICE_UP'] = BEFORE_PRICE_UPDOWN + 0
                                    STOCK_LIST_DATA['PRICE_DOWN'] = 0
                                    pass

                                if CHANCE_TIME in CHANCE_CHECKER:
                                    STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) + int(CHANCE_RANDOM)
                                    pass

                                else:
                                    LAST_PRICE_UPDOWN_CHANCE = random.randint(1, 10)
                                    if STOCK_PRICE_BFCH <= 3500:

                                        if LAST_PRICE_UPDOWN_CHANCE >= 8:
                                            STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) + int(CHANCE_RANDOM)
                                            pass

                                        else:
                                            STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) + round(float(STOCK_CHANGE_RANGE), 0)
                                            pass
                                    else:
                                        STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) + round(float(STOCK_CHANGE_RANGE), 0)
                                        pass
                            else:
                                pass



                elif PRICE_CHANGE_PL_MI >= 6:
                    
                    
                    #await channel_st.send(f"STOCK_NAME = {STOCK_NAME}\nPRICE_CHANGE_PL_MI = {PRICE_CHANGE_PL_MI}\nSTOCK_PRICE_AFCH = {STOCK_PRICE_AFCH}\nSTOCK_CHANGE_RANGE = {round(float(STOCK_CHANGE_RANGE), 0)}\nCHANCE_RANDOM = {CHANCE_RANDOM}\n\n")

                    for COUNT in range(PRICE_UPDOWN_CHECK_COUNTER):


                        if PRICE_UPDOWN_CHECK[COUNT] not in STOCK_LIST_DATA:
                            STOCK_LIST_DATA[PRICE_UPDOWN_CHECK[COUNT]] = 0

                            if PRICE_UPDOWN_CHECK[COUNT] == "PRICE_DOWN":
                                BEFORE_PRICE_UPDOWN = STOCK_LIST_DATA['PRICE_DOWN']
                                if BEFORE_PRICE_UPDOWN < 2:
                                    STOCK_LIST_DATA['PRICE_DOWN'] = BEFORE_PRICE_UPDOWN + 1
                                    STOCK_LIST_DATA['PRICE_UP'] = 0
                                    pass
                                    
                                else:
                                    STOCK_LIST_DATA['PRICE_DOWN'] = BEFORE_PRICE_UPDOWN + 0
                                    STOCK_LIST_DATA['PRICE_UP'] = 0
                                    pass

                                if CHANCE_TIME in CHANCE_CHECKER:
                                    STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) - round((float(STOCK_CHANGE_RANGE) / 10), 0)
                                    pass

                                else:
                                    LAST_PRICE_UPDOWN_CHANCE = random.randint(1, 10)
                                    if STOCK_PRICE_BFCH <= 3500:

                                        if LAST_PRICE_UPDOWN_CHANCE >= 8:
                                            STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) - round((float(STOCK_CHANGE_RANGE) / 10), 0)
                                            pass

                                        else:
                                            STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) - round(float(STOCK_CHANGE_RANGE), 0)
                                            pass
                                    else:
                                        STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) - round(float(STOCK_CHANGE_RANGE), 0)
                                        pass
                            else:
                                pass
                            

                        else:
                            BEFORE_PRICE_UPDOWN = STOCK_LIST_DATA[PRICE_UPDOWN_CHECK[COUNT]]

                            if PRICE_UPDOWN_CHECK[COUNT] == "PRICE_DOWN":
                                BEFORE_PRICE_UPDOWN = STOCK_LIST_DATA['PRICE_DOWN']
                                if BEFORE_PRICE_UPDOWN < 2:
                                    STOCK_LIST_DATA['PRICE_DOWN'] = BEFORE_PRICE_UPDOWN + 1
                                    STOCK_LIST_DATA['PRICE_UP'] = 0
                                    pass
                                    
                                else:
                                    STOCK_LIST_DATA['PRICE_DOWN'] = BEFORE_PRICE_UPDOWN + 0
                                    STOCK_LIST_DATA['PRICE_UP'] = 0
                                    pass

                                if CHANCE_TIME in CHANCE_CHECKER:
                                    STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) - round((float(STOCK_CHANGE_RANGE) / 10), 0)
                                    pass

                                else:
                                    LAST_PRICE_UPDOWN_CHANCE = random.randint(1, 10)
                                    if STOCK_PRICE_BFCH <= 3500:

                                        if LAST_PRICE_UPDOWN_CHANCE >= 8:
                                            STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) - round((float(STOCK_CHANGE_RANGE) / 10), 0)
                                            pass

                                        else:
                                            STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) - round(float(STOCK_CHANGE_RANGE), 0)
                                            pass
                                    else:
                                        STOCK_PRICE_AFCH = int(STOCK_PRICE_BFCH) - round(float(STOCK_CHANGE_RANGE), 0)
                                        pass
                            else:
                                pass



                
                with open(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json", "w", encoding = "utf-8") as STOCK_LIST_PROFILE:
                    STOCK_LIST_DATA['STOCK_PRICE'] = STOCK_PRICE_AFCH
                    json.dump(STOCK_LIST_DATA, STOCK_LIST_PROFILE, indent = 4)

               #=================================================가격 이상 판별 테스트 코드=================================================
                
                TEST_VALUE_CHECK = "STOCK_PRICE_CHECK"  

                with open(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json", "r", encoding = "utf-8") as STOCK_LIST_PROFILE:
                    STOCK_LIST_DATA = json.load(STOCK_LIST_PROFILE)
                    STOCK_LIST_PROFILE.close()

                if TEST_VALUE_CHECK not in STOCK_LIST_DATA:
                    with open(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json", "w", encoding = "utf-8") as STOCK_LIST_PROFILE:
                        STOCK_LIST_DATA['STOCK_PRICE_CHECK'] = str(STOCK_PRICE_AFCH)
                        json.dump(STOCK_LIST_DATA, STOCK_LIST_PROFILE, indent = 4)
                else:
                    EXISITING_VALUE = STOCK_LIST_DATA['STOCK_PRICE_CHECK']
                    with open(f"{User_Data_dir}\\Stock_List\\{STOCK_NAME}.json", "w", encoding = "utf-8") as STOCK_LIST_PROFILE:
                        STOCK_LIST_DATA['STOCK_PRICE_CHECK'] = f"{EXISITING_VALUE}_{str(STOCK_PRICE_AFCH)}"
                        json.dump(STOCK_LIST_DATA, STOCK_LIST_PROFILE, indent = 4)
                    
                #=================================================가격 이상 판별 테스트 코드=================================================
                
            embed = discord.Embed(title = f"##[주식 목록 & 주식 가격]##\n\n", description = f"")

            for STOCK in range(ARRAY_COUNTER):
                STOCK_NAME = str(CHANGE_PRICE_STOCK_LIST[STOCK])
                STOCK_PRICE = Checking_Stock_Price(STOCK_NAME)
                embed.add_field(name = f"{STOCK_NAME}", value = f"{STOCK_PRICE}원", inline = False)
            
            await DELAY_EMBED.edit(embed = embed)

            Del(5)

        

    else:
        pass  




    

    
            
            

@bot.command()
async def 등록인원(ctx):
    embed = discord.Embed(title = f"[##자가진단 등록 인원##]", description = f"1. 이건보\n2. 이윤행 \n3. 김기정 \n4. 정윤호 \n5. 종다훈 \n6. 고준혁 \n7. 임원경 \n8. 두동규")
    await ctx.send(embed = embed)

@bot.command()
async def 자가진단(ctx, *arg):
    UserData = list(arg) #UserData[0] = UserName / UserData[1] = UserBirth / UserData[2] = UserPass
    
    msg = await ctx.send("자가진단을 진행하고 있습니다. (약 30초 ~ 1분 정도 소요됩니다.)")

    Courrent_Status = myHealthy_SelfCheck(UserData[0])

    if Courrent_Status != 1:
        await msg.send("자가진단에 실패하였습니다. 제작자를 호출하여주세요.")

    elif Courrent_Status == 1:
        embed = discord.Embed(title = f"[##자가 진단 완료##]", description = f"##<{UserData[0]}>님의 자가진단을 완료하였습니다##", color=0x00ff00)
        await msg.delete()
        await ctx.send(embed = embed)

    


        


@bot.command()
async def 마이크(ctx, *, arg):
    await ctx.send(content=arg, tts=True)

"""
@bot.command()
async def 테스트(ctx, arg):
    testVar = Del(arg)
    try:
        await ctx.send(f"딜레이 테스트 (sec)  : {testVar}sec")

    except:
        await ctx.send(f"딜레이 테스트 (sec)  : {testVar}sec")
        """
@bot.command()
async def 주사위놀이(ctx):
    
    #봇과의 대전
    Rnd_dice_BOT = random.randint(1,6)
    Rnd_dice_USER = random.randint(1, 6)

    embed_1=discord.Embed(title = f'[##주사위 게임##]', description = f'##더 높은 주사위 눈이 나온 사람이 승리##', color=0x00ff00)
    embed_2=discord.Embed(title = f'[##주사위 게임##]', description = f'##통돌이의 주사위 눈의 갯수는 {Rnd_dice_BOT}개 입니다##', color=0x00ff00)
    embed_3=discord.Embed(title = f'[##주사위 게임##]', description = f'##당신의 주사위 눈의 갯수는 {Rnd_dice_USER}개 입니다##', color=0x00ff00)
    
        
    msg = await ctx.send(embed = embed_1)
    time.sleep(1.5)
    await msg.edit(embed = embed_2)
    time.sleep(1.5)
    await msg.edit(embed = embed_3)
    time.sleep(0.7)
    await msg.delete()

    if Rnd_dice_BOT > Rnd_dice_USER:
        embed=discord.Embed(title = f'[##주사위 게임##]', description = f'##통돌이의 주사위 갯수가 {Rnd_dice_BOT}으로 \n더 높으므로 통돌이의 승리##', color=0x00ff00)
        await ctx.send(embed = embed)

    elif Rnd_dice_USER > Rnd_dice_BOT:
        embed=discord.Embed(title = f'[##주사위 게임##]', description = f'##당신의 주사위 갯수가 {Rnd_dice_USER}으로 \n더 높으므로 당신의 승리##', color=0x00ff00)
        await ctx.send(embed = embed)
            
    elif Rnd_dice_USER == Rnd_dice_BOT:
        embed=discord.Embed(title = f'[##주사위 게임##]', description = f'##통돌이, 당신의 주사위 갯수가 {Rnd_dice_USER}으로 \n 같으므로  무승부##', color=0x00ff00)
        await ctx.send(embed = embed)
        

    

@bot.command()
async def 클래스룸(ctx, *arg):
    ClsData = list(arg) #ClsData[0] 요일 / ClsData[1] 교시
    
    ClsData[0] = int(ClsData[0])
    ClsData_Type = type(ClsData[0])
    await ctx.send(f"ClsData[0] = {ClsData_Type}")

    if ClsData[0] == 0:
        Print_Dotw = "월요일"
        pass

    elif ClsData[0] == 1:
        Print_Dotw = "화요일"
        pass
    
    elif ClsData[0] == 2:
        Print_Dotw = "수요일"
        pass
    
    elif ClsData[0] == 3:
        Print_Dotw = "목요일"
        pass

    elif ClsData[0] == 4:
        Print_Dotw = "금요일"
        pass

    else:
        Print_Dotw = "주말"
        pass

    if ClsData[0] <= 4:
        todSub = Today_Dotw_Checker(int(ClsData[0]))
        Today = datetime.datetime.today()
        
        
        msg1 = await ctx.send("현재 클래스룸 접속중입니다. 잠시만 기다려주십시오.")

        nowSub = Auto_ClsRoom_Loader(todSub[1], int(ClsData[1])) #nowSub[0] 과목 / nowSub[1] 기능 실행 소요시간
        await msg1.edit(content = f"{Print_Dotw} {ClsData[1]}교시의 과목인 [{nowSub[0]}]의 클래스룸으로 접속을 완료하였습니다.")
        await ctx.send(f"소요시간 : {nowSub[1]}초")

    elif ClsData[0] >= 5:
        await ctx.send("해당 요일은 주말입니다. 따라서 과목데이터가 존재하지 않습니다.")



@bot.command()
async def 다음교시(ctx, *, arg): #다고침!!!!!!!!!!!!!!!!!!!!!!!! 이거 고치는데 3일 넘게 걸린듯;;

    p1 = ["5", "5qks", "5반"]
    p2 = ["4", "4qks", "4반"]
    p3 = ["2", "2qks", "2반"]

    if arg in p1:
        nextSub_Embed = Next_Period_Sub_Send(5)
        await ctx.send(embed=nextSub_Embed)

    elif arg in p2:

        nextSub_Embed = Next_Period_Sub_Send(4)
        await ctx.send(embed=nextSub_Embed)

    elif arg in p3:

        nextSub_Embed = Next_Period_Sub_Send(2)
        await ctx.send(embed=nextSub_Embed)



    
    
@tasks.loop(seconds=10)
async def kimkijung(self):
    
    channel = bot.get_channel(txtchId)

    Rnd_Kijung = random.randint(1, 100)


    if Rnd_Kijung in range(1,10):
        msg = await channel.send(content = f"김기정 시간당 200만원 고급 창부", tts = True)
        time.sleep(5)
        await msg.delete()










@tasks.loop(seconds=1)
async def Auto_Check(self):
    nowDay = datetime.datetime.today()
    Dotw = nowDay.weekday()
    Td_Hour = nowDay.hour
    Td_min = nowDay.min
    Td_sec = nowDay.second
    channel = bot.get_channel(817688404631617546)

    if Dotw != 5 or 6:
        if Td_Hour == 16:
            if Td_min == 19:
                if Td_sec == 0:
                    runningTime_st = time.perf_counter()
                    UserData = User6_data
                    USER_NAME = UserData[0]
                    msg = await channel.send("자가진단을 진행하고 있습니다. (약 30초 ~ 1분 정도 소요됩니다.)")

                    Courrent_Status = myHealthy_SelfCheck(USER_NAME)

                    runningTime_fi = time.perf_counter()
                    runningTime = runningTime_fi - runningTime_st

                    if Courrent_Status != 1:
                        await msg.edit(content = "자가진단에 실패하였습니다. 제작자를 호출하여주세요.")

                    elif Courrent_Status == 1:
                        embed = discord.Embed(title = f"[##자가 진단 완료##]", description = f"##<{UserData[0]}>님의 자가진단을 완료하였습니다##", color=0x00ff00)
                        embed.set_footer(text = f"소요시간 : {runningTime}초")
                        await msg.delete()
                        await channel.send(embed = embed)
    
"""
@tasks.loop(seconds=1)
async def Unyang_Period_Check(self):
    nowPeriod_fin = 0
    Td_Date = datetime.datetime.today()
    Td_Dotw = Td_Date.weekday()
    Td_hour = Td_Date.hour
    Td_min = Td_Date.minute
    Td_sec = Td_Date.second

    nowPeriod = [] #현재 교시를 저장할 배열
    todSub_Array = [] #각 반의 과목을 저장할 배열

    channel = bot.get_channel(txtchId) #txtchId에 할당된 채널 아이디를 기준으로 봇이 메세지를 보낼 채널 선정

    todSub_Array = Today_Dotw_Checker(Td_Dotw) #현재 요일의 각 반의 과목 배열을 받아와 todSub_Array 배열에 저장
    nowPeriod = Get_Now_Period(Td_hour, Td_min, Td_sec) #현재 교시를 Td_hour, Td_min값을 기준으로 측정해 nowPeriod배열에 저장
    nowPeriod_fin = Period_Changer(nowPeriod) #현재 교시의 값이 배열을 지정할 수 있도록 변환
    todDotw = Get_Dotw(Td_Dotw) #현재의 Dotw값을 받아서 알맞은 요일을 반환

    tts_arg = "출첵"

    


    if nowPeriod != None:

        if Td_min == 10:
            print(f"{todDotw}")
            print(f"운양고 {nowPeriod}"교시)

            embed = discord.Embed(title = f'[{nowPeriod}교시 출첵을 해야할 시간입니다.]', description = f'##{nowPeriod}교시 출첵 알람##', color=0x00ff00)
            embed.add_field(name=f'[운양고 2학년 5반]', value=f'[{todSub_Array[2][nowPeriod_fin]}]', inline=False)

"""
        
@tasks.loop(seconds=1)
async def Sawoo_Period_Check(self): #완성....    

    nowPeriod_fin = 0

    Td_Date = datetime.datetime.today()
    Td_Dotw = Td_Date.weekday()
    Td_hour = Td_Date.hour
    Td_min = Td_Date.minute
    Td_sec = Td_Date.second

    nowPeriod = [] #현재 교시를 저장할 배열
    todSub_Array = [] #각 반의 과목을 저장할 배열

    channel = bot.get_channel(txtchId) #txtchId에 할당된 채널 아이디를 기준으로 봇이 메세지를 보낼 채널 선정

    todSub_Array = Today_Dotw_Checker(Td_Dotw) #현재 요일의 각 반의 과목 배열을 받아와 todSub_Array 배열에 저장
    nowPeriod = Get_Now_Period(Td_hour, Td_min, Td_sec) #현재 교시를 Td_hour, Td_min값을 기준으로 측정해 nowPeriod배열에 저장
    nowPeriod_fin = Period_Changer(nowPeriod) #현재 교시의 값이 배열을 지정할 수 있도록 변환
    todDotw = Get_Dotw(Td_Dotw) #현재의 Dotw값을 받아서 알맞은 요일을 반환

    tts_arg = "출첵"
        

    

    if nowPeriod != None: #nowPeriod 값이 재 시간이 아닌 경우 None으로 리턴되어 재시간이 아닐시 멈춤

        if Td_min == 10:    
            print(f"{todDotw}")
            print(f"사우고 {nowPeriod}교시")

            embed=discord.Embed(title = f'[{nowPeriod}교시 출첵을 해야할 시간입니다.]', description = f'##{nowPeriod}교시 출첵 알람##', color=0x00ff00)
            #embed.add_field(name=f'[김포고 2학년 6반]', value=f'[{todSub_Array[3][nowPeriod_fin]}]', inline=False)
            embed.add_field(name=f'[사우고 2학년 5반]', value=f'[{todSub_Array[2][nowPeriod_fin]}]', inline=False)
            embed.add_field(name=f'[사우고 2학년 4반]', value=f'[{todSub_Array[1][nowPeriod_fin]}]', inline=False)
            embed.add_field(name=f'[사우고 2학년 2반]', value=f'[{todSub_Array[0][nowPeriod_fin]}]', inline=False)
            
            await channel.send(content = tts_arg, tts = True)
            time.sleep(1)
            await channel.send(embed=embed)
            time.sleep(1)
            

            #if not vc.is_playing():
            #    mp3 = "D:\\Check_Sound_File\\2021-03-29 10-32-45.mkv"
            #    vc.play(FFmpegPCMAudio(mp3, **FFMPEG_OPTIONS))
            
            #else:
            #    await channel.send("이미 재생되고 있습니다!")

        elif Td_min == 9:
            print(f"{todDotw}")
            print(f"{nowPeriod}교시")

            embed=discord.Embed(title = f'[{nowPeriod}교시 출첵을 해야할 시간입니다.]', description = f'##{nowPeriod}교시 출첵 알람##', color=0x00ff00)
            #embed.add_field(name=f'[김포고 2학년 6반]', value=f'[{todSub_Array[3][nowPeriod_fin]}]', inline=False)
            embed.add_field(name=f'[사우고 2학년 5반]', value=f'[{todSub_Array[2][nowPeriod_fin]}]', inline=False)
            embed.add_field(name=f'[사우고 2학년 4반]', value=f'[{todSub_Array[1][nowPeriod_fin]}]', inline=False)
            embed.add_field(name=f'[사우고 2학년 2반]', value=f'[{todSub_Array[0][nowPeriod_fin]}]', inline=False)

            time.sleep(1)
            await channel.send(embed=embed)
            time.sleep(1)
            
    elif nowPeriod == None:
        pass
    

    if Td_Dotw == 2: # 수요일과 수요일이 아닌 날의 마지막 교시를 확인하여 루프를 종료하는 구문
        if nowPeriod_fin == 6:
            Period_Check.stop()

    elif Td_Dotw != 2:
        if nowPeriod_fin == 7:
            Period_Check.stop()
    
    else:
        pass



bot.run(BOT_TOKEN)
