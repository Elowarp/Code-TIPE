'''
 Name : Elowan
 Creation : 02-06-2023 11:00:02
 Last modified : 03-06-2023 18:54:32
'''
from random import randint, seed, choice
seed(22)

class Figure:
    instanceCount = 0

    def __init__(self, name, duration, complexity):
        self.id = self.instanceCount
        self.name = name
        self.duration = duration
        self.complexity = complexity
        Figure.instanceCount += 1
    
    def __repr__(self) -> str:
        return self.name
    
class Athlete: 
    instanceCount = 0

    def __init__(self, xp, figureFav):
        self.id = self.instanceCount
        self.xp = xp
        self.figureFav = figureFav
        self.score = 0
        self.combos = []
        self.position = {
            "x": 0,
            "y": 0,
        }
        self.state = {                          # Etat de l'athlete 
            "isMoving": False,
            "ticksSinceStartedMoving": 0,
            "movement": FIGURES["do_nothing"],  # Pas en mouvement 
        }
        self.field = None

        Athlete.instanceCount += 1

    def takeAction(self):
        """Fait faire une figure à l'athlete"""

        if self.state["movement"] != FIGURES["do_nothing"]:
            if self.state["ticksSinceStartedMoving"]+1 >= self.state["movement"].duration:
                self._endMovement()
            
            else:
                self.state["ticksSinceStartedMoving"] += 1

        else:
            # Choisir sur quelle case se déplacer
            self._moveAround()

            # Fait la figure
            self._startMovement()
            pass 
    
    def _moveAround(self):
        "Fait bouger l'athlete sur une case collée"
        # Note les cases adjacentes de 0 à 8 (0 = haut gauche
        # et croissant dans le sens horaire) et
        # supprime celles ou l'athlete ne peut aller
        possibleNextPosition = \
            self._removeImpossibleNextCases([x for x in range(8)])
        
        # Choisit aléatoirement parmis ces cases possibles
        nextCase = choice(possibleNextPosition)

        # Met a jour les coordonnees
        self._setNewCoords(nextCase)
        
        
    def _setNewCoords(self, nextCase):
        match nextCase:
            case 0:
                self.position = {
                    "x": self.position["x"]-1,
                    "y": self.position["y"]+1,
                }   
            case 1:
                self.position = {
                    "x": self.position["x"],
                    "y": self.position["y"]+1,
                }    
            case 2:
                self.position = {
                    "x": self.position["x"]+1,
                    "y": self.position["y"]+1,
                }   
            case 3:
                self.position = {
                    "x": self.position["x"]+1,
                    "y": self.position["y"],
                }   
            case 4:
                self.position = {
                    "x": self.position["x"]+1,
                    "y": self.position["y"]-1,
                }    
            case 5:
                self.position = {
                    "x": self.position["x"],
                    "y": self.position["y"]-1,
                }  
            case 6:
                self.position = {
                    "x": self.position["x"]-1,
                    "y": self.position["y"]-1,
                }  
            case 7:
                self.position = {
                    "x": self.position["x"]-1,
                    "y": self.position["y"],
                }   
    
    def _removeImpossibleNextCases(self, cases):
        positionToRemove = []

        # Dernier x/y qui est encore sans le terrain
        lastCoordPossible = len(self.field)-1 

        if self.position["x"] == 0:
            if 0 not in positionToRemove: positionToRemove.append(0)
            if 7 not in positionToRemove: positionToRemove.append(7)
            if 6 not in positionToRemove: positionToRemove.append(6)
            
        elif self.position["x"] == lastCoordPossible:
            if 2 not in positionToRemove: positionToRemove.append(2)
            if 3 not in positionToRemove: positionToRemove.append(3)
            if 4 not in positionToRemove: positionToRemove.append(4)

        if self.position["y"] == 0:
            if 0 not in positionToRemove: positionToRemove.append(0)
            if 1 not in positionToRemove: positionToRemove.append(1)
            if 2 not in positionToRemove: positionToRemove.append(2)

        elif self.position["y"] == lastCoordPossible:
            if 4 not in positionToRemove: positionToRemove.append(4)
            if 5 not in positionToRemove: positionToRemove.append(5)
            if 6 not in positionToRemove: positionToRemove.append(6)

        # Retire toutes les cases impossibles
        for i in range(len(cases)-1, -1, -1):
            if i in positionToRemove: 
                cases.pop(i)

        return cases


    def _startMovement(self):
        """
        Regarde sur quelle case est l'athlete et commence la figure
        associée
        """
        figures = self.field.getCase(
            self.position["x"], self.position["y"]
            ).figuresPossible
        
        # Choisit aléatoirement le mouvement à faire parmis la liste possible
        self.state["movement"] = figures[randint(0, len(figures)-1)]

        self.state["isMoving"] = True
        self.state["ticksSinceStartedMoving"] = 0


    def _endMovement(self):
        self.state["isMoving"] = False
        self.score += self._noteMovement()
        self.state["movement"] = FIGURES["do_nothing"]
        self.state["ticksSinceStartedMoving"] = 0

    def _noteMovement(self) -> int:
        """Attribut une note au mouvement"""
        return 0

    def setField(self, field):
        self.field = field

    def __repr__(self) -> str:
        return "{} : - xp : {}\n    - figure fav : {}\n".format(
            self.id, self.xp, self.figureFav.name
        )

FIGURES = {
    "do_nothing": Figure("do_nothing", 2, 0),       # Ne rien faire pendant 2s
    "walk_forward": Figure("walk_forward", 1, 0),   # Avancer pendant 1s
    "turn_right": Figure("turn_right", 1, 0),       # Tourner a droite pendant 1s
    "turn_left": Figure("turn_left", 1, 0),         # Tourner a gauche pendant 1s
    
    "jump": Figure("jump", 3, 2),                   # Jump pendant 5s
    "palm_flip": Figure("palm_flip", 5, 7),         # Palm_flip pendant 5s
    "backflip": Figure("backflip", 5, 4),           # Backflip pendant 5s
    "frontflip": Figure("frontflip", 5, 5),         # Frontflip pendant 5s
    "cork": Figure("cork", 5, 8),                   # Cork pendant 5s
}

if __name__ == "__main__":
    athlete = Athlete(5, FIGURES["frontflip"])
    print(athlete)