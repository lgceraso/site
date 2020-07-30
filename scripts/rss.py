#dependencies: sfeed, mpv and youtube-dl
import os
import re
feedsdir = "/home/luiz/.sfeed/feeds" #your feeds directory
os.chdir(feedsdir) 
os.system("sfeed_update")
feeds = os.listdir(".")
urlregex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
while True:
    try:
        os.chdir(feedsdir)
        count = -1
        os.system("clear")
        print("-> The RSS feeds are:")
        for c in feeds:
            count+=1
            print("[{}]\t{}".format(count,c))
        choice = int(input("-> Type the RSS feed number: "))
        lines = os.popen("sfeed_plain {}".format(feeds[choice]))
        nfeeds = [line.strip() for line in lines]
        count = 0
        os.system("clear")
        for l in nfeeds:
            link = re.findall(urlregex,nfeeds[count])
            link = list(link[0])
            z = list(nfeeds[count])
            if nfeeds[count][0] == "N":
                del(z[0:2])
                nfeeds[count] = "".join(z)
            for c in feeds:
                if c in nfeeds[count]:
                    a = nfeeds[count].replace(link[0],"")
                    a = a.replace(c,"")
            print("[{}]\t{}\t{}".format(count,a,link[0]))
            count += 1
        count += 1
        choice = int(input("-> Type the feed number: "))
        link = re.findall(urlregex,nfeeds[choice])
        link = list(link[0])
        if "www.youtube.com/watch?v=" in link[0]:
            print("-> The video is loading...")
            os.system("mpv --really-quiet=yes {}".format(link[0]))
        elif "www.twitch.tv/videos/" in link[0]:
            print("-> The stream is loading...")
            os.system("mpv --really-quiet=yes {}".format(link[0]))
        else:
            os.system("xdg-open {}".format(link[0]))
        choice = input("-> Type Q to quit: ").lower()
        if choice == "q":
            break
    except Exception as e:
        #print(e) #uncomment these to display error messages
        #input()
        pass
