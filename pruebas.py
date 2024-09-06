import openal
import math
from soundCofiguration import Sound, ListSounds

openal.oalInit()
# Crear algunos sonidos de prueba
# sound1 = Sound(name='xgPruebas.wav', position=(0, 0, 0), volume=1.0, velocity=(0, 0, 0))


# Crear un sonido que suena a la derecha (eje x positivo)
# sound1 = Sound(name='xgPruebas.wav', position=(10, 0, 0), volume=1.0, velocity=(0, 0, 0))

# # Crear un sonido que suena por encima (eje y positivo)
# sound1 = Sound(name='xgPruebas.wav', position=(0, 5, 0), volume=1.0, velocity=(0, 0, 0))

# # # Crear un sonido que suena detrás (eje z positivo)
# sound1 = Sound(name='xgPruebas.wav', position=(0, 0, 5), volume=1.0, velocity=(0, 2, 0))
# Configurar la velocidad del oyente para que OpenAL aplique el efecto Doppler

# Establecer la posición del oyente
openal.Listener.position = (0, 0, 0)
openal.Listener.orientation = ((0, 0, -1), (0, 1, 0))
# Simulación de eco con un volumen reducido y retraso
sound_echo = Sound(name='xgPruebas.wav', position=(0, 0, 2), volume=0.5, velocity=(0, 0, 0))

# Crear una lista de sonidos
list_of_sounds = ListSounds([sound_echo])
def move_sound_in_circle(sound, radius, speed):
    """Move the sound around the listener in a circular path."""
    angle = 0
    while sound.buffer.get_state() == openal.AL_PLAYING:
        x = radius * math.cos(angle)
        y = 0
        z = radius * math.sin(angle)
        
        sound.set_position((x, y, z))
        
        angle += speed
        if angle >= 2 * math.pi:
            angle = 0
        openal.oalSleep(0.05)

# move_sound_in_circle(sound_echo, radius=5, speed=0.1)
# Reproducir los sonidos
list_of_sounds.play()
openal.oalQuit()



