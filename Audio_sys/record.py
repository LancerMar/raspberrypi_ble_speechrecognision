# import os

# command = "arecord -D plughw:1 -c1 -r 48000 -f S32_LE -t wav -V mono -v record.wav"
# os.system(command)

# import subprocess
# import time

# command = "arecord -D plughw:1 -c1 -r 48000 -f S32_LE -t wav -V mono -v record.wav"
# p = subprocess.Popen(command,shell=True)

# time.sleep(10)

# p.kill()


import sounddevice as sd
import numpy as np
import wavio as wv


class record:
    def __init__(self,file_name):
        self.file_name = file_name

        sd.default.device = 'snd_rpi_i2s_card'
        sd.default.samplerate = 48000
        sd.default.channels = 1

    # time(int) :seconds
    def record(self,time):
        print("start recording speech ...")
        self.rec = sd.rec(np.int32(time * 48000))
        sd.wait()
        wv.write(self.file_name, self.rec, 48000, sampwidth=4)
