#!bin/bash
#Purpose: Reverse a String
#Version: 1.0
#Created Date: Fri Jan 3 08:34:58 PM IST 2025
#Modified Date:
#Author: Kajal Chauhan
# START #
if [ $# -eq 0 ]
then
	echo "Argument not found"
exit
else
	i=`echo $*|wc -w`
	while [ $i -gt 0 ]
	do
		s=`echo $*|cut -d " " -f $i`
		temp=`echo $temp $s`
		i=`expr $i - 1`
	done
	echo "Total number of arguments: $#"
	echo "Arguments list:$*"
	echo "Reversed list: $temp"
fi
# END #
