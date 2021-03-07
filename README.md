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
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install
```

- WiringPi for python
```
sudo apt-get install python-dev python-setuptools swig
git clone --recursive https://github.com/WiringPi/WiringPi-Python.git
cd WiringPi-Python
sudo python setup.py install
```

Crontab configure:
```
sudo crontab -e
```
```
*/1 * * * * /usr/bin/python /home/pi/inKoutPi/init.py
*/1 * * * * sleep 30 && /usr/bin/python /home/pi/inKoutPi/init.py
```

Version 1.1 inKoutPi

- MongoDB
```
sudo apt-get install mongodb
sudo /etc/init.d/mongodb start
mongo < /home/pi/inKoutPi/DB/mongo-init.js 
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
python -m pip install --upgrade pip setuptools
sudo python3 -m pip install django
sudo pip install pymongo==3.4.0
```

Configuración inicio
```
sudo cp inKoutPi/inkoutpiIU /etc/init.d/
sudo chmod 755 /etc/init.d/inkoutpiIU
sudo update-rc.d inkoutpiIU defaults
```
