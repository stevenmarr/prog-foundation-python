def read_text():
    quotes = open("/users/stevenmarr/prog-found-python")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    
read_text()
