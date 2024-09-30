from colorama import Style, Back, Fore, init, just_fix_windows_console
from bs4 import BeautifulSoup
from os import system, name
import requests
import sys
import datetime
import time
import json


now = datetime.datetime.today()
year = str(now.year)
month = str(now.month)
day = str(now.day)
hh = str(now.hour)
mm = str(now.minute)
ss = str(now.second)
token = "TOKEN"
Users = []
users = {}
repeater = ""

init(autoreset=False)
just_fix_windows_console()

def slowPrint(text, timer):
    for word in text:
        print(word, end="", flush=True)
        time.sleep(timer)

def load_users():
    with open("./db/Users.txt", "r", encoding="utf-8") as file:
        for user in file:
            user = user.replace("\n", "")
            Users.append(user)
            time.sleep(0.1)
            print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Fore.YELLOW}INFO{Fore.GREEN}] {Fore.WHITE}User {user} Loaded!")

    time.sleep(0.1)
    for user in Users:
        name, number = user.split()
        users[name] = number
    time.sleep(0.1)
    print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Fore.YELLOW}INFO{Fore.GREEN}] {Fore.WHITE} Ok Users Loaded, Let‘s GO to CHATS.")
    
def Running():
    load_users()
    time.sleep(0.1)
    print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Fore.MAGENTA}WARNING{Fore.GREEN}] {Fore.WHITE} Add New User from Telegram!")
    time.sleep(0.1)
    ID = input("What is ID New User: ")
    with open("./db/Users.txt", 'a+', encoding="utf-8") as file:
        file.write(str("\n"+ID))
        file.flush()
        
    time.sleep(0.1)
    print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Fore.YELLOW}INFO{Fore.GREEN}] {Fore.WHITE} User Saved on DataBase!")        
    
def banner():
    banner= f"""
\t╔════════════════════════════════════════════════════════════════════════════════════════════════════════╗
\t║                                                                                                        ║
\t║  ██████╗██╗  ██╗ █████╗ ████████╗██████╗  ██████╗ ████████╗    ██╗   ██╗ █████╗ ███████╗██╗██████╗ ██╗ ║
\t║ ██╔════╝██║  ██║██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗╚══██╔══╝    ██║   ██║██╔══██╗╚══███╔╝██║██╔══██╗██║ ║
\t║ ██║     ███████║███████║   ██║   ██████╔╝██║   ██║   ██║       ██║   ██║███████║  ███╔╝ ██║██████╔╝██║ ║
\t║ ██║     ██╔══██║██╔══██║   ██║   ██╔══██╗██║   ██║   ██║       ╚██╗ ██╔╝██╔══██║ ███╔╝  ██║██╔══██╗██║ ║
\t║ ╚██████╗██║  ██║██║  ██║   ██║   ██████╔╝╚██████╔╝   ██║        ╚████╔╝ ██║  ██║███████╗██║██║  ██║██║ ║
\t║  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═════╝  ╚═════╝    ╚═╝         ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝ ║
\t║                          {Fore.GREEN}CoDed By Vaziri Telegram:@Now_Republic_of_Humanity {Fore.RED}                           ║
\t╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝
\n\nAdmin: alivazirim1@gmail.com"""                    
    print(Fore.RED+banner)
    print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Fore.YELLOW}INFO{Fore.GREEN}] {Fore.WHITE} If You want to close app Please Press key <CTRL+C>")
    load_users()
    names = users.keys()
    time.sleep(2)
    print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Fore.YELLOW}INFO{Fore.GREEN}] {Fore.WHITE} User List:")
    for name in names:
        print("\t"+f"{Fore.YELLOW}[{Fore.BLUE}+{Fore.YELLOW}] {Fore.WHITE}"+name)
        time.sleep(0.1)
        
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def update(User):
    my_data = {
        "UrlBox": f"https://api.telegram.org/bot{token}/Getupdates",
        "AgentList": "Internet Explorer",
        "VersionsList": "HTTP/1.1",
        "MethodList": "GET"
    }
    try:
        source = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=my_data).content.decode()
    except:
        time.sleep(0.1)
        print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Back.RED+Fore.WHITE}PROBLEM{Fore.GREEN}] {Fore.WHITE} Network Error! Try again.")
        sys.exit(1)
    soup = BeautifulSoup(source, "html.parser")
    find_tag = json.loads(str(soup.findAll("pre"))[61:-7])
    if str(find_tag["result"]) == "[]":
        time.sleep(0.1)
        print("Data Fot Found!")
    else:
        Date = f"{year}-{month}-{day} {hh}:{mm}:{ss}"
        first_name = find_tag["result"][-1]["message"]["from"]["first_name"]
        username = find_tag["result"][-1]["message"]["from"]["username"]
        language_code = find_tag["result"][-1]["message"]["from"]["language_code"]
        id = find_tag["result"][-1]["message"]["from"]["id"]
        is_bot = find_tag["result"][-1]["message"]["from"]["is_bot"]
        type = find_tag["result"][-1]["message"]["chat"]["type"]
        Info = f"""Information user {User}:\n\tDate: {Date}\n\tFirst name: {first_name}\n\tUsername: {username}\n\tlanguage account: {language_code}\n\tNumber id: {id}\n\tis Bot: {is_bot}\n\tType account: {type}"""
        Name_U = input("What is Your Name? ")
        text = f"User {Name_U} is talking to you"
        send(text=text, User=id)
        print(Fore.WHITE+Info)
        for text in find_tag["result"]:
            txt = text["message"]["text"]
            shower = f"{Fore.BLUE+User+Fore.WHITE} has said: {Fore.WHITE+txt}"
            time.sleep(0.1)
            print(shower)
        while True:
            try:
                source = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=my_data).content.decode()
            except:
                time.sleep(0.1)
                print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Back.RED+Fore.WHITE}PROBLEM{Fore.GREEN}] {Fore.WHITE} Network Error! Try again.")
                sys.exit(1)
            soup = BeautifulSoup(source, "html.parser")
            find_tag = json.loads(str(soup.findAll("pre"))[61:-7])
            if str(find_tag["result"]) == "[]":
                time.sleep(0.1)
                print("Data Fot Found!")
            else:
                try:
                    time.sleep(0.1)
                    you = input(f"{Fore.RED}You: ")
                    send(str(you), id)
                    try:
                        text = find_tag["result"][-1]["message"]["text"]
                        if text == "":
                            time.sleep(0.1)
                            print(f"{User}: {Fore.GREEN} User DiSconnected!")
                        else:
                            time.sleep(5)
                            time.sleep(0.1)
                            print(f"{Fore.BLUE+User}:"+text)
                            repeater = text
                
                    except:
                        pass
                except:
                    time.sleep(0.1)
                    print(f"\n{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Back.RED+Fore.WHITE}PROBLEM{Back.RESET+Fore.GREEN}] {Fore.WHITE} There is a problem in the chat connection area, please report the problem to the admin")
                    time.sleep(0.1)
                    print(Fore.WHITE+"Admin: alivazirim1@gmail.com")
                    time.sleep(0.1)
                    print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Back.RED+Fore.WHITE}PROBLEM{Back.RESET+Fore.GREEN}] {Fore.WHITE} The program is closed for security reasons")
                    sys.exit(1)

