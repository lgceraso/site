import requests
import random
import string
import json
import os

#I use this with Tor Browser xD
# Maybe you may need to install request -- just pip install requests

times = 1 #THE NUMBER OF LISTS TO GENERATE
count = 0 
login = []
files = []
os.chdir("/home/luiz/downloads")
file = open("data.txt","a")
file.write("https://teste.flashiptv.me/\nhttps://teste.beeiptv.me/\nhttps://teste.hardtv.me/\nhttps://teste.turbotv.me/\nhttps://teste.besttv.me/")

while count < times:
    
    #temp-mail
    letters = string.ascii_lowercase
    login.append(''.join(random.choice(letters) for i in range(10)))
    email = "{}@1secmail.com".format(login[count])

    #name
    #namegen = requests.get("http://names.drycodes.com/1?nameOptions=boy_names")
    #namejson = json.loads(namegen.text)
    #nome = namejson[0].replace("_"," ")

    #phone
    #phonerequest = requests.get("http://geradorapp.com/api/v1/cpf/generate?token=1c63d9ead1361c98e0a2fb820e2bff21")
    #phonejson = json.loads(phonerequest.text)
    #phone = phonejson["data"]["number"]

    #data
    file.write("\n{}".format(email))
    count+=1

file.close()
os.system("clear")
os.system("cat data.txt")
#os.system(r"proxychains surf")
count = 0
#checking the mail
while count < times:
    input("\nPress Enter to check the email")
    check = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login={}&domain=1secmail.com".format(login[count]))
    checkj = json.loads(check.text)
    mailid = checkj[0]["id"]
    read = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login={}&domain=1secmail.com&id={}".format(login[count],mailid))
    content = read.text
    file = open("iptv{}.html".format(count),"w")
    file.write(content)
    file.close()
    os.system(r"chromium /home/luiz/downloads/iptv{}.html".format(count))
    count+=1

#Managing the .m3u files
count = 0
input("Press Enter if you've downloaded the files")
a = os.listdir(".")
for c in a:
    if ".m3u" in c:
        files.append(c)
for c in files:
    count+=1
    os.system("mv {} lista{}.m3u".format(c,count))
os.system(r"mv *.m3u /home/luiz/docs/git/site/")
os.system("rm iptv*.html && rm data.txt")
print("Now pls \"gitsite iptv\"")
