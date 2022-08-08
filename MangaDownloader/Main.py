from OnePieceEnDl import DlOnePieceEn
from OnePieceVfDl import DlOnePieceVf
from Berserk import DlBerserk

def Main():
    Tome = int(input("Voulez vous telechargé One Piece (1) ou Berserk (2) ? "))
    if Tome == 1:
        T = int (input("Entrez le Tome a téléchargé : "))
        Lang = int (input("Voulez vous telechargé One Piece en ou en Francais(1) Anglais(2) ?"))
        if Lang == 1: #fr
            DlOnePieceVf(T)
        if Lang == 2: #An
            DlOnePieceEn(T)
    if Tome == 2: #berserk
        DlBerserk()


Main()