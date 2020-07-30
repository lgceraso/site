#!/bin/bash
# dependencie: sfeed
# if fails: try https://aur.archlinux.org/font-symbola.git
echo "-> Updating the feeds"
sfeed_update
while true
do
  clear
  cd "${HOME}"/.sfeed/feeds || exit # change this!
  echo "-> The last feeds are:"
  sfeed_plain ./* | grep '^N' | sort -n | cut -c 3-
  printf "\n\n\n"
  echo "-> The feeds are:"
  ls
  read -rp "-> Type the feed name: " feed
  clear
  cat "$feed" | sfeed_plain | cut -c 3- | sed 's/^/\t/' | grep -n '^' | sort -nr || exit
  read -p "-> Type the feed number: " line
  url=$(cat "$feed" | sfeed_plain | cut -c 2- | sed 's/^/\t/' | grep -n '^' | sed -n "$line p" | grep -Eo '(http|https)://[a-zA-Z0-9./?=_%:-]*')
  if [ ! "$(echo "$url" | grep "https://www.youtube.com/watch?v=")" ]; then
    xdg-open "$url" && clear
  else
    echo "-> The video is loading..."
    mpv --really-quiet=yes "$url" || xdg-open "$url" && clear
  fi
done
