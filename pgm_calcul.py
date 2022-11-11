
#__________________________________________________#
__author__ = "Erwan LABADIE"
__copyright__ = "Copyright 11/2022"
__credits__ = [""]
__version__ = "0.1.9"
__maintainer__ = "Erwan LABADIE"
__email__ = ""
__status__ = "Prototype"
#__________________________________________________#


#_______________# PROGRAM DESCRIPTION #_______________#

"""
For more information about the sources that helped developping this software, please refer to "data\docs\ExtRessources" file.

Erreur 20 : PB chargement images
"""

#_______________# IMPORT #_______________#

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
import tkinter.font as font

from lib import clacanval
from lib import angcal
from lib import circldta
from lib import EntrCorr
from lib import ec_vidata
from lib import Cal_roul


############################################################
#                                                          #
#                           SETUP                          #
#                                                          #
############################################################

WindowHeightSize = 670
WindowWidthSize = 880
ToolbarHeight = 50
WindowSize = str(WindowWidthSize) + "x" + str(WindowHeightSize)

PrintClickPosition = False

Pi_val = 3.14159265359

### ACTIVE WINDOW ###
MenuActif = True
VisWindowActif = False
EcrouWindowActif = False
EcroupageSetup = False # Was this page setted up ?
SerrageVisActif = False
ClavetteWindowActif = False
TriangleWindowActif = False
CirclipsWindowActive = False
CalculVieRoulementActive = False
CalculsGeomWindowActive = False

### MENU image coordinates ###
MarginSize = 15
XmenuImgSize, YmenuImgSize = 273, 186
XVisMenu, YVisMenu = MarginSize, MarginSize
XClavettesMenu, YClavettesMenu = (XmenuImgSize+(2*MarginSize)), MarginSize
XCirclipsMenu, YCirclipsMenu = ((2*XmenuImgSize)+(3*MarginSize)), MarginSize
XAjustementsMenu, YAjustementsMenu = MarginSize, (YmenuImgSize+(2*MarginSize))
XCisaillementMenu, YCisaillementMenu = (XmenuImgSize+(2*MarginSize)), (YmenuImgSize+(2*MarginSize))
XJointsMenu, YJointsMenu = ((2*XmenuImgSize)+(3*MarginSize)), (YmenuImgSize+(2*MarginSize))
XCalculsMenu, YCalculsMenu = MarginSize, ((2*YmenuImgSize)+(3*MarginSize))
XConversionMenu, YConversionMenu = (XmenuImgSize+(2*MarginSize)), ((2*YmenuImgSize)+(3*MarginSize))
XAnglesMenu, YAnglesMenu = ((2*XmenuImgSize)+(3*MarginSize)), ((2*YmenuImgSize)+(3*MarginSize))


### VIS data ###
ListScrewSizeISO = ["M1.6", "M2", "M2.5", "M3", "M4", "M5", "M6", "M8", "M10", "M12", "M16", "M20", "M24", "M30", "M36"]

DiametreVis = ["1.6", "2", "2.5", "3", "4", "5", "6", "8", "10", "12", "16", "20", "24", "30", "36"]
PasVis = ["0.35", "0.4", "0.45", "0.5", "0.7", "0.8", "1", "1.25", "1.5", "1.75", "2", "2.5", "3", "3.5", "4"]#
PasVisFin = ["0.2", "0.25", "0.35", "0.35", "0.5", "0.5", "0.75", "1", "1.25", "1.5", "1.5", "2", "2", "2", "3"]
PassageVisFin = ["1.8", "2.2", "2.7", "3.2", "4.3", "5.3", "6.4", "8.4", "10.5", "13", "17", "21", "25", "31", "37"]
PassageVisMoyen = ["2", "2.4", "2.9", "3.4", "4.5", "5.5", "6.6", "9", "11", "13.5", "17.5", "22", "26", "33", "39"]
PassageVisLarge = ["2.1", "2.5", "3.1", "3.6", "4.8", "5.8", "7", "10", "12", "14.5", "18.5", "24", "28", "35", "42"]
DiaChambrageMin = ["8.5", "6", "11", "8", "10", "11", "13", "18", "20", "22", "30", "36", "42", "53", "63"]
TailleEmpreinteCHC = ["1.5", "1.5", "2", "2.5", "3", "4", "5", "6", "8", "10", "14", "17", "19", "22", "27", "32", "36"]
TailleEmpreinteFHC = ["0.9", "1.3", "1.5", "2", "2.5", "3", "4", "5", "6", "8", "10", "12", "no", "no", "no", "no", "no"]
DiaMaxFHC = ["3.52", "4.4", "5.5", "5.5", "8.4", "9.3", "11.3", "15.8", "18.3", "22.5", "30", "38", "no", "no", "no", "no", "no"]
DiaTeteCHC = ["3", "3.8", "4.5", "5.5", "7", "8.5", "10", "13", "16", "18", "24", "30", "36", "45", "54", "63", "72"]
DimTeteH = ["no", "no", "no", "5.5", "7", "8", "10", "13", "16", "18", "24", "30", "no", "no", "no", "no", "no"]
HauteurTeteH = ["no", "no", "no", "2", "2.8", "3.5", "4", "5.3", "6.4", "7.5", "10", "12.5", "no", "no", "no", "no", "no"]


############################################################
#                                                          #
#                         FUNCTIONS                        #
#                                                          #
############################################################

def InfoBtn():
    showinfo('Info', "Coded by E.LABADIE \nENIMien Promo 2022 (option CMAO) \nVersion logiciel : " + __version__)

def ToolBarSetup():
    BoutonFermer = Button(ToolbarCanvas, width = 15, text = "Fermer", command = fenetre.quit)
    BoutonFermer['font'] = ToolBarTextFont
    BoutonFermer.place(x = 10, y = 6)

    BoutonMenu = Button(ToolbarCanvas, width = 15, text = "Menu", command = MENU_Setup)
    BoutonMenu['font'] = ToolBarTextFont
    BoutonMenu.place(x = 370, y = 6)

    BoutonInfo = Button(ToolbarCanvas, width = 10, text = "Info", command = InfoBtn)
    BoutonInfo['font'] = ToolBarTextFont
    BoutonInfo.place(x = 770, y = 6)


def MENU_Setup():
    # Menu images size : 273x186 (Width x Height)
    # 21051999 : geometry a changer ?? redimensionner images
    ClearAllWindowContent()
    global MenuActif
    MenuActif = True
    ColorRectangle = 'gray50'
    MainCanvas.create_rectangle(XVisMenu - 1, YVisMenu - 1, (XVisMenu+XmenuImgSize), (YVisMenu+YmenuImgSize), outline=ColorRectangle)
    MainCanvas.create_image(XVisMenu, YVisMenu, anchor=NW, image = ImgVis)
    MainCanvas.create_rectangle(XClavettesMenu - 1, YClavettesMenu - 1, (XClavettesMenu+XmenuImgSize), (YClavettesMenu+YmenuImgSize), outline=ColorRectangle)
    MainCanvas.create_image(XClavettesMenu, YClavettesMenu, anchor=NW, image = ImgClavette)
    MainCanvas.create_rectangle(XCirclipsMenu - 1, YCirclipsMenu - 1, (XCirclipsMenu+XmenuImgSize), (YCirclipsMenu+YmenuImgSize), outline=ColorRectangle)
    MainCanvas.create_image(XCirclipsMenu, YCirclipsMenu, anchor=NW, image = ImgCirclips)
    MainCanvas.create_rectangle(XAjustementsMenu - 1, YAjustementsMenu - 1, (XAjustementsMenu+XmenuImgSize), (YAjustementsMenu+YmenuImgSize), outline=ColorRectangle)
    MainCanvas.create_image(XAjustementsMenu, YAjustementsMenu, anchor=NW, image = ImgCroRou)#ImgAjustements)
    MainCanvas.create_rectangle(XCisaillementMenu - 1, YCisaillementMenu - 1, (XCisaillementMenu+XmenuImgSize), (YCisaillementMenu+YmenuImgSize), outline=ColorRectangle)
    MainCanvas.create_image(XCisaillementMenu, YCisaillementMenu, anchor=NW, image = ImgCroRou)#ImgCisaillement)
    MainCanvas.create_rectangle(XJointsMenu - 1, YJointsMenu - 1, (XJointsMenu+XmenuImgSize), (YJointsMenu+YmenuImgSize), outline=ColorRectangle)
    MainCanvas.create_image(XJointsMenu, YJointsMenu, anchor=NW, image = ImgCroRou)#ImgJoints)
    MainCanvas.create_rectangle(XCalculsMenu - 1, YCalculsMenu - 1, (XCalculsMenu+XmenuImgSize), (YCalculsMenu+YmenuImgSize), outline=ColorRectangle)
    MainCanvas.create_image(XCalculsMenu, YCalculsMenu, anchor=NW, image = ImgCalculs)
    MainCanvas.create_rectangle(XConversionMenu - 1, YConversionMenu - 1, (XConversionMenu+XmenuImgSize), (YConversionMenu+YmenuImgSize), outline=ColorRectangle)
    MainCanvas.create_image(XConversionMenu, YConversionMenu, anchor=NW, image = ImgCalculRoulement)
    MainCanvas.create_rectangle(XAnglesMenu - 1, YAnglesMenu - 1, (XAnglesMenu+XmenuImgSize), (YAnglesMenu+YmenuImgSize), outline=ColorRectangle)
    MainCanvas.create_image(XAnglesMenu, YAnglesMenu, anchor=NW, image = ImgAngles)
    MainCanvas.pack()



