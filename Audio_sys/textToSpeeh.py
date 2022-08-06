import pyttsx3


def speek(text_speek):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    # engie.say("turn left and go straight to the end of this road")
    engine.say(text_speek)
    engine.runAndWait()


# speek("turn left and go straight to the end of this road")