"""
This module has concret and abstract classes of a Shop of Machine Arcade.

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

from abc import ABC, abstractmethod

class Game(ABC):
    """
    This class represents the behavior of a game.
    """

    name: str
    cod: int

    def __init__(self, name: str, code: int):
        """
        This method initializes the game.

        Args:
            name(str): The name of the game.
            code(int): The code of the game.
        """
        self.name = name
        self.code = code

class AbstractArcadeMachine(ABC):
    """
    This class represents the behavior of an abstract arcade machine.
    """

    material: str
    color: str
    games: list[Game]

    def ___init__(self):
        """
        This method initializes the arcade machine.
        """
        self.material = None
        self.color = None
        self.games = []

    @abstractmethod
    def select_material(self, material: str):
        """
        This method selects the material of the arcade machine.

        Args:
            material(str): The material of the arcade machine.
        """

    @abstractmethod
    def select_color(self, color: str):
        """
        This method selects the color of the arcade machine.

        Args:
            color(str): The color of the arcade machine.
        """

    @abstractmethod
    def add_game(self, game: Game):
        """
        This method adds a game to the arcade machine.

        Args:
            game(Game): The game to be added to the arcade machine.
        """

    def show_games(self):
        """
        This method shows the games available in the arcade machine.
        """
        if self.games:
            for game in self.games:
                print(f"- {game.name} (Code: {game.code})")
        else:
            print("No games available.")


class RetroArcadeMachine(AbstractArcadeMachine):
    """
    This class represents the behavior of a retro arcade machine.
    """


    def __init__(self):
        """
        This method initializes the retro arcade machine.
        """
        super().__init__()
        self.theme = "Retro"

    def select_material(self, material: str):
        """
        This method selects the material of the retro arcade machine.

        Args: material(str): The material of the retro arcade machine.

        return: Messege with the material selected.
        """
        if material in ["wood", "metal"]:
            self.material = material
            print(f"Material selected for retro machine: {self.material}")
        else:
            print("Invalid material for retro machine.")

    def select_color(self, color: str):
        """
        This method selects the color of the retro arcade machine.

        args: color(str): The color of the retro arcade machine.

        return: Messege with the color selected.
        """
        if color in ["brown", "black"]:
            self.color = color
            print(f"Color selected for retro machine: {self.color}")
        else:
            print("Invalid color for retro machine.")

    def add_game(self, game: "Game"):
        """
        This method adds a game into the retro machine.

        This method takes the game selected from the user and adds it
        to the retro machine games list, but if the machine already has
        five games, it will not be added.

        Args: game(Game): The game to be added to the retro machine.

        return: Messege with the game added or messege with the limitation of games.
        """
        if len(self.games) < 5:  
            self.games.append(game) 
            print(f"Game {game.name} added to retro machine.")
        else:
            print("Retro machine can only hold 5 games.")

class User(ABC):
    """
    This class represents the behavior of a user.
    """
    name: str
    address: str
    
    def __init__(self, name: str, address: str):
        """
        This method initializes the user.

        Args:
            name(str): The name of the user.
            address(str): The address of the user.
        """
        self.name = name
        self.address = address




