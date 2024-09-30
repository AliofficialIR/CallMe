from os import system, name

if name == "nt":
    system("cls")
else:
    system("clear")
    
try:
    import colorama
except:
    system("pip install colorama")
    
try:
    import requests
except:
    system("pip install requests")
    
try: 
    import bs4
except:
    system("pip install bs4")
try: 
    import datetime
except:
    system("pip install datetime")
    
