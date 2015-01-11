import urllib

def open_file():
    try:
        file=open("/dusers/stevenmarr/prog-found-python/speech.txt")
        text = file.read()
        file.close()
        return(text)
    except: return("Grrr someting broke mate!")


def make_pirate_speech():
    text = open_file()
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text)
    print(connection.read())
    connection.close()
make_pirate_speech()
