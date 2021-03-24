"""Une seule même action"""

import time, csv

def import_share(file_name):
    """Create share list from .csv file"""
    list_share = []
    try:
        with open(file_name, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader :
                list_share.append(line)
        del list_share[0]
        list_share2 =[]
        for share in list_share:
            if share[1] != "0.0" and "-" not in share[1]:
                share[1] = float(share[1])
                share[2] = float(share[2])
                list_share2.append(share)
        return list_share2
    except FileNotFoundError:
        return "error"

def total_benefit(selection):
    """Accumulation benefit"""
    benefit = 0
    for share in selection:
        benefit += share[2]*share[1]/100
    return round(benefit, 2)
 
def total_money(selection):
    """Accumulation money"""
    money = 0
    for share in selection:
        money += share[1]
    return money

def total_name(selection):
    """Accumulation name"""
    money = ""
    for share in selection:
        money += (share[0] + " | ")
    return money
 
def force_brute(shares, max_price):                                 # Fonction (liste des action, prix maximum)
    """bruteforce using binary knapsack 0/1 system"""

    nb_share = len(shares)                                          # Longueur de la liste des action (20)
    power_nb_share = 2 ** nb_share                                  # Puissance de 2 de nb_share (1048576)
    response = []                                                    # Déclaration liste à retourner

    for cle in range(power_nb_share):                               # Pour chaque nombre dans power_nb_share
        
        loop_bin = bin(cle)[2:]                                     # Convertir en binaire
        length_bin = len(loop_bin)                                  # Longueur des nombres binaires (de 1 à 20)
        if length_bin < nb_share:                                   # Si longueur des nombres binaires < nb_share(20)
            loop_bin = (nb_share - length_bin) * '0' + loop_bin     # Met les 0 qui manque devant le chiffre binaire
        combination = []                                            # Déclaration liste pour combinaison 
        for i in range(nb_share):                                   # Pour chaque action dans la liste des action
            if loop_bin[i] != '0':                                  # Si chifre binaire = 1
                combination.append(shares[i])                       # Ajoute l'action dans la liste

        if total_benefit(combination) > total_benefit(response):    # Si cumul des benefices de Combinaison > cumul des benefice de response
            if total_money(combination) < max_price:                # Si cumul de la liste combinaison(argent) < prix_max
                response = combination                              # liste response = liste combinaison

    return response                                                  # retourne la liste response


file_name = input("Veuillez rentrer le nom du fichier csv à analyser (ex dataset1): ")
shares = import_share(file_name + ".csv")
if shares == "error":
    print("fichier inexistant")
else:
    print("Application de l'algorithme de force brute :")
    time_start = time.time()
    response = force_brute(shares, 500)
    time_stop = time.time()
    print("Liste des actions choisies : ", total_name(response))
    print("Ce qui fait :", total_benefit(response), "Euros de benefice")
    print("pour :", total_money(response), "Euros placés")
    print("Durée du calcul :", int(time_stop-time_start), "secondes")
    print("Complexité algorithmique : O(n^2)")