def Vis_Page_Setup():
    ClearAllWindowContent()
    global Menu_deroulant_taille_vis, VisWindowActif, BoutonEcrouPage, BoutonVisPage#, BoutonSerragePage
    global labelPassageVisMoyen, labelPassageVisFin, labelPassageVisLarge, labelPassageFin, labelPassageMoyen, labelPassageLarge
    global labelChambrageMin, labelEmpreinteCHC, labelEmpreinteFHC, labelDiaVis1, labelDiaVis2, labelDiaVis3, labelDiaVis4, labelDiaMaxFHC
    global labelDiaTeteCHC, labelDimTeteH, labelHauteurTeteH, labelPasVis, labelPasDV, labelPasFinDV, labelPasFinVis
    VisWindowActif = True

    BoutonVisPage = Button(MainCanvas, text="Vis", command=Vis_Page_Setup)
    # BoutonVisPage['font'] = CalGeomTextFont
    BoutonVisPage.place(x = 250, y = 15)

    BoutonEcrouPage = Button(MainCanvas, text="Ecrou", command=Ecrou_Page_Setup)
    # BoutonEcrouPage['font'] = CalGeomTextFont
    BoutonEcrouPage.place(x = 350, y = 15)

    #BoutonSerragePage = Button(MainCanvas, text="Serrage vis", command=SerrageVis_Page_Setup)
    # BoutonEcrouPage['font'] = CalGeomTextFont
    #BoutonSerragePage.place(x = 650, y = 15)

    Menu_deroulant_taille_vis = ttk.Combobox(MainCanvas, values = ListScrewSizeISO) # Menu déroulant des tailles de vis
    Menu_deroulant_taille_vis['font'] = VisTextFont
    Menu_deroulant_taille_vis.place(x = 15, y = 15)
    Menu_deroulant_taille_vis.current(0) # par défaut, l'affichage sera le premier element de la liste
    Menu_deroulant_taille_vis.bind("<<ComboboxSelected>>", Vis_Page_Callback)
    MainCanvas.create_image(15, 52, anchor=NW, image = ImgVisSetup)
    # Labels with sizes and informations about the Screw Size
    labelPassageVisFin = tk.Label(MainCanvas, text = PassageVisFin[0], bg="white")
    labelPassageVisFin['font'] = VisTextFont
    labelPassageVisFin.place(x = 347, y = 150)
    labelPassageFin = tk.Label(MainCanvas, text = "fin", bg="white")
    labelPassageFin['font'] = VisTextFont
    labelPassageFin.place(x = 372, y = 150)
    labelPassageVisMoyen = tk.Label(MainCanvas, text = PassageVisMoyen[0], bg="white")
    labelPassageVisMoyen['font'] = VisTextFont
    labelPassageVisMoyen.place(x = 347, y = 175)
    labelPassageMoyen = tk.Label(MainCanvas, text = "moyen", bg="white")
    labelPassageMoyen['font'] = VisTextFont
    labelPassageMoyen.place(x = 372, y = 175)
    labelPassageVisLarge = tk.Label(MainCanvas, text = PassageVisLarge[0], bg="white")
    labelPassageVisLarge['font'] = VisTextFont
    labelPassageVisLarge.place(x = 347, y = 200)
    labelPassageLarge = tk.Label(MainCanvas, text = "large", bg="white")
    labelPassageLarge['font'] = VisTextFont
    labelPassageLarge.place(x = 372, y = 200)
    labelChambrageMin = tk.Label(MainCanvas, text = DiaChambrageMin[0], bg="white")
    labelChambrageMin['font'] = VisTextFont
    labelChambrageMin.place(x = 60, y = 175)
    labelEmpreinteCHC = tk.Label(MainCanvas, text = TailleEmpreinteCHC[0], bg="white")
    labelEmpreinteCHC['font'] = VisTextFont
    labelEmpreinteCHC.place(x = 430, y = 230)
    labelEmpreinteFHC = tk.Label(MainCanvas, text = TailleEmpreinteFHC[0], bg="white")
    labelEmpreinteFHC['font'] = VisTextFont
    labelEmpreinteFHC.place(x = 430, y = 535)
    labelDiaVis1 = tk.Label(MainCanvas, text = DiametreVis[0], bg="white")
    labelDiaVis1['font'] = VisTextFont
    labelDiaVis1.place(x = 570, y = 168)
    labelDiaVis2 = tk.Label(MainCanvas, text = DiametreVis[0], bg="white")
    labelDiaVis2['font'] = VisTextFont
    labelDiaVis2.place(x = 565, y = 450)
    labelDiaVis3 = tk.Label(MainCanvas, text = DiametreVis[0], bg="white")
    labelDiaVis3['font'] = VisTextFont
    labelDiaVis3.place(x = 810, y = 255)
    labelDiaVis4 = tk.Label(MainCanvas, text = DiametreVis[0], bg="white")
    labelDiaVis4['font'] = VisTextFont
    labelDiaVis4.place(x = 200, y = 475)
    labelDiaMaxFHC = tk.Label(MainCanvas, text = DiaMaxFHC[0], bg="white")
    labelDiaMaxFHC['font'] = VisTextFont
    labelDiaMaxFHC.place(x = 763, y = 450)
    labelDiaTeteCHC = tk.Label(MainCanvas, text = DiaTeteCHC[0], bg="white")
    labelDiaTeteCHC['font'] = VisTextFont
    labelDiaTeteCHC.place(x = 822, y = 167)
    labelDimTeteH = tk.Label(MainCanvas, text = DimTeteH[0], bg="white")
    labelDimTeteH['font'] = VisTextFont
    labelDimTeteH.place(x = 115, y = 585)
    labelHauteurTeteH = tk.Label(MainCanvas, text = HauteurTeteH[0], bg="white")
    labelHauteurTeteH['font'] = VisTextFont
    labelHauteurTeteH.place(x = 320, y = 568)
    labelPasDV = tk.Label(MainCanvas, text = "Pas (gros) :", bg="white")
    labelPasDV['font'] = VisTextFont
    labelPasDV.place(x = 10, y = 50)
    labelPasVis = tk.Label(MainCanvas, text = PasVis[0], bg="white")
    labelPasVis['font'] = VisTextFont
    labelPasVis.place(x = 83, y = 50)
    labelPasFinDV = tk.Label(MainCanvas, text = "Pas fin :", bg="white")
    labelPasFinDV['font'] = VisTextFont
    labelPasFinDV.place(x = 10, y = 75)
    labelPasFinVis = tk.Label(MainCanvas, text = PasVisFin[0], bg="white")
    labelPasFinVis['font'] = VisTextFont
    labelPasFinVis.place(x = 64, y = 75)

def Vis_Page_Callback(event):
    # Lors de l'appel de cette fonction, les valeurs de dimensions sont mises à jours
    #print("New Element Selected :", Menu_deroulant_taille_vis.get())
    positiontaille = ListScrewSizeISO.index(Menu_deroulant_taille_vis.get())
    labelPassageVisMoyen.config(text = PassageVisMoyen[positiontaille])
    labelPassageVisFin.config(text = PassageVisFin[positiontaille])
    labelPassageVisLarge.config(text = PassageVisLarge[positiontaille])
    labelChambrageMin.config(text = DiaChambrageMin[positiontaille])
    labelEmpreinteCHC.config(text = TailleEmpreinteCHC[positiontaille])
    labelEmpreinteFHC.config(text = TailleEmpreinteFHC[positiontaille])
    labelDiaVis1.config(text = DiametreVis[positiontaille])
    labelDiaVis2.config(text = DiametreVis[positiontaille])
    labelDiaVis3.config(text = DiametreVis[positiontaille])
    labelDiaVis4.config(text = DiametreVis[positiontaille])
    labelDiaMaxFHC.config(text = DiaMaxFHC[positiontaille])
    labelDiaTeteCHC.config(text = DiaTeteCHC[positiontaille])
    labelDimTeteH.config(text = DimTeteH[positiontaille])
    labelHauteurTeteH.config(text = HauteurTeteH[positiontaille])
    labelPasVis.config(text = PasVis[positiontaille])
    labelPasFinVis.config(text = PasVisFin[positiontaille])


