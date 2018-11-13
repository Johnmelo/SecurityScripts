#!/bin/bash
if [ "$1" == "" ];
then
echo "forma de uso: "
echo "./getMails.sh target.com"
else
echo "####################################################"
echo "BUSCANDO EMAILS"
echo "####################################################"

wget -nv --output-document index.html "$1" 

cat index.html | grep "@" > mails.out
fi
