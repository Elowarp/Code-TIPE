'''
 Name : Elowan
 Creation : 02-06-2023 11:00:02
 Last modified : 03-06-2023 18:50:24
'''

from Models import Figure, FIGURES
class Case:
    instanceCount = 0

    def __init__(self, name, figuresPossible):
        self.id = self.instanceCount
        self.name = name
        self.figuresPossible = figuresPossible
        Case.instanceCount += 1

    def __repr__(self) -> str:
        return str(self.id)
    
    def __str__(self) -> str:
        return self.__repr__()

class Field:
    def __init__(self, grille = None):
        self.grille = grille

    def createField(self):
        self.grille = [
            [CASES["empty"], CASES["hole"], CASES["wall"]],
            [CASES["wall"], CASES["empty"], CASES["empty"]],
            [CASES["hole"], CASES["wall"], CASES["hole"]],
        ]

    def getCase(self, x, y) -> Case:
        """Retourne la case en coordonée x y"""
        return self.grille[y][x]

    def __len__(self) -> int:
        return len(self.grille)

    def __repr__(self) -> str:
        # Représente le terrain comme une grille
        result = ""
        for i in range(len(self.grille)):
            result += "| "
            for case in self.grille[i]:
                result += str(case) + " | "

            # Empeche le dernier saut a la ligne
            result += "\n"

        return result
    
    def __str__(self) -> str:
        return self.__repr__()

CASES = {
    "empty": Case("empty", [                        # Sol plat vide
        FIGURES["do_nothing"], 
        FIGURES["backflip"], 
        FIGURES["frontflip"], 
        FIGURES["cork"]
    ]),           
    "wall":  Case("wall", [                         # Mur 
        FIGURES["do_nothing"], 
        FIGURES["jump"], 
        FIGURES["palm_flip"],
    ]),            
    "hole":  Case("hole", [                         # Trou
        FIGURES["do_nothing"], 
        FIGURES["jump"],
        FIGURES["frontflip"],
    ]),               
}

if __name__ == "__main__":
    # Grille 3x3
    field = Field()
    print(field)