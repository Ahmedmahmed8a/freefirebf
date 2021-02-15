from os import popen
from os import mkdir
import itertools,requests,readline,random,string
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
while(True):
 temp=digits+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
 print("\x1b[92m[*]Trying the code ["+temp+"]")
 r = requests.post(url, cookies=cookies,json={"serialno":temp})
 print("\x1b[93m"+r.text)
