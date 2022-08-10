from PIL import Image


def ConvertBerserk(formatF):
    Tome = int(input("Quel est le Tome à convertir en PDF ?: "))
    images_list = []
    for i in range(1, 350):
        try:
            path = str(
                "./Berserk/BerserkTome"+str(Tome)+"/"+str(i)+"."+str(formatF))

            image = Image.open(str(path))
            im = image.convert('RGB')
            images_list.append(im)
        except:
            images_list[0].save(r'BerserkTome'+str(Tome)+'.pdf',
                                save_all=True, append_images=images_list)
            print("PDF de "+str(i) + " pages généré")
            break


def ConvertOp(formatF):
    Tome = int(input("Quel est le Tome à convertir en PDF ?: "))
    Langue = int(input("la langue du pdf (fr:1 En:2)?: "))
    
    images_list = []
    for i in range(1, 40):
        
        try:
            if Langue == 1:
                path = str(
                    "./OnePieceVf/OnePiece"+str(Tome)+"/"+str(i)+"."+str(formatF)) #if out of range pb change name
            if Langue == 2:
                path = str(
                    "./OnePieceEn/OnePiece"+str(Tome)+"/"+str(i)+"."+str(formatF))
            image = Image.open(str(path))
            im = image.convert('RGB')
            images_list.append(im)
            
        except:
            images_list[0].save(r'OnePieceTome'+str(Tome)+'.pdf', save_all=True, append_images=images_list)
            print("PDF de "+str(i) + " pages généré")
            break


def Mainpdf():
    choix = int(input("Convertir One Piece(1) Ou berserk(2) ? "))
    formatF = str(input("quelle est le format du fichier ex(png,jpeg,webp ...) ? "))

    if choix == 2:
        ConvertBerserk(formatF)
    if choix == 1:
        ConvertOp(formatF)
