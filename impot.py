#!/usr/bin/python

import sys

def help():
    print("Utilisation : ./impot.py SALAIRE NB_PARTS NB_ENFANTS\n")

    print("Les tranches d'impôt sont les suivantes :")
    print("\t - [0, 10225] : 0 %")
    print("\t - [10226, 26070] : 11 %")
    print("\t - [26071, 74545] : 30 %")
    print("\t - [74546, 160336] : 41 %")
    print("\t - [160336, inf] : 45 %.\n")

    print("On applique ces tranches sur 90 % du salaire divisé par le nombre de parts. On multiplie ensuite par le résultat par le nombre de parts.\n")
    
    print("Attention : il y a un plafonnement de l'effet du Quotient Familial. Un enfant ne peut réduire l'impôt que de 1592 € maximum, d'où l'intérêt des deux colonnes :")
    print("\t - QF : colonne en prenant en compte le quotient familial.")
    print("\t - Sans QF : colonne ne prenant pas en compte le quotient familial auquel on enlève 1592 € / enfant.")


def impot(mb, part, enfants):
    mp = round(mb * 0.9 / part, 2)
    m = [mp, mb*0.9]

    taux = [0, 0.11, 0.30, 0.41, 0.45]
    tranches = [0,10225, 26070, 74545, 160336]
    plafond_QF = 1592
    
    tp = [0,0]

    print("Impôt \t \t| QF \t\t| Sans QF")
    print("Revenu \t\t|", round(m[0],2), "€\t|", round(m[1],2), "€")
    print("----------------------------------------------------")
    for i in range(len(taux)-1):
        imp = [0, 0]
        
        for j in range(len(imp)):
            if m[j] > tranches[i+1]:
                imp[j] = (tranches[i+1] - tranches[i]) * taux[i]
            elif m[j] > tranches[i]:
                imp[j] = (m[j] - tranches[i]) * taux[i]
            else:
                imp[j] = 0
            if j == 0:
                imp[j] *= part
            tp[j] += round(imp[j],2)
        print("Tranche ", i, "\t|", str(round(imp[0],2)).ljust(8), "€ \t|", str(round(imp[1],2)).ljust(8), "€")
    
    print("----------------------------------------------------")
    print("Pré-totaux \t|", str(round(tp[0],2)).ljust(8), "€ \t|", str(round(tp[1],2)).ljust(8), "€")
    plafonnement_QF = -plafond_QF * enfants
    print("Plafonnement QF\t|\t\t|", str(plafonnement_QF).ljust(8), "€\t")
    tp[1] += plafonnement_QF
    print("Totaux \t\t|", str(round(tp[0],2)).ljust(8), "€ \t|", str(round(tp[1],2)).ljust(8), "€")
    
    return max(tp)

try:
    imp = impot(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    print("----------------------------------------------------")
    print("Total (max)\t|", imp,"€\t|")
except:
    help()

        
        
