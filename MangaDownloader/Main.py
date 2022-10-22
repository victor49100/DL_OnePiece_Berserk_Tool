from OnePieceEnDl import DlOnePieceEn
from OnePieceVfDl import DlOnePieceVf
from PdfConv import Mainpdf
from Berserk import DlBerserkEn

def dl():
    Tome = int(input("Voulez vous telechargé One Piece (1) ou Berserk (2) ? "))
    if Tome == 1:
        T = int (input("Entrez le Tome a téléchargé : "))
        Lang = int (input("Voulez vous telechargé One Piece en ou en Francais(1) Anglais(2) ?"))
        if Lang == 1: #fr
            DlOnePieceVf(T)
        if Lang == 2: #An
            DlOnePieceEn(T)
    if Tome == 2: #berserk
        DlBerserkEn()

def pdf():
    Mainpdf()


print (""" 
      ____             _____ _                 ____                          _     
     / __ \           |  __ (_)               |  _ \                        | |    
    | |  | |_ __   ___| |__) |  ___  ___ ___  | |_) | ___ _ __ ___  ___ _ __| | __ 
    | |  | | '_ \ / _ \  ___/ |/ _ \/ __/ _ \ |  _ < / _ \ '__/ __|/ _ \ '__| |/ / 
    | |__| | | | |  __/ |   | |  __/ (_|  __/ | |_) |  __/ |  \__ \  __/ |  |   <  
     \____/|_| |_|\___|_|   |_|\___|\___\___| |____/ \___|_|  |___/\___|_|  |_|\_\ 
    """)


choice = int(input("Voulez vous telechargé (1) ou Convertir en PDF (2) ? "))
if choice == 1:
    dl()
if choice == 2:
    pdf()

