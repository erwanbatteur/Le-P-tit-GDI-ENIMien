
#__________________________________________________#
__author__ = "Erwan LABADIE"
__copyright__ = "Copyright 04/2022"
__maintainer__ = "Erwan LABADIE"
#__________________________________________________#

"""
Program description :
This sub-program is used to print the result of calculation about triangle to the user on the main program.
"""

# https://www.calculat.org/fr/aire-perimetre/triangle-rectangle.html

import math

Nb_arrondi = 3

def Calcul_Tri_window(ValA, ValC, ValAlph, ValBeth):
    print("Calc Tri")

    ValA = ValA.replace(",", ".")
    ValC = ValC.replace(",", ".")
    ValAlph = ValAlph.replace(",", ".")
    ValBeth = ValBeth.replace(",", ".")

    ValA = ValA.replace(" ", "")
    ValC = ValC.replace(" ", "")
    ValAlph = ValAlph.replace(" ", "")
    ValBeth = ValBeth.replace(" ", "")

    ValA = ValA.replace("-", "")
    ValC = ValC.replace("-", "")
    ValAlph = ValAlph.replace("-", "")
    ValBeth = ValBeth.replace("-", "")

    if ValA != "" and ValAlph != "" and ValC == "" and ValBeth == "":
        print("A et alpha")
        try:
            val_A = float(ValA)
            val_Alpha = float(ValAlph)
        except ValueError:
            print("Probleme dans les parametres d'entree")
            return -1, -1, -1, -1, -1 # retourner -1 partout car erreur
            # EXIT the function
        val_C = round(val_A / math.sin(val_Alpha*(math.pi / 180)), Nb_arrondi)
        val_B = round(math.sqrt(val_C**2 - val_A**2), Nb_arrondi)
        val_Betha = 90 - val_Alpha
        return val_A, val_B, val_C, val_Alpha, val_Betha
    
    elif ValA != "" and ValBeth != "" and ValC == "" and ValAlph == "":
        print("A et betha")
        try:
            val_A = float(ValA)
            val_Betha = float(ValBeth)
        except ValueError:
            print("Probleme dans les parametres d'entree")
            return -1, -1, -1, -1, -1 # retourner -1 partout car erreur
            # EXIT the function
        val_C = round(val_A / math.cos(val_Betha*(math.pi / 180)), Nb_arrondi)
        val_B = round(math.sqrt(val_C**2 - val_A**2), Nb_arrondi)
        val_Alpha = 90 - val_Betha
        return val_A, val_B, val_C, val_Alpha, val_Betha
    
    elif ValC != "" and ValAlph != "" and ValA == "" and ValBeth == "":
        print("C et alpha")
        try:
            val_C = float(ValC)
            val_Alpha = float(ValAlph)
        except ValueError:
            print("Probleme dans les parametres d'entree")
            return -1, -1, -1, -1, -1 # retourner -1 partout car erreur
            # EXIT the function
        val_A = round(val_C * math.sin(val_Alpha*(math.pi / 180)), Nb_arrondi)
        val_B = round(val_C * math.cos(val_Alpha*(math.pi / 180)), Nb_arrondi)
        val_Betha = 90 - val_Alpha
        return val_A, val_B, val_C, val_Alpha, val_Betha
    
    elif ValC != "" and ValBeth != "" and ValA == "" and ValAlph == "":
        print("C et betha")
        try:
            val_C = float(ValC)
            val_Betha = float(ValBeth)
        except ValueError:
            print("Probleme dans les parametres d'entree")
            return -1, -1, -1, -1, -1 # retourner -1 partout car erreur
            # EXIT the function
        val_A = round(val_C * math.cos(val_Betha*(math.pi / 180)), Nb_arrondi)
        val_B = round(val_C * math.sin(val_Betha*(math.pi / 180)), Nb_arrondi)
        val_Alpha = 90 - val_Betha
        return val_A, val_B, val_C, val_Alpha, val_Betha
    
    else:
        print("donees d'entree pas coherentes (calculs triangle)")
        return -1, -1, -1, -1, -1


# print(Calcul_Tri_window("", "-11", "", "60"))
