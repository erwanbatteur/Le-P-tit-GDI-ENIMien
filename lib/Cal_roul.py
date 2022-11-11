
#__________________________________________________#
__author__ = "Erwan LABADIE"
__copyright__ = "Copyright 10/2022"
#__________________________________________________#

"""
This program calculates the life of a bearing
"""

FaCoratio = [0.014, 0.028, 0.056, 0.084, 0.11, 0.17, 0.28, 0.42, 0.566]
e = [0.19, 0.22, 0.26, 0.28, 0.3, 0.34, 0.38, 0.42, 0.44]
Y = [2.3, 1.99, 1.71, 1.55, 1.45, 1.31, 1.15, 1.04, 1]


# charge axiale
# charge radiale
# Charge a vide
# charge totale ?????

def CalculVieRoulement(Fa, Fr, C0, C, n, omega):
    position = 0
    Valinf = 0
    Valsup = 0
    Valegale = 0
    ecalcul = 0
    Ycalcul = 0
    P = 0

    # Etape 1
    ratioFaC0 = Fa/C0
    for i in range (len(FaCoratio) - 1):
        if ratioFaC0 > FaCoratio[i]:
            Valinf = FaCoratio[i]
            Valsup = FaCoratio[i+1]
            position = i
        """
        if ratioFaC0 < FaCoratio[i]:
            Valsup = FaCoratio[i+1]
        """
        if ratioFaC0 == FaCoratio[i]:
            Valegale = FaCoratio[i]
    
    # Etape 2
    if Valegale != 0:
        ecalcul = e[position]
        Ycalcul = Y[position]
    else:
        RatioTemp = (ratioFaC0-Valinf)/(Valsup-Valinf)
        ecalcul = (RatioTemp * (e[position+1]-e[position])) + e[position]
        Ycalcul = (RatioTemp * (Y[position+1]-Y[position])) + Y[position]
    
    # Etape 3
    if (Fa/Fr) <= ecalcul:
        P = Fr
    else:
        #print("cette solution")
        P = (0.56*Fr)+(Ycalcul*Fa)
    
    # Etape 4
    L10 = (C/P)**n # Duree de vie en millions de tours
    L10h = L10*((10**6)/(60*omega)) # Duree de vie en heures
    
    return L10, L10h


# print(CalculVieRoulement(400, 1000, 3800, 6200, 3, 150)) # Valeurs tirees d'un exercice, reponses : L10=157.8 / L10h=17535
