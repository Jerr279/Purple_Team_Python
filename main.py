import mybanner, colorama, os, subprocess
from colorama import just_fix_windows_console
from colorama import Fore
from colorama import Style
from colorama import Back
from subprocess import run
from Blue_Team import *
from Red_Team import *
try:
    colorama.init()
except:
    print("[+] Please Setup Tool\npython3 install.py")

# ==================================================================================================================== #

def main():
    RTBT = input("Choice: ")
    if RTBT == "1":       
        run('python3 Red_Team/RedTeam.py')
        # os.system("python3 Blue_Team/RedTeam.py")
    elif RTBT == "2":
        run('python3 Blue_Team/BlueTeam.py')
        # os.system("python3 Blue_Team/BlueTeam.py")
    else:
        print("input error")
        main()

# ==================================================================================================================== #

if __name__ == "__main__":
    mybanner.PrintBanner()
    main()