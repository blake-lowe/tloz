from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC

PlaySound('audio/Intro.wav', SND_FILENAME|SND_ASYNC|SND_LOOP)

input()

PlaySound(None, SND_FILENAME)
