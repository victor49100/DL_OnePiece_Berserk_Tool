
import requests  # to get image from the web
import shutil  # to save it locally
import os
# Set up the image URL and filename


def DlOnePieceVf(Tome):
    #Tome = int(input("Quel est le chapitre à télécharger ?: "))
    dirname = ("OnePiece"+str(Tome))
    if not os.path.exists('OnePieceVf'):
        os.makedirs("OnePieceVf")

    os.chdir('OnePieceVf')
    if os.path.exists("OnePiece"+str(Tome)):
        os.chdir(dirname)
    else:
        dirname = ("OnePiece"+str(Tome))
        os.mkdir(dirname)
        os.chdir(dirname)

    for page in range(1, 300):
        if page < 10:
            idp = str('0'+str(page))
        else:
            idp = str(page)


        ## JPG ###
        image_url = "https://i2.wp.com/sushiscan.su/wp-content/uploads26/OPChap" + \
            str(Tome)+"fix-"+str(idp)+".png"
        print(image_url)
        filename = image_url.split("/")[-1]
        filename = str(filename)
        if page < 100:
            filename = filename[0:]
        r = requests.get(image_url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            print('Image sucessfully Downloaded: ', filename)
        else:
            
            ## png ##
            image_url = "https://i2.wp.com/sushiscan.su/wp-content/uploads26/OPChap" + \
            str(Tome)+"fix-"+str(idp)+".jpg"
            filename = image_url.split("/")[-1]
            filename = str(filename)
            if page < 100:
                filename = filename[0:]
            r = requests.get(image_url, stream=True)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print('Image sucessfully Downloaded: ', filename)

            else:
                ## Webp ##
                image_url = "https://i2.wp.com/sushiscan.su/wp-content/uploads26/OPChap" + \
                str(Tome)+"fix-"+str(idp)+".webp"
                filename = image_url.split("/")[-1]
                filename = str(filename)
                if page < 100:
                    filename = filename[0:]
                r = requests.get(image_url, stream=True)
                if r.status_code == 200:
                    r.raw.decode_content = True
                    with open(filename, 'wb') as f:
                        shutil.copyfileobj(r.raw, f)
                else:
                    os.chdir('..')
                    os.rmdir("OnePiece"+str(Tome))
                    print('Aucun contenu trouvé !')
                    print("fin :"+str((page-1))+" pages tétéchargé")
                    os.system('pause')
                    break

#DlOnePieceVf(1056)