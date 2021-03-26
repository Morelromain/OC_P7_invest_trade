"""Une seule même action"""

import time

import manage_share as manage


def total_benefit(selection):
    """Accumulation benefit"""
    benefit = sum(share[2]*share[1]/100 for share in selection)
    return round(benefit, 2)
 

def total_money(selection):
    """Accumulation money"""
    return sum(share[1] for share in selection)


def total_name(selection):
    """Accumulation name"""
    return "".join((share[0] + " | ") for share in selection)
 

def force_brute(shares, max_price):
    """bruteforce using binary knapsack 0/1 system"""
    nb_share = len(shares)
    power_nb_share = 2 ** nb_share
    response = []
    for cle in range(power_nb_share):
        loop_bin = bin(cle)[2:]
        length_bin = len(loop_bin)
        if length_bin < nb_share:
            loop_bin = (nb_share - length_bin) * '0' + loop_bin
        combination = [shares[i] for i in range(nb_share) if loop_bin[i] != '0']
        if (
            total_benefit(combination) > total_benefit(response)
            and total_money(combination) < max_price
        ):
            response = combination
    return response


file_name = input("Veuillez rentrer le nom du fichier csv à analyser (ex dataset1): ")
shares = manage.import_share(file_name + ".csv")
if shares != "error":
    print("Application de l'algorithme de force brute :")
    start = time.time()
    response = force_brute(shares, 500)
    stop = time.time()
    print("Liste des actions choisies : {0}\n\
Bénéfices : {1} euros \nSomme placée : {2} euros \n\
Durée du calcul : {3} secondes \nComplexité algorithmique : O(n^2)"
.format(total_name(response), total_benefit(response), total_money(response), stop-start))
