#!bin/bash
#Purpose: To find the file size of all the files in the directory
#Version: 1.0
#Created Date: Fri Jan 3 09:25:48 PM IST 2025
#Modified Date:
#Author: Kajal Chauhan
# START #
echo "Enter Directory name"
read dir
if [ ! -d $dir ]
then
	echo "Invalid Directory"
	exit
fi
large=0
for file in `find $dir -type f`
do
	size=`stat -c %s $file`
	echo "size of $file is $size"
	if [ $size -gt $large ]
	then
		large=$size
	fi
done
echo "File with Maximum size is $large"
# END #
