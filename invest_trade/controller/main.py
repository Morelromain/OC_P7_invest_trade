"""Main"""

from invest_trade.view import vmenu
from invest_trade.model import share


class Menu:
    """Menu Controller"""
    
    file_name = vmenu.ViewMenu().menustart()
    list_share = share.ModelShare().share(file_name)
    vmenu.ViewMenu().printlist(list_share)
    #itertool?