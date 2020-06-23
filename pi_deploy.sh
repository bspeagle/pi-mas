#!/bin/bash
set -e

LAMBDA_EXPORT=audio.zip

echo "Adding files to ZIP export"
zip -r $LAMBDA_EXPORT src/. -x '*__pycache__*'
zip -g $LAMBDA_EXPORT ".env"
zip -g $LAMBDA_EXPORT requirements.txt

echo "Clearing out directory on Pi"
ssh pi@192.168.1.114 rm -R /home/pi/pi-mas/* /home/pi/pi-mas/.env

echo "Copying ZIP to Pi"
scp $LAMBDA_EXPORT pi@192.168.1.114:/home/pi/

echo "Unzipping export"
ssh pi@192.168.1.114 unzip /home/pi/$LAMBDA_EXPORT -d /home/pi/pi-mas/

echo "Deleting local export ZIP file: {$LAMBDA_EXPORT}"
rm $LAMBDA_EXPORT