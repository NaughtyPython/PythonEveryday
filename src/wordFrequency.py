import string
import os
import math
import re
BASE_PATH =  os.path.dirname(__file__)
diary_path = os.path.join(BASE_PATH, "..","assets","diary")
'''
Function: read string in article.txt and count the words with a dict output
use re.sub to replace all unmatched chars in line
the following code will replace all non-word chacter with ' '

         line = re.sub('[^\w ]','', line)
'''


'''
Algorithm:
    TF: Term Frequency
    TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document).

    countWords()/total_term_number


    IDF: Inverse Document Frequency, 
    IDF(t) = log_e(Total number of documents / Number of documents with term t in it).

    total_doc/number_doc_with_term
'''


def countWords(file_path):
    '''
    Number of times term t appears in a document
    '''
    dict = {}

    with open(file_path) as f:
        for line in list(f):

            line = re.sub('[^\w ]','',line)
            for word in line.split():
                if word not in dict.keys():
                    dict[word] = 1
                else:
                    dict[word] = dict[word] + 1
    return dict


def get_total_term_number(file_path):

    '''
        Total number of terms in the document
    '''
    count = 0
    with open(file_path) as f:
        for line in list(f):
            line = re.sub('[^\w ]','', line)
            for word in line.split():
                count = count+1
    print "total_term_number: %s" % count
    return count


def getKeywords(howmany=3):
    total_doc = len(os.listdir(diary_path))
    # To store all of the term and its computing result for comparison between them later
    # total_dict: key is the filename , value is the dict of each file
    total_dict = {}
    for filename in next(os.walk(diary_path))[2]:
        # For each filename, calulate its TF and store it in total_dict
        file_path = os.path.abspath(os.path.join(BASE_PATH, "..","assets", "diary", filename))
        total_term_number = get_total_term_number(file_path)
        with open(file_path) as f:
            dict = countWords(file_path)
            for item in dict.keys():
                term_times = dict[item]
                TF = float(term_times)/float(total_term_number)
                dict[item] = TF
                total_dict[filename] = dict

    # See if the term is also in other file's dict
    for each_dict in total_dict.values():
        for item in each_dict.keys():
            number_doc_with_term = 0
            for other_dict in total_dict.values():
                if other_dict != each_dict and other_dict.has_key(item):
                        #  Calculate the number of doc which has the term
                        number_doc_with_term = number_doc_with_term + 1
        if number_doc_with_term != 0:
            # Calculate its IDF and store it in its dict
            IDF = math.log((float(total_doc)/float(number_doc_with_term)))
            each_dict[item] = each_dict[item] * IDF
            # Sort the dict descending with the values
            from operator import itemgetter
            sorted_list = sorted(each_dict.items(), key=itemgetter(1), reverse=True)
            print each_dict
            # Select the first three keywords with highest values
            for k in range(howmany):
                print "keyword: %s Result:%s" % (sorted_list[k][0],sorted_list[k][1]) 


if __name__ == "__main__":
    getKeywords(4)
    