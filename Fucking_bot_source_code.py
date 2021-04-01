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


images_file_dir = "D:\\건보\\동기화\\Naver MYBOX\\C언어반 예습\\매크로\\디스코드 봇 만들기\\images_file\\"
yunh_image_dir = images_file_dir + "yunh\\"
kimki_image_dir = images_file_dir + "kimki\\"
juns_image_dir = images_file_dir + "juns\\"
bot = commands.Bot(command_prefix='!')
BOT_TOKEN = 'Your_BOT_TOKEN' #'ODI0NjU3OTY5MTEwODQzNDEy.YFyklQ.5aYtkTh1mZZNT8d65SLr72Uw1zs' #현재 기능 테스트용 봇 토큰 후에 변경 필요



#=========================================변수============================================
user = []
musictitle = []
song_queue = []
musicnow = []


stop_loop = 1


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


dotwName = ["토요일", "일요일"]

holiSub = ["주말이당"]
txtchId = 714475326708908133 #744199524138090501 
#=========================================변수============================================

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
        if td_min == 10:
            if td_sec == 0:
                Get_period = 1 #Get_period에 현재 교시를 추가
                return Get_period

    elif td_hour == 10:
        if td_min == 10:
            if td_sec == 0:
                Get_period = 2 #Get_period에 현재 교시를 추가
                return Get_period

    elif td_hour == 11:
        if td_min == 10:
            if td_sec == 0:
                Get_period = 3 #Get_period에 현재 교시를 추가
                return Get_period

    elif td_hour == 12:
        if td_min == 10:
            if td_sec == 0:
                Get_period = 4 #Get_period에 현재 교시를 추가
                return Get_period

    elif td_hour == 14:
        if td_min == 0:
            if td_sec == 0:
                Get_period = 5 #Get_period에 현재 교시를 추가
                return Get_period

    elif td_hour == 15:
        if td_min == 0:
            if td_sec == 0:
                Get_period = 6 #Get_period에 현재 교시를 추가
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

    Class_Chk = 0
    if classNum == 2:
        Class_Chk = 0
        pass
    elif classNum == 4:
        Class_Chk = 1
        pass
    elif classNum == 5:
        Class_Chk = 2
        pass


    Td_Date = datetime.datetime.today()
    Td_Dotw = Td_Date.weekday()
    Td_hour = Td_Date.hour
    Td_min = Td_Date.minute
    Td_sec = Td_Date.second
    

    nowPeriod_chk = Get_Now_Period(Td_hour, Td_min, Td_sec) #현재 교시를 받아옴


    if nowPeriod_chk == 7:
        nowPeriod_chk = "last_time"
        pass

    else:
        pass

    nextSub = Get_Period_Sub(classNum, Td_Dotw) #nowPeriod_chk에대한 nextSub가 반환

    

        
    if nowPeriod_chk == "끝":
        embed=discord.Embed(title = f'[##다음교시##]', description = f'##다음교시는?##', color=0x00ff00)
        embed.add_field(name=f'[사우고 {ClassName}]', value=f'[끝]', inline=False)
        return embed
        
    else:
        embed=discord.Embed(title = f'[##다음교시##]', description = f'##다음교시는?##', color=0x00ff00)
        embed.add_field(name=f'[사우고 {ClassName}]', value=f'[{nextSub[Class_Chk][nowPeriod_chk - 1]}]', inline=False)
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


@bot.event
async def on_ready():
    print("=============")
    print(" 실 행 완 료 ")
    print("=============")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("노래"))
    Period_Check.start(txtchId)

    #if not discord.opus.is_loaded():
    #    discord.opus.load_opus('opus')


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
async def 사진첩(ctx, *arg):
    
    images_file_dir = "D:\\건보\\동기화\\Naver MYBOX\\C언어반 예습\\매크로\\디스코드 봇 만들기\\images_file\\"
    yunh_image_dir = images_file_dir + "yunh\\"
    kimki_image_dir = images_file_dir + "kimki\\"

    
    picTuple_Conv = list(arg) #<!사진첩 1 2> 입력시 picTuple_Conv[0] = 1, picTuple_Conv[1] = 2 #picTuple_Conv[2]값은 무조건 int형으로 변환 시킬것 str형 들어가면 TypeError발생
    
    unLimit_ch = bot.get_channel(817688404631617546)

    p1 = "윤행이"
    p2 = "기정이"
    
    if ctx.channel == unLimit_ch:
            
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
async def 통돌아(ctx, *, arg):
    

    p1 = "놀아줘"
    p2 = "기정이는"
    p3 = "윤행이는"
    p4 = "윤행"
    p5 = "기정"
    p6 = "유빈"
    p7 = "다훈"
    
    
    p10 = "대화목록"

    #p6 = "다음교시"
    
    #Using_image_dir = ""
    ##image_count_list = list(os.listdir(images_file_dir)) 
    ##Image_files_count = len(image_count_list)


    Images_file_list = []
    Image_file_count = 0

    if arg == str(p1):
        await ctx.send("싫어")
        
    
    elif arg == str(p4) or str(p5) or str(p6) or str(p7):
        unlimit_ch = bot.get_channel(817688404631617546)
        if ctx.channel == unlimit_ch:
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

        elif arg == str(p7):
            await ctx.send("너 때문에 내가 격리 당했어...죽일꺼야...")
        elif ctx.channel != unlimit_ch:
            await ctx.send("여기는 다훈이에 의해 명령어를 칠 수 없게 변했어요")
   


        

    
    elif arg == str(p2) or str(p3):
        Text_1 = ["@승엽이 따까리", "ㄱㅗㅏㅇ ㅁㅗ 남편", "윤슬이 ㄴㅍ", "원숭이", "고급 남창", "개떡장애 새끼", "뒤에서 1등급", "오른쪽 땜빵", "기탈난발"]
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
        

        


@bot.command()
async def 마이크(ctx, *, arg):
    await ctx.send(content=arg, tts=True)

#@bot.command()
#async def 테스트(ctx):

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
        embed=discord.Embed(title = f'[##주사위 게임##]', description = f'##당신의 주사위 갯수가 {Rnd_dice_USER}으로 \n더 높으므로 통돌이의 승리##', color=0x00ff00)
        await ctx.send(embed = embed)
            
    elif Rnd_dice_USER == Rnd_dice_BOT:
        embed=discord.Embed(title = f'[##주사위 게임##]', description = f'##통돌이, 당신의 주사위 갯수가 {Rnd_dice_USER}으로 \n 같으므로  무승부##', color=0x00ff00)
        await ctx.send(embed = embed)
        

    


        



@bot.command()
async def 다음교시(ctx, *, arg): #고쳐야함...귀찮다...

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

    
    




@tasks.loop(seconds=1)
async def Period_Check(self): #완성....    

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

        print(f"{todDotw}")
        print(f"{nowPeriod}교시")

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
