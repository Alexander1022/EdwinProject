import sys, os
import random
from bg_tts import talk
from mpyg321.mpyg321 import MPyg321Player

def play_music_os(filename):
    return os.system("mpg123 '" + filename + "'")

def find_music(directory):
    songs = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                songs.append(os.path.join(root, filename))
    return songs


def player(directory):
    try:
        songs = find_music(directory)
        song = random.choice(songs)
        play_music_os(song)
        
    except IndexError as error:
        print("Не намерих песни.")
        talk("Не намерих песни.")