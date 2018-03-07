def Jeux():
    continuer=True
    while(continuer):
        continuer2=True
        while(continuer2):
            jeu=input("\n\nA quoi voulez-vous jouer? Veuillez entrer l'un des chiffres s'il vous plait :\n\n1 - Pendu\n2 - Morpion\n3 - Puissance 4\n4 - Bataille Navale (multijoueur)\n5 - Plus ou moins (jusqu'à 10 joueurs)\n6 - Sudoku (Grille aléatoire)\n7 - MasterMind (jusqu'à 10 joueurs)\n\nJeu = ")
            if(jeu=="1"):
                continuer2=False
                Pendu()
            elif(jeu=="2"):
                continuer2=False
                Morpion()
            elif(jeu=="3"):
                continuer2=False
                Puissance4()
            elif(jeu=="4"):
                continuer2=False
                Bataille_Navale()
            elif(jeu=="5"):
                continuer2=False
                Plus_Moins()
            elif(jeu=="6"):
                continuer2=False
                Sudoku()
            elif(jeu=="7"):
                continuer2=False
                MasterMind()
            else:
                print("\nN'entrez que l'un de ces 4 chiffres s'il vous plait !!!")
        jouer=input("\n\nVoulez-vous continuer de jouer à un autre jeu? Entrez Oui ou Non : ")
        jouer=jouer.upper()
        if(jouer=="NON"):
            continuer=False
            print("\nAu revoir ! Merci d'avoir joué !!!")

def Pendu():
    print("\n"*60)
    import time
    rejouer=True
    while(rejouer):
        cont=True
        while(cont):
            mot=input("\nDonnez le mot qu'il faudra chercher : ")
            L=list(mot)
            L=Pendu_Maj(L)
            if(Pendu_Test_Mot_Lettre(L)):
                cont=False
        longueur=len(L)
        fin=""
        i=0
        while(i<longueur):
            fin=fin+str(L[i])
            i=i+1
        dessin=10
        liste_mauvais=[]
        resultat=[]
        i=0
        while(i<longueur):
            resultat.append("_")
            i=i+1
        continuer=True
        while(continuer):
            print("\n"*60+" "*7+"_"*30+"\n")
            mot=" "
            i=0
            while(i<longueur):
                mot=mot+resultat[i]+" "
                i=i+1
            print("\nVoici le mot que vous cherchez : "+mot+"\n")
            if(liste_mauvais!=[]):
                mauvais=""
                k=len(liste_mauvais)
                i=0
                while(i<k):
                    if(i>0):
                        mauvais=mauvais+", "
                    mauvais=mauvais+str(liste_mauvais[i])
                    i=i+1
                print("La liste de mauvaises lettres est : "+mauvais)
            cont=True
            while(cont):
                a=input("\nDonnez une lettre : ")
                a=a.upper()
                A=[a]
                if(Pendu_Test_Mot_Lettre(A)):
                    if(Pendu_Test_Lettre(a, liste_mauvais)):
                        cont=False
            j=0
            mauvais=True
            while(j<longueur):
                if(a==L[j]):
                    resultat[j]=a
                    mauvais=False
                if(j==longueur-1 and mauvais):
                    dessin=dessin-1
                    liste_mauvais.append(a)
                    print("\nMauvaise lettre !!!\n")
                elif(j==longueur-1 and not(mauvais)):
                    print("\nBravo !!!")
                j=j+1
            Pendu_Dessin(dessin)
            continuer=Pendu_Fin_Partie(dessin, resultat, L, fin)
            if(continuer):
                print("\n"*2+"( Waiting... )")
                time.sleep(4.0)
        jouer=input("\nVoulez-vous rejouer? Entrez Oui ou Non : ")
        jouer=jouer.upper()
        if(jouer=="NON"):
            rejouer=False

def Pendu_Dessin(dessin):
    print("\n"*2+" "*18+"dessin\n"+" "*7+"_"*30+"\n"*2)
    if(dessin==0):
        print(" "*16+"---------")
        print(" "*16+"|  /    |")
        print(" "*16+"| /    ---")
        print(" "*16+"|/    |O.0|")
        print(" "*16+"|      ---")
        print(" "*16+"|       |")
        print(" "*16+"|    ---|---")
        print(" "*16+"|       |")
        print(" "*16+"|       |")
        print(" "*16+"|      / \ ")
        print(" "*16+"|     /   \ ")
        print(" "*16+"|")
        print(" "*16+"|")
    elif(dessin==1):
        print(" "*16+"---------")
        print(" "*16+"|  /    |")
        print(" "*16+"| /    ---")
        print(" "*16+"|/    |O.0|")
        print(" "*16+"|      ---")
        print(" "*16+"|       |")
        print(" "*16+"|    ---|---")
        print(" "*16+"|       |")
        print(" "*16+"|       |")
        print(" "*16+"|      /")
        print(" "*16+"|     /")
        print(" "*16+"|")
        print(" "*16+"|")
    elif(dessin==2):
        print(" "*16+"---------")
        print(" "*16+"|  /    |")
        print(" "*16+"| /    ---")
        print(" "*16+"|/    |O.0|")
        print(" "*16+"|      ---")
        print(" "*16+"|       |")
        print(" "*16+"|    ---|---")
        print(" "*16+"|       |")
        print(" "*16+"|       |")
        i=0
        while(i<4):
            print(" "*16+"|")
            i=i+1
    elif(dessin==3):
        print(" "*16+"---------")
        print(" "*16+"|  /    |")
        print(" "*16+"| /    ---")
        print(" "*16+"|/    |O.0|")
        print(" "*16+"|      ---")
        print(" "*16+"|       |")
        print(" "*16+"|    ---|")
        print(" "*16+"|       |")
        print(" "*16+"|       |")
        i=0
        while(i<4):
            print(" "*16+"|")
            i=i+1
    elif(dessin==4):
        print(" "*16+"---------")
        print(" "*16+"|  /    |")
        print(" "*16+"| /    ---")
        print(" "*16+"|/    |O.0|")
        print(" "*16+"|      ---")
        i=0
        while(i<4):
            print(" "*16+"|       |")
            i=i+1
        i=0
        while(i<4):
            print(" "*16+"|")
            i=i+1
    elif(dessin==5):
        print(" "*16+"---------")
        print(" "*16+"|  /    |")
        print(" "*16+"| /    ---")
        print(" "*16+"|/    |O.0|")
        print(" "*16+"|      ---")
        i=0
        while(i<8):
            print(" "*16+"|")
            i=i+1
    elif(dessin==6):
        print(" "*16+"---------")
        print(" "*16+"|  /    |")
        print(" "*16+"| /")
        print(" "*16+"|/")
        i=0
        while(i<9):
            print(" "*16+"|")
            i=i+1
    elif(dessin==7):
        print(" "*16+"---------")
        print(" "*16+"|  /")
        print(" "*16+"| /")
        print(" "*16+"|/")
        i=0
        while(i<8):
            print(" "*16+"|")
            i=i+1
    elif(dessin==8):
        print(" "*16+"---------")
        i=0
        while(i<12):
            print(" "*16+"|")
            i=i+1
    elif(dessin==9):
        print(" "*16+" ")
        i=0
        while(i<12):
            print(" "*16+"|")
            i=i+1
    print("\n"*2+" "*7+"_"*30)

def Pendu_Fin_Partie(dessin, resultat, L, fin):
    continuer=True
    if(dessin==0):
        print("\nPERDU !!!")
        print("\nLe mot était: "+fin)
        continuer=False
    elif(resultat==L):
        print("\nBRAVO !!!")
        print("\nLe mot est bien: "+fin)
        continuer=False
    return(continuer)

def Pendu_Test_Mot_Lettre(L):
    continuer=True
    i=0
    longueur=len(L)
    while(i<longueur and continuer):
        if(L[i]!="A" and L[i]!="B" and L[i]!="C" and L[i]!="D" and L[i]!="E" and L[i]!="F" and L[i]!="G" and L[i]!="H" and L[i]!="I" and L[i]!="J" and L[i]!="K" and L[i]!="L" and L[i]!="M" and L[i]!="N" and L[i]!="O" and L[i]!="P" and L[i]!="Q" and L[i]!="R" and L[i]!="S" and L[i]!="T" and L[i]!="U" and L[i]!="V" and L[i]!="W" and L[i]!="X" and L[i]!="Y" and L[i]!="Z"):
            continuer=False
            print("\nVeuillez à ne rentrer que des lettres s'il vous plait !!!")
        i=i+1
    return(continuer)

def Pendu_Test_Lettre(a, liste_mauvais):
    continuer=True
    longueur=len(liste_mauvais)
    i=0
    while(i<longueur and continuer):
        if(a==liste_mauvais[i]):
            continuer=False
            print("\nVous avez déjà essayé cette lettre !!!")
        i=i+1
    return(continuer)

def Pendu_Maj(L):
    i=0
    longueur=len(L)
    while(i<longueur):
        L[i]=L[i].upper()
        if(L[i]=="À" or L[i]=="Â" or L[i]=="Ä"):
            L[i]="A"
        elif(L[i]=="È" or L[i]=="Ê" or L[i]=="Ë" or L[i]=="É"):
            L[i]="E"
        elif(L[i]=="Ÿ"):
            L[i]="Y"
        elif(L[i]=="Ì" or L[i]=="Î" or L[i]=="Ï"):
            L[i]="I"
        elif(L[i]=="Ò" or L[i]=="Ô" or L[i]=="Ö"):
            L[i]="O"
        elif(L[i]=="Ù" or L[i]=="Û" or L[i]=="Ü"):
            L[i]="U"
        i=i+1
    return(L)

