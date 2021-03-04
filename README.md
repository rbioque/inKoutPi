# inKoutPi 
Incubator automated

Dependencies:
To use the tempControl you will first need a few dependencies:

- Python library
```
sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
```

- Adafruit_Python_DHT
```
sudo pip3 install Adafruit_DHT
```

- WiringPi for python
```
sudo apt-get install python-dev python-setuptools swig
sudo pip3 install wiringpi
```

Crontab configure:
```
sudo crontab -e
```
```
*/1 * * * * /usr/bin/python /home/pi/inKoutPi/tempControl.py
*/1 * * * * sleep 30 && /usr/bin/python /home/pi/inKoutPi/tempControl.py
```

Version 1.1 inKoutPi

- MongoDB
```
sudo apt-get install mongodb
sudo /etc/init.d/mongodb start
mongo < /home/pi/inKoutPi/DB/mongo-1.0.js 
```

- PyMongo
```
sudo apt-get install python-pip
sudo apt-get install build-essential python-dev
sudo python -m pip install pymongo==3.0.3
```

Version 2.0 inKoutPi

- DJango
```
git clone https://github.com/django/django.git
```
