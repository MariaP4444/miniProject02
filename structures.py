import time
import sys

class Nodo:
    def __init__(self, dialog, sounds, options, well_being ):
        """
        Constructor of the Nodo class.

        dialog: Text of the dialog to be shown to the player.
        sounds: Associated sound effects.
        options: Dictionary of available options for the player.
        bienestar: A numeric value indicating if the node affects the player's life (positive or negative).
        """
        self.dialog = dialog
        self.sounds = sounds
        self.options = options
        self.well_being  = well_being   # Can be positive (increases life) or negative (decreases life) or zero (does not affect)
        
    def get_text(self):
        """
        Returns the dialog text along with the options.
        """
        text = self.dialog
        for option in self.options:
            text = f'\n{option}. '.join([text, self.options[option]['text']])
        return text
    
    def get_next_nodo(self, key_option):
        """
        Given a player-selected option, returns the next node of the story.
        
        key_option: The option selected by the player.
        """
        return self.options[key_option]["siguiente"]
    
    def print_nodo(self):
        """
        Prints the node dialog with a typing effect.
        """
        for char in self.get_text():
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.04)
        print()

    def modify_life(self, life):
        """
        Modifies the player's life depending on the node's well_being  value.
        Ensures that life does not exceed 100 or drop below 0.
        
        life: Current life of the player.
        """
        life += self.well_being 
        
        # Ensure life stays between 0 and 100
        if life > 100:
            life = 100
        elif life < 0:
            life = 0
        
        return life
    

class Character:
    def __init__(self, life):
        """
        Constructor of the Character class.
        life: Current life value of the character (0 to 100).
        """
        self.life = life

    def get_life(self):
        """
        Returns the current life of the character.
        """
        return self.life

    def set_life(self, life):
        """
        Modifies the life of the character, ensuring it remains between 0 and 100.
        """
        self.life = life

    def print_info(self):
        """
        Prints the character's attributes in a stylized way for a console game.
        """
        border = "═" * 30
        print(f"╔{border}╗")
        print(f"║{' Character Info '.center(30)}║")
        print(f"╠{border}╣")
        print(f"║ Life: {str(self.life).ljust(22)}/100║")
        print(f"╚{border}╝")


