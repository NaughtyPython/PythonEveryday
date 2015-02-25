
import os
from path import *


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def calculateCode():
    '''
    calculate number of lines in the files within a folder
    '''
    code_path = os.path.abspath(os.path.join(assets_path, 'codes'))
    print code_path
    total_num = 0   # total number of lines
    space_line = 0  # number of blank lines
    comment_line = 0  # number of comment lines
    for filename in next(os.walk(code_path))[2]:
        print filename
        file_path = os.path.abspath(os.path.join(code_path, filename))
        with open(file_path, 'r') as f:
            for line in f.readlines():
                import re
                if re.search('#', line) or re.search('\'''', line):
                    comment_line = comment_line + 1
                if re.search('^\s*$', line):
                    space_line = space_line + 1
                total_num = total_num + 1

    print space_line
    print comment_line
    print total_num


def findBodyHTML():
    '''
    find body in html file
    '''
    with open(os.path.abspath(os.path.join(assets_path, 'google.html')), 'r') as f:
        data = f.read()
        import re
        s = find_between(data, '<body', '</body>')
        print '<body%s</body>' % s