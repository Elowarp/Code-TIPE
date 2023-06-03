'''
 Name : Elowan
 Creation : 02-06-2023 11:00:02
 Last modified : 03-06-2023 18:52:24
'''

from Terrain import Field
from Models import Athlete, FIGURES

MAX_TICK_COUNT = 70 # Maximum de 70s d'après les règles

class Game:
    def __init__(self, athlete):
        self.field = Field()
        self.field.createField()
        self.athlete = athlete
        self.state = 0          # Etat de la partie
        self.tickCount = 0      # 1 tick = 1 seconde 

        self.athlete.setField(self.field)

    def start(self):
        """Initialisation des valeurs de depart de la competition"""
        self.tickCount = 0
        self.state = 1
        self.athlete.position = {
            "x": 0,
            "y": 0,
        }

    def update(self):
        """Met à jour l'état de l'athlète et retourne l'état de la compétition"""
        if self.tickCount >= MAX_TICK_COUNT:
            self.end()
            return self.state
        
        self.athlete.takeAction()

        self.tickCount += 1
        return self.state

    def end(self):
        """Fonction appelée lorque la competition termine"""
        self.state = 2

if __name__ == "__main__":
    athlete = Athlete(5, FIGURES["backflip"])
    game = Game(athlete)
    game.start()
    print("Game started !")

    while game.update() == 1:
        print("Athlete state (in the second {}) : ".format(game.tickCount))
        print("  - Position ({},{})".format(
                athlete.position["x"], athlete.position["y"]
        ))
        print("  - Case : {}".format(
            game.field.getCase(
                athlete.position["x"], athlete.position["y"]
            ).name
        ))
        print("  - Current movement : {} since {} seconds".format(
            athlete.state["movement"], athlete.state["ticksSinceStartedMoving"]
        ))
        print()

    print("Game state : {}\nIn {} ticks".format(game.state, game.tickCount))