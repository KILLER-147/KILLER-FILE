#Developer-HExX-XD#
import os,platform
os.system('git pull')
os.system("clear")
hexx=platform.architecture()[0]
if hexx=="32bit":
    __import__("nn")
elif hexx=="64bit":
    __import__("nn")
