from audio_module_input import myAudioThread

thread_rec_speech = myAudioThread()

thread_rec_speech.start()
thread_rec_speech.join()

# from record import record
# import speechToText

# record_audio = record("testSpeech3text.wav")
# print("1")
# record_audio.record(5)
# print("2")
# speechToText.speechToText("testSpeech2text.wav")