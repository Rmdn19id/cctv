# Author : Mr.Rm19
# jangan ganti author cape tau bikin nya!

import DATA
from DATA.id import *
import requests,re,os

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"



def main():
    os.system('clear')
    print("{}        ____ ").format(r)
    print("   _[]_/____\__n_ ")
    print("  |_____.--.__()_|")
    print("  |I   //# \\\    |")
    print("{}  |P   \\\__//    | ").format(w)
    print("  |CS   '--'     | ")
    print("{}  '--------------'----------{}------------------.  ").format(r,w)
    print("{}  | {}Author  : {}Mr.Rm19 {}     | {}INDO{}N{}{}ESIA         | ").format(r,w,r,w,r,ir,reset,w)
    print("{}  | {}email   : {}ramdan19id@gmail.com {}| {}cctv hacked {}|").format(r,w,w,w,lgray,w)
    print("{}  '------------------------------------{}-------'  ").format(r,w)
    print ("  {}[ 1 ] {}Indonesia").format(r,w)
    print ""
    select = input("\033[1;31m[ \033[1;37mSelect@Number \033[1;31m]\033[1;37m> ")
    filtering(select)



def filtering(pilih):
    if pilih == 1:
        indonesia()
        print (r+"Exiting ..."+w)
        os.sys.exit()
    else:
        print (r+"Exiting ..."+w)
        os.sys.exit()

if __name__ == '__main__':
    main()
