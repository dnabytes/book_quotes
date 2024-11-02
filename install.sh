#!/bin/bash

if [ -L "/usr/local/bin/quotes" ]; then
    sudo rm "/usr/local/bin/quotes"
fi

if [ -d "/usr/local/bin/quotes_files" ]; then
    sudo rm -r "/usr/local/bin/quotes_files"
fi

if [ -z "$bookquotes" ];then
    while : ; do
        echo -n "path to your quotes dir: "
        read pathToQuotes
        if [ -d "$pathToQuotes" ]; then
            echo "export bookquotes=$pathToQuotes" >> $HOME/.bashrc
            break
        else
            echo "$pathToQuotes doesn't exist, try again."
        fi
    done
fi

if [ "$1" == "local" ];then
    sudo cp -r src /usr/local/bin/quotes_files
else
    wget http://github.com/dnabytes/quotes/archive/master.zip -O /tmp/quotes.zip
    unzip -o /tmp/quotes.zip -d /tmp
    sudo cp -r /tmp/quotes-main/src /usr/local/bin/quotes_files
fi
cd /usr/local/bin
sudo ln -s /usr/local/bin/quotes_files/quotes.py quotes
sudo chmod a+rx quotes
bash
