#from Class.USER_JSON_RW.rw_json import READ_WRITE
from genericpath import exists
import sys
import datetime
import os
import random
import discord
import json
#sys.path.append("D:\\건보\\동기화\\Naver MYBOX\\C언어반 예습\\매크로\\통돌이\\Class\\USER_JSON_RW")
#from rw_json import READ_WRITE
from Class.USER_JSON_RW.rw_json import READ_WRITE



DASKTOP_DIR = "C:\\Users\\leegu\\Desktop\\통돌이"
SCHOOL_COM_DIR = "C:\\Users\\Admin\\Downloads\\통돌이"
MAINCOM_DIR = "D:\\건보\\동기화\\Naver MYBOX\\C언어반 예습\\매크로\\통돌이"
WORKTEST_DIR = "C:\\Users\\leegu\\Desktop\\통돌이"
BASIC_DIR = MAINCOM_DIR


class STOCK:
    def DATA_CHECK(USER_NAME):
        USER_EXISTING_CHECK = os.path.exists(f"{BASIC_DIR}\\Class\\STOCK\\USER_DATA\\{USER_NAME}.json")
        if USER_EXISTING_CHECK == True:
            return True
        else:
            return False

    def TIME_CHECK():
        CONFIG_DIR = f"{BASIC_DIR}\\Class\\STOCK\\STOCK_CONFIG\\Stock_Config.json"

        NOWDAY = datetime.datetime.today()
        TD_HOUR = NOWDAY.hour
        TD_MIN = NOWDAY.minute
        TD_SEC = NOWDAY.second

        BASETIME_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)
        BASETIME_OPEN_HOUR = BASETIME_DATA["TIME"]["BASETIME_OPEN_HOUR"]
        BASETIME_CLOSE_HOUR = BASETIME_DATA["TIME"]["BASETIME_CLOSE_HOUR"]
        BASETIME_MIN = BASETIME_DATA["TIME"]["BASETIME_MIN"]

        TIME_CHECK_VAL = TD_MIN % BASETIME_MIN

        
        if TD_HOUR >= BASETIME_OPEN_HOUR:
            if TIME_CHECK_VAL == 0:
                if TD_SEC == 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if TD_HOUR <= BASETIME_CLOSE_HOUR:
                if TIME_CHECK_VAL == 0:
                    if TD_SEC == 0:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

    def STOCK_LIST():
        CONFIG_DIR = f"{BASIC_DIR}\\Class\\STOCK\\STOCK_CONFIG\\Stock_Config.json"
        READ_STOCK_CONFIG = READ_WRITE.READ_JSON(CONFIG_DIR)
        
        STOCK_LIST = READ_STOCK_CONFIG["STOCK_DATA"]["STOCK_LIST"]
        COUNTER = len(STOCK_LIST)

        EMBED_STOCK_PRICE_LIST = discord.Embed(title = f":bar_chart: [주식 목록 & 주식 가격] :bar_chart:", description = f"")

        for COUNT in range(COUNTER):
            STOCK_NAME = STOCK_LIST[COUNT]
            STOCK_DATA_FILE_DIR = f"{BASIC_DIR}\\Class\\STOCK\\STOCK_LIST\\{STOCK_NAME}.json"
            READ_STOCK_DATA = READ_WRITE.READ_JSON(STOCK_DATA_FILE_DIR)
            STOCK_PRICE = READ_STOCK_DATA["STOCK_PROFILE"]["STOCK_PRICE"]
            STOCK_UP_DOWN_EMOJI = READ_STOCK_DATA["STOCK_PROFILE"]["PRICE_UP_DOWN"]["UP_DOWN_EMOJI"]
            EMBED_STOCK_PRICE_LIST.add_field(name = f"{STOCK_UP_DOWN_EMOJI}{STOCK_NAME}", value = f"{STOCK_PRICE}원", inline = True)
        return EMBED_STOCK_PRICE_LIST
        
    def USER_PROPERTY(USER_NAME):
        USER_DATA_FILE_DIR = f"{BASIC_DIR}\\Class\\STOCK\\USER_DATA\\{USER_NAME}.json"
        READ_USER_DATA = READ_WRITE.READ_JSON(USER_DATA_FILE_DIR)
        EMBED_USER_PROPERTY = discord.Embed(title = f":clipboard: [##현재 자산##] :clipboard:", description = f"")
        USER_DATA_KEY_LIST = [KEYS for KEYS in READ_USER_DATA]
        STOCK_KEY = "USER_STOCK_DATA"
        USER_DATA_KEY = "USER_DATA"
        try:
            if USER_DATA_KEY in USER_DATA_KEY_LIST:
                USER_MONEY = READ_USER_DATA[USER_DATA_KEY]["USER_INFO"]["USERMONEY"]
                EMBED_USER_PROPERTY.add_field(name = f":coin: 보유현금 :coin:", value = f"`{USER_MONEY}원`", inline = False)

            if STOCK_KEY in USER_DATA_KEY_LIST:
                USER_OWN_STOCK_LIST = READ_USER_DATA[STOCK_KEY]
                NOT_OWN_CHECK = 0
                IF_STOCK_EXIST = 0
                POSSESSION_STOCK_CHECK = len(USER_OWN_STOCK_LIST)
                if POSSESSION_STOCK_CHECK != 0:
                    for STOCK_NAME in USER_OWN_STOCK_LIST:
                        USER_OWN_AMOUNT = READ_USER_DATA[STOCK_KEY][str(STOCK_NAME)]["AMOUNT"]
                        if USER_OWN_AMOUNT != 0:
                            EMBED_USER_PROPERTY.add_field(name = f"`{STOCK_NAME}`", value = f"`{USER_OWN_AMOUNT}주`", inline = True)
                            IF_STOCK_EXIST += 1
                        else:
                            NOT_OWN_CHECK += 1
                    
                    if NOT_OWN_CHECK != 0:
                        if IF_STOCK_EXIST == 0:
                            EMBED_USER_PROPERTY.add_field(name = f"`보유 주식 없음`", value = f"`0주`")

                else:
                    EMBED_USER_PROPERTY.add_field(name = f"`보유 주식 없음`", value = f"`0주`")

            return EMBED_USER_PROPERTY
        except Exception as Message:
            return Message
        
    def PRICE_CHANGE(TIME_CHECK, STOCK_NAME):
        if TIME_CHECK == True:
            CONFIG_DIR = f"{BASIC_DIR}\\Class\\STOCK\\STOCK_CONFIG\\Stock_Config.json"
            READ_STOCK_CONFIG = READ_WRITE.READ_JSON(CONFIG_DIR)
            
            READ_CONFIG_STOCK_LIST = READ_STOCK_CONFIG["STOCK_DATA"]["STOCK_LIST"]
            STOCK_PRICE_CHANGE_RANGE = READ_STOCK_CONFIG["STOCK_DATA"]["PRICE_CHANGE_RANGE"]
            

            if STOCK_NAME in READ_CONFIG_STOCK_LIST:
                #STOCK_NAME가 READ_CONFIG_STOCK_LIST에 포함되어 있다면 밑에 코드 실행
                STOCK_DATA_FILE_DIR = f"{BASIC_DIR}\\Class\\STOCK\\STOCK_LIST\\{STOCK_NAME}.json"
                READ_STOCK_DATA = READ_WRITE.READ_JSON(STOCK_DATA_FILE_DIR)
                STOCK_PL_MI_CHECK = random.randint(1, 2)
                BF_STOCK_PRICE = READ_STOCK_DATA["STOCK_PROFILE"]["STOCK_PRICE"]
                UP_DOWN_EMOJI = [":chart_with_upwards_trend:", ":chart_with_downwards_trend:"] #1번 : 가격 상승 / 2번 : 가격 하락
                CHANCE_QUALIFICATION = READ_STOCK_CONFIG["STOCK_DATA"]["CHANCE_QUALIFICATION"]
                RANDOM_CHANCE_PROBABILITY = READ_STOCK_CONFIG["STOCK_DATA"]["CHANCE_PROBABILITY"]
            
                if BF_STOCK_PRICE <= CHANCE_QUALIFICATION:
                    CHANCE_CHECK = random.randint(1, 100)
                    if CHANCE_CHECK <= RANDOM_CHANCE_PROBABILITY:
                        CHANCE_PLUS_PRICE = random.randint(3000, 10000) #찬스타임 발동시 3000원 ~ 10000원 사이의 금액이 확정적으로 오름
                        AF_STOCK_PRICE = BF_STOCK_PRICE + CHANCE_PLUS_PRICE
                        CHANGE_STOCK_PRICE = AF_STOCK_PRICE - BF_STOCK_PRICE
                        return AF_STOCK_PRICE, CHANGE_STOCK_PRICE, UP_DOWN_EMOJI[0]
                    else:
                        if STOCK_PL_MI_CHECK == 1: #가격 상승
                            AF_STOCK_PRICE = BF_STOCK_PRICE + round((BF_STOCK_PRICE * (STOCK_PRICE_CHANGE_RANGE / 100)), 0)
                            CHANGE_STOCK_PRICE = AF_STOCK_PRICE - BF_STOCK_PRICE
                            STOCK_PRICE_UP_VAR = READ_STOCK_DATA["STOCK_PROFILE"]["PRICE_UP_DOWN"]["PRICE_UP"]
                            if STOCK_PRICE_UP_VAR < 3:
                                STOCK_JSON_DATA = [
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "PRICE_UP"], "VALUE": int(STOCK_PRICE_UP_VAR + 1)
                                    }, 
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "UP_DOWN_EMOJI"], "VALUE": str(UP_DOWN_EMOJI[0])
                                    }
                                ]
                                READ_WRITE.WRITE_JSON(FILE_DIR = STOCK_DATA_FILE_DIR, JSON_DATA = STOCK_JSON_DATA)

                            elif STOCK_PRICE_UP_VAR == 3:
                                STOCK_JSON_DATA = [
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "PRICE_UP"], "VALUE": 3
                                    }, 
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "UP_DOWN_EMOJI"], "VALUE": str(UP_DOWN_EMOJI[0])
                                    }
                                ]
                                READ_WRITE.WRITE_JSON(FILE_DIR = STOCK_DATA_FILE_DIR, JSON_DATA = STOCK_JSON_DATA)

                            return AF_STOCK_PRICE, CHANGE_STOCK_PRICE, UP_DOWN_EMOJI[0]

                        elif STOCK_PL_MI_CHECK == 2: #가격 하락
                            AF_STOCK_PRICE = BF_STOCK_PRICE - round((BF_STOCK_PRICE * (STOCK_PRICE_CHANGE_RANGE / 100)), 0)
                            CHANGE_STOCK_PRICE = AF_STOCK_PRICE - BF_STOCK_PRICE
                            STOCK_PRICE_DOWN_VAR = READ_STOCK_DATA["STOCK_PROFILE"]["PRICE_UP_DOWN"]["PRICE_DOWN"]
                            if STOCK_PRICE_DOWN_VAR < 3:
                                STOCK_JSON_DATA = [
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "PRICE_UP"], "VALUE": int(STOCK_PRICE_DOWN_VAR + 1)
                                    }, 
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "UP_DOWN_EMOJI"], "VALUE": str(UP_DOWN_EMOJI[1])
                                    }
                                ]
                                READ_WRITE.WRITE_JSON(FILE_DIR = STOCK_DATA_FILE_DIR, JSON_DATA = STOCK_JSON_DATA)
                                
                            elif STOCK_PRICE_DOWN_VAR == 3:
                                STOCK_JSON_DATA = [
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "PRICE_UP"], "VALUE": 3
                                    }, 
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "UP_DOWN_EMOJI"], "VALUE": str(UP_DOWN_EMOJI[1])
                                    }
                                ]
                                READ_WRITE.WRITE_JSON(FILE_DIR = STOCK_DATA_FILE_DIR, JSON_DATA = STOCK_JSON_DATA)

                            return AF_STOCK_PRICE, CHANGE_STOCK_PRICE, UP_DOWN_EMOJI[1]
                
                elif BF_STOCK_PRICE > CHANCE_QUALIFICATION:
                    CHANCE_CHECK = random.randint(1, 1000)
                    if CHANCE_CHECK <= RANDOM_CHANCE_PROBABILITY:
                        CHANCE_PLUS_PRICE = random.randint(3000, 10000) #찬스타임 발동시 3000원 ~ 10000원 사이의 금액이 확정적으로 오름
                        AF_STOCK_PRICE = BF_STOCK_PRICE + CHANCE_PLUS_PRICE
                        CHANGE_STOCK_PRICE = AF_STOCK_PRICE - BF_STOCK_PRICE
                        return AF_STOCK_PRICE, CHANGE_STOCK_PRICE, UP_DOWN_EMOJI[0]
                    else:
                        if STOCK_PL_MI_CHECK == 1: #가격 상승
                            AF_STOCK_PRICE = BF_STOCK_PRICE + round((BF_STOCK_PRICE * (STOCK_PRICE_CHANGE_RANGE / 100)), 0)
                            CHANGE_STOCK_PRICE = AF_STOCK_PRICE - BF_STOCK_PRICE
                            STOCK_PRICE_UP_VAR = READ_STOCK_DATA["STOCK_PROFILE"]["PRICE_UP_DOWN"]["PRICE_UP"]
                            if STOCK_PRICE_UP_VAR < 3:
                                STOCK_JSON_DATA = [
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "PRICE_UP"], "VALUE": int(STOCK_PRICE_UP_VAR + 1)
                                    }, 
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "UP_DOWN_EMOJI"], "VALUE": str(UP_DOWN_EMOJI[0])
        
                                    }
                                ]
                                READ_WRITE.WRITE_JSON(FILE_DIR = STOCK_DATA_FILE_DIR, JSON_DATA = STOCK_JSON_DATA)

                            elif STOCK_PRICE_UP_VAR == 3:
                                STOCK_JSON_DATA = [
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "PRICE_UP"], "VALUE": 3
                                    }, 
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "UP_DOWN_EMOJI"], "VALUE": str(UP_DOWN_EMOJI[0])
                                    }
                                ]
                                READ_WRITE.WRITE_JSON(FILE_DIR = STOCK_DATA_FILE_DIR, JSON_DATA = STOCK_JSON_DATA)

                            return AF_STOCK_PRICE, CHANGE_STOCK_PRICE, UP_DOWN_EMOJI[0]

                        elif STOCK_PL_MI_CHECK == 2: #가격 하락
                            AF_STOCK_PRICE = BF_STOCK_PRICE - round((BF_STOCK_PRICE * (STOCK_PRICE_CHANGE_RANGE / 100)), 0)
                            CHANGE_STOCK_PRICE = AF_STOCK_PRICE - BF_STOCK_PRICE
                            STOCK_PRICE_DOWN_VAR = READ_STOCK_DATA["STOCK_PROFILE"]["PRICE_UP_DOWN"]["PRICE_DOWN"]
                            if STOCK_PRICE_DOWN_VAR < 3:
                                STOCK_JSON_DATA = [
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "PRICE_UP"], "VALUE": int(STOCK_PRICE_DOWN_VAR + 1)
                                    }, 
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "UP_DOWN_EMOJI"], "VALUE": str(UP_DOWN_EMOJI[1])
                                    }
                                ]
                                READ_WRITE.WRITE_JSON(FILE_DIR = STOCK_DATA_FILE_DIR, JSON_DATA = STOCK_JSON_DATA)
                                
                            elif STOCK_PRICE_DOWN_VAR == 3:
                                STOCK_JSON_DATA = [
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "PRICE_UP"], "VALUE": 3
                                    }, 
                                    {
                                        "KEY": ["STOCK_PROFILE", "PRICE_UP_DOWN", "UP_DOWN_EMOJI"], "VALUE": str(UP_DOWN_EMOJI[1])
                                    }
                                ]
                                READ_WRITE.WRITE_JSON(FILE_DIR = STOCK_DATA_FILE_DIR, JSON_DATA = STOCK_JSON_DATA)

                            return AF_STOCK_PRICE, CHANGE_STOCK_PRICE, UP_DOWN_EMOJI[1]
            
            elif STOCK_NAME not in READ_CONFIG_STOCK_LIST:    
                DEACTIVATION_STOCK = f"[비활성화 상태]"
                return DEACTIVATION_STOCK
            
            else:
                ERROR_MSG = "잘못된 주식 정보 입니다"
                return ERROR_MSG
        else:
            pass
       
    def PURCHASE_SELL(USER_NAME, MODE, STOCK_INFO):

        STOCK_NAME = str(STOCK_INFO[0]) #무조건 str타입
        AMOUNT_TYPE = STOCK_INFO[1] 
        USER_DATA_FILE_DIR = f"{BASIC_DIR}\\Class\\STOCK\\USER_DATA\\{USER_NAME}.json"
        STOCK_DATA_FILE_DIR = f"{BASIC_DIR}\\Class\\STOCK\\STOCK_LIST\\{STOCK_NAME}.json"

        if int(AMOUNT_TYPE) == 0:
            ERROR_MSG = f"0주는 {MODE}할 수 없습니다."
            return ERROR_MSG

        elif AMOUNT_TYPE == None:
            ERROR_MSG = f"{MODE}갯수 인자는 비워둘수 없습니다."
            return ERROR_MSG
        
        try:
            READ_USER_DATA = READ_WRITE.READ_JSON(USER_DATA_FILE_DIR)
        except:
            ERROR_MSG = f"유저정보를 읽어오는데 에러가 발생하였습니다. 제작자를 호출하여 주십시오."
            return ERROR_MSG

        try:
            READ_STOCK_DATA = READ_WRITE.READ_JSON(STOCK_DATA_FILE_DIR)
        except:
            ERROR_MSG = f"해당 주식은 존재하지 않습니다. 주식 이름을 확인하여 주십시오."
            return ERROR_MSG
        BF_USER_MONEY = READ_USER_DATA["USER_DATA"]["USER_INFO"]["USERMONEY"]
        CURRENT_STOCK_PRICE = READ_STOCK_DATA["STOCK_PROFILE"]["STOCK_PRICE"] #현재의 주식 가격을 가져온다
        try: #USER_OWN_STOCK_AMOUNT = READ_USER_DATA["USER_STOCK_DATA"][f"{STOCK_NAME}"]["AMOUNT"] 
            USER_OWN_STOCK_AMOUNT = READ_USER_DATA["USER_STOCK_DATA"][f"{STOCK_NAME}"]["AMOUNT"] 
        except: #USER_OWN_STOCK_AMOUNT = READ_USER_DATA["USER_STOCK_DATA"][f"{STOCK_NAME}"]["AMOUNT"] 에러 시
        
            F_KEY_LIST = READ_USER_DATA
            STOCK_DATA_KEY = "USER_STOCK_DATA"

            if STOCK_DATA_KEY in F_KEY_LIST: #주식 관련 키가 존재 할때
                S_KEY_LIST = READ_USER_DATA["USER_STOCK_DATA"] #"USER_STOCK_DATA"키의 하위 키
                
                if STOCK_NAME in S_KEY_LIST: #"USER_STOCK_DATA", "f{STOCK_NAME}", ("AMOUNT" or "PREVIOUS_PRICE") 이 3가지 키가 모두 있을때
                    USER_OWN_STOCK_AMOUNT = READ_USER_DATA["USER_STOCK_DATA"][f"{STOCK_NAME}"]["AMOUNT"] #USER_OWN_STOCK_AMOUNT = 유저가 현재 보유하고 있는 해당 주식 갯수
                    
                elif STOCK_NAME not in S_KEY_LIST: #"USER_STOCK_DATA" 1가지 키만 있을때
                    with open(f"{USER_DATA_FILE_DIR}", "w", encoding = "utf-8") as REWRITE_USER_PROFILE:
                        READ_USER_DATA["USER_STOCK_DATA"][f"{STOCK_NAME}"] = {}
                        json.dump(READ_USER_DATA, REWRITE_USER_PROFILE, indent = 4)

                    with open(f"{USER_DATA_FILE_DIR}", "w", encoding = "utf-8") as REWRITE_USER_PROFILE:
                        READ_USER_DATA["USER_STOCK_DATA"][f"{STOCK_NAME}"]["AMOUNT"] = 0
                        READ_USER_DATA["USER_STOCK_DATA"][f"{STOCK_NAME}"]["PREVIOUS_PRICE"] = 0
                        json.dump(READ_USER_DATA, REWRITE_USER_PROFILE, indent = 4)
                    
                    USER_OWN_STOCK_AMOUNT = READ_WRITE.READ_JSON(USER_DATA_FILE_DIR)["USER_STOCK_DATA"][f"{STOCK_NAME}"]["AMOUNT"] #USER_OWN_STOCK_AMOUNT = 유저가 현재 보유하고 있는 해당 주식 갯수

            elif STOCK_DATA_KEY not in F_KEY_LIST: #주식 관련 키가 존재하지 않을때
                with open(f"{USER_DATA_FILE_DIR}", "w", encoding = "utf-8") as REWRITE_USER_PROFILE:
                    READ_USER_DATA["USER_STOCK_DATA"] = {}
                    json.dump(READ_USER_DATA, REWRITE_USER_PROFILE, indent = 4)

                with open(f"{USER_DATA_FILE_DIR}", "w", encoding = "utf-8") as REWRITE_USER_PROFILE:
                    READ_USER_DATA["USER_STOCK_DATA"][f"{STOCK_NAME}"] = {}
                    json.dump(READ_USER_DATA, REWRITE_USER_PROFILE, indent = 4)

                with open(f"{USER_DATA_FILE_DIR}", "w", encoding = "utf-8") as REWRITE_USER_PROFILE:
                    READ_USER_DATA["USER_STOCK_DATA"][f"{STOCK_NAME}"]["AMOUNT"] = 0
                    READ_USER_DATA["USER_STOCK_DATA"][f"{STOCK_NAME}"]["PREVIOUS_PRICE"] = 0
                    json.dump(READ_USER_DATA, REWRITE_USER_PROFILE, indent = 4)
                
                USER_OWN_STOCK_AMOUNT = READ_WRITE.READ_JSON(USER_DATA_FILE_DIR)["USER_STOCK_DATA"][f"{STOCK_NAME}"]["AMOUNT"] #USER_OWN_STOCK_AMOUNT = 유저가 현재 보유하고 있는 해당 주식 갯수

        
            
        READ_USER_DATA = READ_WRITE.READ_JSON(USER_DATA_FILE_DIR) #READ_USER_DATA 수정 후 새로고침

        if MODE == "구매":
            if AMOUNT_TYPE == "최대":
                AMOUNT = round((BF_USER_MONEY / CURRENT_STOCK_PRICE), 0) - 1
                
                TOTAL_PURCHASE_STOCK_PRICE = CURRENT_STOCK_PRICE * AMOUNT
                
            elif AMOUNT_TYPE != "최대":
                AMOUNT = int(AMOUNT_TYPE)
                
                TOTAL_PURCHASE_STOCK_PRICE = CURRENT_STOCK_PRICE * AMOUNT
            
            if BF_USER_MONEY >= TOTAL_PURCHASE_STOCK_PRICE:
                AF_USER_MONEY = BF_USER_MONEY - TOTAL_PURCHASE_STOCK_PRICE
                with open(f"{USER_DATA_FILE_DIR}", "w", encoding = "utf-8") as REWRITE_USER_PROFILE:
                    READ_USER_DATA["USER_DATA"]["USER_INFO"]["USERMONEY"] = AF_USER_MONEY
                    READ_USER_DATA["USER_STOCK_DATA"][f"{STOCK_NAME}"]["AMOUNT"] = AMOUNT
                    READ_USER_DATA["USER_STOCK_DATA"][f"{STOCK_NAME}"]["PREVIOUS_PRICE"] = CURRENT_STOCK_PRICE #CURRENT_STOCK_PRICE = 함수 실행 당시의 주식 가격
                    json.dump(READ_USER_DATA, REWRITE_USER_PROFILE, indent = 4)
                return STOCK_NAME, AF_USER_MONEY, AMOUNT, CURRENT_STOCK_PRICE

            elif BF_USER_MONEY < TOTAL_PURCHASE_STOCK_PRICE:
                ERROR_MSG = f"현재 `{USER_NAME}`님이 보유하신 현금 `{BF_USER_MONEY}원`은 총 구매금액인 `{TOTAL_PURCHASE_STOCK_PRICE}원`보다 작습니다."
                return ERROR_MSG

        elif MODE == "판매":
            if AMOUNT_TYPE == "최대":
                AMOUNT = USER_OWN_STOCK_AMOUNT
                TOTAL_SELL_STOCK_PRICE = CURRENT_STOCK_PRICE * AMOUNT
                
            elif AMOUNT_TYPE != "최대":
                AMOUNT = int(AMOUNT_TYPE)
                TOTAL_SELL_STOCK_PRICE = CURRENT_STOCK_PRICE * AMOUNT
            
            if USER_OWN_STOCK_AMOUNT >= AMOUNT:
                AF_USER_MONEY = BF_USER_MONEY + TOTAL_SELL_STOCK_PRICE
                with open(f"{USER_DATA_FILE_DIR}", "w", encoding = "utf-8") as REWRITE_USER_PROFILE:
                    READ_USER_DATA["USER_DATA"]["USER_INFO"]["USERMONEY"] = AF_USER_MONEY
                    READ_USER_DATA["USER_STOCK_DATA"][f"{STOCK_NAME}"]["AMOUNT"] -= AMOUNT
                    json.dump(READ_USER_DATA, REWRITE_USER_PROFILE, indent = 4)
                    
                    return STOCK_NAME, AF_USER_MONEY, AMOUNT, CURRENT_STOCK_PRICE
            elif USER_OWN_STOCK_AMOUNT < AMOUNT:
                ERROR_MSG = f"현재 판매하시려는 `{STOCK_NAME}` `{AMOUNT}주`는 `{USER_NAME}`님이 보유하신 `{USER_OWN_STOCK_AMOUNT}주`보다 큽니다."
                return ERROR_MSG


                    

    
            
