#write check profanity programme. The programme will detect rude wrods.

from urllib.request import urlopen

def check_profanity(text_to_check):
    #connect to the website
    #connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    url = urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = url.read()
    output = output.decode('utf8').strip()
    if "true" in output:
        print("Profanity Alert !")
    elif "false" in output:
        print("The document is secure.")
    else:
        print("Can not scan the Document Properly")
    url.close()

#read text fromt he file and check for profanities
def read_text():
    quotes = open(r"C:\Personal\GitHub\Udacity-Full-Stack-Web-Developer-Nanodegree\Supporting courses\Programming Foundations with Python\text.txt")
    contents_of_file = quotes.read()
    contents_of_file = contents_of_file.replace(" ", "")
    contents_of_file = contents_of_file.replace('\n', '')
    quotes.close()
    check_profanity(contents_of_file)
read_text()
