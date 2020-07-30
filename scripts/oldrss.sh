#!/bin/bash
# Dependencies: dmenu, sfeed, mpv, youtube-dl and of course a browser
# In order to this to work you have to put a * in the lines that you want to play
browser="chromium"
sfeed_update && clear && echo "->Look skyward my friend..."
op=$(ls -I "\n" /home/luiz/.sfeed/feeds | dmenu -i -p "Pick a feed:")
clear && echo "->Loading..." && cat /home/luiz/.sfeed/feeds/$op | sfeed_plain  > urltemp && vim urltemp && grep \* urltemp | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" > url && mv url urltemp
for i in $(cat urltemp)
do
    if [ -z $(echo $i | grep "https://www.youtube.com/watch?v=") ]; then
    $browser $i
    else
      echo $i >> yts
    fi
done
touch yts
cat yts | mpv --really-quiet=yes --playlist=-
rm yts urltemp
read #I added this just in case the browser isn't fast enough
