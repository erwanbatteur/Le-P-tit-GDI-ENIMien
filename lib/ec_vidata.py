
#__________________________________________________#
__author__ = "Erwan LABADIE"
__copyright__ = "Copyright 10/2022"
__maintainer__ = "Erwan LABADIE"
#__________________________________________________#

"""
Program description :
This sub-program is used to print the result from a database to the user on the main program.
"""

# vis / dimensions / section / pas / couple serrage recommande / force serrage (same)

# Data ecrous GDI p.204
ListScrewSizeISO = ["M1.6", "M2", "M2.5", "M3", "M4", "M5", "M6", "M8", "M10", "M12", "M16", "M20", "M24", "M30", "M36"]
ScrewSized = ["1.6", "2", "2.5", "3", "4", "5", "6", "8", "10", "12", "16", "20", "24", "30", "36"]
EcrouDima = ["3.2", "4", "5", "5.5", "7", "8", "10", "13", "16", "18", "24", "30", "36", "46", "no"]
EcrouDimb1 = ["1.3", "1.6", "2", "2.4", "3.2", "4.7", "5.2", "6.8", "8.4", "10.8", "14.8", "18", "21.5", "25.6", "no"]
EcrouDimb2 = ["1", "1.2", "1.6", "1.8", "2.2", "2.7", "3.2", "4", "5", "6", "8", "10", "12", "15", "no"]
EcrouDimg = ["no", "no", "no", "no", "no", "11.8", "14.2", "17.9", "21.8", "26", "34.5", "42.8", "no", "no", "no"]
EcrouDimc = ["no", "M2", "M2.5", "M3", "M4", "M5", "M6", "M8", "M10", "M12", "M16", "M20", "M24", "M30", "no"] # = 0.8 * d
EcrouDime = ["no", "no", "no", "2.4", "3.2", "4", "5", "6.5", "8", "10", "13", "16", "19", "24", "no"]
EcrouDimf = ["no", "no", "no", "5.1", "6.7", "8", "10", "13", "16.5", "19.5", "25", "31", "37", "47", "no"]
# Data ecrous GDI p.205
EcrouCreneauDima = ["no", "no", "no", "no", "7", "8", "10", "13", "16", "18", "24", "30", "36", "46", "55"] #65, 75
EcrouCreneauDimd1 = ["no", "no", "no", "no", "M4", "M5", "M6", "M8", "M10", "M12", "M16", "M20", "M24", "M30", "M36"]
EcrouCreneauDimhmax = ["no", "no", "no", "no", "M4", "M5", "M6", "M8", "M10", "M12", "M16", "M20", "M24", "M30", "M36"]
EcrouCreneauDimg = ["no", "no", "no", "no", "M4", "M5", "M6", "M8", "M10", "M12", "M16", "M20", "M24", "M30", "M36"]
EcrouCreneauDimm = ["no", "no", "no", "no", "M4", "M5", "M6", "M8", "M10", "M12", "M16", "M20", "M24", "M30", "M36"]


def Ecrous_Callback(Screwsize):
    positiontaille = ListScrewSizeISO.index(Screwsize)
    #print(positiontaille)
    EDd = ScrewSized[positiontaille]
    EDa = EcrouDima[positiontaille]
    EDb1 = EcrouDimb1[positiontaille]
    EDb2 = EcrouDimb2[positiontaille]
    EDg = EcrouDimg[positiontaille]
    EDc = EcrouDimc[positiontaille]
    EDe = EcrouDime[positiontaille]
    EDf = EcrouDimf[positiontaille]
    ECDa = EcrouCreneauDima[positiontaille]
    ECDd1 = EcrouCreneauDimd1[positiontaille]
    ECDhmax = EcrouCreneauDimhmax[positiontaille]
    ECDg = EcrouCreneauDimg[positiontaille]
    ECDm = EcrouCreneauDimm[positiontaille]
    return EDd, EDa, EDb1, EDb2, EDg, EDc, EDe, EDf, ECDa, ECDd1, ECDhmax, ECDg, ECDm



# print(Ecrous_Callback('M5'))
