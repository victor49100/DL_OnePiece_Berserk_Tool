import requests  # to get image from the web
import shutil  # to save it locally
import os
import Url


def DlOnePieceEn(Tome):
    #iTome = int(input("Which chapter is your download?: "))
    dirname = ("OnePiece"+str(Tome))
    file = open ("lastChapter.txt","r")
    lastChapter = file.readline()
    lastChapter = int(lastChapter)
    print (lastChapter)

    if not os.path.exists('OnePieceEn'):
        os.makedirs("OnePieceEn")

    os.chdir('OnePieceEn')
    if os.path.exists("OnePiece"+str(Tome)):
        os.chdir(dirname)
    else:
        dirname = ("OnePiece"+str(Tome))
        os.mkdir(dirname)
        os.chdir(dirname)

    for page in range(1, 50):

        if Tome <= lastChapter:
            image_url = Url.ConvertUrlToTome(Tome)
            image_url = image_url.replace("X", str(page))
            filename = image_url.split("/")[-1]
            r = requests.get(image_url, stream=True)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print('Image sucessfully Downloaded: ', filename)
            else:
                image_url = Url.ConvertUrlToTome(Tome)
                image_url = image_url.replace("X", str(page))
                image_url = image_url.replace("jpeg", str("png"))
                filename = image_url.split("/")[-1]
                r = requests.get(image_url, stream=True)
                if r.status_code == 200:
                    r.raw.decode_content = True
                    with open(filename, 'wb') as f:
                        shutil.copyfileobj(r.raw, f)
                    print('Image sucessfully Downloaded: ', filename)
                else:
                    print('aucun contenu trouvé !')
                    break
        else:
            image_url = "https://cdn.readonepiece.com/file/CDN-M-A-N/onepiecetcb_X_0Y.png"
            image_url = image_url.replace("Y", str(page))
            image_url = image_url.replace("X", str(Tome))
            print(image_url)
            filename = image_url.split("/")[-1]
            r = requests.get(image_url, stream=True)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)

                print('Image sucessfully Downloaded: ', filename)
            else:
                print('aucun contenu trouvé !')
                break
#DlOnePieceEn(Tome)