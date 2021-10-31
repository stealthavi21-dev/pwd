import string
import random
from plyer import notification
from bs4 import BeautifulSoup
import requests

def notifi(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="",
        timeout=4
    )
if __name__ == "__main__":
    

    s1=string.digits
    s2=string.ascii_uppercase
    s3=string.punctuation
    s4=string.octdigits
    #len=int(input('length of pwd\n'))#hdo gibbershish
    s=[]
    s5=[]
    s.extend(list(s1))
    #s.extend(list(s2))
    s5.extend(list(s2))
    #s.extend(list(s4))
    #random.shuffle(s)
    #print(s[0:len])
    t="OTP"
    m=f'Your one time password is \n {"".join(random.sample(s5,3))}-{"".join(random.sample(s,6))}'
    notifi(t,m)
    #random.sample
    #print("".join(s[0:len]))
