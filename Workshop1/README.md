# Retro Arcade Machine Purchase Simulator

This project simulates the process of purchasing a retro arcade machine. The user can select the material, color, and games for the arcade machine from a predefined catalog of classic retro games. The program is written in Python and follows an object-oriented approach with the use of abstract classes and inheritance.

## Project Owner

**David Felipe García León**  
Email: [dfgarcial@udistrital.edu.co](mailto:dfgarcial@udistrital.edu.co)  
This is the first workshop for the **System Modeling Foundations** class.

## Table of Contents

- [Retro Arcade Machine Purchase Simulator](#retro-arcade-machine-purchase-simulator)
  - [Project Owner](#project-owner)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Classes](#classes)
    - [Key Methods](#key-methods)
  - [How to Run](#how-to-run)

## Description

This project provides an interactive command-line interface that allows a user to purchase a retro arcade machine by:

1. Selecting the material (wood/metal).
2. Selecting the color (brown/black).
3. Choosing up to five classic games from a catalog.
4. Providing user details like name and address.
5. Displaying a final purchase summary with all selected options.

The project leverages OOP concepts like inheritance and abstract methods. The retro arcade machine extends the behavior of a generic arcade machine, and games are managed within a catalog.


## Classes

- **`Game`**: Represents a game with attributes like `name` and `code`.
- **`AbstractArcadeMachine`**: Abstract base class for an arcade machine with methods for selecting material, color, and adding games.
- **`RetroArcadeMachine`**: Inherits from `AbstractArcadeMachine` and implements behavior specific to a retro-themed machine.
- **`Catalog`**: Contains a list of available retro games.
- **`User`**: Represents a user purchasing the arcade machine.
  
### Key Methods

- `select_material(material: str)`: Selects the material for the arcade machine.
- `select_color(color: str)`: Selects the color for the arcade machine.
- `add_game(game: Game)`: Adds a game to the arcade machine (up to 5 games).
- `show_games()`: Displays the games added to the machine.

## How to Run

1. Clone the repository.
2. Make sure you have Python installed.
3. Navigate to the project directory.
4. Run the program using the command:
   ```bash
   python main.py



This file provides an overview of your project, its structure, and how to run it. You can adapt it as needed!
