import string
import os
BASE_PATH =  os.path.dirname(__file__)

'''
Function: read string in article.txt and count the words with a dict output
use re.sub to replace all unmatched chars in line
the following code will 

         line = re.sub('[^\w ]','', line)
'''

def countWords():
    dict = {}
    file_path = os.path.abspath(os.path.join(BASE_PATH, "..", "assets", "article.txt"))
    with open(file_path) as f:
        for line in list(f):
            import re
            line = re.sub('[^\w ]','', line)
            print line
            for word in line.split():
                if word not in dict.keys():
                    dict[word] = 1
                else:
                    dict[word] = dict[word] + 1
    print dict


if __name__ == "__main__":
    countWords()