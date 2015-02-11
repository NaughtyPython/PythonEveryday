import random
import string
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
'''
1. generate a id in range(200)
2. remember the id as the key
3. transfer to hex as the prefix  e.g. 72
4. fill up the half length of code by e.g. 00072 
5. randomly create a char and put it after each char created  e.g. 0X0B0A7S2T
6. return both code and key


should apt-get install pymongo, mongodb-server, mysql-server

the following command to start db server:
    sudo service mysql restart
    mongod
'''


def activation_code(id, length=10):
    origin = hex(int(id))
    key = str(int(id))
    for i in range(length/2-len(origin)):
        origin = '0' + origin
    chars = string.ascii_letters
    final_code = ''
    for j in origin:
        final_code = final_code + j + random.choice(chars)
    return final_code, key


def insert_mongodb(dict):
    client = MongoClient('localhost', 27017)
    db = client.test_db
    collection = db.test_collection
    collection.insert(dict)
#     print collection.find({'id':'11'}).explain()['cursor']
    collection.create_index([('id', ASCENDING), ('code', DESCENDING)])
#     print collection.find({'id':'11'}).explain()['cursor']
    # query all matching items and sort it
    for c in collection.find({'id':'171'}).sort('code'):
        print c

    # remove db.collection
#     db.test_collection.remove()


def insert_mysql():
    cnx = mysql.connector.connect(user='angela', db='test_mysql')
    
    
if __name__ == "__main__":

    code_list = []
    for id in range(200):
        code_dict = {}
        final_code, key = activation_code(id)
        code_dict['id'] = key
        code_dict['code'] = final_code
        code_list.append(code_dict)
    insert_mongodb(code_list)