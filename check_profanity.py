import urllib

def read_text():
    quotes = open("/users/stevenmarr/prog-found-python/movie_quotes.txt")
    check_profanity(quotes.read())
    quotes.close()
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+
    text_to_check)
    print(connection.read())
    connection.close()


read_text()
