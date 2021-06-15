import datetime, json, time, os, sys
from Class.USER_JSON_RW.rw_json import READ_WRITE
#sys.path.append("D:\\건보\\동기화\\Naver MYBOX\\C언어반 예습\\매크로\\통돌이\\Class\\USER_JSON_RW")
#from rw_json import READ_WRITE


DASKTOP_DIR = "C:\\Users\\leegu\\Desktop\\통돌이"
MAINCOM_DIR = "D:\\건보\\동기화\\Naver MYBOX\\C언어반 예습\\매크로\\통돌이"
WORKTEST_DIR = "C:\\Users\\leegu\\Desktop\\통돌이"
BASIC_DIR = MAINCOM_DIR

class SUBJECT_CHECK:
    def TIME_CHECK(CLASS_INFO):
        """
        현재 시간이 교시 시간이랑 일치할경우 해당 교시를 리턴함.\n
        CLASS_INFO 타입 = list\n
        CLASS_INFO[0] ==> SCHOOL_CODE\n
        CLASS_INFO[1] ==> CLASS_NUM\n

        
        리턴
        --------
        TIME_CHECK = True / False\n 
        return_val_type = bool

        """

        TODAY = datetime.datetime.today()
        DOTW = TODAY.weekday()
        TD_HOUR = TODAY.hour
        TD_MIN = TODAY.minute
        TD_SEC = TODAY.second

        CONFIG_DIR = f"{BASIC_DIR}\\Class\\ATTENDANCE_CHECKER\\ATTENDANCE_CHECKER\\ATTENDANCE_TIME_CONFIG\\Attendance_Time_Config.json"
        READ_BASETIME_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)
        BASETIME_LIST = READ_BASETIME_DATA["TIME"]["PERIOD"]
        SCHOOL_CODE = CLASS_INFO[0]
        CLASS_NUM = CLASS_INFO[1]

        if DOTW == 0:
            DOTW = "MONDAY"

        elif DOTW == 1:
            DOTW = "TUESDAY"

        elif DOTW == 2:
            DOTW = "WEDNESDAY"

        elif DOTW == 3:
            DOTW = "THURSDAY"

        elif DOTW == 4:
            DOTW = "FRIDAY"

        DOTW_PERIOD_LIST = READ_BASETIME_DATA["SUBJECT"]["SCHOOL"][f"{SCHOOL_CODE}"][f"{CLASS_NUM}"][f"{DOTW}"]
        
        COUNTER = len(DOTW_PERIOD_LIST)  
        """
        BASETIME_LIST_COUNTER = len(BASETIME_LIST)

        if DOTW == 2:
            COUNTER = BASETIME_LIST_COUNTER - 1
            pass
        elif DOTW != 2:
            COUNTER = BASETIME_LIST_COUNTER 
            pass
        """
        for COUNT in range(COUNTER):
            NUM = COUNT + 1
            BASETIME_HOUR = BASETIME_LIST[f"{NUM}"][0]
            BASETIME_MIN = BASETIME_LIST[f"{NUM}"][1]

            if TD_HOUR == BASETIME_HOUR and TD_MIN == BASETIME_MIN:
                
                if TD_SEC == 0:
                    NOW_PERIOD = NUM
                    return True, NOW_PERIOD
                else:
                    pass
            else:
                pass

        return False

    def NOW_SUBJECT(TIME_CHECK, CLASS_INFO, NOW_PERIOD):
        """
        TIME_CHECK는 SUBJECT.TIME_CHECK의 리턴 값(SUBJECT.TIME_CHECK[0])\n
        CLASS_INFO는 :func:`list`형으로 CLASS_INFO[0] = 반 / CLASS_INFO[1] = 학교\n
        NOW_PERIOD는 SUBJECT.TIME_CHECK의 리턴 값(SUBJECT.TIME_CHECK[1])
        """
        CONFIG_DIR = f"{BASIC_DIR}\\Class\\ATTENDANCE_CHECKER\\ATTENDANCE_CHECKER\\ATTENDANCE_TIME_CONFIG\\Attendance_Time_Config.json"
        if TIME_CHECK == True:
            TODAY = datetime.datetime.today()
            COUNT = TODAY.weekday()
            CLASS_NUM = CLASS_INFO[0]
            SCHOOL = CLASS_INFO[1]

            READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)
            print(f"COUNT = {COUNT}")
            if COUNT == 0:
                DOTW = "MONDAY"

            elif COUNT == 1:
                DOTW = "TUESDAY"

            elif COUNT == 2:
                DOTW = "WEDNESDAY"

            elif COUNT == 3:
                DOTW = "THURSDAY"

            elif COUNT == 4:
                DOTW = "FRIDAY"
                

            SUBJECT_LIST = READ_CONFIG_DATA["SUBJECT"]["SCHOOL"][f"{SCHOOL}"][f"{CLASS_NUM}"][f"{DOTW}"]

            NOW_PERIOD = NOW_PERIOD

            return NOW_PERIOD, SUBJECT_LIST



        





#class ATTENDANCE:


    