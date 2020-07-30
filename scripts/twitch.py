import threading
import time
import socket
import os

#vars
chatop = int(input("-> Chat Type:\n[0] Integrated\n[1] Twitch GUI\n"))
playerop = int(input("-> Player:\n[0] Integrated\n[1] GUI\n"))
channel = input("-> Type the channel id: " )
quality = int(input("-> Quality:\n[0] 160p\n[1] 360p\n[2] 480\n[3] 720p\n[4] Source\n"))
server = "irc.chat.twitch.tv"
port = 6667
nickname = "horadocontra"
token = "oauth:dnhgvm7p692kmaxth8zbup5pndd76t"

#integrated chat
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
    time.sleep(3)
    count = 0
    while True:
        count += 1
        #print("{} reset".format(count))
        sock = socket.socket()
        sock.settimeout(40)
        sock.connect((server,port))
        sock.send(f"PASS {token}\n".encode("utf-8"))
        sock.send(f"NICK {nickname}\n".encode("utf-8"))
        sock.send(f"JOIN #{channel}\n".encode("utf-8"))
        os.system("clear")
        try:
            while True:
                resp = sock.recv(1024).decode("utf-8")
                # print (resp) enable this for debuging
                if "PRIVMSG" in resp:
                    user = getuser(resp)
                    message = getmessage(resp)
                    print("{}: {}".format(user,message))
        except Exception as e:
            print(e)
            sock.close()

#GUI chat
def guichat():
    time.sleep(3)
    os.system("xdg-open https://www.twitch.tv/popout/{}/chat?popout=".format(channel))

#Player
def player():
    if playerop == 0:
        if quality == 0:
            os.system("st -e mpv -vo=caca --really-quiet=yes --ytdl-format=160p https://www.twitch.tv/{}".format(channel))
        elif quality == 1:
            os.system("st -e mpv -vo=caca --really-quiet=yes --ytdl-format=360p https://www.twitch.tv/{}".format(channel))
        elif quality == 2:
            os.system("st -e mpv -vo=caca --really-quiet=yes --ytdl-format=480p https://www.twitch.tv/{}".format(channel))
        elif quality == 3:
            os.system("st -e mpv -vo=caca --really-quiet=yes --ytdl-format=720p https://www.twitch.tv/{}".format(channel))
        elif quality == 4:
            os.system("st -e mpv -vo=caca --really-quiet=yes https://www.twitch.tv/{}".format(channel))
        else:
            print("-> Error on quality definition!")
    if playerop == 1:
        if quality == 0:
            os.system("st -e mpv --really-quiet=yes --ytdl-format=160p https://www.twitch.tv/{}".format(channel))
        elif quality == 1:
            os.system("st -e mpv --really-quiet=yes --ytdl-format=360p https://www.twitch.tv/{}".format(channel))
        elif quality == 2:
            os.system("st -e mpv --really-quiet=yes --ytdl-format=480p https://www.twitch.tv/{}".format(channel))
        elif quality == 3:
            os.system("st -e mpv --really-quiet=yes --ytdl-format=720p https://www.twitch.tv/{}".format(channel))
        elif quality == 4:
            os.system("st -e mpv --really-quiet=yes https://www.twitch.tv/{}".format(channel))
        else:
            print("-> Error on quality definition!")

#Threading
c = threading.Thread(target=chat)
cgui = threading.Thread(target=guichat)
p = threading.Thread(target=player)
if chatop == 0:
    c.start()
elif chatop == 1:
    cgui.start()
else:
    print("-> Error on chat definition!")
p.start()

#For debugging
#print(threading.activeCount())