def Ecrou_Page_Setup():
    ClearAllWindowContent()
    global Menu_deroulant_taille_ecrou, EcrouWindowActif, EcroupageSetup
    global BoutonVisPage, BoutonEcrouPage#, BoutonSerragePage
    global labelEcroud, labelEcroua, labelEcroub1, labelEcroub2, labelEcroug, labelEcrouc, labelEcroue, labelEcrouf
    global labelEcrouCreneaud, labelEcrouCreneaua, labelEcrouCreneaud1, labelEcrouCreneauhmax, labelEcrouCreneaug, labelEcrouCreneaum
    EcrouWindowActif = True
    
    BoutonVisPage = Button(MainCanvas, text="Vis", command=Vis_Page_Setup)
    # BoutonVisPage['font'] = CalGeomTextFont
    BoutonVisPage.place(x = 250, y = 15)

    BoutonEcrouPage = Button(MainCanvas, text="Ecrou", command=Ecrou_Page_Setup)
    # BoutonEcrouPage['font'] = CalGeomTextFont
    BoutonEcrouPage.place(x = 350, y = 15)

    #BoutonSerragePage = Button(MainCanvas, text="Serrage vis", command=SerrageVis_Page_Setup)
    # BoutonEcrouPage['font'] = CalGeomTextFont
    #BoutonSerragePage.place(x = 650, y = 15)

    Menu_deroulant_taille_ecrou = ttk.Combobox(MainCanvas, values = ListScrewSizeISO) # Menu déroulant des tailles de vis
    Menu_deroulant_taille_ecrou['font'] = VisTextFont
    Menu_deroulant_taille_ecrou.place(x = 15, y = 15)
    Menu_deroulant_taille_ecrou.current(0) # par défaut, l'affichage sera le premier element de la liste
    Menu_deroulant_taille_ecrou.bind("<<ComboboxSelected>>", Ecrou_Page_Callback)
    MainCanvas.create_image(10, 55, anchor=NW, image = ImgEcrouSetup)

    # Labels pour ecrous 'normaux'
    labelEcroud = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcroud.place(x = 82, y = 91)
    labelEcroua = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcroua.place(x = 82, y = 116)
    labelEcroub1 = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcroub1.place(x = 82, y = 141)
    labelEcroub2 = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcroub2.place(x = 82, y = 173)
    labelEcroug = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcroug.place(x = 82, y = 199)
    labelEcrouc = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcrouc.place(x = 82, y = 228)
    labelEcroue = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcroue.place(x = 82, y = 252)
    labelEcrouf = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcrouf.place(x = 82, y = 281)
    # Labels pour ecrous a creneau
    labelEcrouCreneaud = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcrouCreneaud.place(x = 82, y = 382)
    labelEcrouCreneaua = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcrouCreneaua.place(x = 82, y = 406)
    labelEcrouCreneaud1 = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcrouCreneaud1.place(x = 82, y = 436)
    labelEcrouCreneauhmax = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcrouCreneauhmax.place(x = 82, y = 461)
    labelEcrouCreneaug = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcrouCreneaug.place(x = 82, y = 486)
    labelEcrouCreneaum = tk.Label(MainCanvas, text = "no", bg="white")
    labelEcrouCreneaum.place(x = 82, y = 515)

    if EcroupageSetup == False:
        #print("Ecrou setted up !")
        UpdateEcrouPageLabels("M1.6")
        EcroupageSetup = True

def Ecrou_Page_Callback(event):
    Screwsize = Menu_deroulant_taille_ecrou.get()
    #print("New Element Selected :", Screwsize)
    UpdateEcrouPageLabels(Screwsize)
def UpdateEcrouPageLabels(Screwsize):
    EDd, EDa, EDb1, EDb2, EDg, EDc, EDe, EDf, ECDa, ECDd1, ECDhmax, ECDg, ECDm = ec_vidata.Ecrous_Callback(Screwsize)
    labelEcroud.config(text = EDd)
    labelEcroua.config(text = EDa)
    labelEcroub1.config(text = EDb1)
    labelEcroub2.config(text = EDb2)
    labelEcroug.config(text = EDg)
    labelEcrouc.config(text = EDc)
    labelEcroue.config(text = EDe)
    labelEcrouf.config(text = EDf)
    labelEcrouCreneaud.config(text = EDd)
    labelEcrouCreneaua.config(text = ECDa)
    labelEcrouCreneaud1.config(text = ECDd1)
    labelEcrouCreneauhmax.config(text = ECDhmax)
    labelEcrouCreneaug.config(text = ECDg)
    labelEcrouCreneaum.config(text = ECDm)


def SerrageVis_Page_Setup():
    ClearAllWindowContent()
    global SerrageVisActif
    global BoutonVisPage, BoutonEcrouPage, BoutonSerragePage
    SerrageVisActif = True

    print("serrage vis")
    
    BoutonVisPage = Button(MainCanvas, text="Vis", command=Vis_Page_Setup)
    # BoutonVisPage['font'] = CalGeomTextFont
    BoutonVisPage.place(x = 250, y = 15)

    BoutonEcrouPage = Button(MainCanvas, text="Ecrou", command=Ecrou_Page_Setup)
    # BoutonEcrouPage['font'] = CalGeomTextFont
    BoutonEcrouPage.place(x = 350, y = 15)

    BoutonSerragePage = Button(MainCanvas, text="Serrage vis", command=SerrageVis_Page_Setup)
    # BoutonEcrouPage['font'] = CalGeomTextFont
    BoutonSerragePage.place(x = 650, y = 15)

    # Preparer choix de classe ?? => Choisir la classe mediane !!
    # Section utilisable
    # Cisaillement
    # Couple serrage vis => differentes classes de vis
    # Force serrage vis => differentes classes de vis



