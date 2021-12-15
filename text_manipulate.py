def add_entry(entry, file='news_url.txt'):
    myText = open(file,'a')
    myString = entry
    myText.write(myString+'\n')
    myText.close()

def read_entry(file='news_url.txt'):
    a_file = open(file, "r")
    lines = a_file.readlines()[0].replace('\n','')
    a_file.close()
    return lines

if __name__ == "__main__":
    add_entry()
    read_entry()