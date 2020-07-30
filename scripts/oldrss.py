#dependencies: linux, mpv and sfeed
import os
import tty
import sys
import termios


k = 0
os.chdir("/home/luiz/.sfeed/feeds") #Your feeds directory
os.system("sfeed_update")
browser = "surf" #Change this for the browser that you use
feeds = os.listdir(".")
orig_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
count = 0

def ib(k):
	if k == chr(27) or k == chr(113):
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
		sys.exit()

while True:
	try:
		os.system("clear")
		os.chdir("/home/luiz/.sfeed/feeds")
		count = -1
		print("-> The RSS feeds are:")
		for c in feeds:
			count+=1
			print("[{}] {}".format(count,c))
		k = int(input("-> Type the feed number: "))
		lines = os.popen("sfeed_plain {}".format(feeds[int(k)]))
		nfeeds = [line.strip() for line in lines]
		count = 0
		line = 1
		os.system("clear")
		while count < 10:
			if nfeeds[count][0] == "N":
				z = list(nfeeds[count])
				del(z[0:2])
				nfeeds[count] = "".join(z)
			print("[{}]	{}".format(count,nfeeds[count]))
			count+=1
		k = sys.stdin.read(1)[0]
		ib(k)
		link=nfeeds[int(k)][106::]
		if "https://www.youtube.com/watch?v=" in link:
			os.system("mpv --really-quiet=yes --ytdl-format=22 {}".format(link))
		else:
			os.system("{} {}".format(browser,link))
		k = sys.stdin.read(1)[0]
		ib(k)
	except Exception as e:
		print(e)
		input()
