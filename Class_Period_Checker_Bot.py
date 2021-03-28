def Today_Dotw_Checker(Date_Of_The_Week1): #오늘의 Dotw값을 받아서 해당 요일의 과목 배열을 각 반의 순서대로 2차원 배열의 형식으로 과목을 리턴

    Second_todSub_204 = [] #위의 시간표에서 해당요일 시간표 저장하는 배열
    Second_todSub_202 = [] #위의 시간표에서 해당요일 시간표 저장하는 배열

    if Date_Of_The_Week1 >= 5: #Date_Of_The_Week1의 값이 5보다 크거나 같다면 주말이므로 밑의 if문 안의 코드 실행
        #테스트용 코드
        Rnd_mix = random.randint(0, 4)
        Date_Of_The_Week1 = Rnd_mix
        pass
    
    else: #위의 경우를 제외한 모든 경우에는 바로 밑의 코드를 실행한다.
        pass

    if Date_Of_The_Week1 == 0:
        print("월요일")
        Second_todSub_204 = monSub_204
        Second_todSub_202 = monSub_202

        return Second_todSub_202, Second_todSub_204

    elif Date_Of_The_Week1 == 1:
        print("화요일")
        Second_todSub_204 = tusSub_204
        Second_todSub_202 = tusSub_202

        return Second_todSub_202, Second_todSub_204

    elif Date_Of_The_Week1 == 2:
        print("수요일")
        Second_todSub_204 = wenSub_204
        Second_todSub_202 = wenSub_202

        return Second_todSub_202, Second_todSub_204

    elif Date_Of_The_Week1 == 3:
        print("목요일")
        Second_todSub_204 = thrSub_204
        Second_todSub_202 = thrSub_202

        return Second_todSub_202, Second_todSub_204

    elif Date_Of_The_Week1 == 4:
        print("금요일")
        Second_todSub_204 = friSub_204
        Second_todSub_202 = friSub_202

        return Second_todSub_202, Second_todSub_204

def Get_Now_Period(td_hour, td_min): #Td_hour, Td_min의 값을 기준으로 현재의 교시를 받아오는 Get_period 배열을 리턴
    
    Get_period = 0

    if td_hour == 9:
        if td_min == 10:
            Get_period = 1 #Get_period에 현재 교시를 추가
            return Get_period

    elif td_hour == 10:
        if td_min == 10:
            Get_period = 2 #Get_period에 현재 교시를 추가
            return Get_period

    elif td_hour == 11:
        if td_min == 10:
            Get_period = 3 #Get_period에 현재 교시를 추가
            return Get_period

    elif td_hour == 12:
        if td_min == 10:
            Get_period = 4 #Get_period에 현재 교시를 추가
            return Get_period

    elif td_hour == 14:
        if td_min == 0:
            Get_period = 5 #Get_period에 현재 교시를 추가
            return Get_period

    elif td_hour == 15:
        if td_min == 0:
            Get_period = 6 #Get_period에 현재 교시를 추가
            return Get_period

    elif td_hour == 16:
        if td_min == 0:
            Get_period = 7 #Get_period에 현재 교시를 추가
            return Get_period
    else: #테스트용 코드
        Rnd_period = random.randint(1,7)
        Get_period = Rnd_period
        return Get_period

