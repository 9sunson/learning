#!/bin/bash

# A shell countdown

clear
filename=$(date '+%Y/%m/%d %H:%M:%S')
echo $filename
echo -e
for((i=1800;i>0;i--));do
	echo -n -e "$i\r"
	sleep 1
done
echo "Please have a rest!!!"
echo "Please have a rest!!!"
echo "Please have a rest!!!"
echo -e
filename=$(date '+%Y/%m/%d %H:%M:%S')
echo $filename
