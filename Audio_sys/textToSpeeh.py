import pyttsx3


def speek(text_speek):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    # engie.say("turn left and go straight to the end of this road")
    engine.say(text_speek)
    engine.runAndWait()


# speek("turn left and go straight to the end of this road")

# data_test = bytearray([0x01,0x02,0x03,0x04])
# data_test[2] = 0x88

# print(data_test)