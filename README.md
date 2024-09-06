# miniProject02

# Interactive Story Game with Sound Effects

## Team Members
- Maria Paula Castillo Erazo
- Valeria Fernanda Gustin 

## Project Description

This project is an interactive narrative game developed in Python, incorporating 3D sound effects using the OpenAL library. The player follows a storyline by making decisions that affect the character’s well-being. The narrative is structured in nodes where each decision leads to a new path, affecting the outcome of the game.

The game includes:
- A life points system that changes based on player decisions.
- Multiple possible endings depending on the player's life status and choices.
- Immersive sound effects that enhance the storytelling experience by simulating 3D audio.

## Justification

### 1. **Use of Python and OpenAL**
We chose Python for its simplicity and readability, which makes it an ideal choice for rapid prototyping and collaborative work. OpenAL was selected for handling 3D sound because it offers powerful tools to simulate realistic audio environments, crucial for immersing players in the game.

### 2. **Narrative Structure**
The decision to structure the story in nodes (`Nodo` class) allows for easy expansion and modification of the game. This design lets us add more branches and outcomes by simply updating the data structure (`data.py`). The life system (`Character` class) was implemented to add stakes to the player’s decisions, increasing the sense of immersion.

### 3. **Sound Design**
Using the `Sound` and `ListSounds` classes, we could implement multiple sound effects in each node to give the player a spatial audio experience. The integration of sound was crucial to immerse players and simulate different environmental effects, such as the sound of footsteps or ambient noises, based on the character’s location.

### 4. **Player Interaction**
The player's input is continuously validated to avoid crashes and ensure the experience remains smooth. We intentionally avoided infinite loops (`while True`) to make the code clearer and to reduce potential errors, opting instead for a controlled and safe input process.

## Conclusion

Our game was designed with modularity and scalability in mind. The use of a node-based structure for the narrative, combined with dynamic sound effects and player-driven outcomes, ensures that the project can be expanded in the future to include more complex features without a complete rewrite of the system.
