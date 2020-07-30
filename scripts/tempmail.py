import requests
import random
import json
import string
import os

os.chdir("/home/luiz/downloads") # change this
times = int(input("-> Quantos emails você precisa? "))
login = []
count = 0

# generate the email
while count < times:
	letters = string.ascii_lowercase
	login.append(''.join(random.choice(letters) for i in range(10)))
	email = "{}@1secmail.com".format(login[count])
	print("-> Seu email é: {}".format(email))
	count += 1

# check the email
count = 0
while count < times:
	input("-> Pressione ENTER para checar o email.")
	check = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login={}&domain=1secmail.com".format(login[count]))
	checkj = json.loads(check.text)
	mailid = checkj[0]["id"]
	read = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login={}&domain=1secmail.com&id={}".format(login[count],mailid))
	content = read.text
	print(content)
	file = open("mailbox{}.html".format(count),"w")
	file.write(content)
	file.close()
	os.system(r"surf /home/luiz/downloads/mailbox{}.html".format(count))
	count+=1
