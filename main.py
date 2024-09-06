import openal
import time
from soundCofiguration import Sound, ListSounds
from structures import Nodo, Character
from data import get_data


def create_Nodo(current_nodo_data):
    return  Nodo(
        current_nodo_data["text"],
        ListSounds([Sound(s["name"], s["position"], s["volume"], s["velocity"]) for s in current_nodo_data["sounds_config"]]),
        current_nodo_data["options"],
        current_nodo_data["well_being"]
    )

def get_valid_option(nodo):
    """ Ask the user for input until a valid option is provided """
    key_option = None
    valid = False
    
    while not valid:
        try:
            key_option = int(input("Elige una opción: "))
            if key_option in nodo.options:
                valid = True
            else:
                print("Opción inválida. Por favor, elige de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
    
    return key_option


def main():
    openal.oalInit()  # Initialize OpenAL

    # Create the main character with 100 life points
    player = Character(100)
    
    # Get the narrative (this should be a dictionary or structure in the data file)
    narrative = get_data()

    # Start the story at the "inicio" node
    current_nodo_key = "inicio"
    current_nodo_data = narrative[current_nodo_key]
    
    # Create the current node
    current_nodo = create_Nodo(current_nodo_data)

    # Print the initial node and play associated sounds
    current_nodo.print_nodo()
    current_nodo.sounds.play()

    # Update the player's life points
    player.set_life(current_nodo.modify_life(player.get_life()))
    player.print_info()
    end = False

    # User input to select an option
    key_option = get_valid_option(current_nodo)
    # Loop to iterate through the story
    while len(narrative[current_nodo.get_next_nodo(key_option)]["options"]) > 0 and end == False:
        current_nodo_key = current_nodo.get_next_nodo(key_option)
        current_nodo_data = narrative[current_nodo_key]

        current_nodo = create_Nodo(current_nodo_data)

        # Print the story of the current node and play the sounds
        current_nodo.print_nodo()
        current_nodo.sounds.play()

        # Modify the player's life based on the current node
        player.set_life(current_nodo.modify_life(player.get_life()))
        player.print_info()

        if player.get_life() == 0:
            end == True
        else:
            # Ask the user to select the next valid option
            key_option = get_valid_option(current_nodo)

    if player.get_life() == 0:
        print(" ---------- GAME OVER ----------  ")
        print("        Te quedaste sin vida ")
    else:
        # Final node (without options)
        current_nodo_key = current_nodo.get_next_nodo(key_option)
        current_nodo_data = narrative[current_nodo_key]

        current_nodo = create_Nodo(current_nodo_data)

        # Print the final node and play the sounds
        current_nodo.print_nodo()
        current_nodo.sounds.play()

    

    openal.oalQuit()  # Finalize OpenAL


main()