# raspberrypi_ble_speechrecognision


```
sudo apt-get -y update
sudo apt-get -y upgrade
```

## audio module

i2s_mic for linux: [link](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-i2s-mems-microphone-breakout.pdf)

```
sudo apt-get install libasound2-dev python3-pip libboost-all-dev
```

switch pin: 29 GND

```
python3 -m pip install sounddevice
sudo apt-get install libportaudio2
pip3 install wavio
pip3 install SpeechRecognition
sudo apt-get install flac

pip3 install pyttsx3
sudo apt install espeak
pip3 install pyaudio
```



## BLE module

sudo apt-get install libportaudio2
```
sudo apt-get install python-pip libglib2.0-dev
sudo pip install bluepy
```
