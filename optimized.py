"""optimisé"""

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



def ratio(share):
    """ratio benefit/lenght"""
    return (share[2] * share[1] / 100) / share[1]


def glouton(shares, max_price, choice):
    """greedy algorithm using binary knapsack 0/1 system"""

    shares_sorted = sorted(shares, key=choice, reverse=True)    # tri la liste par ratio
    response = []
    total_benefit, total_price, i = 0, 0, 0

    while i < len(shares) and total_price <= max_price:         # tant que i inferieur liste et prix inf à prix max
        name, price, benefit = shares_sorted[i]                 # nom, prix et benefice = action(i) de liste trié
        if total_price + price <= max_price:                    # si cumul du prix + prix inferieur à prix max:
            response.append(name)                               # ajout nom
            total_price += price                                # ajout prix
            total_benefit += benefit * price / 100              # ajout rendement
        i += 1                                                  
    return response, total_benefit, total_price                 # renvoi le total de noms, benefices, prix


file_name = input("Veuillez rentrer le nom du fichier csv à analyser (ex dataset1): ")
shares = import_share(file_name + ".csv")
if shares == "error":
    print("fichier inexistant")
else:
    time_start = time.time()
    response, total_benefit, total_price = (glouton(shares, 500, ratio))
    time_stop = time.time()
    print("Liste des actions choisies : ", response)
    print("Ce qui fait :", round(total_benefit, 2), "Euros de benefice")
    print("pour :", round(total_price, 2), "Euros placés")
    print("Durée du calcul :", time_stop-time_start, "secondes")
    print("Complexité algorithmique : O(log n)")



#(nb[1]*nb[2])/100
# O(log(n))