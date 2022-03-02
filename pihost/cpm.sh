#!/usr/bin/sh
[ -f /tmp/cpm.pid ] && cpm_pid=`cat /tmp/cpm.pid`; [ $cpm_pid != $$ ] && exit 
#ok try to start cpm
echo $$ >/tmp/cpm.pid
export TERM=vt102
sudo stty raw -F /dev/ttyUSB1
tcpser -n 0=bbs.fozztexx.com -n 1=rc2014.ddns.net:2014 -n 2=particlesbbs.dyndns.org:6400 3=blackicebbs.ddnss.ch -d /dev/ttyUSB1 -s 115200 -S 19200 -I &
python printproxy.py >/dev/null 2>&1 &
minicom -con -aon -S startup.script cpm 
pkill -9 -f tcpser
pkill -9 -f printproxy.py
rm /tmp/cpm.pid
