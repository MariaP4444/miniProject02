import openal
import os

# Define the base path for sounds as a folder in the same directory as this Python file
path = os.path.join(os.path.dirname(__file__), 'sounds')

class Sound:
    def __init__(self, name, position, volume, velocity):
        # Build the file path using the base path and the name of the file
        sound_path = os.path.join(path, f"[MONO] {name}")

        # currentDir = os.path.dirname(os.path.abspath(__file__))
        # fileM = os.path.join(currentDir, "Music", self.__sound)
        
        self.buffer = openal.oalOpen(sound_path)
        self.buffer.set_position(position)
        self.buffer.set_gain(volume)
        self.buffer.set_velocity(velocity)
    
    def play_in_loop(self):
        self.buffer.set_looping(True)
        self.buffer.play()

class ListSounds:
    def __init__(self, sounds):
        self.sounds = sounds
    
    def play(self):
        for sound in self.sounds:
            sound.buffer.play()
        
        # Keep the program running until all sounds have finished
        while any(sound.buffer.get_state() == openal.AL_PLAYING for sound in self.sounds):
            pass