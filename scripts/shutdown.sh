#!/bin/bash
op=$(echo -e "Poweroff\nReboot" | dmenu -i -p "Which?")
if [ "$op" = "Poweroff" ]; then
  poweroff
elif [ "$op" = "Reboot" ]; then
  reboot
else
  exit && exit
fi
