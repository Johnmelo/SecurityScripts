#!/bin/bash

helpusage="Uso: ./auto_mapping.sh TARGET_URL WORDLIST"
if [ "$1" == "" ];
then
	echo "$helpusage"
else
	if [ "$2" == "" ];
	then
		echo "$helpusage"
	else
		for word in $(cat $2)
		do
			response=$(curl -s -o /dev/null -w "%{http_code}" $1/$word/)
			if [ $response == "200" ];
			then
				echo "$1/$word/ [DIR]"
			else
				response=$(curl -s -o /dev/null -w "%{http_code}" $1/$word)
				if [ $response == "200" ];
				then
					echo "$1/$word [FILE]"
				fi
			fi

		done
	fi
fi
