import RPi.GPIO as GPIO
import time
import threading

from record import record
import speechToText


class myAudioThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("start audio threading")
        audio_switch()


speech_file_name = "speech.wav"

def switch(channel):
    if(GPIO.input(channel)):
        print("loose the switch")
    else:
        print("press the switch")
        print("0")
        record_audio = record(speech_file_name)
        print("1")
        record_audio.record(10)
        print("2")
        speechToText.speechToText(speech_file_name)


def audio_switch():
    Switch_input_pin = 29
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Switch_input_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(Switch_input_pin,GPIO.BOTH,callback=switch,bouncetime=200)

    while(True):
        print("wait switching operate...")
        time.sleep(1)
        pass