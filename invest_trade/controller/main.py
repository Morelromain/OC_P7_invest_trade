"""Main"""

from invest_trade.controller import bruteforce, optimized


class Menu:
    """Menu Controller"""

    algo = '0'
    while algo != '3':
        print("1:BruteForce        2:Optimisé         3:Exit")
        algo = input("Quel algorythme voulez-vous utiliser?: ")
        if algo == '1':
            bruteforce.control_fb()
        elif algo == '2':
            optimized.control_op()
        elif algo == '3':
            exit
