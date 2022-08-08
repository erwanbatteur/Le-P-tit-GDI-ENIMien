
#__________________________________________________#
__author__ = "Erwan LABADIE"
__copyright__ = "Copyright 04/2022"
__maintainer__ = "Erwan LABADIE"
#__________________________________________________#

"""
Program description :
This sub-program is used to print the result from a database to the user on the main program.
"""

### CLAVETTE data ###
ClavetteDiaInclu = [6, 9, 11, 13, 18, 23, 31, 39, 45, 51, 59, 66, 76, 86, 96, 110] # max 110
ClavetteValeur_a = ["2", "3", "4", "5", "6", "8", "10", "12", "14", "16", "18", "20", "22", "25", "28"]
ClavetteValeur_b = ["2", "3", "4", "5", "6", "7", "8", "8", "9", "10", "11", "12", "14", "14", "16"]
ClavetteValeur_s = ["0.16 a 0.25","0.16 a 0.25","0.16 a 0.25","0.25 a 0.40","0.25 a 0.40","0.25 a 0.40","0.40 a 0.60","0.40 a 0.60","0.40 a 0.60","0.60 a 0.80","0.60 a 0.80","0.60 a 0.80","1 a 1.2","1 a 1.2","1 a 1.2"]
ClavetteValeur_J = ["1.2", "1.8", "2.5", "3", "3.5", "4", "5", "5", "5.5", "6", "7", "7.5", "9", "9", "10"]
ClavetteValeur_K = ["1", "1.4", "1.8", "2.3", "2.8", "3.3", "3.3", "3.3", "3.8", "4.3", "4.4", "4.9", "5.4", "5.4", "6.4"]
ClavetteValeur_L = ["6 a 20","6 a 36","8 a 45","10 a 56","14 a 70","18 a 90","22 a 110","28 a 140","36 a 160","45 a 180","50 a 200","56 a 220","63 a 250","70 a 280","80 a 320"]
ClavetteValeur_vis = ["no", "no", "no", "no", "M2.5-M6", "M3-M8", "M4-M10", "M5-M10", "M6-M10", "M6-M10", "M8-M12", "M8-M12", "M10-M12", "M10-M12", "M10-M16"]
ClavetteValeur_t = ["no", "no", "no", "no", "5", "6.5", "8", "10", "12", "12", "16", "16", "20", "20", "20"]
ClavetteValeur_z = ["no", "no", "no", "no", "2.9", "3.4", "4.5", "5.5", "6.6", "6.6", "9", "9", "11", "11", "11"]
ClavetteValeur_g = ["no", "no", "no", "no", "3", "3.5", "4.5", "5.5", "6.5", "6.5", "8.5", "8.5", "10.5", "10.5", "10.5"]
ClavetteValeur_r = ["no", "no", "no", "no", "2.5", "3", "4", "5", "6", "6", "8", "8", "10", "10", "10"]

### CANNELURE data ###
CannelureDia = [11, 13, 16, 18, 21, 23, 26, 28, 32, 36, 42, 46, 52, 56, 62, 72, 82, 92, 102, 112]
CannelureValeur_D = ["14", "16", "20", "22", "25", "28", "32", "34", "38", "42", "48", "54", "60", "65", "72", "82", "92", "102", "112", "125"]
CannelureValeur_N = ["6", "6", "6", "6", "6", "6", "6", "6", "8", "8", "8", "8", "8", "8", "8", "10", "10", "10", "10", "10"]
CannelureValeur_B = ["3", "3.5", "4", "5", "5", "6", "6", "7", "6", "7", "8", "9", "10", "10", "12", "12", "12", "14", "16", "18"]

def Values_Cla_Can_Call(Curr_dia):
    print("call :", str(Curr_dia))

    ####### CLAVETTE #######
    if Curr_dia < 6 or Curr_dia > 110:
        val_a = val_b = val_s = val_J = val_K = val_L = val_vis = val_t = val_z = val_g = val_r = "no"
    else:
        i = 0
        while ClavetteDiaInclu[i+1] <= Curr_dia:
            i = i + 1
        #print(i)
        val_a = ClavetteValeur_a[i]
        val_b = ClavetteValeur_b[i]
        val_s = ClavetteValeur_s[i]
        val_J = ClavetteValeur_J[i]
        val_K = ClavetteValeur_K[i]
        val_L = ClavetteValeur_L[i]
        val_vis = ClavetteValeur_vis[i]
        val_t = ClavetteValeur_t[i]
        val_z = ClavetteValeur_z[i]
        val_g = ClavetteValeur_g[i]
        val_r = ClavetteValeur_r[i]
    
    ####### CANNELURE #######
    if Curr_dia > 112:
        val_d = "no"
        val_D = "no"
        val_N = "no"
        val_B = "no"
    else:
        j = 0
        while CannelureDia[j] < Curr_dia:
            j = j + 1
        #print(j)
        val_d = CannelureDia[j]
        val_D = CannelureValeur_D[j]
        val_N = CannelureValeur_N[j]
        val_B = CannelureDia[j]

    # return val_a, val_D # Test Function
    return val_a, val_b, val_s, val_J, val_K, val_L, val_vis, val_t, val_z, val_g, val_r, val_d, val_D, val_N, val_B # retour des 15 sorties


# Test du programme :
#print(Values_Cla_Can_Call(112.1))
