#!/bin/bash
set -e

PI_IP=192.168.1.114
ZIP_EXPORT=pi-mas.zip
PI_DIR=/home/pi/pi-mas/

echo "Adding files to ZIP export"
zip -r $ZIP_EXPORT src/. -x '*__pycache__*'
zip -g $ZIP_EXPORT ".env"
zip -g $ZIP_EXPORT requirements.txt
zip -r $ZIP_EXPORT audio/.

trap "rm $ZIP_EXPORT" INT

echo "Checking if Pi 0 is up..."
if ping -c 1 $PI_IP
then
    if ssh pi@$PI_IP "[ -d $PI_DIR ]"
    then
        echo "Clearing out directory on Pi"
        ssh pi@$PI_IP rm -R $PI_DIR
    else
        echo "Creating directory on Pi"
        ssh pi@$PI_IP mkdir $PI_DIR
    fi

    echo "Copying ZIP to Pi"
    scp $ZIP_EXPORT pi@$PI_IP:/home/pi/

    echo "Unzipping export"
    ssh pi@$PI_IP unzip /home/pi/$ZIP_EXPORT -d /home/pi/pi-mas/

    echo "Deleting ZIP $ZIP_EXPORT on Pi"
    ssh pi@$PI_IP rm $ZIP_EXPORT

    echo "Deleting local export ZIP file: $ZIP_EXPORT"
    rm $ZIP_EXPORT

    # echo "Installing Python requirements..."
    # ssh pi@$PI_IP pip3 install -r pi-mas/requirements.txt
else
    rm $ZIP_EXPORT
    exit 0
fi
