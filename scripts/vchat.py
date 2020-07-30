import socket
import pyttsx3

channel = input("Type the channel ID: ")
engine = pyttsx3.init()
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'horadocontra'
token = 'oauth:j3hkqw1fyrhaerttnr6cpvuir57jx8'

def getuser(resp):
	separate = resp.split(":",2)
	user = separate[1].split("!",1)[0]
	return user

def getmessage(resp):
	try:
		message = resp.split(":",2)[2]
	except Exception as e:
		print(e)
		message = ""
	return message

def chat():
	count = 0
	while True:
		count+=1
		print("{} reset".format(count))
		sock = socket.socket()
		sock.settimeout(40)
		sock.connect((server, port))
		sock.send(f"PASS {token}\n".encode('utf-8'))
		sock.send(f"NICK {nickname}\n".encode('utf-8'))
		sock.send(f"JOIN #{channel}\n".encode('utf-8'))
		try:
			while True:
				resp = sock.recv(1024).decode('utf-8')
				#print (resp) enable this for debuging
				if "PRIVMSG" in resp:
					user = getuser(resp)
					message = getmessage(resp)
					print("{}: {}".format(user,message))
					engine.say("{}: {}".format(user,message))
					engine.runAndWait()
		except Exception as e:
			#print(e)
			sock.close()

chat()
