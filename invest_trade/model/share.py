"""Share model"""

import csv


class ModelShare:
    """Create share"""

    def share(self, file_name):
        """Create share list from .csv file"""

        list_share = []
        try:
            with open("invest_trade/bdd/"+file_name, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader :
                    list_share.append(line)
            return list_share
        except FileNotFoundError:
            print("fichier inexistant")
