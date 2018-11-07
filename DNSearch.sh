#!/bin/bash

if [ "$1" == "" ] || [ "$2" == "" ];
then
echo "Uso: "
echo "./dns.sh TARGET_DOMAIN WORDLIST"
else
servers=$(host -t ns $1 | cut -d " " -f 4)
echo "==============SERVERS================"
echo "${servers[@]}"
echo ""
echo "====================================="

echo "===========MAIL SERVERS=============="
host -t mx $1 | cut -d " " -f7
echo "====================================="
echo "=========TRY BRUTEFORCE NAME========="
for word in $(cat $2)
do
host $word.$1 | grep "has address" | grep -v "92.242.140.20"
done
echo "===================================="
echo "=========TRY ZONE TRANSFER=========="
for server in $servers;
do
host -l $1 $server | grep "has address"
done
fi