def Cannelures_Clavettes_Page_Setup():
    global ClavetteWindowActif, DiaClaCannEntry, label_cla_a_value, label_cla_a, label_cla_diam, label_cla_b, label_cla_b_value, label_cla_J, label_cla_J_value
    global label_Clavette_Label, label_cla_s, label_cla_s_value, label_cla_K, label_cla_K_value, label_cla_L, label_cla_L_value, label_cla_vis, label_cla_vis_value
    global label_cla_t, label_cla_t_value, label_cla_z, label_cla_z_value, label_cla_g, label_cla_g_value, label_cla_r, label_cla_r_value, label_Cannelure_Label
    global label_can_D, label_cla_D_value, label_can_N, label_can_N_value, label_can_B, label_can_B_value, label_Cannelure2_Label, label_can_d, label_cla_d_value
    ClavetteWindowActif = True
    MainCanvas.create_image(10, 50, anchor=NW, image = ImgClaCannSetup)
    label_cla_diam = tk.Label(MainCanvas, text = "d =", bg="white")
    label_cla_diam['font'] = ClaCanTextFont
    label_cla_diam.place(x = 15, y = 15)

    var = StringVar()
    var.trace("w", lambda name, index,mode, var=var: Cannelures_Clavettes_Page_Callback(var))
    #var.set("0") # Create problems !!
    DiaClaCannEntry = Entry(MainCanvas, textvariable=var)
    DiaClaCannEntry.place(x = 40, y = 15)

    XOrigin, XOrigin2 = 20, 130
    XSpace = 26
    YOrigin, YOrigin2 = 65, 200
    InterspaceLines = 21
    # Data for Clavette
    label_Clavette_Label = tk.Label(MainCanvas, text = "Clavette", bg="white")
    label_Clavette_Label['font'] = ClaCanTextFont
    label_Clavette_Label.place(x = 20, y = 42)

    label_cla_a = tk.Label(MainCanvas, text = "a =", bg="white")
    label_cla_a['font'] = ClaCanTextFont
    label_cla_a.place(x = XOrigin, y = YOrigin)
    label_cla_a_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_cla_a_value['font'] = ClaCanTextFont
    label_cla_a_value.place(x = (XOrigin + XSpace), y = YOrigin)
    label_cla_b = tk.Label(MainCanvas, text = "b =", bg="white")
    label_cla_b['font'] = ClaCanTextFont
    label_cla_b.place(x = XOrigin, y = (YOrigin + 1*InterspaceLines))
    label_cla_b_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_cla_b_value['font'] = ClaCanTextFont
    label_cla_b_value.place(x = (XOrigin + XSpace), y = (YOrigin + 1*InterspaceLines))
    label_cla_s = tk.Label(MainCanvas, text = "s =", bg="white")
    label_cla_s['font'] = ClaCanTextFont
    label_cla_s.place(x = XOrigin, y = (YOrigin + 2*InterspaceLines))
    label_cla_s_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_cla_s_value['font'] = ClaCanTextFont
    label_cla_s_value.place(x = (XOrigin + XSpace), y = (YOrigin + 2*InterspaceLines))
    label_cla_J = tk.Label(MainCanvas, text = "J =", bg="white")
    label_cla_J['font'] = ClaCanTextFont
    label_cla_J.place(x = XOrigin, y = (YOrigin + 3*InterspaceLines))
    label_cla_J_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_cla_J_value['font'] = ClaCanTextFont
    label_cla_J_value.place(x = (XOrigin + XSpace), y = (YOrigin + 3*InterspaceLines))
    label_cla_K = tk.Label(MainCanvas, text = "K =", bg="white")
    label_cla_K['font'] = ClaCanTextFont
    label_cla_K.place(x = XOrigin, y = (YOrigin + 4*InterspaceLines))
    label_cla_K_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_cla_K_value['font'] = ClaCanTextFont
    label_cla_K_value.place(x = (XOrigin + XSpace), y = (YOrigin + 4*InterspaceLines))
    label_cla_L = tk.Label(MainCanvas, text = "L =", bg="white")
    label_cla_L['font'] = ClaCanTextFont
    label_cla_L.place(x = XOrigin, y = (YOrigin + 5*InterspaceLines))
    label_cla_L_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_cla_L_value['font'] = ClaCanTextFont
    label_cla_L_value.place(x = (XOrigin + XSpace), y = (YOrigin + 5*InterspaceLines))
    label_cla_vis = tk.Label(MainCanvas, text = "vis =", bg="white")
    label_cla_vis['font'] = ClaCanTextFont
    label_cla_vis.place(x = XOrigin, y = (YOrigin + 6*InterspaceLines))
    label_cla_vis_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_cla_vis_value['font'] = ClaCanTextFont
    label_cla_vis_value.place(x = (XOrigin + XSpace + 7), y = (YOrigin + 6*InterspaceLines))
    label_cla_t = tk.Label(MainCanvas, text = "t =", bg="white")
    label_cla_t['font'] = ClaCanTextFont
    label_cla_t.place(x = XOrigin, y = (YOrigin + 7*InterspaceLines))
    label_cla_t_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_cla_t_value['font'] = ClaCanTextFont
    label_cla_t_value.place(x = (XOrigin + XSpace), y = (YOrigin + 7*InterspaceLines))
    label_cla_z = tk.Label(MainCanvas, text = "z =", bg="white")
    label_cla_z['font'] = ClaCanTextFont
    label_cla_z.place(x = XOrigin, y = (YOrigin + 8*InterspaceLines))
    label_cla_z_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_cla_z_value['font'] = ClaCanTextFont
    label_cla_z_value.place(x = (XOrigin + XSpace), y = (YOrigin + 8*InterspaceLines))
    label_cla_g = tk.Label(MainCanvas, text = "g =", bg="white")
    label_cla_g['font'] = ClaCanTextFont
    label_cla_g.place(x = XOrigin, y = (YOrigin + 9*InterspaceLines))
    label_cla_g_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_cla_g_value['font'] = ClaCanTextFont
    label_cla_g_value.place(x = (XOrigin + XSpace), y = (YOrigin + 9*InterspaceLines))
    label_cla_r = tk.Label(MainCanvas, text = "r =", bg="white")
    label_cla_r['font'] = ClaCanTextFont
    label_cla_r.place(x = XOrigin, y = (YOrigin + 10*InterspaceLines))
    label_cla_r_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_cla_r_value['font'] = ClaCanTextFont
    label_cla_r_value.place(x = (XOrigin + XSpace), y = (YOrigin + 10*InterspaceLines))

    # Data for Cannelures
    label_Cannelure_Label = tk.Label(MainCanvas, text = "Cannelure", bg="white")
    label_Cannelure_Label['font'] = ClaCanTextFont
    label_Cannelure_Label.place(x = 131, y = 45)

    label_Cannelure2_Label = tk.Label(MainCanvas, text = "au plus proche :", bg="white")
    label_Cannelure2_Label['font'] = ClaCanTextFont
    label_Cannelure2_Label.place(x = XOrigin2, y = YOrigin)

    label_can_d = tk.Label(MainCanvas, text = "d =", bg="white")
    label_can_d['font'] = ClaCanTextFont
    label_can_d.place(x = XOrigin2, y = (YOrigin + 1*InterspaceLines))
    label_cla_d_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_cla_d_value['font'] = ClaCanTextFont
    label_cla_d_value.place(x = (XOrigin2 + XSpace), y = (YOrigin + 1*InterspaceLines))
    label_can_D = tk.Label(MainCanvas, text = "D =", bg="white")
    label_can_D['font'] = ClaCanTextFont
    label_can_D.place(x = XOrigin2, y = (YOrigin + 2*InterspaceLines))
    label_cla_D_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_cla_D_value['font'] = ClaCanTextFont
    label_cla_D_value.place(x = (XOrigin2 + XSpace), y = (YOrigin + 2*InterspaceLines))
    label_can_N = tk.Label(MainCanvas, text = "N =", bg="white")
    label_can_N['font'] = ClaCanTextFont
    label_can_N.place(x = XOrigin2, y = (YOrigin + 3*InterspaceLines))
    label_can_N_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_can_N_value['font'] = ClaCanTextFont
    label_can_N_value.place(x = (XOrigin2 + XSpace), y = (YOrigin + 3*InterspaceLines))
    label_can_B = tk.Label(MainCanvas, text = "B =", bg="white")
    label_can_B['font'] = ClaCanTextFont
    label_can_B.place(x = XOrigin2, y = (YOrigin + 4*InterspaceLines))
    label_can_B_value = tk.Label(MainCanvas, text = "0", bg="white")
    label_can_B_value['font'] = ClaCanTextFont
    label_can_B_value.place(x = (XOrigin2 + XSpace), y = (YOrigin + 4*InterspaceLines))
    # RAJOUTER Couple maximum (Cisaillement clavette)

def Cannelures_Clavettes_Page_Callback(Var_dia):
    content = EntrCorr.Correct_Entry_to_Nb(Var_dia.get()) # Corrige si l'entree est incorrecte

    try:
       ValeurEntree = float(content)
    except ValueError:
        print("Probleme dans les parametres d'entree")
        # EXIT the function
    #label_cla_a_value.config(text = str(round(ValeurEntree*2, 3))) # Debug output test
    val_a, val_b, val_s, val_J, val_K, val_L, val_vis, val_t, val_z, val_g, val_r, val_d, val_D, val_N, val_B = clacanval.Values_Cla_Can_Call(ValeurEntree)
    # Mise A Jour des valeurs des Labels
    label_cla_a_value.config(text = val_a)
    label_cla_b_value.config(text = val_b)
    label_cla_s_value.config(text = val_s)
    label_cla_J_value.config(text = val_J)
    label_cla_K_value.config(text = val_K)
    label_cla_L_value.config(text = val_L)
    label_cla_vis_value.config(text = val_vis)
    label_cla_t_value.config(text = val_t)
    label_cla_z_value.config(text = val_z)
    label_cla_g_value.config(text = val_g)
    label_cla_r_value.config(text = val_r)
    label_cla_d_value.config(text = val_d)
    label_cla_D_value.config(text = val_D)
    label_can_N_value.config(text = val_N)
    label_can_B_value.config(text = val_B)


def Triangle_angle_Page_Setup():
    global TriangleWindowActif, ValAEntry, ValB, ValCEntry, ValAlphaEntry, ValBethaEntry
    global label_A, label_B, label_C, label_Alpha, label_Betha, BoutonTri, BoutonTriRaz, label_Deg1, label_Deg2
    TriangleWindowActif = True
    MainCanvas.create_image(275, 100, anchor=NW, image = ImgTriSetup)

    Xpos = 50
    label_A = tk.Label(MainCanvas, text = "a =", bg="white")
    label_A['font'] = TriTextFont
    label_A.place(x = 20, y = 40)
    ValAEntry = Entry(MainCanvas)
    ValAEntry.place(x = Xpos, y = 40)
    label_B = tk.Label(MainCanvas, text = "b =", bg="white")
    label_B['font'] = TriTextFont
    label_B.place(x = 20, y = 70)
    ValB = tk.Label(MainCanvas, text = "no", bg="white")
    ValB['font'] = TriTextFont # TODO : MAJ la valeur de B
    ValB.place(x = Xpos, y = 70)
    label_C = tk.Label(MainCanvas, text = "c =", bg="white")
    label_C['font'] = TriTextFont
    label_C.place(x = 20, y = 100)
    ValCEntry = Entry(MainCanvas)
    ValCEntry.place(x = Xpos, y = 100)
    label_Alpha = tk.Label(MainCanvas, text = "\u03B1 =", bg="white")
    label_Alpha['font'] = TriTextFont
    label_Alpha.place(x = 20, y = 130)
    ValAlphaEntry = Entry(MainCanvas)
    ValAlphaEntry.place(x = Xpos, y = 130)
    label_Betha = tk.Label(MainCanvas, text = "\u03B2 =", bg="white")
    label_Betha['font'] = TriTextFont
    label_Betha.place(x = 20, y = 160)
    ValBethaEntry = Entry(MainCanvas)
    ValBethaEntry.place(x = Xpos, y = 160)
    BoutonTri = Button(MainCanvas, text="Calcul", command=Triangle_angle_Callback)
    BoutonTri['font'] = TriTextFont
    BoutonTri.place(x = 40, y = 200)
    BoutonTriRaz = Button(MainCanvas, text="Reset", command=Triangle_RAZ)
    BoutonTriRaz['font'] = TriTextFont
    BoutonTriRaz.place(x = 120, y = 200)
    label_Deg1 = tk.Label(MainCanvas, text = "°", bg="white")
    label_Deg1['font'] = TriTextFont
    label_Deg1.place(x = 175, y = 160)
    label_Deg2 = tk.Label(MainCanvas, text = "°", bg="white")
    label_Deg2['font'] = TriTextFont
    label_Deg2.place(x = 175, y = 130)
    # MESSAGE EXPLICATION (mettre dans selection des pages)
    # AJOUTER perimetre + aire (why not)

