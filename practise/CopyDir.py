import sys
import os.path

def processDirectory(sou_path, dest_path):
    for tmp in os.listdir(sou_path):
        tmp_path = sou_path+'\\'+tmp
        if os.path.isfile(tmp_path) == True:
            dest_file_path = dest_path +'\\'+tmp
            print(tmp_path,dest_file_path)
            os.system("copy %s %s" % (tmp_path,dest_file_path))
        else:
            dest_file_path = dest_path + '\\' + tmp
            if os.path.exists(dest_file_path) != True :
                os.mkdir(dest_file_path)
            processDirectory(tmp_path,dest_file_path)

source_dir_path = input("plz input the source dir:")
destination_dir_path = input("plz input the destination dir:")
processDirectory(source_dir_path,destination_dir_path)