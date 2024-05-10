#Developer-HExX-XD#
import os, platform, time, sys
os.system('pkg install espeak -y')
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
 
print('\033[1;97m[\033[1;97m•\033[1;97m] \033[1;97mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')
hexxxd = platform.architecture()[0]
if hexxxd == '64bit':
 print('\033[1;97m[\033[1;97m•\033[1;97m] \033[1;97mYour Device is 64bit')
 import nn
elif hexxxd == '32bit':
 print('\033[1;97m[\033[1;97m•\033[1;97m] \033[1;97mYour Devive is 32bit')
 import nn
