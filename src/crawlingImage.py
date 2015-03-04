import urllib2
import path
import os
'''
crawl image from url baidu.tieba
'''

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""



def getContent(url):
    urls = []
    content = urllib2.urlopen(url).readlines()
    for line in content:
        import re
        if re.search('<img pic_type="0" class="BDE_Image" src=', line):
            urls.append(find_between(line, 'src="', '"'))
    return urls


def download(urls):
    count = 0
    for url in urls:
        try:
            response = urllib2.urlopen(url)
        except Exception, e:
            print e
        print response
        count = count + 1
        with open(os.path.abspath(os.path.join(path.download_path, '%s.jpg' % count)), 'w') as output:
            output.write(response.read())
    output.close()


if __name__ == '__main__':
    urls = getContent('http://tieba.baidu.com/p/2166231880')
    print urls
    download(urls)