def Triangle_angle_Callback():
    print("triangle calcul")
    inputA = ValAEntry.get()
    inputC = ValCEntry.get()
    inputAlph = ValAlphaEntry.get()
    inputBeth = ValBethaEntry.get()
    val_A, val_B, val_C, val_Alpha, val_Betha = angcal.Calcul_Tri_window(inputA, inputC, inputAlph, inputBeth)
    if val_A >= 0 and val_B >= 0 and val_C >= 0 and val_Alpha >= 0 and val_Betha >= 0:
        ValAEntry.delete(0,END)
        ValAEntry.insert(0,str(val_A))
        ValB.config(text = str(val_B))
        ValCEntry.delete(0,END)
        ValCEntry.insert(0,str(val_C))
        ValAlphaEntry.delete(0,END)
        ValAlphaEntry.insert(0,str(val_Alpha))
        ValBethaEntry.delete(0,END)
        ValBethaEntry.insert(0,str(val_Betha))
    else:
        Triangle_RAZ()
        showinfo('Info', "Des caracteres autres que des nombres ont etes rentres, veuillez n'inserer que des nombres !")

def Triangle_RAZ():
    print("triangle RAZ")
    ValAEntry.delete(0, END)
    ValCEntry.delete(0, END)
    ValB.config(text = "0")
    ValAlphaEntry.delete(0, END)
    ValBethaEntry.delete(0, END)


def Circlips_angle_Page_Setup():
    global CirclipsWindowActive
    global DiaClaCannEntry, label_DiaAl, label_E, label_C, label_F, label_G, label_GTol, label_K, label_DiaAr, label_e, label_c
    global label_f, label_g, label_gtol, label_k
    CirclipsWindowActive = True
    MainCanvas.create_image(50, 10, anchor=NW, image = ImgCirclipsSetup)

    var = StringVar()
    var.trace("w", lambda name, index,mode, var=var: Circlips_Callback(var))
    #var.set("0") # Create problems !!
    DiaClaCannEntry = Entry(MainCanvas, textvariable=var)
    DiaClaCannEntry.place(x = 210, y = 78)

    label_DiaAl = tk.Label(MainCanvas, text = "no", bg="white")
    label_DiaAl.place(x = 205, y = 132)
    label_E = tk.Label(MainCanvas, text = "no", bg="white")
    label_E.place(x = 95, y = 154)
    label_C = tk.Label(MainCanvas, text = "no", bg="white")
    label_C.place(x = 96, y = 179)
    label_F = tk.Label(MainCanvas, text = "no", bg="white")
    label_F.place(x = 96, y = 202)
    label_G = tk.Label(MainCanvas, text = "no", bg="white")
    label_G.place(x = 96, y = 225)
    label_GTol = tk.Label(MainCanvas, text = "no", bg="white")
    label_GTol.place(x = 170, y = 244)
    label_K = tk.Label(MainCanvas, text = "no", bg="white")
    label_K.place(x = 97, y = 266)

    label_DiaAr = tk.Label(MainCanvas, text = "no", bg="white")
    label_DiaAr.place(x = 190, y = 305)
    label_e = tk.Label(MainCanvas, text = "no", bg="white")
    label_e.place(x = 97, y = 329)
    label_c = tk.Label(MainCanvas, text = "no", bg="white")
    label_c.place(x = 97, y = 354)
    label_f = tk.Label(MainCanvas, text = "no", bg="white")
    label_f.place(x = 97, y = 378)
    label_g = tk.Label(MainCanvas, text = "no", bg="white")
    label_g.place(x = 97, y = 400)
    label_gtol = tk.Label(MainCanvas, text = "no", bg="white")
    label_gtol.place(x = 167, y = 420)
    label_k = tk.Label(MainCanvas, text = "no", bg="white")
    label_k.place(x = 97, y = 442)

def Circlips_Callback(Var_in):
    Dia_in = EntrCorr.Correct_Entry_to_Nb(Var_in.get()) # Corrige si l'entree est incorrecte

    try:
       Diam = float(Dia_in) # Conversion en chaine de caractères
    except ValueError:
        print("Probleme dans les parametres d'entree")
        Diam = 0.0 # valeur par défaut
        # EXIT the function
    
    # Appel a la fonction
    dia_Al, val_E, val_C, val_F, val_G, val_G_adj, val_K, dia_Ar, val_e, val_c, val_f, val_g, val_g_adj, val_k = circldta.Circlips_data(Diam)
    # Mise A Jour des valeurs des Labels
    label_DiaAl.config(text = str(dia_Al))
    label_E.config(text = str(val_E))
    label_C.config(text = str(val_C))
    label_F.config(text = str(val_F))
    label_G.config(text = str(val_G))
    val_G_adj = "+" + str(val_G_adj) + " / 0"
    label_GTol.config(text = val_G_adj) # A CORRIGER TODO
    label_K.config(text = str(val_K))

    label_DiaAr.config(text = str(dia_Ar))
    label_e.config(text = str(val_e))
    label_c.config(text = str(val_c))
    label_f.config(text = str(val_f))
    label_g.config(text = str(val_g))
    val_g_adj = "0 / " + str(val_g_adj)
    label_gtol.config(text = val_g_adj) # A CORRIGER TODO
    label_k.config(text = str(val_k))


def Calcul_Vie_Roulement_Page_Setup():
    ClearAllWindowContent()
    global CalculVieRoulementActive, chkBille, chkRouleau
    global RoulBilleCheck, RoulRouleauCheck, BoutonCalRoul, RoulChargeAxialeEntry, RoulChargeRadialeEntry, RoulChargeVideEntry, RoulChargeTotaleEntry
    global RoulVitesseRotationEntry, label_DDVH, label_DDVM
    CalculVieRoulementActive = True

    chkBille = tk.BooleanVar()
    chkBille.set(False)
    chkRouleau = tk.BooleanVar()
    chkRouleau.set(False)
    posXCheckboxes = 200
    posyCheckboxes = 85
    posyEntries = 140
    Yseparation = 40

    MainCanvas.create_image(20, 50, anchor=NW, image = ImgCalculsRoulementsSetup)
    # Label "type de roulement :"
    RoulBilleCheck = Checkbutton(MainCanvas, text='Roulement a billes', var=chkBille, command=CallbackCheckRBille, bg="white")
    RoulBilleCheck.place(x = (posXCheckboxes-70), y = posyCheckboxes)
    RoulRouleauCheck = Checkbutton(MainCanvas, text='Roulement a rouleaux', var=chkRouleau, command=CallbackCheckRRouleau, bg="white")
    RoulRouleauCheck.place(x = (posXCheckboxes+70), y = posyCheckboxes)
    # charge axiale (daN)
    # charge radiale (daN)
    # Charge a vide (daN)
    # charge totale (daN)
    # Vitesse de rotation (tr/min)
    
    FaEntry = StringVar()
    FrEntry = StringVar()
    FvEntry = StringVar()
    ChTotEntry = StringVar()
    VRotEntry = StringVar()

    RoulChargeAxialeEntry = Entry(MainCanvas, textvariable=FaEntry)
    RoulChargeAxialeEntry.place(x = 255, y = posyEntries)
    RoulChargeRadialeEntry = Entry(MainCanvas, textvariable=FrEntry)
    RoulChargeRadialeEntry.place(x = 255, y = (posyEntries + (1 * Yseparation)))
    RoulChargeVideEntry = Entry(MainCanvas, textvariable=FvEntry)
    RoulChargeVideEntry.place(x = 255, y = (posyEntries + (2 * Yseparation)))
    RoulChargeTotaleEntry = Entry(MainCanvas, textvariable=ChTotEntry)
    RoulChargeTotaleEntry.place(x = 255, y = (posyEntries + (3 * Yseparation)))
    RoulVitesseRotationEntry = Entry(MainCanvas, textvariable=VRotEntry)
    RoulVitesseRotationEntry.place(x = 255, y = (posyEntries + (4 * Yseparation)))
    
    BoutonCalRoul = Button(MainCanvas, text="Calcul", command=Calcul_Vie_Roulement_Callback)
    BoutonCalRoul.place(x = 125, y = (posyEntries + 215))

    label_DDVM = tk.Label(MainCanvas, text = "Millions de tours = no", bg="white")
    label_DDVM.place(x = 30, y = 430)
    label_DDVH = tk.Label(MainCanvas, text = "Heures = no", bg="white")
    label_DDVH.place(x = 30, y = 470)

