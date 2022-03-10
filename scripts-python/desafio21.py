from pygame import *
init()
mixer.music.load("e:\Musica\Musicas\DROELOE - Open Blinds.mp3")
mixer.music.play()


while mixer.music.get_busy():
    time.Clock().tick(10)
