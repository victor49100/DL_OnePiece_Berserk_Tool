import requests # to get image from the web
import shutil # to save it locally
import os
import sys


def DlBerserk():
    Tome = int(input("Quel est le Tome à télécharger ?: "))
    dirname = ("BerserkTome"+str(Tome))
    if not os.path.exists('Berserk'):
        os.makedirs("Berserk")

    os.chdir('Berserk')
    if os.path.exists("BerserkTome"+str(Tome)):
        os.chdir(dirname)
    else : 
        dirname = ("BerserkTome"+str(Tome))
        os.mkdir(dirname)
        os.chdir(dirname)

    for page in range (1,300):
        if page<10:
            idp = str("00"+str(page))
        if page<99 and page >10:
            idp = str("00"+str(page))
        if page>99:
            idp = str("00"+str(page))
        image_url = "https://opfrcdn.xyz/uploads/manga/berserk/chapters/Volume%20"+str(Tome)+"/"+str(idp)+".jpg"
        print (image_url)
        filename = image_url.split("/")[-1]
        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(image_url, stream = True)
        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
            print('Image sucessfully Downloaded: ',filename)
        else:
            image_url = "https://opfrcdn.xyz/uploads/manga/berserk/chapters/Volume%20"+str(Tome)+"/"+str(idp)+".png"
            filename = image_url.split("/")[-1]
            r = requests.get(image_url, stream = True)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print('Image sucessfully Downloaded: ',filename)
            else:
                image_url = "https://opfrcdn.xyz/uploads/manga/berserk/chapters/Volume%20"+str(Tome)+"/"+str(idp)+".webp"
            filename = image_url.split("/")[-1]
            r = requests.get(image_url, stream = True)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                cmd = ('cmd /k "Image sucessfully Downloaded"')
                os.system(cmd)
            else:
                os.chdir('..')
                os.rmdir("BerserkTome"+str(Tome))
                print('aucun contenu trouvé !')
                print ("fin :"+str((page-1))+" pages tétéchargé")
                os.system('pause')
                break

#https://opfrcdn.xyz/uploads/manga/berserk/chapters/Volume%2019/001.jpg
