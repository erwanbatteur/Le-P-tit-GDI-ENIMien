
#__________________________________________________#
__author__ = "Erwan LABADIE"
__copyright__ = "Copyright 11/2022"
__maintainer__ = "Erwan LABADIE"
#__________________________________________________#

"""
Program description :
This sub-program is used to correct the entry data from the user. For instance, if the user is entering something that does not correspond to the waited data, it will
be corrected.
"""

def Correct_Entry_to_Nb(StringVal):
    # print("Correction de l'entree")
    StringVal = StringVal.replace(",", ".")
    StringVal = StringVal.replace(" ", "")
    StringVal = StringVal.replace("-", "")
    StringVal = StringVal.replace("^", "")

    if StringVal != "":
        try:
            FloatVal = float(StringVal)
        except ValueError:
            print("Probleme dans les parametres d'entree")
            return -1
    
    else:
        print("Probleme dans les parametres d'entree")
        return -1
    
    return FloatVal


#print(Correct_Entry_to_Nb("sdfghj"))
