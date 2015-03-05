import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password,salt = None):
    if salt is None:
        salt = os.urandom(8)
    assert 8 == len(salt)
    assert isinstance(salt, str)
    
    if isinstance(password, unicode):
        password = password.encode('utf-8')
    
    assert isinstance(password, str)
    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).digest()

    return result + salt


if  __name__ == '__main__':
    print encrypt_password('@wsx3edc')    
