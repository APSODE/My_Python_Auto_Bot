import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.ext import tasks
import discord
import asyncio
import time
import nacl
import sys
sys.path.append("C:\\Users\\leegu\\AppData\\Local\\Programs\\Python\\Python38\\Scripts")
from youtube_dl import YoutubeDL
import random
import time
import datetime



bot = commands.Bot(command_prefix='!')
BOT_TOKEN = 'MY_Discord_Bot_TOKEN'



#=========================================변수============================================
user = []
musictitle = []
song_queue = []
musicnow = []


stop_loop = 1

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

dotwName = ["토요일", "일요일"]

holiSub = ["주말이당"]
txtchId = 744199524138090501 #714475326708908133
#=========================================변수============================================




def title(msg):
    global music

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    chromedriver_dir = "D:\\Chrome_Search_Engine\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver_dir, options = options)
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
        driver = webdriver.Chrome(chromedriver_dir, options = options)
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
    url = ["https://www.youtube.com/watch?v=PojjikO8zb4&list=PLYW5J-00fLS3_H4gK0tMwaswoaQ6hEwji&index=3", "https://www.youtube.com/watch?v=PojjikO8zb4&list=PLYW5J-00fLS3_H4gK0tMwaswoaQ6hEwji&index=3", "https://www.youtube.com/watch?v=zGmK9WFnQhg", "https://www.youtube.com/watch?v=aH-uM4I5hq8", "https://www.youtube.com/watch?v=P_xlimP0MTw"]
    title = "plum"
    Rnd_plum = random.randint(0, 4)

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url[Rnd_plum], download=False)
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
        driver = webdriver.Chrome(chromedriver_dir, options = options)
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
async def 자비스(ctx, *, arg):
    
    
    Rnd_1 = random.randint(1, 10)

    p1 = "놀아줘"
    p10 = "들어와"

    if arg == str(p1):
        await ctx.send("싫어")


    elif arg == str(p10):
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
async def 마이크(ctx, *, arg):
    await ctx.send(content=arg, tts=True)

