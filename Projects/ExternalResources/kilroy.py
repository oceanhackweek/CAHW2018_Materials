def Show(folder, filename, width, height):
    import requests
    import shutil
    from PIL import Image
    fullpath = 'https://raw.githubusercontent.com/robfatland/othermathclub/master/images/' + folder + '/' + filename
    a = requests.get(fullpath, stream = True)
    outf = './tmp.jpg'
    if a.status_code == 200:
        with open(outf, 'wb') as f:
            a.raw.decode_content = True
            shutil.copyfileobj(a.raw, f)
    return Image.open(outf).resize((width,height),Image.ANTIALIAS)

# A proper version of 'Show' with username, repo name, folder name, sub-folder name, and filename + render dimensions
def ShowImageFromGitHub(un, rn, fn, sfn, filename, width, height):
    import requests
    import shutil
    from PIL import Image
    fullpath = 'https://raw.githubusercontent.com/' + un + '/' + \
		    rn + '/master/' + fn + '/' + sfn + '/' + filename
    a = requests.get(fullpath, stream = True)
    outf = './tmp.jpg'
    if a.status_code == 200:
        with open(outf, 'wb') as f:
            a.raw.decode_content = True
            shutil.copyfileobj(a.raw, f)
    return Image.open(outf).resize((width,height),Image.ANTIALIAS)
