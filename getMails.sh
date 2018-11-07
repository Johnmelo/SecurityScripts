#!/bin/bash
if [ "$1" == "" ];
then
echo "forma de uso: "
echo "./webParsing.sh target.com"
else
echo "####################################################"
echo "BUSCANDO EMAILS"
echo "####################################################"

wget -nv --output-document index.html "$1" 

cat index.html | grep "@" > mails.out
#echo ####################################################"
#echo EMAILS"
#echo ####################################################"

#for url in $(cat hosts.txt);do
#host $url | grep has address" >> temp_actives.txt
#done
#cat temp_actives.txt | sort -u > hosts_actives.txt
#cat hosts_actives.txt
#rm parsing.txt temp_actives.txt
fi
