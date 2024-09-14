"""
This module has simple CLI interface of a shop of Arcade Machines.

Author: David Felipe García León <dfgarcial@udistrital.edu.co>

This file is part of Arcade Machine Workshop1.

Arcade Machine Workshop1 is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

Arcade Machine Workshop1 is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with Arcade Machine Workshop1. If not, see <https://www.gnu.org/licenses/>. 
"""
from ArcadeMachineCLIWorkshop import RetroArcadeMachine, Game, User

class Catalog:
    """
    This class represents a catalog of available games for purchase.
    """
    available_games: list[Game]

    def __init__(self):
        """
        Initialize the catalog with a set of available games.
        """
        self.available_games = [
            Game("Pac-Man", 101),
            Game("Donkey Kong", 102),
            Game("Space Invaders", 103),
            Game("Street Fighter", 104),
            Game("Galaga", 105),
            Game("Tetris", 106),
            Game("Mortal Kombat", 107),
            Game("Sonic the Hedgehog", 108)
        ]

    def show_available_games(self):
        """
        This method displays the available games in the catalog.
        """
        print("\nAvailable Games in Catalog:")
        for game in self.available_games:
            print(f"- {game.name} (Code: {game.code})")
        print("\n")


def buy_retro_arcade_machine():
    """
    Function to simulate the process of purchasing a retro arcade machine.
    """
    # Create a retro arcade machine instance
    retro_machine = RetroArcadeMachine()

    # Let the user select material
    material = input("Enter the material for the retro machine (wood/metal): ")
    if material not in ["wood", "metal"]:
        print("Invalid material. Please try again.") 
        return input("Enter the material for the retro machine (wood/metal): ")
    else:
        retro_machine.select_material(material)


    # Let the user select color
    color = input("Enter the color for the retro machine (brown/black): ")
    if color not in ["brown", "black"]:
        print("Invalid color. Please try again.")
        return input("Enter the color for the retro machine (brown/black): ")
    else:
        retro_machine.select_color(color)

    # Create a catalog instance and show available games
    catalog = Catalog()
    catalog.show_available_games()

    # Let the user add games to the retro machine
    while True:
        add_game = input("Do you want to add a game to the retro machine? (yes/no): ").lower()
        if add_game == "yes":
            game_code = int(input("Enter the game code from the catalog: "))
            selected_game = next((game for game in catalog.available_games if game.code == game_code), None)
            if selected_game:
                retro_machine.add_game(selected_game)
            else:
                print("Invalid game code. Please try again.")
        elif add_game == "no":
            break
        else:
            print("Invalid option. Please enter 'yes' or 'no'.")

    # Collect customer information
    customer_name = input("\nEnter your name: ")
    customer_address = input("Enter your delivery address: ")

    # Create user instance
    user = User(customer_name, customer_address)

    # Finalize purchase and show summary
    print("\n--- Purchase Summary ---")
    print(f"Customer Name: {user.name}")
    print(f"Delivery Address: {user.address}")
    print(f"Arcade Machine Type: {retro_machine.theme}")
    print(f"Material: {retro_machine.material}")
    print(f"Color: {retro_machine.color}")
    print("Games added to the retro machine:")
    retro_machine.show_games()
    print("\nPurchase completed successfully!\n")


if __name__ == "__main__":
    buy_retro_arcade_machine()
    def main():
        buy_retro_arcade_machine()

    if __name__ == "__main__":
        main()