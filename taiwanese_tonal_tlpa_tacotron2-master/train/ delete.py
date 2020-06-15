import os
import shutil
with open('/home/mu/tacotron2/filelists/train_file_del_list.txt','r')as del_file:
	lines=del_file.readlines()
	for i in range(0,len(lines)):
		path_in=lines[i]
		file_name_n = os.path.split(lines[i])[1]
		file_name = file_name_n.split()[0]
		print(file_name)
		new_Folder="/home/mu/tacotron2/train_wav_160/"
		shutil.copyfile(file_name,os.path.join(new_Folder,file_name))