def send(text, User):
    if text == ".":
        pass
    else:
        url = (f"https://api.telegram.org/bot{token}/sendmessage?chat_id={User}&text="+str(text))
        my_date = {
            "UrlBox":url,
            "AgentList":"Internet Explorer",
            "VersionsList":"HTTP/1.1",
            "MethodList":"GET"  
                    }
        try:
            source = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=my_date)
        except:
            print(f"\n{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Back.RED+Fore.WHITE}PROBLEM{Fore.GREEN+Back.RESET}] {Fore.RED} There is a problem in sending your message. Please check your internet. If you were connected, please share the problem with the admin!")

def chat():
    print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Fore.MAGENTA}WARNING{Fore.GREEN}] {Fore.WHITE} Next, you need usernames for chatting!")
    User = input("Enter the username you want: ")
    if User == "":
        print(Fore.RED+Back.WHITE+"Your choice is INVALID!",Back.RESET)
    print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Fore.YELLOW}INFO{Fore.GREEN}] {Fore.WHITE} Connecting to user")
    if User in users.keys():
        time.sleep(0.1)
        print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Fore.MAGENTA}WARNING{Fore.GREEN}] {Fore.WHITE} User {User} Founded!")
        time.sleep(0.1)
        print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Fore.YELLOW}INFO{Fore.GREEN}] {Fore.WHITE+Back.RED} Let‘s Chat {User}{Back.RESET}")
        Help = f"""{Fore.CYAN}In the <You> field, write the text you want to display for the user! And if you have nothing to say and you want to see what message the destination user has sent you,\n\tenter the message <.> and press enter.\n\tIn the section {User}, the messages of the destination user will be displayed for you\n\tYou can send a message every 5 seconds!"""
        slowPrint("Help:\n\t"+Help, 0.04)
        time.sleep(0.1)
        print("\n\n\t",Fore.WHITE+"-"* 25+f"<{Fore.RED+User+Fore.WHITE}>"+"-" * 25)
        time.sleep(0.1)
        update(User=User)
    else:
        print(f"{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Back.RED+Fore.WHITE}PROBLEM{Fore.GREEN+Back.RESET}] {Fore.WHITE} User Not Found!")    

def application():
    add_qs = input("Do you want Add User?[Y/N]")
    if add_qs.lower() == 'y':
        Running()
        time.sleep(5)
        clear()
        banner()
        chat()
    else:
        clear()
        banner()
        chat()



if __name__ == "__main__":
    try:
        application()
        
    except:
        print(f"\n{Fore.WHITE}[{Fore.CYAN}{hh}{Fore.GREEN}:{Fore.CYAN}{mm}{Fore.GREEN}:{Fore.CYAN}{ss}{Fore.WHITE}] {Fore.GREEN}[{Back.RED+Fore.WHITE}PROBLEM{Fore.GREEN+Back.RESET}] {Fore.WHITE} The program was terminated by the user")
        sys.exit(1)
