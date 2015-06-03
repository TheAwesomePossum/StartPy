import Globals as g
Sound = g.pygame.mixer.Sound
g.pygame.mixer.pre_init(44100, -16, 2, 2048)

class SoundClip:
    def __init__(self, file):
        self.sound = Sound(file)

    def play(self):
        self.sound.play()

    def loop(self):
        self.sound.play(loops=-1)

    def stop(self):
        self.sound.stop()

    def setVolume(self, v):
        self.sound.set_volume(v)
