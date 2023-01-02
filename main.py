import requests
import sys
from time import sleep as wait
from colorama import init
#set-up

init()
res = requests

#Api (Roblox api)
api = 'https://api.roblox.com/users/get-by-username?username='
#Classes 
class tool:
    def property_change(host, content, val):
        while True:
            api = requests.get(host)
            status = api.json()
            if  status[content] == val:
                return True
                break
            else:
                print('Checking status . . .')
                wait(2)
    def afk():
        pass
class color_text:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'
class banner:
    text = '''
                 _____       _           _             
       /\       |_   _|     (_)         | |            
      /  \   ___  | |  _ __  _  ___  ___| |_ ___  _ __ 
     / /\ \ / __| | | | '_ \| |/ _ \/ __| __/ _ \| '__| 
    / ____ \ (__ _| |_| | | | |  __/ (__| || (_) | |   
   /_/    \_\___|_____|_| |_| |\___|\___|\__\___/|_|   
                        _/ |                        
                       |__/                      
    '''
class login:
    def user_insert_display():
        print(f'{color_text.lightred}{banner.text}{color_text.reset}')
        print(f'{color_text.bold}Press verify to your roblox account :DDD\nAcInjector will wait untill your status online . . .{color_text.reset}')
        user = input(f'Insert Username : ')
        return user
    def user_insert(user):
        user_info = res.get(f'{api}{user}')
        if user_info.status_code == 200:
            print(f'Connected To Roblox.api >#<\n')
            user_json = user_info.json()
            wait(1)
            print(f'Checking data for Username . . . {user}')
            check = login.login_log.nil_gets(user_json)
            if check == True:
                print('Found User !')
                print(f'\nLoading User Data . . .')
                wait(.2)
                print(f'\n\nUser : {user_json["Username"]}\nId : {user_json["Id"]}\n\n', f"{color_text.bold}note - Please turn on your Roblox, if you didn't make it real quick, The program will cooldowns.{color_text.reset}")
                waitfor = input(f"Press enter when you're ready, The program will knows if you been joined the game.\n\n")
                bl = tool.property_change(f'https://api.roblox.com/users/{user_json["Id"]}/onlinestatus/','IsOnline', True)
                if bl == True:
                    print(f'{user}, Is now Online ! . . . Checking if The player is in the game already')
                    wait(3)
                    waitfor = input(f"Press enter whenever you've enter the game -- {color_text.lightblue}https://www.roblox.com/games/11951597012/Verify-ac-inject{color_text.reset}")
                    bl = tool.property_change(f'https://api.roblox.com/users/{user_json["Id"]}/onlinestatus/', 'PlaceId', 11951597012)
                    if bl == True:
                        print(True)
            else:
                print('User not found.\n Please close and renew program login page.')
                wait_for = input()
        elif user_info.status_code == 429:
            print(f"Cooldown . . . verifying got declind, Please wait for new request quota.")
        else:
            print(f'The status code responed : {user_info.status_code}')
    class login_log:
        def nil_gets(user_json):
            try:
                user_json['success']
                return False
            except:
                return True



#index runnin
user = login.user_insert_display()
login.user_insert(user)


