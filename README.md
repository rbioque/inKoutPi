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

- WiringPi for python
sudo apt-get install python-dev python-setuptools swig
git clone --recursive https://github.com/WiringPi/WiringPi-Python.git
cd WiringPi-Python
./build.sh
sudo python setup.py install

Crontab configure:
sudo crontab -e

*/1 * * * * /usr/bin/python /home/pi/inKoutPi/tempControl.py
*/1 * * * * sleep 30 && /usr/bin/python /home/pi/inKoutPi/tempControl.py


Version 1.1 inKoutPi

- MongoDB
sudo apt-get install mongodb
sudo /etc/init.d/mongodb start
mongo < /home/pi/inKoutPi/DB/mongo-1.0.js 

- PyMongo
sudo apt-get install python-pip
sudo apt-get install build-essential python-dev
sudo python -m pip install pymongo
