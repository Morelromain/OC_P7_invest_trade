"""optimisé"""

import time

import invest_trade.controller.manage_share as manage


def ratio(share):
    """ratio benefit/lenght"""
    return (share[2] * share[1] / 100) / share[1]


def glouton(shares, max_price, choice):
    """greedy algorithm using binary knapsack 0/1 system"""
    shares_sorted = sorted(shares, key=choice, reverse=True)
    response, total_benefit, total_price, i = [], 0, 0, 0
    while i < len(shares) and total_price <= max_price:
        name, price, benefit = shares_sorted[i]
        if total_price + price <= max_price:
            response.append(name)
            total_price += price
            total_benefit += benefit * price / 100
        i += 1
    return response, total_benefit, total_price


def control_op():
    file_name = input("Nom du fichier csv à analyser (ex dataset1): ")
    shares = manage.import_share(file_name + ".csv")
    if shares != "error":
        start = time.time()
        response, total_b, total_p = (glouton(shares, 500, ratio))
        stop = time.time()
        print("Liste des actions choisies : {0}\n\
Bénéfices : {1} euros \nSomme placée : {2} euros \n\
Durée du calcul : {3} secondes \nComplexité algorithmique : O(log n)"
.format(response, round(total_b, 2), round(total_p, 2), stop-start))
        manage.save_choice(file_name, response,
                           round(total_b, 2), round(total_p, 2))
        print("Sauvegarde données : investment_decisions/{0}".format(file_name))
