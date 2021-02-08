"""Menu view"""


class ViewMenu:
    """display menu"""

    def menustart(self):
        """display menu start"""

        file_name = str(input("Donner nom du fichier a analyser (dataFinanceTest.csv) : "))
        return file_name

    def printlist(self, list_share):
        """display menu start"""

        print(list_share)
