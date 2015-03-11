import os
import path
import shutil

resume_path = os.path.abspath(os.path.join(path.assets_path, 'diary'))


def getOutputPath(keyword):
    output_path = os.path.abspath(os.path.join(resume_path, keyword))
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    return output_path


def arrangeFileToSeperateFolder():

    for filename in next(os.walk(resume_path))[2]:
        file_path = os.path.abspath(os.path.join(resume_path, filename))
        toCopy = []
        with open(file_path, 'rwb') as f:
            for line in f.readlines():
                import re
                if re.search('[S|s][H|h][A|a][R|r][E|e][P|p][O|o][I|i][N|n][T|t]', line):
                    keyword = 'Sharepoint'
                    toCopy.append(keyword)
                    output_path = getOutputPath(keyword)
                    print "%s: %s" % (filename, line)
                    print "keyword: %s - copy %s to path: %s" % (keyword, filename, output_path)
                    break

                if re.search('CRM', line) or re.search('crm', line):
                    keyword = 'CRM'
                    toCopy.append(keyword)
                    output_path = getOutputPath(keyword)
                    print "%s: %s" % (filename, line)
                    print "keyword: %s - copy %s to path: %s" % (keyword, filename, output_path)
                    break

                if re.search('BI', line):
                    keyword = 'BI'
                    toCopy.append(keyword)
                    output_path = getOutputPath(keyword)
                    print "%s: %s" % (filename, line)
                    print "keyword: %s - copy %s to path: %s" % (keyword, filename, output_path)
                    break

        for keyword in ['Sharepoint', 'CRM']:
            if keyword in toCopy:
                output_file_path = os.path.abspath(os.path.join(getOutputPath(keyword), filename))
                shutil.copy(file_path, output_file_path)
                print "copied %s to %s" % (file_path, output_file_path)


if __name__ == '__main__':
    arrangeFileToSeperateFolder()
