import csv, os


def import_share(file_name):
    """Create share list from .csv file"""
    list_share = []
    try:
        with open('dataset/'+file_name, "r") as csv_file:
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
        print("fichier inexistant")
        return "error"


def save_choice(file_name, responses, benefice, price):
    os.makedirs('investment_decisions', exist_ok=True)
    with open('investment_decisions/'+file_name+'.csv', 'w') as f:
        for response in responses:
            f.write(response + "\n")
        f.write("Benefices : {0} euros \nSomme placee : {1} euros"
        .format(benefice, price))