def Calcul_Vie_Roulement_Callback():
    #print("calcul duree de vie de reoulement")
    if chkRouleau.get() == False and chkBille.get() == False:
        # Rien de coche => message pour prevenir
        showinfo('Info', "Aucun type de roulement n'a ete selectionne !")
        return
    else:
        if chkRouleau.get() == True:
            n = 10/3
        else:
            n = 3
    
    # content = EntrCorr.Correct_Entry_to_Nb(Var_dia.get()) # Corrige si l'entree est incorrecte
    ChargeAxiale = float(EntrCorr.Correct_Entry_to_Nb(RoulChargeAxialeEntry.get()))
    ChargeRadiale = float(EntrCorr.Correct_Entry_to_Nb(RoulChargeRadialeEntry.get()))
    ChargeAVide = float(EntrCorr.Correct_Entry_to_Nb(RoulChargeVideEntry.get()))
    ChargeTotale = float(EntrCorr.Correct_Entry_to_Nb(RoulChargeTotaleEntry.get()))
    VitesseRotation = float(EntrCorr.Correct_Entry_to_Nb(RoulVitesseRotationEntry.get()))

    if ChargeAxiale==-1 or ChargeRadiale==-1 or ChargeAVide==-1 or ChargeTotale==-1 or VitesseRotation==-1: 
        #Si une des entrees n'est pas correcte, alors pas de calcul
        showinfo('Erreur', "L'un des parametres d'entree n'est pas correct !")
        return #Arret de la fonction car plus besoin

    else:
        #(400, 1000, 3800, 6200, 3, 150) : Reponse 157,8Millions / 17535,4h
        MtRoul, HRoul = Cal_roul.CalculVieRoulement(ChargeAxiale, ChargeRadiale, ChargeAVide, ChargeTotale, n, VitesseRotation)

        stg_tours = "Millions de tours = " + str(round(MtRoul, 5))
        stg_heures = "Heures = " + str(round(HRoul, 5))
        label_DDVM.config(text = stg_tours)
        label_DDVH.config(text = stg_heures)

def CallbackCheckRBille():
    if chkRouleau.get() == True:
        # print("uncheck rouleaux")
        chkRouleau.set(False)
def CallbackCheckRRouleau():
    if chkBille.get() == True:
        # print("uncheck billes")
        chkBille.set(False)


def Calculs_Geom_Page_Setup():
    global CalculsGeomWindowActive
    global ValacarreEntry, ValbcarreEntry, BoutonCalCarre, label_Perim_Carre, label_Surf_Carre
    global ValacubeEntry, ValbcubeEntry, ValccubeEntry, label_Vol_Cube, label_Surf_Cube, BoutonCalCube
    global BoutonCalCone, ValrconeEntry, ValhconeEntry, label_Vol_Cone, label_Surf_Cone
    global BoutonCalCercle, ValrcercleEntry, label_Circonference_Cercle, label_Surf_Cercle
    global BoutonCalSphere, ValrsphereEntry, label_Vol_Sphere, label_Surf_Sphere
    global BoutonCalCylindre, ValrcylindreEntry, ValhcylindreEntry, label_Vol_Cylindre, label_Surf_Cylindre
    CalculsGeomWindowActive = True

    MainCanvas.create_image(10, 10, anchor=NW, image = ImgCalculsGeomSetup)
    # Carre
    ValacarreEntry = Entry(MainCanvas)
    ValacarreEntry['font'] = CalGeomTextFont
    ValacarreEntry.place(x = 73, y = 127)
    ValbcarreEntry = Entry(MainCanvas)
    ValbcarreEntry['font'] = CalGeomTextFont
    ValbcarreEntry.place(x = 73, y = 158)
    BoutonCalCarre = Button(MainCanvas, text="Calcul", command=Geom_carre)
    BoutonCalCarre['font'] = CalGeomTextFont
    BoutonCalCarre.place(x = 95, y = 200)
    label_Perim_Carre = tk.Label(MainCanvas, text = "no", bg="white")
    label_Perim_Carre['font'] = CalGeomTextFont
    label_Perim_Carre.place(x = 195, y = 245)
    label_Surf_Carre = tk.Label(MainCanvas, text = "no", bg="white")
    label_Surf_Carre['font'] = CalGeomTextFont
    label_Surf_Carre.place(x = 127, y = 271)
    # Cube
    ValacubeEntry = Entry(MainCanvas)
    ValacubeEntry['font'] = CalGeomTextFont
    ValacubeEntry.place(x = 359, y = 123)
    ValbcubeEntry = Entry(MainCanvas)
    ValbcubeEntry['font'] = CalGeomTextFont
    ValbcubeEntry.place(x = 359, y = 154)
    ValccubeEntry = Entry(MainCanvas)
    ValccubeEntry['font'] = CalGeomTextFont
    ValccubeEntry.place(x = 359, y = 188)
    BoutonCalCube = Button(MainCanvas, text="Calcul", command=Geom_cube)
    BoutonCalCube['font'] = CalGeomTextFont
    BoutonCalCube.place(x = 405, y = 209)
    label_Vol_Cube = tk.Label(MainCanvas, text = "no", bg="white")
    label_Vol_Cube['font'] = CalGeomTextFont
    label_Vol_Cube.place(x = 419, y = 241)
    label_Surf_Cube = tk.Label(MainCanvas, text = "no", bg="white")
    label_Surf_Cube['font'] = CalGeomTextFont
    label_Surf_Cube.place(x = 419, y = 268)
    #Cone
    ValrconeEntry = Entry(MainCanvas)
    ValrconeEntry['font'] = CalGeomTextFont
    ValrconeEntry.place(x = 646, y = 125)
    ValhconeEntry = Entry(MainCanvas)
    ValhconeEntry['font'] = CalGeomTextFont
    ValhconeEntry.place(x = 649, y = 158)
    BoutonCalCone = Button(MainCanvas, text="Calcul", command=Geom_cone)
    BoutonCalCone['font'] = CalGeomTextFont
    BoutonCalCone.place(x = 690, y = 200)
    label_Vol_Cone = tk.Label(MainCanvas, text = "no", bg="white")
    label_Vol_Cone['font'] = CalGeomTextFont
    label_Vol_Cone.place(x = 705, y = 244)
    label_Surf_Cone = tk.Label(MainCanvas, text = "no", bg="white")
    label_Surf_Cone['font'] = CalGeomTextFont
    label_Surf_Cone.place(x = 703, y = 270)
    #Cercle
    ValrcercleEntry = Entry(MainCanvas)
    ValrcercleEntry['font'] = CalGeomTextFont
    ValrcercleEntry.place(x = 70, y = 441)
    BoutonCalCercle = Button(MainCanvas, text="Calcul", command=Geom_cercle)
    BoutonCalCercle['font'] = CalGeomTextFont
    BoutonCalCercle.place(x = 108, y = 495)
    label_Circonference_Cercle = tk.Label(MainCanvas, text = "no", bg="white")
    label_Circonference_Cercle['font'] = CalGeomTextFont
    label_Circonference_Cercle.place(x = 191, y = 544)
    label_Surf_Cercle = tk.Label(MainCanvas, text = "no", bg="white")
    label_Surf_Cercle['font'] = CalGeomTextFont
    label_Surf_Cercle.place(x = 124, y = 570)
    #Sphere
    ValrsphereEntry = Entry(MainCanvas)
    ValrsphereEntry['font'] = CalGeomTextFont
    ValrsphereEntry.place(x = 360, y = 445)
    BoutonCalSphere = Button(MainCanvas, text="Calcul", command=Geom_sphere)
    BoutonCalSphere['font'] = CalGeomTextFont
    BoutonCalSphere.place(x = 393, y = 495)
    label_Vol_Sphere = tk.Label(MainCanvas, text = "no", bg="white")
    label_Vol_Sphere['font'] = CalGeomTextFont
    label_Vol_Sphere.place(x = 417, y = 538)
    label_Surf_Sphere = tk.Label(MainCanvas, text = "no", bg="white")
    label_Surf_Sphere['font'] = CalGeomTextFont
    label_Surf_Sphere.place(x = 414, y = 570)
    #Cylindre
    ValrcylindreEntry = Entry(MainCanvas)
    ValrcylindreEntry['font'] = CalGeomTextFont
    ValrcylindreEntry.place(x = 642, y = 445)
    ValhcylindreEntry = Entry(MainCanvas)
    ValhcylindreEntry['font'] = CalGeomTextFont
    ValhcylindreEntry.place(x = 645, y = 473)
    BoutonCalCylindre = Button(MainCanvas, text="Calcul", command=Geom_cylindre)
    BoutonCalCylindre['font'] = CalGeomTextFont
    BoutonCalCylindre.place(x = 670, y = 495)
    label_Vol_Cylindre = tk.Label(MainCanvas, text = "no", bg="white")
    label_Vol_Cylindre['font'] = CalGeomTextFont
    label_Vol_Cylindre.place(x = 701, y = 538)
    label_Surf_Cylindre = tk.Label(MainCanvas, text = "no", bg="white")
    label_Surf_Cylindre['font'] = CalGeomTextFont
    label_Surf_Cylindre.place(x = 701, y = 570)