@tasks.loop(seconds=10)
async def Period_Check(self): #완성....


    nowDay = datetime.datetime.today() #현재 날짜를 nowDay라는 변수에 저장
    Dotw = nowDay.weekday() #nowDay변수를 이용해 해당날짜 요일을 구함 Dotw값은 0 ~ 6까지 존재, 0부터 순서대로 월요일 ~~
    td_hour = nowDay.hour #nowDay변수를 이용해 현재 "시간" 구함
    td_min = nowDay.minute #nowDay변수를 이용해 현재 "분" 구함
    
    
    #mainSub = ["수학","문학","영어"]
    #othSub = ["음감","운건","일본어","창체","진로"]
    #selSub = ["선택과목 A","선택과목 B","선택과목 C"] #{selSub[0]} ==> 선택과목 A 


    channel = bot.get_channel(txtchId) #알람을 보낼 텍스트 채널을 저장하는 변수


    todSub_204 = [] #위의 시간표에서 해당요일 시간표 저장하는 배열
    todSub_202 = [] #위의 시간표에서 해당요일 시간표 저장하는 배열
    


    if Dotw != 2:
        if Dotw == 0:
            print("월요일")
            todSub_204 = monSub_204
            todSub_202 = monSub_202


            if td_hour == 9:
                if td_min == 10:
                    print("1교시")
                    embed=discord.Embed(title='[1교시 출첵을 해야할 시간입니다.]', description='##1교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[0]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[0]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 10:
                if td_min == 10:
                    print("2교시")
                    embed=discord.Embed(title='[2교시 출첵을 해야할 시간입니다.]', description='##2교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[1]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[1]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 11:
                if td_min == 10:
                    print("3교시")
                    embed=discord.Embed(title='[3교시 출첵을 해야할 시간입니다.]', description='##3교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[2]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[2]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 12:
                if td_min == 10:
                    print("4교시")
                    embed=discord.Embed(title='[4교시 출첵을 해야할 시간입니다.]', description='##4교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[3]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[3]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 14:
                if td_min == 0:
                    print("5교시")
                    embed=discord.Embed(title='[5교시 출첵을 해야할 시간입니다.]', description='##5교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[4]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[4]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 15:
                if td_min == 0:
                    print("6교시")
                    embed=discord.Embed(title='[6교시 출첵을 해야할 시간입니다.]', description='##6교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[5]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[5]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 16:
                if td_min == 0:
                    print("7교시")
                    embed=discord.Embed(title='[7교시 출첵을 해야할 시간입니다.]', description='##7교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[6]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[6]}]', inline=False)
                    await channel.send(embed=embed)

                    Period_Check.stop()

        elif Dotw == 1:
            print("화요일")
            todSub_204 = tusSub_204
            todSub_202 = tusSub_202


            if td_hour == 9:
                if td_min == 10:
                    print("1교시")
                    embed=discord.Embed(title='[1교시 출첵을 해야할 시간입니다.]', description='##1교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[0]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[0]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 10:
                if td_min == 10:
                    print("2교시")
                    embed=discord.Embed(title='[2교시 출첵을 해야할 시간입니다.]', description='##2교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[1]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[1]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 11:
                if td_min == 10:
                    print("3교시")
                    embed=discord.Embed(title='[3교시 출첵을 해야할 시간입니다.]', description='##3교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[2]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[2]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 12:
                if td_min == 10:
                    print("4교시")
                    embed=discord.Embed(title='[4교시 출첵을 해야할 시간입니다.]', description='##4교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[3]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[3]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 14:
                if td_min == 0:
                    print("5교시")
                    embed=discord.Embed(title='[5교시 출첵을 해야할 시간입니다.]', description='##5교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[4]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[4]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 15:
                if td_min == 0:
                    print("6교시")
                    embed=discord.Embed(title='[6교시 출첵을 해야할 시간입니다.]', description='##6교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[5]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[5]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 16:
                if td_min == 0:
                    print("7교시")
                    embed=discord.Embed(title='[7교시 출첵을 해야할 시간입니다.]', description='##7교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[6]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[6]}]', inline=False)
                    await channel.send(embed=embed)

                    Period_Check.stop()

        elif Dotw == 3:
            print("목요일")
            todSub_204 = thrSub_204
            todSub_202 = thrSub_202
            
            
            if td_hour == 9:
                if td_min == 10:
                    print("1교시")
                    embed=discord.Embed(title='[1교시 출첵을 해야할 시간입니다.]', description='##1교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[0]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[0]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 10:
                if td_min == 10:
                    print("2교시")
                    embed=discord.Embed(title='[2교시 출첵을 해야할 시간입니다.]', description='##2교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[1]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[1]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 11:
                if td_min == 10:
                    print("3교시")
                    embed=discord.Embed(title='[3교시 출첵을 해야할 시간입니다.]', description='##3교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[2]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[2]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 12:
                if td_min == 10:
                    print("4교시")
                    embed=discord.Embed(title='[4교시 출첵을 해야할 시간입니다.]', description='##4교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[3]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[3]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 14:
                if td_min == 0:
                    print("5교시")
                    embed=discord.Embed(title='[5교시 출첵을 해야할 시간입니다.]', description='##5교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[4]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[4]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 15:
                if td_min == 0:
                    print("6교시")
                    embed=discord.Embed(title='[6교시 출첵을 해야할 시간입니다.]', description='##6교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[5]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[5]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 16:
                if td_min == 0:
                    print("7교시")
                    embed=discord.Embed(title='[7교시 출첵을 해야할 시간입니다.]', description='##7교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[6]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[6]}]', inline=False)
                    await channel.send(embed=embed)

                    Period_Check.stop()

        elif Dotw == 4:
            print("금요일")
            todSub_204 = friSub_204
            todSub_202 = friSub_202
        

            if td_hour == 9:
                if td_min == 10:
                    print("1교시")
                    embed=discord.Embed(title='[1교시 출첵을 해야할 시간입니다.]', description='##1교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[0]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[0]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 10:
                if td_min == 10:
                    print("2교시")
                    embed=discord.Embed(title='[2교시 출첵을 해야할 시간입니다.]', description='##2교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[1]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[1]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 11:
                if td_min == 10:
                    print("3교시")
                    embed=discord.Embed(title='[3교시 출첵을 해야할 시간입니다.]', description='##3교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[2]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[2]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 12:
                if td_min == 10:
                    print("4교시")
                    embed=discord.Embed(title='[4교시 출첵을 해야할 시간입니다.]', description='##4교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[3]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[3]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 14:
                if td_min == 0:
                    print("5교시")
                    embed=discord.Embed(title='[5교시 출첵을 해야할 시간입니다.]', description='##5교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[4]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[4]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 15:
                if td_min == 0:
                    print("6교시")
                    embed=discord.Embed(title='[6교시 출첵을 해야할 시간입니다.]', description='##6교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[5]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[5]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 16:
                if td_min == 0:
                    print("7교시")
                    embed=discord.Embed(title='[7교시 출첵을 해야할 시간입니다.]', description='##7교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[6]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[6]}]', inline=False)
                    await channel.send(embed=embed)

                    Period_Check.stop()

        elif Dotw == 5:
            
            todSub_202 = holiSub
            todSub_204 = holiSub

            embed=discord.Embed(title=f'[{dotwName[0]}]', description=f'{dotwName[0]}', color=0x00ff00)
            embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[0]}]', inline=False)
            embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[0]}]', inline=False)
            await channel.send(embed=embed)

            Period_Check.stop()
            
        elif Dotw == 6:

            todSub_204 = holiSub
            todSub_202 = holiSub

            embed=discord.Embed(title=f'[{dotwName[1]}]', description=f'{dotwName[1]}', color=0x00ff00)
            embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[0]}]', inline=False)
            embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[0]}]', inline=False)
            await channel.send(embed=embed)

            Period_Check.stop()

    elif Dotw == 2:
        if Dotw == 2:
            todSub_204 = wenSub_204
            todSub_202 = wenSub_202

            if td_hour == 9:
                if td_min == 10:
                    print("1교시")
                    embed=discord.Embed(title='[1교시 출첵을 해야할 시간입니다.]', description='##1교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[0]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[0]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 10:
                if td_min == 10:
                    print("2교시")
                    embed=discord.Embed(title='[2교시 출첵을 해야할 시간입니다.]', description='##2교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[1]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[1]}]', inline=False)
                    await channel.send(embed=embed)

            elif td_hour == 11:
                if td_min == 10:
                    print("3교시")
                    embed=discord.Embed(title='[3교시 출첵을 해야할 시간입니다.]', description='##3교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[2]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[2]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 12:
                if td_min == 10:
                    print("4교시")
                    embed=discord.Embed(title='[4교시 출첵을 해야할 시간입니다.]', description='##4교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[3]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[3]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 14:
                if td_min == 0:
                    print("5교시")
                    embed=discord.Embed(title='[5교시 출첵을 해야할 시간입니다.]', description='##5교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[4]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[4]}]', inline=False)
                    await channel.send(embed=embed)
            
            elif td_hour == 15:
                if td_min == 0:
                    print("6교시")
                    embed=discord.Embed(title='[6교시 출첵을 해야할 시간입니다.]', description='##6교시 출첵 알람##', color=0x00ff00)
                    embed.add_field(name=f'[2학년 4반]', value=f'[{todSub_204[5]}]', inline=False)
                    embed.add_field(name=f'[2학년 2반]', value=f'[{todSub_202[5]}]', inline=False)
                    await channel.send(embed=embed)

                    Period_Check.stop()
"""
    @Period_Check.after_loop
    #async def Period_Check_Loop_Checker(self):
    #    if Period_Check.is_running == True:
    #        print("실패")
    #
    #    elif Period_Check.is_running == False:
    #        print("성공")



    #    channel = bot.get_channel(txtchId)
    #    loop_chk = []
    #    if 1 in loop_chk:
    #        await channel.send(f"루프를 다 돌아 루프횟수가 [{loop_chk[0]}]이 되었으므로 루프를 종료합니다.")
    #        Period_Check.stop(txtchId)
    """



bot.run(BOT_TOKEN)
