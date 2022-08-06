import speech_recognition as sr

def speechToText(filename):
    r=sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)


# speechToText("testSpeech2text.wav")

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# r=sr.Recognizer()

# with sr.Microphone() as source:
#     r.dynamic_energy_threshold = True
#     r.energy_threshold = 100
#     r.pause_threshold = 0.7
#     print("Say something:")
#     audio = r.listen(source,timeout=5)

# with open("microphone_results.wav", "wb") as f:
#     f.write(audio.get_wav_data())

# try:
#     text = r.recognize_google(audio)
# except sr.UnknownValueError:
#     print("could not understand the audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))

# print(text)