def Geom_carre():
    InputaCorr = EntrCorr.Correct_Entry_to_Nb(ValacarreEntry.get())
    InputbCorr = EntrCorr.Correct_Entry_to_Nb(ValbcarreEntry.get())

    if InputaCorr != -1 and InputbCorr != -1:
        # Circonference
        Circ_Carre_val = (InputaCorr + InputbCorr) * 2
        label_Perim_Carre.config(text = Circ_Carre_val)
        Surf_Carre_val = (InputaCorr * InputbCorr)
        label_Surf_Carre.config(text = Surf_Carre_val)
    else:
        label_Perim_Carre.config(text = "error")
        label_Surf_Carre.config(text = "error")
def Geom_cube():
    InputaCorr = EntrCorr.Correct_Entry_to_Nb(ValacubeEntry.get())
    InputbCorr = EntrCorr.Correct_Entry_to_Nb(ValbcubeEntry.get())
    InputcCorr = EntrCorr.Correct_Entry_to_Nb(ValccubeEntry.get())

    if InputaCorr != -1 and InputbCorr != -1 and InputcCorr != -1:
        Vol_Cube = InputaCorr * InputbCorr * InputcCorr
        label_Vol_Cube.config(text = Vol_Cube)
        Surf_Cube = 2*(InputaCorr*InputbCorr) + 2*(InputcCorr*InputbCorr) + 2*(InputaCorr*InputcCorr)
        label_Surf_Cube.config(text = Surf_Cube)
    else:
        label_Vol_Cube.config(text = "error")
        label_Surf_Cube.config(text = "error")
def Geom_cone():
    InputrCorr = EntrCorr.Correct_Entry_to_Nb(ValrconeEntry.get())
    InputhCorr = EntrCorr.Correct_Entry_to_Nb(ValhconeEntry.get())
    if InputrCorr != -1 and InputhCorr != -1:
        Vol_Cone = ((Pi_val * InputrCorr * InputrCorr) * InputhCorr) / 3
        label_Vol_Cone.config(text = round(Vol_Cone, 4))
        Surf_Cone = (Pi_val * InputhCorr * InputrCorr) + (Pi_val * InputrCorr * InputrCorr)
        label_Surf_Cone.config(text = round(Surf_Cone, 4))
    else:
        label_Vol_Cone.config(text = "error")
        label_Surf_Cone.config(text = "error")
def Geom_cercle():
    # A faire
    InputrCorr = EntrCorr.Correct_Entry_to_Nb(ValrcercleEntry.get())
    if InputrCorr != -1:
        Circ_Cercle = (Pi_val * InputrCorr * 2)
        label_Circonference_Cercle.config(text = round(Circ_Cercle, 4))
        Surf_Cercle = (Pi_val * InputrCorr * InputrCorr)
        label_Surf_Cercle.config(text = round(Surf_Cercle, 4))
    else:
        label_Circonference_Cercle.config(text = "error")
        label_Surf_Cercle.config(text = "error")
def Geom_sphere():
    # A faire
    InputrCorr = EntrCorr.Correct_Entry_to_Nb(ValrsphereEntry.get())
    if InputrCorr != -1:
        Vol_Sphere = (Pi_val * InputrCorr * InputrCorr * InputrCorr) * (4/3)
        label_Vol_Sphere.config(text = round(Vol_Sphere, 4))
        Surf_Sphere = (Pi_val * InputrCorr * InputrCorr * 4)
        label_Surf_Sphere.config(text = round(Surf_Sphere, 4))
    else:
        label_Vol_Sphere.config(text = "error")
        label_Surf_Sphere.config(text = "error")
def Geom_cylindre():
    # A faire
    InputrCorr = EntrCorr.Correct_Entry_to_Nb(ValrcylindreEntry.get())
    InputhCorr = EntrCorr.Correct_Entry_to_Nb(ValhcylindreEntry.get())
    if InputrCorr != -1 and InputhCorr != -1:
        Vol_Cylindre = ((Pi_val * InputrCorr * InputrCorr) * InputhCorr)
        label_Vol_Cylindre.config(text = round(Vol_Cylindre, 4))
        Surf_Cylindre = (Pi_val * InputrCorr * InputrCorr * 2) + (Pi_val * InputrCorr * InputhCorr * 2)
        label_Surf_Cylindre.config(text = round(Surf_Cylindre, 4))
    else:
        label_Vol_Cylindre.config(text = "error")
        label_Surf_Cylindre.config(text = "error")



def ClearAllWindowContent():
    global MenuActif, VisWindowActif, ClavetteWindowActif, TriangleWindowActif, CirclipsWindowActive, CalculsGeomWindowActive, EcrouWindowActif, EcroupageSetup, SerrageVisActif
    global CalculVieRoulementActive
    # Function that delete all elements in the main canvas (active elements)
    if MenuActif == True:
        MainCanvas.delete("all")
        MenuActif = False
    if VisWindowActif == True:
        MainCanvas.delete("all")
        BoutonEcrouPage.place_forget()
        BoutonVisPage.place_forget()
        Menu_deroulant_taille_vis.place_forget()
        labelPassageVisFin.place_forget()
        labelPassageFin.place_forget()
        labelPassageVisMoyen.place_forget()
        labelPassageMoyen.place_forget()
        labelPassageVisLarge.place_forget()
        labelPassageLarge.place_forget()
        labelChambrageMin.place_forget()
        labelEmpreinteCHC.place_forget()
        labelEmpreinteFHC.place_forget()
        labelDiaVis1.place_forget()
        labelDiaVis2.place_forget()
        labelDiaVis3.place_forget()
        labelDiaVis4.place_forget()
        labelDiaMaxFHC.place_forget()
        labelDiaTeteCHC.place_forget()
        labelDimTeteH.place_forget()
        labelHauteurTeteH.place_forget()
        labelPasDV.place_forget()
        labelPasVis.place_forget()
        #BoutonSerragePage.place_forget()
        labelPasFinDV.place_forget()
        labelPasFinVis.place_forget()
        VisWindowActif = False
    if ClavetteWindowActif == True:
        MainCanvas.delete("all")
        DiaClaCannEntry.place_forget()
        label_Clavette_Label.place_forget()
        label_cla_a.place_forget()
        label_cla_a_value.place_forget()
        label_cla_diam.place_forget()
        label_cla_b.place_forget()
        label_cla_b_value.place_forget()
        label_cla_J.place_forget()
        label_cla_J_value.place_forget()
        label_cla_s.place_forget()
        label_cla_s_value.place_forget()
        label_cla_K.place_forget()
        label_cla_K_value.place_forget()
        label_cla_L.place_forget()
        label_cla_L_value.place_forget()
        label_cla_vis.place_forget()
        label_cla_vis_value.place_forget()
        label_cla_t.place_forget()
        label_cla_t_value.place_forget()
        label_cla_z.place_forget()
        label_cla_z_value.place_forget()
        label_cla_g.place_forget()
        label_cla_g_value.place_forget()
        label_cla_r.place_forget()
        label_cla_r_value.place_forget()
        label_Cannelure_Label.place_forget()
        label_can_D.place_forget()
        label_cla_D_value.place_forget()
        label_can_N.place_forget()
        label_can_N_value.place_forget()
        label_can_B.place_forget()
        label_can_B_value.place_forget()
        label_Cannelure2_Label.place_forget()
        label_can_d.place_forget()
        label_cla_d_value.place_forget()
        ClavetteWindowActif = False
    if TriangleWindowActif == True:
        MainCanvas.delete("all")
        ValAEntry.place_forget()
        ValB.place_forget()
        ValCEntry.place_forget()
        ValAlphaEntry.place_forget()
        ValBethaEntry.place_forget()
        label_A.place_forget()
        label_B.place_forget()
        label_C.place_forget()
        label_Alpha.place_forget()
        label_Betha.place_forget()
        BoutonTri.place_forget()
        BoutonTriRaz.place_forget()
        label_Deg1.place_forget()
        label_Deg2.place_forget()
        TriangleWindowActif = False
    if CirclipsWindowActive == True:
        MainCanvas.delete("all")
        DiaClaCannEntry.place_forget()
        label_DiaAl.place_forget()
        label_E.place_forget()
        label_C.place_forget()
        label_F.place_forget()
        label_G.place_forget()
        label_GTol.place_forget()
        label_K.place_forget()
        label_DiaAr.place_forget()
        label_e.place_forget()
        label_c.place_forget()
        label_f.place_forget()
        label_g.place_forget()
        label_gtol.place_forget()
        label_k.place_forget()
        CirclipsWindowActive = False
    if CalculsGeomWindowActive == True:
        MainCanvas.delete("all")
        ValacarreEntry.place_forget()
        ValbcarreEntry.place_forget()
        BoutonCalCarre.place_forget()
        label_Perim_Carre.place_forget()
        label_Surf_Carre.place_forget()
        ValacubeEntry.place_forget()
        ValbcubeEntry.place_forget()
        ValccubeEntry.place_forget()
        label_Vol_Cube.place_forget()
        label_Surf_Cube.place_forget()
        BoutonCalCube.place_forget()
        ValrconeEntry.place_forget()
        ValhconeEntry.place_forget()
        BoutonCalCone.place_forget()
        label_Vol_Cone.place_forget()
        label_Surf_Cone.place_forget()
        ValrcercleEntry.place_forget()
        BoutonCalCercle.place_forget()
        label_Circonference_Cercle.place_forget()
        label_Surf_Cercle.place_forget()
        ValrsphereEntry.place_forget()
        BoutonCalSphere.place_forget()
        label_Vol_Sphere.place_forget()
        label_Surf_Sphere.place_forget()
        ValrcylindreEntry.place_forget()
        ValhcylindreEntry.place_forget()
        BoutonCalCylindre.place_forget()
        label_Vol_Cylindre.place_forget()
        label_Surf_Cylindre.place_forget()
        CalculsGeomWindowActive = False
    if EcrouWindowActif == True:
        MainCanvas.delete("all")
        BoutonVisPage.place_forget()
        BoutonEcrouPage.place_forget()
        #BoutonSerragePage.place_forget()
        Menu_deroulant_taille_ecrou.place_forget()
        labelEcroud.place_forget()
        labelEcroua.place_forget()
        labelEcroub1.place_forget()
        labelEcroub2.place_forget()
        labelEcroug.place_forget()
        labelEcrouc.place_forget()
        labelEcroue.place_forget()
        labelEcrouf.place_forget()
        labelEcrouCreneaud.place_forget()
        labelEcrouCreneaua.place_forget()
        labelEcrouCreneaud1.place_forget()
        labelEcrouCreneauhmax.place_forget()
        labelEcrouCreneaug.place_forget()
        labelEcrouCreneaum.place_forget()
        EcrouWindowActif = False
        EcroupageSetup = False
    if SerrageVisActif == True:
        MainCanvas.delete("all")
        BoutonVisPage.place_forget()
        BoutonEcrouPage.place_forget()
        BoutonSerragePage.place_forget()
        SerrageVisActif = False
    if CalculVieRoulementActive == True:
        MainCanvas.delete("all")
        RoulBilleCheck.place_forget()
        RoulRouleauCheck.place_forget()
        BoutonCalRoul.place_forget()
        RoulChargeAxialeEntry.place_forget()
        RoulChargeRadialeEntry.place_forget()
        RoulChargeVideEntry.place_forget()
        RoulChargeTotaleEntry.place_forget()
        RoulVitesseRotationEntry.place_forget()
        label_DDVH.place_forget()
        label_DDVM.place_forget()
        CalculVieRoulementActive = False



