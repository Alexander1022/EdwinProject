import time
import simpleaudio as saudio

def alarm():
    wave_obj = saudio.WaveObject.from_wave_file("./sounds/edwin_alarm.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    