def Morpion():
    Morpion_Efface()
    import time
    rejouer=True
    a=True
    while(rejouer):
        tableau=["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        if(a):
            print("\nJoueur 1 :")
            Joueur1=Morpion_Nom_Joueur()
            print("\nJoueur 2 :")
            Joueur2=Morpion_Nom_Joueur()
        joueur1="X"
        joueur2="O"
        partie_nulle=False
        continuer=True
        while(continuer):
            Morpion_Efface()
            print("A votre tour, "+Joueur1+" : \n")
            Morpion_Tableau(tableau)
            continuer2=True
            while(continuer2):
                case=Morpion_Case()
                tableau0=[]
                i=0
                while(i<9):
                    a=tableau[i]
                    tableau0.append(a)
                    i=i+1
                tableau=Morpion_Joueur(tableau, case, joueur1)
                if(tableau0!=tableau):
                    continuer2=False
            continuer=Morpion_Gagner(tableau, joueur1)
            if (continuer==False):
                Morpion_Efface()
                Morpion_Tableau(tableau)
                print("\nBravo "+Joueur1+" vous avez gagné !")
                time.sleep(8.0)
            partie_nulle=Morpion_Partie_nulle(tableau)
            if(partie_nulle):
                continuer=False
            if(continuer):
                Morpion_Efface()
                print("A votre tour, "+Joueur2+" : \n")
                Morpion_Tableau(tableau)
                continuer2=True
                while(continuer2):
                    case=Morpion_Case()
                    tableau0=[]
                    i=0
                    while(i<9):
                        a=tableau[i]
                        tableau0.append(a)
                        i=i+1
                    tableau=Morpion_Joueur(tableau, case, joueur2)
                    if(tableau0!=tableau):
                        continuer2=False
                continuer=Morpion_Gagner(tableau, joueur2)
                if (continuer==False):
                    Morpion_Efface()
                    Morpion_Tableau(tableau)
                    print("\nBravo "+Joueur2+" vous avez gagné !")
                    time.sleep(8.0)
                    Efface()
        jouer=input("Voulez-vous rejouer? Entrez Oui ou Non : ")
        jouer=jouer.upper()
        if(jouer=="NON"):
            rejouer=False
        changer="Oui"
        if(rejouer):
            changer=input("\n\n\nVoulez-vous changer les noms? Entrez Oui ou Non : ")
            changer=changer.upper()
        if(changer=="NON"):
            a=False
        else:
            a=True

def Morpion_Nom_Joueur():
    nom=input("Donnez votre nom : ")
    return(nom)

def Morpion_Joueur(tableau, case, joueur):
    continuer=True
    k=0
    while(k<9 and continuer):
        i=1
        while(i<4 and continuer):
            j=1
            while(j<4 and continuer):
                if(case==(i, j)):
                    if(tableau[k]=="-"):
                        tableau[k]=joueur
                        continuer=False
                    else:
                        print("\nCase déjà prise !!! Entrez de nouvelles coordonnées !!!\n")
                elif(continuer and k==8):
                    print("\nEntrez de bonnes coordonnées !!!\n")
                j=j+1
                k=k+1
            i=i+1
    return(tableau)

def Morpion_Case():
    continuer=True
    while(continuer):
        x1=input("\nDonnez les coordonnées de la case :\nLigne = ")
        y1=input("Colonne = ")
        if((x1=="1" or x1=="2" or x1=="3") and (y1=="1" or y1=="2" or y1=="3")):
            continuer=False
            cont=True
            i=1
            while(i<4 and cont):
                if(str(i)==x1):
                    cont=False
                    x=i
                i=i+1
            cont=True
            i=1
            while(i<4 and cont):
                if(str(i)==y1):
                    cont=False
                    y=i
                i=i+1
        else:
            print("\nEntrez un nombre du tableau s'il vous plait !!!")
    return(x, y)

def Morpion_Tableau(tableau):
    print("\n ", " ", "1", " ", "2", " ", "3")
    print("  ", "---", "---", "---")
    i=1
    a=0
    while(i<=3):
        print(i, "|", tableau[a], "|", tableau[a+1], "|", tableau[a+2], "|")
        print("  ", "---", "---", "---")
        a=a+3
        i=i+1
    print("\n")

def Morpion_Efface():
    print("\n"*60)

def Morpion_Gagner(tableau, joueur):
    continuer=True
    if(tableau[0]==joueur and tableau[1]==joueur and tableau[2]==joueur):
        continuer=False
    if(tableau[3]==joueur and tableau[4]==joueur and tableau[5]==joueur):
        continuer=False
    if(tableau[6]==joueur and tableau[7]==joueur and tableau[8]==joueur):
        continuer=False
    if(tableau[0]==joueur and tableau[3]==joueur and tableau[6]==joueur):
        continuer=False
    if(tableau[1]==joueur and tableau[4]==joueur and tableau[7]==joueur):
        continuer=False
    if(tableau[2]==joueur and tableau[5]==joueur and tableau[8]==joueur):
        continuer=False
    if(tableau[0]==joueur and tableau[4]==joueur and tableau[8]==joueur):
        continuer=False
    if(tableau[2]==joueur and tableau[4]==joueur and tableau[6]==joueur):
        continuer=False
    return(continuer)

def Morpion_Partie_nulle(tableau):
    Morpion_Efface()
    partie_nulle=False
    if(tableau[0]!="-" and tableau[1]!="-" and tableau[2]!="-" and tableau[3]!="-" and tableau[4]!="-" and tableau[5]!="-" and tableau[6]!="-" and tableau[7]!="-" and tableau[8]!="-"):
        partie_nulle=True
        print("Partie nulle !!!")
    return(partie_nulle)

def Puissance4():
    Puissance4_Efface()
    import time
    rejouer=True
    a=True
    while(rejouer):
        tableau=[]
        i=0
        while(i<42):
            tableau.append("-")
            i=i+1
        if(a):
            print("\nJoueur 1 :")
            Joueur1=Puissance4_Nom_Joueur()
            print("\nJoueur 2 :")
            Joueur2=Puissance4_Nom_Joueur()
        joueur1="X"
        joueur2="O"
        partie_nulle=False
        continuer=True
        while(continuer):
            Puissance4_Efface()
            print("A votre tour, "+Joueur1+" :\n")
            Puissance4_Tableau(tableau)
            continuer2=True
            while(continuer2):
                case=Puissance4_Case()
                j=Puissance4_Joueur(tableau, case)
                if(j!=42):
                    tableau[j]=joueur1
                    continuer2=False
            continuer=Puissance4_Gagner(tableau, joueur1)
            if(continuer==False):
                Puissance4_Efface()
                Puissance4_Tableau(tableau)
                print("\nBravo "+Joueur1+" vous avez gagné !")
                time.sleep(8.0)
            else:
                Puissance4_Efface()
                print("A votre tour, "+Joueur2+" :\n")
                Puissance4_Tableau(tableau)
                continuer2=True
                while(continuer2):
                    case=Puissance4_Case()
                    j=Puissance4_Joueur(tableau, case)
                    if(j!=42):
                        tableau[j]=joueur2
                        continuer2=False
                continuer=Puissance4_Gagner(tableau, joueur2)
                if(continuer==False):
                    Puissance4_Efface()
                    Puissance4_Tableau(tableau)
                    print("\nBravo "+Joueur2+" vous avez gagné !")
                    time.sleep(8.0)
            partie_nulle=Puissance4_Partie_nulle(tableau)
            if(partie_nulle):
                continuer=False
        jouer=input("Voulez-vous rejouer? Entrez Oui ou Non : ")
        jouer=jouer.upper()
        if(jouer=="NON"):
            rejouer=False
        changer="Oui"
        if(rejouer):
            changer=input("\n\n\nVoulez-vous changer les noms? Entrez Oui ou Non : ")
            changer=changer.upper()
        if(changer=="NON"):
            a=False
        else:
            a=True

def Puissance4_Nom_Joueur():
    nom=input("Donnez votre nom : ")
    return(nom)

def Puissance4_Efface():
    print("\n"*60)

def Puissance4_Tableau(tableau):
    print("\n ", "1", " ", "2", " ", "3", " ", "4", " ", "5", " ", "6", " ", "7")
    print(" ---", "---", "---", "---", "---", "---", "---")
    i=0
    a=0
    while(i<6):
        print("|", tableau[a], "|", tableau[a+1], "|", tableau[a+2], "|", tableau[a+3], "|", tableau[a+4], "|", tableau[a+5], "|", tableau[a+6], "|")
        print(" ---", "---", "---", "---", "---", "---", "---")
        a=a+7
        i=i+1
    print("\n")

def Puissance4_Case():
    continuer=True
    while(continuer):
        x1=input("\nDonnez un numéro de colonne : ")
        i=1
        while(i<8 and continuer):
            if(str(i)==x1):
                continuer=False
                x=i
            i=i+1
        if(continuer):
            print("\nVeuillez entrer une valeur du tableau s'il vous plait !!!")
    return(x)

def Puissance4_Joueur(tableau, case):
    cont=True
    i=1
    while(i<8 and cont):
        if(case==i):
            cont=False
            continuer=True
            j=34+i
            while(j>=i-1 and continuer):
                if(tableau[j]=="-"):
                    continuer=False
                else:
                    if(j==i-1 and continuer):
                        j=42
                        print("\nLa colonne est complète ! Choisissez-en une autre !")
                        continuer=False
                    else:
                        j=j-7
        else:
            i=i+1
    return(j)

def Puissance4_Partie_nulle(tableau):
    Puissance4_Efface()
    partie_nulle=False
    if(tableau[0]!="-" and tableau[1]!="-" and tableau[2]!="-" and tableau[3]!="-" and tableau[4]!="-" and tableau[5]!="-" and tableau[6]!="-" and tableau[7]!="-" and tableau[8]!="-" and tableau[9]!="-" and tableau[10]!="-" and tableau[11]!="-" and tableau[12]!="-" and tableau[13]!="-" and tableau[14]!="-" and tableau[15]!="-" and tableau[16]!="-" and tableau[17]!="-" and tableau[18]!="-" and tableau[19]!="-" and tableau[20]!="-" and tableau[21]!="-" and tableau[22]!="-" and tableau[23]!="-" and tableau[24]!="-" and tableau[25]!="-" and tableau[26]!="-" and tableau[27]!="-" and tableau[28]!="-" and tableau[29]!="-" and tableau[30]!="-" and tableau[31]!="-" and tableau[32]!="-" and tableau[33]!="-" and tableau[34]!="-" and tableau[35]!="-" and tableau[36]!="-" and tableau[37]!="-" and tableau[38]!="-" and tableau[39]!="-" and tableau[40]!="-" and tableau[41]!="-"):
        partie_nulle=True
        print("Partie nulle !!!")
    return(partie_nulle)

def Puissance4_Gagner(tableau, joueur):
    continuer=True
    ligne1=[]
    ligne2=[]
    ligne3=[]
    ligne4=[]
    ligne5=[]
    ligne6=[]
    i=0
    while(i<=6):
        ligne1.append(tableau[i])
        i=i+1
    i=7
    while(i<=13):
        ligne2.append(tableau[i])
        i=i+1
    i=14
    while(i<=20):
        ligne3.append(tableau[i])
        i=i+1
    i=21
    while(i<=27):
        ligne4.append(tableau[i])
        i=i+1
    i=28
    while(i<=34):
        ligne5.append(tableau[i])
        i=i+1
    i=35
    while(i<=41):
        ligne6.append(tableau[i])
        i=i+1
    cases=1
    j=0
    while(j<6):
        if(ligne1[j]==joueur and ligne1[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<6):
        if(ligne2[j]==joueur and ligne2[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<6):
        if(ligne3[j]==joueur and ligne3[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<6):
        if(ligne4[j]==joueur and ligne4[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<6):
        if(ligne5[j]==joueur and ligne5[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<6):
        if(ligne6[j]==joueur and ligne6[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    colonne1=[]
    colonne2=[]
    colonne3=[]
    colonne4=[]
    colonne5=[]
    colonne6=[]
    colonne7=[]
    i=0
    while(i<42):
        colonne1.append(tableau[i])
        i=i+7
    i=1
    while(i<42):
        colonne2.append(tableau[i])
        i=i+7
    i=2
    while(i<42):
        colonne3.append(tableau[i])
        i=i+7
    i=3
    while(i<42):
        colonne4.append(tableau[i])
        i=i+7
    i=4
    while(i<42):
        colonne5.append(tableau[i])
        i=i+7
    i=5
    while(i<42):
        colonne6.append(tableau[i])
        i=i+7
    i=6
    while(i<42):
        colonne7.append(tableau[i])
        i=i+7
    cases=1
    j=0
    while(j<5):
        if(colonne1[j]==joueur and colonne1[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<5):
        if(colonne2[j]==joueur and colonne2[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<5):
        if(colonne3[j]==joueur and colonne3[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<5):
        if(colonne4[j]==joueur and colonne4[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<5):
        if(colonne5[j]==joueur and colonne5[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<5):
        if(colonne6[j]==joueur and colonne6[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<5):
        if(colonne7[j]==joueur and colonne7[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    diagonale11=[]
    diagonale12=[]
    diagonale13=[]
    diagonale14=[]
    diagonale15=[]
    diagonale16=[]
    i=3
    while(i<=21):
        diagonale11.append(tableau[i])
        i=i+6
    i=4
    while(i<=28):
        diagonale12.append(tableau[i])
        i=i+6
    i=5
    while(i<=35):
        diagonale13.append(tableau[i])
        i=i+6
    i=6
    while(i<=36):
        diagonale14.append(tableau[i])
        i=i+6
    i=13
    while(i<=37):
        diagonale15.append(tableau[i])
        i=i+6
    i=20
    while(i<=38):
        diagonale16.append(tableau[i])
        i=i+6
    cases=1
    j=0
    while(j<3):
        if(diagonale11[j]==joueur and diagonale11[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<4):
        if(diagonale12[j]==joueur and diagonale12[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<5):
        if(diagonale13[j]==joueur and diagonale13[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<5):
        if(diagonale14[j]==joueur and diagonale14[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<4):
        if(diagonale15[j]==joueur and diagonale15[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<3):
        if(diagonale16[j]==joueur and diagonale16[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    diagonale21=[]
    diagonale22=[]
    diagonale23=[]
    diagonale24=[]
    diagonale25=[]
    diagonale26=[]
    i=14
    while(i<=38):
        diagonale21.append(tableau[i])
        i=i+8
    i=7
    while(i<=39):
        diagonale22.append(tableau[i])
        i=i+8
    i=0
    while(i<=40):
        diagonale23.append(tableau[i])
        i=i+8
    i=1
    while(i<=41):
        diagonale24.append(tableau[i])
        i=i+8
    i=2
    while(i<=34):
        diagonale25.append(tableau[i])
        i=i+8
    i=3
    while(i<=27):
        diagonale26.append(tableau[i])
        i=i+8
    cases=1
    j=0
    while(j<3):
        if(diagonale21[j]==joueur and diagonale21[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<4):
        if(diagonale22[j]==joueur and diagonale22[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<5):
        if(diagonale23[j]==joueur and diagonale23[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<5):
        if(diagonale24[j]==joueur and diagonale24[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<4):
        if(diagonale25[j]==joueur and diagonale25[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    cases=1
    j=0
    while(j<3):
        if(diagonale26[j]==joueur and diagonale26[j+1]==joueur):
            cases=cases+1
        else:
            cases=1
        if(cases==4):
            continuer=False
        j=j+1
    return(continuer)

def Bataille_Navale():
    Bataille_Navale_Efface()
    import time
    a=True
    continuer=True
    print("\n!!! Veuillez jouer à la Bataille Navale avec la fenêtre en plein écran s'il vous plait !!!")
    while(continuer):
        continuer2=True
        while(continuer2 and a):
            Joueurs1=input("\nMode 1 Joueur ou Mode 2 Joueurs? Entrez 1 ou 2 : ")
            b=1
            if(str(b)==Joueurs1):
                Joueurs=b
                continuer2=False
            elif(str(b+1)==Joueurs1):
                Joueurs=b+1
                continuer2=False
            else:
                print("Vous n'avez pas entré une bonne valeur !!! Réessayez :")
        if(a):
            cont=True
            while(cont):
                print("\nJoueur 1 :")
                joueur1=Bataille_Navale_Nom_Joueur()
                if(Joueurs==2):
                    print("\nJoueur 2 :")
                    joueur2=Bataille_Navale_Nom_Joueur()
                else:
                    joueur2="Ordinateur"
                if(len(joueur1)<20 and len(joueur2)<20):
                    cont=False
                else:
                    print("N'écrivez pas un nom trop long s'il vous plait !")
        longueur_N1=len(joueur1)
        longueur_N2=len(joueur2)
        N=0
        N=Bataille_Navale_Valeur_N()
        G=Bataille_Navale_Grille_Initiale(N)
        Bataille_Navale_Efface()
        print("\n"+joueur1+", entrez votre bateau :")
        B1=Bataille_Navale_Bateau(N, G, joueur1)
        Bataille_Navale_Efface()
        if(joueur2!="Ordinateur"):
            print("\n"+joueur2+", entrez votre bateau :")
            B2=Bataille_Navale_Bateau(N, G, joueur2)
            Bataille_Navale_Efface()
        else:
            B2=Bataille_Navale_Bateau(N, G, joueur2)
        G1=Bataille_Navale_Grille_Initiale(N)
        G2=Bataille_Navale_Grille_Initiale(N)
        k=Bataille_Navale_Valeur_k(B1)
        while(Bataille_Navale_Total(G1)<k and Bataille_Navale_Total(G2)<k):
            print("\n\nA votre tour "+joueur1+" :")
            J=1
            blanc=51-longueur_N1+(N-5)*4
            print("\n"+" "*8+joueur1+" :"+" "*blanc+joueur2+" :")
            Bataille_Navale_Affiche_Grille2(G1, G2, J)
            (i1, j1)=Bataille_Navale_Coup(G1, N)
            if(Bataille_Navale_Touche(i1, j1, B2)):
                print("\nTouché !!!")
                G1[i1][j1]=1
            else:
                print("\nManqué !!!")
                G1[i1][j1]=-1
            Bataille_Navale_Coule(i1, j1, B2, G1)
            time.sleep(5.0)
            Bataille_Navale_Efface()
            print("\n\nA votre tour "+joueur2+" :")
            J=2
            blanc=51-longueur_N2+(N-5)*4
            print("\n"+" "*8+joueur2+" :"+" "*blanc+joueur1+" :")
            Bataille_Navale_Affiche_Grille2(G1, G2, J)
            if(joueur2=="Ordinateur"):
                (i2, j2)=Bataille_Navale_Coup_Ordinateur(G2, N, B1)
            else:
                (i2, j2)=Bataille_Navale_Coup(G2, N)
            if(Bataille_Navale_Touche(i2, j2, B1)):
                print("\nTouché !!!")
                G2[i2][j2]=1
            else:
                print("\nManqué !!!")
                G2[i2][j2]=-1
            Bataille_Navale_Coule(i2, j2, B1, G2)
            time.sleep(5.0)
            Bataille_Navale_Efface()
            if(Bataille_Navale_Total(G1)==Bataille_Navale_Total(G2) and Bataille_Navale_Total(G1)==k):
                print("\nMATCH NUL !!!")
            elif(Bataille_Navale_Total(G1)>Bataille_Navale_Total(G2) and Bataille_Navale_Total(G1)==k):
                print("\nVICTOIRE POUR "+joueur1+" !!!")
            elif(Bataille_Navale_Total(G2)>Bataille_Navale_Total(G1) and Bataille_Navale_Total(G2)==k):
                print("\nVICTOIRE POUR "+joueur2+" !!!")
        recommencer=input("\nVoulez-Vous rejouer? Entrez Oui ou Non : ")
        recommencer=recommencer.upper()
        if(recommencer=="NON"):
            continuer=False
        changer="Oui"
        if(continuer):
            changer=input("\n\n\nVoulez-vous changer les noms? Entrez Oui ou Non : ")
            changer=changer.upper()
        if(changer=="NON"):
            a=False
        else:
            a=True

def Bataille_Navale_Vérifier_entre_i(chiffre, N):
    continuer=False
    if(str(chiffre)=="a" or str(chiffre)=="b" or str(chiffre)=="c" or str(chiffre)=="d" or str(chiffre)=="e" or str(chiffre)=="f" or str(chiffre)=="g" or str(chiffre)=="h" or str(chiffre)=="i" or str(chiffre)=="j"):
        continuer=True
    elif(str(chiffre)=="A" or str(chiffre)=="B" or str(chiffre)=="C" or str(chiffre)=="D" or str(chiffre)=="E" or str(chiffre)=="F" or str(chiffre)=="G" or str(chiffre)=="H" or str(chiffre)=="I" or str(chiffre)=="J"):
        continuer=True
    return(continuer)

def Bataille_Navale_Vérifier_entre_j(chiffre, N):
    continuer=False
    i=0
    while(i<=N-1 and not(continuer)):
        if(str(i)==str(chiffre)):
            continuer=True
        i=i+1
    return(continuer)

def Bataille_Navale_Str_en_nombre_i(chiffre, N):
    continuer=True
    if(str(chiffre)=="a" or str(chiffre)=="A"):
        nombre=0
    elif(str(chiffre)=="b" or str(chiffre)=="B"):
        nombre=1
    elif(str(chiffre)=="c" or str(chiffre)=="C"):
        nombre=2
    elif(str(chiffre)=="d" or str(chiffre)=="D"):
        nombre=3
    elif(str(chiffre)=="e" or str(chiffre)=="E"):
        nombre=4
    elif(str(chiffre)=="f" or str(chiffre)=="F"):
        nombre=5
    elif(str(chiffre)=="g" or str(chiffre)=="G"):
        nombre=6
    elif(str(chiffre)=="h" or str(chiffre)=="H"):
        nombre=7
    elif(str(chiffre)=="i" or str(chiffre)=="I"):
        nombre=8
    else:
        nombre=9
    return(nombre)

def Bataille_Navale_Str_en_nombre_j(chiffre, N):
    continuer=True
    i=0
    while(i<=N-1 and continuer):
        if(str(i)==str(chiffre)):
            continuer=False
            nombre=i
        i=i+1
    return(nombre)

def Bataille_Navale_Nom_Joueur():
    nom=input("Donnez votre nom : ")
    return(nom)

def Bataille_Navale_Valeur_k(B):
    longueur=len(B)
    k=0
    a=0
    while(a<longueur):
        P=B[a]
        longueur2=len(P)
        k=k+longueur2
        a=a+1
    return(k)

def Bataille_Navale_Bateau(N, G, Joueur):
    resultat=[]
    B=[]
    l=0
    k=0
    if(N==5):
        l=2
        if(Joueur!="Ordinateur"):
            print("\nVous avez "+str(l)+" bateaux.")
        i=1
        while(i<3):
            if(i==1):
                k=2
            else:
                k=3
            resultat=Bataille_Navale_Coordonnées_Bateau(k, i, N, Joueur, G)
            continuer=True
            if(B!=[]):
                a=0
                longueur=len(resultat)
                while(a<longueur and continuer):
                    b=0
                    longueur2=len(B)
                    while(b<longueur2 and continuer):
                        c=0
                        P=B[b]
                        longueur3=len(P)
                        while(c<longueur3 and continuer):
                            if(resultat[a]==P[c]):
                                continuer=False
                            c=c+1
                        b=b+1
                    a=a+1
            if(continuer):
                B.append(resultat)
                i=i+1
            else:
                if(Joueur!="Ordinateur"):
                    print("\nVous avez utilisé une même case pour rentrer votre bateau !!! Réessayez:\n")
    elif(N==6):
        l=3
        if(Joueur!="Ordinateur"):
            print("\nVous avez "+str(l)+" bateaux.")
        i=1
        while(i<4):
            if(i==1 or i==2):
                k=2
            else:
                k=3
            resultat=Bataille_Navale_Coordonnées_Bateau(k, i, N, Joueur, G)
            continuer=True
            if(B!=[]):
                a=0
                longueur=len(resultat)
                while(a<longueur and continuer):
                    b=0
                    longueur2=len(B)
                    while(b<longueur2 and continuer):
                        c=0
                        P=B[b]
                        longueur3=len(P)
                        while(c<longueur3 and continuer):
                            if(resultat[a]==P[c]):
                                continuer=False
                            c=c+1
                        b=b+1
                    a=a+1
            if(continuer):
                B.append(resultat)
                i=i+1
            else:
                if(Joueur!="Ordinateur"):
                    print("\nVous avez utilisé une même case pour rentrer votre bateau !!! Réessayez:\n")
    elif(N==7):
        l=3
        if(Joueur!="Ordinateur"):
            print("\nVous avez "+str(l)+" bateaux.")
        i=1
        while(i<4):
            if(i==1):
                k=2
            elif(i==2):
                k=3
            else:
                k=4
            resultat=Bataille_Navale_Coordonnées_Bateau(k, i, N, Joueur, G)
            continuer=True
            if(B!=[]):
                a=0
                longueur=len(resultat)
                while(a<longueur and continuer):
                    b=0
                    longueur2=len(B)
                    while(b<longueur2 and continuer):
                        c=0
                        P=B[b]
                        longueur3=len(P)
                        while(c<longueur3 and continuer):
                            if(resultat[a]==P[c]):
                                continuer=False
                            c=c+1
                        b=b+1
                    a=a+1
            if(continuer):
                B.append(resultat)
                i=i+1
            else:
                if(Joueur!="Ordinateur"):
                    print("\nVous avez utilisé une même case pour rentrer votre bateau !!! Réessayez:\n")
    elif(N==8):
        l=4
        if(Joueur!="Ordinateur"):
            print("\nVous avez "+str(l)+" bateaux.")
        i=1
        while(i<5):
            if(i==1):
                k=2
            elif(i==2 or i==3):
                k=3
            else:
                k=4
            resultat=Bataille_Navale_Coordonnées_Bateau(k, i, N, Joueur, G)
            continuer=True
            if(B!=[]):
                a=0
                longueur=len(resultat)
                while(a<longueur and continuer):
                    b=0
                    longueur2=len(B)
                    while(b<longueur2 and continuer):
                        c=0
                        P=B[b]
                        longueur3=len(P)
                        while(c<longueur3 and continuer):
                            if(resultat[a]==P[c]):
                                continuer=False
                            c=c+1
                        b=b+1
                    a=a+1
            if(continuer):
                B.append(resultat)
                i=i+1
            else:
                if(Joueur!="Ordinateur"):
                    print("\nVous avez utilisé une même case pour rentrer votre bateau !!! Réessayez:\n")
    elif(N==9):
        l=5
        if(Joueur!="Ordinateur"):
            print("\nVous avez "+str(l)+" bateaux.")
        i=1
        while(i<6):
            if(i==1):
                k=2
            elif(i==2 or i==3):
                k=3
            else:
                k=4
            resultat=Bataille_Navale_Coordonnées_Bateau(k, i, N, Joueur, G)
            continuer=True
            if(B!=[]):
                a=0
                longueur=len(resultat)
                while(a<longueur and continuer):
                    b=0
                    longueur2=len(B)
                    while(b<longueur2 and continuer):
                        c=0
                        P=B[b]
                        longueur3=len(P)
                        while(c<longueur3 and continuer):
                            if(resultat[a]==P[c]):
                                continuer=False
                            c=c+1
                        b=b+1
                    a=a+1
            if(continuer):
                B.append(resultat)
                i=i+1
            else:
                if(Joueur!="Ordinateur"):
                    print("\nVous avez utilisé une même case pour rentrer votre bateau !!! Réessayez:\n")
    else:
        l=5
        if(Joueur!="Ordinateur"):
            print("\nVous avez "+str(l)+" bateaux.")
        i=1
        while(i<6):
            if(i==1):
                k=2
            elif(i==2 or i==3):
                k=3
            elif(i==4):
                k=4
            else:
                k=5
            resultat=Bataille_Navale_Coordonnées_Bateau(k, i, N, Joueur, G)
            continuer=True
            if(B!=[]):
                a=0
                longueur=len(resultat)
                while(a<longueur and continuer):
                    b=0
                    longueur2=len(B)
                    while(b<longueur2 and continuer):
                        c=0
                        P=B[b]
                        longueur3=len(P)
                        while(c<longueur3 and continuer):
                            if(resultat[a]==P[c]):
                                continuer=False
                            c=c+1
                        b=b+1
                    a=a+1
            if(continuer):
                B.append(resultat)
                i=i+1
            else:
                if(Joueur!="Ordinateur"):
                    print("\nVous avez utilisé une même case pour rentrer votre bateau !!! Réessayez:\n")
    return(B)

def Bataille_Navale_Coordonnées_Bateau(k, i, N, Joueur, G):
    import random
    if(Joueur!="Ordinateur"):
        Bataille_Navale_Affiche_Grille(G)
        print("\nLa longueur du bateau n°"+str(i)+" est de "+str(k)+" cases.")
    continuer=True
    while(continuer):
        if(Joueur=="Ordinateur"):
            continuer2=True
            while(continuer2):
                i1=random.randint(0, N-1)
                j1=random.randint(0, N-1)
                VH=random.randint(1, 2)
                if(VH==1):
                    DG=random.randint(1, 2)
                    if(DG==1):
                        i2=i1+(k-1)
                        j2=j1
                    else:
                        i2=i1-(k+1)
                        j2=j1
                else:
                    HB=random.randint(1, 2)
                    if(HB==1):
                        j2=j1+(k-1)
                        i2=i1
                    else:
                        j2=j1-(k+1)
                        i2=i1
                if(i2<N and i2>=0 and j2<N and j2>=0):
                    continuer2=False
        else:
            print("\nCoordonnées de la première case :")
            i11=input("Ligne = ")
            j11=input("Colonne = ")
            print("\nCoordonnées de la dernière case :")
            i22=input("Ligne = ")
            j22=input("Colonne = ")
        if(Joueur=="Ordinateur" or (Bataille_Navale_Vérifier_entre_i(i11, N) and Bataille_Navale_Vérifier_entre_i(i22, N) and Bataille_Navale_Vérifier_entre_j(j11, N) and Bataille_Navale_Vérifier_entre_j(j22, N))):
            if(Joueur!="Ordinateur"):
                i1=Bataille_Navale_Str_en_nombre_i(i11, N)
                i2=Bataille_Navale_Str_en_nombre_i(i22, N)
                j1=Bataille_Navale_Str_en_nombre_j(j11, N)
                j2=Bataille_Navale_Str_en_nombre_j(j22, N)
            resultat=[]
            ligne=False
            colonne=False
            if(i1==i2 and (j2-j1==k-1 or j1-j2==k-1)):
                colonne=True
            elif(j1==j2 and (i2-i1==k-1 or i1-i2==k-1)):
                ligne=True
            if(ligne or colonne):
                continuer=False
            else:
                if(Joueur!="Ordinateur"):
                    print("\nVous n'avez pas rentré les bonnes coordonnées!\n")
            longueur=0
            while(longueur<k-1 and colonne and j2<=j1):
                if(longueur==0):
                    j=j2
                    resultat.append((i2, j2))
                j=j+1
                resultat.append((i1, j))
                longueur=longueur+1
                if(longueur==k-1):
                    boucle=False
            while(longueur<k-1 and colonne and j1<=j2):
                if(longueur==0):
                    j=j1
                    resultat.append((i1, j1))
                j=j+1
                resultat.append((i1, j))
                longueur=longueur+1
            while(longueur<k-1 and ligne and i2<=i1):
                if(longueur==0):
                    i=i2
                    resultat.append((i2, j2))
                i=i+1
                resultat.append((i, j1))
                longueur=longueur+1
                if(longueur==k-1):
                    boucle=False
            while(longueur<k-1 and ligne and i1<=i2):
                if(longueur==0):
                    i=i1
                    resultat.append((i1, j1))
                i=i+1
                resultat.append((i, j1))
                longueur=longueur+1
        else:
            if(Joueur!="Ordinateur"):
                print("\nVous n'avez pas rentré les bonnes coordonnées!\n")
    return(resultat)

def Bataille_Navale_Valeur_N():
    continuer=True
    N=0
    while(continuer):
        VN=input("\nEntrez le chiffre N pour un tableau NxN entre 5 et 10 :  ")
        i=5
        while(i<11):
            if(VN==str(i)):
                continuer=False
                N=i
            i=i+1
        if(continuer):
            print("Vous n'avez pas entré une bonne valeur ! Réessayez :")
    return(N)

def Bataille_Navale_Touche(i,j,B):
    continuer=True
    k=len(B)
    a=0
    while(a<k and continuer):
        P=B[a]
        b=len(P)
        arret=False
        p=0
        while(not (arret) and p<b):
            arret=(i==P[p][0] and j==P[p][1])
            p=p+1
        a=a+1
        if(arret):
            continuer=False
    return(arret)

def Bataille_Navale_Grille_Initiale(N):
    G=[]
    i=0
    while(i<N):
        j=0
        ligne=[]
        while(j<N):
            ligne.append(0)
            j=j+1
        G.append(ligne)
        i=i+1
    return(G)

def Bataille_Navale_Affiche_Grille(G):
    print("\n")
    N=len(G)
    i=0
    j=0
    ligne=" "
    while(j<N):
        ligne=ligne+"   "+str(j)
        j=j+1
    print(ligne)
    print(" ", " ---"*N)
    while(i<N):
        if(i==0):
            ii="A"
        elif(i==1):
            ii="B"
        elif(i==2):
            ii="C"
        elif(i==3):
            ii="D"
        elif(i==4):
            ii="E"
        elif(i==5):
            ii="F"
        elif(i==6):
            ii="G"
        elif(i==7):
            ii="H"
        elif(i==8):
            ii="I"
        else:
            ii="J"
        ligne=ii
        j=0
        while(j<N):
            case=G[i][j]
            x=""
            if(case==1):
                x="X"
            elif(case==-1):
                x="O"
            else:
                x="-"
            ligne=ligne+" | "+x
            j=j+1
        i=i+1
        print(ligne+" |")
        print(" ", " ---"*N)

def Bataille_Navale_Affiche_Grille2(G1, G2, J):
    print("\n")
    N=len(G1)
    i=0
    j=0
    ligne=" "
    while(j<N):
        ligne=ligne+"   "+str(j)
        j=j+1
    ligne=ligne+" "*33
    j=0
    while(j<N):
        ligne=ligne+"   "+str(j)
        j=j+1
    print(ligne)
    print(" ", " ---"*N, " "*31, " ---"*N)
    if(J==1):
        while(i<N):
            if(i==0):
                ii="A"
            elif(i==1):
                ii="B"
            elif(i==2):
                ii="C"
            elif(i==3):
                ii="D"
            elif(i==4):
                ii="E"
            elif(i==5):
                ii="F"
            elif(i==6):
                ii="G"
            elif(i==7):
                ii="H"
            elif(i==8):
                ii="I"
            else:
                ii="J"
            ligne=ii
            j=0
            while(j<N):
                case=G1[i][j]
                x=""
                if(case==1):
                    x="X"
                elif(case==-1):
                    x="O"
                else:
                    x="-"
                ligne=ligne+" | "+x
                j=j+1
            ligne=ligne+" |"
            ligne=ligne+" "*30+ii
            j=0
            while(j<N):
                case=G2[i][j]
                x=""
                if(case==1):
                    x="X"
                elif(case==-1):
                    x="O"
                else:
                    x="-"
                ligne=ligne+" | "+x
                j=j+1
            i=i+1
            print(ligne+" |")
            print(" ", " ---"*N, " "*31, " ---"*N)
    else:
        while(i<N):
            if(i==0):
                ii="A"
            elif(i==1):
                ii="B"
            elif(i==2):
                ii="C"
            elif(i==3):
                ii="D"
            elif(i==4):
                ii="E"
            elif(i==5):
                ii="F"
            elif(i==6):
                ii="G"
            elif(i==7):
                ii="H"
            elif(i==8):
                ii="I"
            else:
                ii="J"
            ligne=ii
            j=0
            while(j<N):
                case=G2[i][j]
                x=""
                if(case==1):
                    x="X"
                elif(case==-1):
                    x="O"
                else:
                    x="-"
                ligne=ligne+" | "+x
                j=j+1
            ligne=ligne+" |"
            ligne=ligne+" "*30+ii
            j=0
            while(j<N):
                case=G1[i][j]
                x=""
                if(case==1):
                    x="X"
                elif(case==-1):
                    x="O"
                else:
                    x="-"
                ligne=ligne+" | "+x
                j=j+1
            i=i+1
            print(ligne+" |")
            print(" ", " ---"*N, " "*31, " ---"*N)

def Bataille_Navale_Total(G):
    résultat=0
    N=len(G)
    i=0
    while(i<N):
        j=0
        while(j<N):
            if(G[i][j]==1):
                résultat=résultat+1
            j=j+1
        i=i+1
    return(résultat)

def Bataille_Navale_Efface():
    print("\n"*60)

def Bataille_Navale_Coule(i, j, B, G):
    continuer=True
    continuer2=False
    longueur=len(B)
    P=[]
    a=0
    while(a<longueur and continuer):
        P=B[a]
        longueur2=len(P)
        b=0
        while(b<longueur2 and continuer):
            if((i, j)==P[b]):
                continuer=False
            b=b+1
        a=a+1
    if(not (continuer)):
        continuer2=True
        b=0
        while(b<longueur2 and continuer2):
            (i, j)=P[b]
            if(G[i][j]==0):
                continuer2=False
            b=b+1
    if(continuer2):
        print("Coulé !!!")

def Bataille_Navale_Coup(G, N):
    continuer=True
    while(continuer):
        i1=input("\nDonnez les coordonnées de la case:\nLigne  = ")
        j1=input("Colonne  = ")
        if(Bataille_Navale_Vérifier_entre_i(i1, N) and Bataille_Navale_Vérifier_entre_j(j1, N)):
            i=Bataille_Navale_Str_en_nombre_i(i1, N)
            j=Bataille_Navale_Str_en_nombre_j(j1, N)
            Case=G[i][j]
            if(Case==0):
                continuer=False
            else:
                print("Case déjà jouée !!!")
        else:
            print("Entrez un nombre qui appartient au tableau s'il vous plait !!!")
    return(i, j)

def Bataille_Navale_Coup_Ordinateur(G, N, B):
    import random
    import time
    continuer=True
    while(continuer):
        continuer2=True
        longueur=len(B)
        a=0
        while(a<longueur and continuer2):
            resultat=[]
            P=B[a]
            longueur2=len(P)
            b=0
            while(b<longueur2):
                (i, j)=P[b]
                if(G[i][j]==1):
                    resultat.append((i, j))
                b=b+1
            if(len(resultat)!=0 and len(resultat)!=longueur2):
                continuer2=False
            a=a+1
        if(continuer2):
            cont=True
            while(cont):
                compte1=[]
                compte2=[]
                compte3=[]
                i=0
                while(i<N):
                    compte=0
                    j=0
                    while(j<N):
                        if(G[i][j]!=0):
                            compte=compte+1
                        j=j+1
                    if(compte==0):
                        compte1.append(i)
                    elif(compte<(N//2)):
                        compte2.append(i)
                    elif(compte<(N//2)+(N//4)):
                        compte3.append(i)
                    i=i+1
                longueur1=len(compte1)
                longueur2=len(compte2)
                longueur3=len(compte3)
                if(longueur1!=0):
                    rand=random.randint(0, longueur1-1)
                    i1=compte1[rand]
                elif(longueur2!=0):
                    rand=random.randint(0, longueur2-1)
                    i1=compte2[rand]
                elif(longueur3!=0):
                    rand=random.randint(0, longueur3-1)
                    i1=compte3[rand]
                else:
                    i1=random.randint(0, N-1)
                compte1=[]
                compte2=[]
                compte3=[]
                j=0
                while(j<N):
                    compte=0
                    i=0
                    while(i<N):
                        if(G[i][j]!=0):
                            compte=compte+1
                        i=i+1
                    if(compte==0):
                        compte1.append(j)
                    elif(compte<(N//2)):
                        compte2.append(j)
                    elif(compte<(N//2)+(N//4)):
                        compte3.append(j)
                    j=j+1
                longueur1=len(compte1)
                longueur2=len(compte2)
                longueur3=len(compte3)
                if(longueur1!=0):
                    rand=random.randint(0, longueur1-1)
                    j1=compte1[rand]
                elif(longueur2!=0):
                    rand=random.randint(0, longueur2-1)
                    j1=compte2[rand]
                elif(longueur3!=0):
                    rand=random.randint(0, longueur3-1)
                    j1=compte3[rand]
                else:
                    j1=random.randint(0, N-1)
                i=i1
                j=j1
                if(G[i][j]==0):
                    continuer=False
                cote=False
                i1=i-1
                i2=i+1
                j1=j-1
                j2=j+1
                if(i1<N and i1>=0):
                    if(G[i1][j]!=0):
                        cote=True
                if(i2<N and i2>=0):
                    if(G[i2][j]!=0):
                        cote=True
                if(j1<N and j1>=0):
                    if(G[i][j1]!=0):
                        cote=True
                if(j2<N and j2>=0):
                    if(G[i][j2]!=0):
                        cote=True
                if(cote):
                    rand=random.randint(0, 1)
                    if(rand==1):
                        cont=False
                else:
                    cont=False
        elif(len(resultat)==1):
            (i, j)=resultat[0]
            rand=random.randint(0, 3)
            if(rand==0 and i==N-1):
                rand=1
            elif(rand==1 and i==0):
                rand=0
            elif(rand==2 and j==N-1):
                rand=3
            elif(rand==3 and j==0):
                rand=2
            if(rand==0):
                i=i+1
            elif(rand==1):
                i=i-1
            elif(rand==2):
                j=j+1
            elif(rand==3):
                j=j-1
            Case=G[i][j]
            if(Case==0):
                continuer=False
        elif(len(resultat)>1):
            (i1, j1)=resultat[0]
            (i2, j2)=resultat[1]
            if(i1==i2):
                rand=random.randint(0, 1)
                i=i1
                longueur=len(resultat)
                rand1=random.randint(0, longueur-1)
                (i3, j3)=resultat[rand1]
                if(rand==0 or j1==0):
                    j=j3+1
                elif(rand==1 or j3==N-1):
                    j=j3-1
            else:
                rand=random.randint(0, 1)
                j=j1
                longueur=len(resultat)
                rand1=random.randint(0, longueur-1)
                (i3, j3)=resultat[rand1]
                if(rand==0 or i1==0):
                    i=i3+1
                elif(rand==1 or i3==N-1):
                    i=i3-1
            Case=G[i][j]
            if(Case==0):
                continuer=False
    if(i==0):
        ii="A"
    elif(i==1):
        ii="B"
    elif(i==2):
        ii="C"
    elif(i==3):
        ii="D"
    elif(i==4):
        ii="E"
    elif(i==5):
        ii="F"
    elif(i==6):
        ii="G"
    elif(i==7):
        ii="H"
    elif(i==8):
        ii="I"
    else:
        ii="J"
    print("\nDonnez les coordonnées de la case:")
    time.sleep(2.0)
    print("Ligne = "+ii)
    time.sleep(2.0)
    print("Colonne = "+str(j))
    return(i, j)

def Plus_Moins():
    import random
    import time
    Plus_Moins_Efface()
    garder_nom=True
    rejouer=True
    while(rejouer):
        if(garder_nom):
            cont=True
            while(cont):
                NJoueur=input("\nChoisissez un nombre de joueurs entre 1 et 10 : ")
                i=1
                while(i<11):
                    if(NJoueur==str(i)):
                        cont=False
                        Joueur=i
                    i=i+1
                if(cont==True):
                    Plus_Moins_Faux(1, 10)
            cont=True
            while(cont):
                a=True
                NMax=input("\nChoisissez un niveau de difficuté :\n\n1 - Entre 0 et 100\n2 - Entre 0 et 1000\n3 - Entre 0 et 10000\n4 - Entre 0 et 100000\n\nDifficulté = ")
                i=1
                while(i<5):
                    if(NMax==str(i)):
                        cont=False
                        Max=i
                        if(Max==1):
                            Max=100
                        elif(Max==2):
                            Max=1000
                        elif(Max==3):
                            Max=10000
                        else:
                            Max=100000
                    i=i+1
                if(cont==True):
                    Plus_Moins_Faux(1, 4)
            Joueurs=[]
            i=1
            while(i<=Joueur):
                print("\nJoueur "+str(i)+" : ")
                Joueurs.append(Plus_Moins_Nom_Joueur())
                i=i+1
        i=0
        Gagner=[]
        while(i<Joueur):
            jouer=True
            Plus_Moins_Efface()
            print("A votre tour, "+Joueurs[i]+" :")
            rand=random.randint(0, Max)
            n=0
            while(jouer):
                print("\n"*2)
                chiffre=Plus_Moins_Entrer(0, Max)
                jouer=Plus_Moins_Fin(rand, chiffre)
                n=n+1
            print("\nVous avez mis "+str(n)+" coups !!!")
            time.sleep(5.0)
            Gagner.append(n)
            i=i+1
        if(Joueur!=1):
            Plus_Moins_Efface()
            i=0
            J=Gagner[0]
            JoueurG=[]
            while(i<Joueur):
                if(J>Gagner[i]):
                    J=Gagner[i]
                i=i+1
            i=0
            while(i<Joueur):
                if(Gagner[i]==J):
                    JoueurG.append(Joueurs[i])
                i=i+1
            if(len(JoueurG)==1):
                print("\nBravo "+JoueurG[0]+" vous avez gagné !!!")
            else:
                longueur=len(JoueurG)
                i=0
                ligne=""
                while(i<longueur):
                    if(i==0):
                        ligne=ligne+Joueurs[i]
                    else:
                        ligne=ligne+" et "+Joueurs[i]
                    i=i+1
                print("\nBravo "+ligne+" !!! Vous êtes ex-aequo !!!")
        recommencer=input("\n\nVoulez-vous rejouer? Entrez Oui ou Non : ")
        recommencer=recommencer.upper()
        if(recommencer=="NON"):
            rejouer=False
        changer="Oui"
        if(rejouer):
            changer=input("\nVoulez-vous changer les noms? Entrez Oui ou Non : ")
        changer=changer.upper()
        if(changer=="NON"):
            garder_nom=False
        else:
            garder_nom=True

def Plus_Moins_Efface():
    print("\n"*60)

def Plus_Moins_Nom_Joueur():
    nom=input("Donnez votre nom : ")
    return(nom)

def Plus_Moins_Faux(a, b):
    print("\nVeillez à rentrer un nombre entre "+str(a)+" et "+str(b)+" s'il vous plait !!!")

def Plus_Moins_Entrer(a, b):
    continuer=True
    while(continuer):
        nombre=input("\nDevinez le chiffre entre "+str(a)+" et "+str(b)+" : ")
        i=a
        while(i<=b):
            if(nombre==str(i)):
                continuer=False
                resultat=i
            i=i+1
        if(continuer):
            Plus_Moins_Faux(a, b)
    return(resultat)

def Plus_Moins_Fin(rand, chiffre):
    if(chiffre>rand):
        print("\nTrop grand !!!")
        jouer=True
    elif(chiffre<rand):
        print("\nTrop petit !!!")
        jouer=True
    else:
        print("\nBravo !!!")
        jouer=False
    return(jouer)

def Sudoku():
    Sudoku_Efface()
    rejouer=True
    while(rejouer):
        G=Sudoku_Grille_Initiale()
        Liste_Vide=Sudoku_Liste_Vide()
        G1=Grille_Initiale_Joueur(G, Liste_Vide)
        G2=Grille_Initiale_Joueur(G, Liste_Vide)
        continuer=True
        while(continuer):
            Sudoku_Efface()
            Sudoku_Affiche_Grille(G2)
            Verifier=input("\nVoulez-vous vérifier la grille ? (Entrez n'importe quoi si vous voulez vérifier, sinon pressez juste Entrer) ...  ")
            if(Verifier!=""):
                Liste_Faux=Sudoku_Verifier(G1, G2)
                longueur=len(Liste_Faux)
                if(longueur==0):
                    print("\nVous avez tout juste !!!")
                else:
                    print("\nVoici la liste de cases fausses :")
                    ligne=""
                    i=0
                    while(i<longueur):
                        if(i==0):
                            ligne=ligne+str(Liste_Faux[i])
                        else:
                            ligne=ligne+", "+str(Liste_Faux[i])
                        i=i+1
                    print(ligne)
            G2=Sudoku_Coup(G1, G2)
            continuer=not(Sudoku_Gagner(G1, G2))
            if(not(continuer)):
                print("\nBravo vous avez résolu le Sudoku !!!")
                jouer=input("\n Voulez-vous rejouer ? (Entrez Oui ou Non)\n\nRejouer = ")
                jouer=jouer.upper()
                if(jouer=="NON"):
                    rejouer=False

def Sudoku_Efface():
    print("\n"*60)

def Sudoku_Vérifier_entre_ij(chiffre):
    continuer=False
    chiffre1=str(chiffre)
    chiffre1=chiffre1.upper()
    if(chiffre1=="A" or chiffre1=="B" or chiffre1=="C" or chiffre1=="D" or chiffre1=="E" or chiffre1=="F" or chiffre1=="G" or chiffre1=="H" or chiffre1=="I"):
        continuer=True
    return(continuer)

def Sudoku_Str_en_nombre_ij(chiffre):
    continuer=True
    chiffre1=str(chiffre)
    chiffre1=chiffre1.upper()
    if(chiffre1=="A"):
        nombre=0
    elif(chiffre1=="B"):
        nombre=1
    elif(chiffre1=="C"):
        nombre=2
    elif(chiffre1=="D"):
        nombre=3
    elif(chiffre1=="E"):
        nombre=4
    elif(chiffre1=="F"):
        nombre=5
    elif(chiffre1=="G"):
        nombre=6
    elif(chiffre1=="H"):
        nombre=7
    else:
        nombre=8
    return(nombre)

def Sudoku_Vérifier_entre_chiffre(chiffre):
    continuer=False
    i=1
    while(i<10 and not(continuer)):
        if(str(i)==str(chiffre)):
            continuer=True
        i=i+1
    return(continuer)

def Sudoku_Str_en_nombre_chiffre(chiffre):
    continuer=True
    i=1
    while(i<10 and continuer):
        if(str(i)==str(chiffre)):
            continuer=False
            nombre=i
        i=i+1
    return(nombre)

def Sudoku_Coup(G1, G2):
    continuer=True
    while(continuer):
        i1=input("\nDonnez les coordonnées de la case:\nLigne  = ")
        j1=input("Colonne  = ")
        chiffre1=input("Donnez le chiffre à mettre dans cette case : ")
        if(Sudoku_Vérifier_entre_ij(i1) and Sudoku_Vérifier_entre_ij(j1) and Sudoku_Vérifier_entre_chiffre(chiffre1)):
            i=Sudoku_Str_en_nombre_ij(i1)
            j=Sudoku_Str_en_nombre_ij(j1)
            chiffre=Sudoku_Str_en_nombre_chiffre(chiffre1)
            Case=G1[i][j]
            if(Case=="-"):
                continuer=False
                G2[i][j]=chiffre
            else:
                print("\nC'est une case de la grille initiale !!!")
        else:
            print("\nEntrez des coordonnées et un nombre qui appartiennent au tableau s'il vous plait !!!")
    return(G2)

def Sudoku_Grille_Initiale():
    import random
    Lignes=[]
    Lignes.append(["d", "a", "e", "f", "c", "h", "i", "g", "b"])
    Lignes.append(["c", "f", "b", "d", "g", "i", "a", "h", "e"])
    Lignes.append(["g", "h", "i", "b", "a", "e", "c", "f", "d"])
    Lignes.append(["i", "b", "f", "c", "d", "a", "g", "e", "h"])
    Lignes.append(["a", "c", "h", "g", "e", "f", "d", "b", "i"])
    Lignes.append(["e", "g", "d", "i", "h", "b", "f", "c", "a"])
    Lignes.append(["b", "e", "g", "a", "f", "d", "h", "i", "c"])
    Lignes.append(["h", "d", "c", "e", "i", "g", "b", "a", "f"])
    Lignes.append(["f", "i", "a", "h", "b", "c", "e", "d", "g"])
    rand=0
    while(rand==0):
        rand=random.randint(0, 120)
        rand=rand%6
    i=0
    while(i<rand):
        Lignes=Sudoku_Echange_Rangs(Lignes)
        Colonnes=Sudoku_Colonnes(Lignes)
        Colonnes=Sudoku_Echange_Rangs(Colonnes)
        Lignes=Sudoku_Colonnes_Lignes(Colonnes)
        Lignes=Sudoku_Echange_Secteurs(Lignes)
        Colonnes=Sudoku_Colonnes(Lignes)
        Colonnes=Sudoku_Echange_Secteurs(Colonnes)
        Lignes=Sudoku_Colonnes_Lignes(Colonnes)
        rand1=0
        while(rand1==0):
            rand1=random.randint(0, 120)
            rand1=rand1%6
        k=0
        while(k<rand1):
            Lignes=Rotation_tableau(Lignes)
            k=k+1
        i=i+1
    Lignes=Sudoku_Change(Lignes)
    return(Lignes)

def Grille_Initiale_Joueur(G, Liste_Vide):
    G1=[]
    i=0
    while(i<9):
        j=0
        ligne=[]
        while(j<9):
            ligne.append(0)
            j=j+1
        G1.append(ligne)
        i=i+1
    i=0
    while(i<9):
        j=0
        while(j<9):
            continuer=True
            k=0
            while(k<len(Liste_Vide) and continuer):
                if((i, j)==Liste_Vide[k]):
                    continuer=False
                k=k+1
            if(not(continuer)):
                G1[i][j]="-"
            else:
                G1[i][j]=G[i][j]
            j=j+1
        i=i+1
    return(G1)

def Sudoku_Liste_Vide():
    import random
    continuer=True
    while(continuer):
        Vide1=input("\nCombien voulez-vous de cases vides ? (Entre 30 et 60)\n\nVides = ")
        i=30
        while(i<61 and continuer):
            if(str(i)==Vide1):
                Vide=i
                continuer=False
            i=i+1
        if(continuer):
            print("\nEntrez une valeur entre 30 et 60 s'il vous plait !!!")
    Case=[]
    i=0
    while(i<9):
        j=0
        while(j<9):
            Case.append((i, j))
            j=j+1
        i=i+1
    Liste_Vide=[]
    i=0
    while(i<Vide):
        longueur=len(Case)
        rand=random.randint(0, 1000)
        rand=rand%longueur
        Liste_Vide.append(Case[rand])
        Case[rand]="0"
        Case.remove("0")
        i=i+1
    return(Liste_Vide)

def Sudoku_Colonnes_Lignes(Colonnes):
    Lignes=[]
    i=0
    while(i<9):
        j=0
        Ligne=[]
        while(j<9):
            Ligne.append(Colonnes[j][i])
            j=j+1
        Lignes.append(Ligne)
        i=i+1
    return(Lignes)

def Sudoku_Echange_Secteurs(Listes):
    import random
    Listes2=[]
    Liste1=[]
    Liste2=[]
    Liste3=[]
    Liste1.append(Listes[0])
    Liste1.append(Listes[1])
    Liste1.append(Listes[2])
    Liste2.append(Listes[3])
    Liste2.append(Listes[4])
    Liste2.append(Listes[5])
    Liste3.append(Listes[6])
    Liste3.append(Listes[7])
    Liste3.append(Listes[8])
    rand=random.randint(0, 120)
    rand=rand%6
    if(rand==0):
        Listes2.extend(Liste3)
        Listes2.extend(Liste1)
        Listes2.extend(Liste2)
    elif(rand==1):
        Listes2.extend(Liste2)
        Listes2.extend(Liste3)
        Listes2.extend(Liste1)
    elif(rand==2):
        Listes2.extend(Liste3)
        Listes2.extend(Liste2)
        Listes2.extend(Liste1)
    elif(rand==3):
        Listes2.extend(Liste1)
        Listes2.extend(Liste3)
        Listes2.extend(Liste2)
    elif(rand==4):
        Listes2.extend(Liste2)
        Listes2.extend(Liste1)
        Listes2.extend(Liste3)
    else:
        Listes2.extend(Liste1)
        Listes2.extend(Liste2)
        Listes2.extend(Liste3)
    return(Listes2)

def Sudoku_Echange_Rangs(Listes):
    import random
    i=0
    while(i<7):
        Liste1=Listes[i]
        Liste2=Listes[i+1]
        Liste3=Listes[i+2]
        rand=random.randint(0, 120)
        rand=rand%6
        if(rand==0):
            Listes[i]=Liste3
            Listes[i+1]=Liste1
            Listes[i+2]=Liste2
        elif(rand==1):
            Listes[i]=Liste2
            Listes[i+1]=Liste3
            Listes[i+2]=Liste1
        elif(rand==2):
            Listes[i]=Liste3
            Listes[i+1]=Liste2
            Listes[i+2]=Liste1
        elif(rand==3):
            Listes[i]=Liste1
            Listes[i+1]=Liste3
            Listes[i+2]=Liste2
        elif(rand==4):
            Listes[i]=Liste2
            Listes[i+1]=Liste1
            Listes[i+2]=Liste3
        else:
            Listes[i]=Liste1
            Listes[i+1]=Liste2
            Listes[i+2]=Liste3
        i=i+3
    return(Listes)

def Sudoku_Colonnes(Lignes):
    G=[]
    i=0
    while(i<9):
        j=0
        while(j<9):
            G.append(Lignes[i][j])
            j=j+1
        i=i+1
    Colonnes=[]
    i=0
    while(i<9):
        Colonne=[]
        j=i
        while(j<81):
            Colonne.append(G[j])
            j=j+9
        Colonnes.append(Colonne)
        i=i+1
    return(Colonnes)

def Rotation_tableau(Lignes):
    Colonnes=Sudoku_Colonnes(Lignes)
    Listes=[]
    i=0
    while(i<9):
        j=8
        Ligne=[]
        while(j>=0):
            Ligne.append(Colonnes[i][j])
            j=j-1
        Listes.append(Ligne)
        i=i+1
    return(Listes)

def Sudoku_Change(Lignes):
    import random
    chiffre=[]
    Liste=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    while(len(Liste)!=0):
        longueur=len(Liste)
        rand=random.randint(0, 120)
        rand=rand%longueur
        rand1=Liste[rand]
        chiffre.append(rand1)
        Liste[rand]=0
        Liste.remove(0)
    i=0
    while(i<9):
        j=0
        while(j<9):
            if(Lignes[i][j]=="a"):
                Lignes[i][j]=chiffre[8]
            if(Lignes[i][j]=="b"):
                Lignes[i][j]=chiffre[7]
            if(Lignes[i][j]=="c"):
                Lignes[i][j]=chiffre[6]
            if(Lignes[i][j]=="d"):
                Lignes[i][j]=chiffre[5]
            if(Lignes[i][j]=="e"):
                Lignes[i][j]=chiffre[4]
            if(Lignes[i][j]=="f"):
                Lignes[i][j]=chiffre[3]
            if(Lignes[i][j]=="g"):
                Lignes[i][j]=chiffre[2]
            if(Lignes[i][j]=="h"):
                Lignes[i][j]=chiffre[1]
            if(Lignes[i][j]=="i"):
                Lignes[i][j]=chiffre[0]
            j=j+1
        i=i+1
    return(Lignes)

def Sudoku_Affiche_Grille(G):
    print("\n")
    Liste=["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    N=len(G)
    i=0
    j=0
    ligne="   "
    while(j<N):
        ligne=ligne+"   "+str(Liste[j])
        if(j==2 or j==5):
            ligne=ligne+"  "
        j=j+1
    print(ligne)
    print("  ", "-"*43)
    print(" ", "| ", ("---"+" ---"*2+" "), (" ---"*3+" "), (" ---"*3), " |")
    while(i<N):
        ligne=str(Liste[i])+" | "
        j=0
        while(j<N):
            x=str(G[i][j])
            ligne=ligne+"| "+x+" "
            if(j==2 or j==5):
                ligne=ligne+"| "
            j=j+1
        i=i+1
        print(ligne+"|", "|")
        print(" ", "| ", ("---"+" ---"*2+" "), (" ---"*3+" "), (" ---"*3), " |")
        if(i==3 or i==6):
            print(" ", "| ", ("---"+" ---"*2+" "), (" ---"*3+" "), (" ---"*3), " |")
    print("  ", "-"*43)

def Sudoku_Cases(G):
    Cases=[]
    i=0
    while(i<9):
        Case=[]
        if(i<3):
            a=0
            j=a
        elif(i>6):
            a=6
            j=a
        else:
            a=3
            j=a
        while(j<a+3):
            Ligne=G[j]
            if(i==0 or i==3 or i==6):
                b=0
                k=b
            elif(i==1 or i==4 or i==7):
                b=3
                k=b
            else:
                b=6
                k=b
            while(k<b+3):
                Case.append(Ligne[k])
                k=k+1
            j=j+1
        Cases.append(Case)
        i=i+1
    return(Cases)

def Sudoku_Verifier(G1, G2):
    Colonnes=Sudoku_Colonnes(G2)
    Cases=Sudoku_Cases(G2)
    Liste1=[]
    Liste2=[]
    Liste3=[]
    i=1
    while(i<10):
        j=0
        while(j<9):
            k=0
            compte=[]
            while(k<9):
                if(i==G2[j][k]):
                    compte.append((j, k))
                k=k+1
            longueur=len(compte)
            if(longueur>1):
                k=0
                while(k<longueur):
                    (a, b)=compte[k]
                    if(((a,b) in Liste1) or G1[a][b]!="-"):
                        compte[k]=(100, 100)
                        compte.remove((100, 100))
                    k=k+1
                    longueur=len(compte)
            else:
                compte=[]
            Liste1.extend(compte)
            j=j+1
        i=i+1
    i=1
    while(i<10):
        j=0
        while(j<9):
            k=0
            compte=[]
            while(k<9):
                if(i==Colonnes[j][k]):
                    compte.append((k, j))
                k=k+1
            longueur=len(compte)
            if(longueur>1):
                k=0
                while(k<longueur):
                    (a, b)=compte[k]
                    if(((a,b) in Liste2) or G1[a][b]!="-"):
                        compte[k]=(100, 100)
                        compte.remove((100, 100))
                    k=k+1
                    longueur=len(compte)
            else:
                compte=[]
            Liste2.extend(compte)
            j=j+1
        i=i+1
    i=1
    while(i<10):
        j=0
        while(j<9):
            k=0
            compte=[]
            while(k<9):
                if(i==Cases[j][k]):
                    if(j==0):
                        if(k==0):
                            a=0
                            b=0
                        elif(k==1):
                            a=0
                            b=1
                        elif(k==2):
                            a=0
                            b=2
                        elif(k==3):
                            a=1
                            b=0
                        elif(k==4):
                            a=1
                            b=1
                        elif(k==5):
                            a=1
                            b=2
                        elif(k==6):
                            a=2
                            b=0
                        elif(k==7):
                            a=2
                            b=1
                        else:
                            a=2
                            b=2
                    elif(j==1):
                        if(k==0):
                            a=0
                            b=3
                        elif(k==1):
                            a=0
                            b=4
                        elif(k==2):
                            a=0
                            b=5
                        elif(k==3):
                            a=1
                            b=3
                        elif(k==4):
                            a=1
                            b=4
                        elif(k==5):
                            a=1
                            b=5
                        elif(k==6):
                            a=2
                            b=3
                        elif(k==7):
                            a=2
                            b=4
                        else:
                            a=2
                            b=5
                    elif(j==2):
                        if(k==0):
                            a=0
                            b=6
                        elif(k==1):
                            a=0
                            b=7
                        elif(k==2):
                            a=0
                            b=8
                        elif(k==3):
                            a=1
                            b=6
                        elif(k==4):
                            a=1
                            b=7
                        elif(k==5):
                            a=1
                            b=8
                        elif(k==6):
                            a=2
                            b=6
                        elif(k==7):
                            a=2
                            b=7
                        else:
                            a=2
                            b=8
                    elif(j==3):
                        if(k==0):
                            a=3
                            b=0
                        elif(k==1):
                            a=3
                            b=1
                        elif(k==2):
                            a=3
                            b=2
                        elif(k==3):
                            a=4
                            b=0
                        elif(k==4):
                            a=4
                            b=1
                        elif(k==5):
                            a=4
                            b=2
                        elif(k==6):
                            a=5
                            b=0
                        elif(k==7):
                            a=5
                            b=1
                        else:
                            a=5
                            b=2
                    elif(j==4):
                        if(k==0):
                            a=3
                            b=3
                        elif(k==1):
                            a=3
                            b=4
                        elif(k==2):
                            a=3
                            b=5
                        elif(k==3):
                            a=4
                            b=3
                        elif(k==4):
                            a=4
                            b=4
                        elif(k==5):
                            a=4
                            b=5
                        elif(k==6):
                            a=5
                            b=3
                        elif(k==7):
                            a=5
                            b=4
                        else:
                            a=5
                            b=5
                    elif(j==5):
                        if(k==0):
                            a=3
                            b=6
                        elif(k==1):
                            a=3
                            b=7
                        elif(k==2):
                            a=3
                            b=8
                        elif(k==3):
                            a=4
                            b=6
                        elif(k==4):
                            a=4
                            b=7
                        elif(k==5):
                            a=4
                            b=8
                        elif(k==6):
                            a=5
                            b=6
                        elif(k==7):
                            a=5
                            b=7
                        else:
                            a=5
                            b=8
                    elif(j==6):
                        if(k==0):
                            a=6
                            b=0
                        elif(k==1):
                            a=6
                            b=1
                        elif(k==2):
                            a=6
                            b=2
                        elif(k==3):
                            a=7
                            b=0
                        elif(k==4):
                            a=7
                            b=1
                        elif(k==5):
                            a=7
                            b=2
                        elif(k==6):
                            a=8
                            b=0
                        elif(k==7):
                            a=8
                            b=1
                        else:
                            a=8
                            b=2
                    elif(j==7):
                        if(k==0):
                            a=6
                            b=3
                        elif(k==1):
                            a=6
                            b=4
                        elif(k==2):
                            a=6
                            b=5
                        elif(k==3):
                            a=7
                            b=3
                        elif(k==4):
                            a=7
                            b=4
                        elif(k==5):
                            a=7
                            b=5
                        elif(k==6):
                            a=8
                            b=3
                        elif(k==7):
                            a=8
                            b=4
                        else:
                            a=8
                            b=5
                    else:
                        if(k==0):
                            a=6
                            b=6
                        elif(k==1):
                            a=6
                            b=7
                        elif(k==2):
                            a=6
                            b=8
                        elif(k==3):
                            a=7
                            b=6
                        elif(k==4):
                            a=7
                            b=7
                        elif(k==5):
                            a=7
                            b=8
                        elif(k==6):
                            a=8
                            b=6
                        elif(k==7):
                            a=8
                            b=7
                        else:
                            a=8
                            b=8
                    compte.append((a, b))
                k=k+1
            longueur=len(compte)
            if(longueur>1):
                k=0
                while(k<longueur):
                    (a, b)=compte[k]
                    if(((a,b) in Liste3) or G1[a][b]!="-"):
                        compte[k]=(100, 100)
                        compte.remove((100, 100))
                    k=k+1
                    longueur=len(compte)
            else:
                compte=[]
            Liste3.extend(compte)
            j=j+1
        i=i+1
    Liste=[]
    Liste.extend(Liste1)
    i=0
    while(i<len(Liste2)):
        if(not(Liste2[i] in Liste)):
            Liste.append(Liste2[i])
        i=i+1
    i=0
    while(i<len(Liste3)):
        if(not(Liste3[i] in Liste)):
            Liste.append(Liste3[i])
        i=i+1
    Liste_Faux=[]
    longueur=len(Liste)
    i=0
    while(i<longueur):
        (a, b)=Liste[i]
        if(a==0):
            A="A"
        elif(a==1):
            A="B"
        elif(a==2):
            A="C"
        elif(a==3):
            A="D"
        elif(a==4):
            A="E"
        elif(a==5):
            A="F"
        elif(a==6):
            A="G"
        elif(a==7):
            A="H"
        else:
            A="I"
        if(b==0):
            B="A"
        elif(b==1):
            B="B"
        elif(b==2):
            B="C"
        elif(b==3):
            B="D"
        elif(b==4):
            B="E"
        elif(b==5):
            B="F"
        elif(b==6):
            B="G"
        elif(b==7):
            B="H"
        else:
            B="I"
        Liste_Faux.append((A, B))
        i=i+1
    return(Liste_Faux)

def Sudoku_Gagner(G1, G2):
    gagner=False
    continuer=True
    i=0
    while(i<9 and continuer):
        j=0
        while(j<9 and continuer):
            if(G2[i][j]=="-"):
                continuer=False
            j=j+1
        i=i+1
    if(continuer and len(Sudoku_Verifier(G1, G2))==0):
        gagner=True
    return(gagner)

def MasterMind():
    MasterMind_Efface()
    import time
    garder_nom=True
    rejouer=True
    while(rejouer):
        Comptes=[]
        if(garder_nom):
            continuer=True
            while(continuer):
                try:
                    N=int(input("\nDonnez un nombre de joueur entre 1 et 10 : "))
                    if(N>0 and N<11):
                        continuer=False
                    else:
                        print("\nEntrez un nombre entre 1 et 10 s'il vous plait!!!")
                except:
                    print("\nEntrez un nombre entre 1 et 10 s'il vous plait!!!")
            Noms=MasterMind_Nom_Joueurs(N)
        L=MasterMind_Difficulte()
        Alphabet=MasterMind_Alpha(L)
        i=0
        while(i<N):
            MasterMind_Efface()
            print("\nA votre tour "+Noms[i]+" :")
            continuer=True
            compte=0
            Coups=[]
            Suite_Deplacements=[]
            Suite_Lettres=[]
            Suite=MasterMind_Suite_Initiale(L, Alphabet)
            while(continuer):
                Coup=MasterMind_Coup_Joueur(L, Alphabet)
                L_Faux=MasterMind_Lettre_Faux(Coup, Suite)
                P_Faux=MasterMind_Placement_Faux(Coup, Suite)
                Coups.append(Coup)
                Suite_Deplacements.append(P_Faux)
                Suite_Lettres.append(L_Faux)
                MasterMind_Afficher(Coups, Suite_Deplacements, Suite_Lettres)
                compte=compte+1
                continuer=MasterMind_Fin(Suite, Coup, compte)
            Comptes.append(compte)
            i=i+1
            time.sleep(5.0)
        if(N!=1):
            MasterMind_Efface()
            i=0
            J=Comptes[0]
            JoueurG=[]
            while(i<N):
                if(J>Comptes[i]):
                    J=Comptes[i]
                i=i+1
            i=0
            while(i<N):
                if(Comptes[i]==J):
                    JoueurG.append(Noms[i])
                i=i+1
            if(len(JoueurG)==1):
                print("\nBravo "+JoueurG[0]+" vous avez gagné !!!")
            else:
                longueur=len(JoueurG)
                i=0
                ligne=""
                while(i<longueur):
                    if(i==0):
                        ligne=ligne+Noms[i]
                    else:
                        ligne=ligne+" et "+Noms[i]
                    i=i+1
                print("\nBravo "+ligne+" !!! Vous êtes ex-aequo !!!")
        recommencer=input("\n\nVoulez-vous rejouer? Entrez Oui ou Non : ")
        recommencer=recommencer.upper()
        if(recommencer=="NON"):
            rejouer=False
        changer="Oui"
        if(rejouer):
            changer=input("\nVoulez-vous changer les noms? Entrez Oui ou Non : ")
        changer=changer.upper()
        if(changer=="NON"):
            garder_nom=False
        else:
            garder_nom=True

def MasterMind_Nom_Joueurs(N):
    Noms=[]
    i=1
    while(i<=N):
        nom=input("\nJoueur "+str(i)+", donnez votre nom : ")
        Noms.append(nom)
        i=i+1
    return(Noms)

def MasterMind_Efface():
    print("\n"*60)

def MasterMind_Alpha(L):
    Alphabet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    while(len(Alphabet)>L):
        Alphabet[L]=0
        Alphabet.remove(0)
    return(Alphabet)

def MasterMind_Difficulte():
    continuer=True
    while(continuer):
        try:
            L=int(input("\nChoisissez votre niveau de difficulté entre 6 et 26 : "))
            if(L>5 and L<27):
                continuer=False
            else:
                print("Entrez un nombre entre 1 et 26 s'il vous plait !!!")
        except:
            print("Entrez un nombre entre 1 et 26 s'il vous plait !!!")
    return(L)

def MasterMind_Coup_Joueur(L, Alphabet):
    longueur=len(Alphabet)
    Lettre=Alphabet[longueur-1]
    print("\nEntrez votre suite de 4 lettres entre A et "+str(Lettre)+" :\n")
    Coup=[]
    i=1
    while(i<5):
        continuer=True
        while(continuer):
            Coup1=input("Entrez la lettre n°"+str(i)+" : ")
            Coup1=Coup1.upper()
            if(Coup1 in Alphabet):
                continuer=False
                Coup.append(Coup1)
            else:
                print("Entrez une lettre entre A et "+str(Lettre)+" s'il vous plait !!!")
        i=i+1
    return(Coup)

def MasterMind_Suite_Initiale(L, Alphabet):
    import random
    Suite=[]
    i=0
    while(i<4):
        rand1=random.randint(0, 120)
        rand1=rand1%L
        j=0
        while(j<L):
            if(rand1==j):
                rand=Alphabet[j]
            j=j+1
        Suite.append(rand)
        i=i+1
    return(Suite)

def MasterMind_Lettre_Faux(Coup, Suite):
    compte=0
    Suite1=[]
    i=0
    while(i<len(Suite)):
        Suite1.append(Suite[i])
        i=i+1
    i=0
    while(i<len(Coup)):
        continuer=True
        j=0
        while(j<len(Suite1) and continuer):
            if(Coup[i]==Suite1[j]):
                Suite1[j]=100
                Suite1.remove(100)
                continuer=False
            j=j+1
        if(continuer):
            compte=compte+1
        i=i+1
    return(compte)

def MasterMind_Placement_Faux(Coup, Suite):
    compte=0
    i=0
    while(i<len(Suite)):
        if(Coup[i]!=Suite[i]):
            compte=compte+1
        i=i+1
    return(compte)

def MasterMind_Afficher(Coups, Suite_Deplacements, Suite_Lettres):
    MasterMind_Efface()
    print("   Lettres Fausses   |          Coups          |   Positions Fausses")
    print("-"*71)
    i=0
    while(i<len(Coups)):
        print("-"*71)
        print(" "*10+str(Suite_Lettres[i])+"          |      "+str(Coups[i][0])+"   "+str(Coups[i][1])+"   "+str(Coups[i][2])+"   "+str(Coups[i][3])+"      |           "+str(Suite_Deplacements[i]))
        i=i+1

def MasterMind_Fin(Suite, Coup, compte):
    if(Suite==Coup):
        print("\n Bravo !!! Vous avez mis "+str(compte)+" coups !!!")
        continuer=False
    else:
        continuer=True
    return(continuer)

Jeux()
