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
    copied_file_count = 0
    copied_file_list = []
    keywords = ['Sharepoint', 'CRM', 'BI']
    for keyword in keywords:
    	copied_file_path = os.path.abspath(os.path.join(resume_path, keyword))
    	if os.path.exists(copied_file_path):
            for copied_file in next(os.walk(copied_file_path))[2]:
                copied_file_list.append(copied_file)

    for filename in next(os.walk(resume_path))[2]:
        if filename not in copied_file_list:
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
            if toCopy != []:
                for keyword in keywords:
                    if keyword in toCopy:
                        copied_file_count += 1
                        output_file_path = os.path.abspath(os.path.join(getOutputPath(keyword), filename))
                        shutil.copy(file_path, output_file_path)
                        print "copied %s to %s" % (file_path, output_file_path)
    print "total %s files are copied" % copied_file_count


if __name__ == '__main__':
    arrangeFileToSeperateFolder()
