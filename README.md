# inKoutPi
Incubator automated

Dependencies:
To use the tempControl you will first need a few dependencies:

- Python library
sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl

- Adafruit_Python_DHT
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT

sudo python setup.py install

Crontab configure:
crontab -e

*/1 * * * * /usr/bin/python /home/pi/inKoutPi/tempControl.py
*/1 * * * * sleep 30 && /usr/bin/python /home/pi/inKoutPi/tempControl.py