def MainClick(event):
    PositionX, PositionY = event.x, event.y
    if PrintClickPosition == True:
        print("Debug",PositionX," ",PositionY)
    
    if MenuActif == True:
        if PositionX>XVisMenu and PositionX<(XVisMenu+XmenuImgSize) and PositionY>YVisMenu and PositionY<(YVisMenu+YmenuImgSize):
            #print("selection : Vis")
            ClearAllWindowContent()
            Vis_Page_Setup()
        elif PositionX>XClavettesMenu and PositionX<(XClavettesMenu+XmenuImgSize) and PositionY>YClavettesMenu and PositionY<(YClavettesMenu+YmenuImgSize):
            #print("selection : Clavettes")
            ClearAllWindowContent()
            Cannelures_Clavettes_Page_Setup()
        elif PositionX>XCirclipsMenu and PositionX<(XCirclipsMenu+XmenuImgSize) and PositionY>YCirclipsMenu and PositionY<(YCirclipsMenu+YmenuImgSize):
            #print("selection : Circlips")
            ClearAllWindowContent()
            Circlips_angle_Page_Setup()
        elif PositionX>XAjustementsMenu and PositionX<(XAjustementsMenu+XmenuImgSize) and PositionY>YAjustementsMenu and PositionY<(YAjustementsMenu+YmenuImgSize):
            print("selection : Ajustements")
            # Clear window
            # Call the function
            showinfo('Info', "Cette page sera disponible dans une future version")
        elif PositionX>XCisaillementMenu and PositionX<(XCisaillementMenu+XmenuImgSize) and PositionY>YCisaillementMenu and PositionY<(YCisaillementMenu+YmenuImgSize):
            print("selection : Cisaillement")
            # Clear window
            # Call the function
            showinfo('Info', "Cette page sera disponible dans une future version")
        elif PositionX>XJointsMenu and PositionX<(XJointsMenu+XmenuImgSize) and PositionY>YJointsMenu and PositionY<(YJointsMenu+YmenuImgSize):
            print("selection : Joints")
            # Clear window
            # Call the function
            showinfo('Info', "Cette page sera disponible dans une future version")
        elif PositionX>XCalculsMenu and PositionX<(XCalculsMenu+XmenuImgSize) and PositionY>YCalculsMenu and PositionY<(YCalculsMenu+YmenuImgSize):
            #print("selection : Calculs")
            ClearAllWindowContent()
            Calculs_Geom_Page_Setup()
        elif PositionX>XConversionMenu and PositionX<(XConversionMenu+XmenuImgSize) and PositionY>YConversionMenu and PositionY<(YConversionMenu+YmenuImgSize):
            print("selection : Calcul roulements")
            ClearAllWindowContent()
            Calcul_Vie_Roulement_Page_Setup()
        elif PositionX>XAnglesMenu and PositionX<(XAnglesMenu+XmenuImgSize) and PositionY>YAnglesMenu and PositionY<(YAnglesMenu+YmenuImgSize):
            #print("selection : Angles")
            ClearAllWindowContent()
            Triangle_angle_Page_Setup()



############################################################
#                                                          #
#                        MAIN PROGRAM                      #
#                                                          #
############################################################

fenetre = tk.Tk(className = " Le P'tit GDI ENIMien v" + __version__)
fenetre.geometry(WindowSize)
fenetre.iconbitmap('data/gdi.ico')

try:
    # Import all images for the Tkinter page (images in png or ppm format)
    ImgVis = PhotoImage(file="data/menu/Vis.png")
    ImgClavette = PhotoImage(file="data/menu/Clavette.png")
    ImgCirclips = PhotoImage(file="data/menu/Circlips.png")
    ImgAjustements = PhotoImage(file="data/menu/Ajustements.png")
    ImgCisaillement = PhotoImage(file="data/menu/Cisaillement.png")
    ImgJoints = PhotoImage(file="data/menu/Joints.png")
    ImgCalculs = PhotoImage(file="data/menu/Surf_Vol.png")
    ImgCalculRoulement = PhotoImage(file="data/menu/Roulements.png")
    ImgAngles = PhotoImage(file="data/menu/Angles.png")

    # Setup pages images
    ImgVisSetup = PhotoImage(file="data/SP/Vis_Setup.png")
    ImgEcrouSetup = PhotoImage(file="data/SP/ecrou_SP.png")
    ImgClaCannSetup = PhotoImage(file="data/SP/Cla_can.png")
    ImgTriSetup = PhotoImage(file="data/SP/Tri_SP.png")
    ImgCirclipsSetup = PhotoImage(file="data/SP/Circl_SP.png")
    ImgCalculsGeomSetup = PhotoImage(file="data/SP/Cal_geom.png")
    ImgCalculsRoulementsSetup = PhotoImage(file="data/SP/Roulement_SP.png")

    ImgCroRou = PhotoImage(file="data/CroixRouge.png")

except:
    showerror('Erreur', "Erreur 20 : Le programme possède des erreurs ou est corrompu")
    #fenetre.quit() # Ne ferme pas la fenetre
    fenetre.destroy()



# Set all fonts of the app
ToolBarTextFont = font.Font(family = 'Helvetica')
ToolBarTextFont = font.Font(size = 13)

ClaCanTextFont = font.Font(size = 10)
VisTextFont = font.Font(size = 10)
TriTextFont = font.Font(size = 11)
CalGeomTextFont = font.Font(size = 12)


MainCanvas = tk.Canvas(fenetre, width = WindowWidthSize, height = (WindowHeightSize - ToolbarHeight), background = 'white')
MainCanvas.pack(expand=True)
ToolbarCanvas = tk.Canvas(fenetre, width = WindowWidthSize, height = ToolbarHeight)
ToolbarCanvas.pack()

ToolBarSetup()

MENU_Setup()

MainCanvas.bind('<Button-1>', MainClick)

fenetre.mainloop()

