from this import d
import requests  # to get image from the web
import shutil  # to save it locally
import os
import Url


def DlBerserkEn():
    print ("listes des chapitres : https://fr.wikipedia.org/wiki/Liste_des_chapitres_de_Berserk")
    ChapitreDebut = int(input("premier Chapitre : "))
    ChapitreFin = int(input("deuxieme Chapitre : "))
    Delta = ChapitreFin-ChapitreDebut
    print ("nombre de chapitre dans le tome :"+str(Delta))
    dirname = ("Berserk"+str(ChapitreDebut))
    if not os.path.exists('Berserk'):
        os.makedirs("Berserk")

    os.chdir('Berserk')
    if os.path.exists("Berserk"+str(ChapitreDebut)):
        os.chdir(dirname)
        NomFichier = 0
        print ("0%")
    else:
        dirname = ("Berserk"+str(ChapitreDebut))
        os.mkdir(dirname)
        os.chdir(dirname)
        NomFichier = 0
        print ("0%")
        Delta=Delta+1
    
    for i in range (0,Delta):
        NomFichier = NomFichier-1
        pourcent = (((i+1)/Delta)*100)
        for page in range(1, 50):
            NomFichier=NomFichier+1
            image_url = Url.ConvertUrlToTomeBs(ChapitreDebut)
            image_url = image_url.replace("X", str(page))
            #print(image_url)
            filename = image_url.split(".")[-1]
            filename = str(NomFichier)+"."+filename
            r = requests.get(image_url, stream=True)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)

                #print('Image sucessfully Downloaded: ', filename)
            else:
                #print('aucun contenu trouvé !')
                print(str(pourcent)+"%")
                ChapitreDebut = ChapitreDebut+1
                break
#print(DlBerserkEn())