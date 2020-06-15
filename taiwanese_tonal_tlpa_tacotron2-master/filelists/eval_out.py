import math
import random
import math
list=[]
with open('eval-file.txt','w')as output_file:
	with open('train_file_del.txt','r')as input_file:
		lines=input_file.readlines()
		for i in range(math.ceil(len(lines)/10)):
			rand_line=random.randint(0,len(lines))
			list.append(lines[rand_line])
		for i in list:
			output_file.write('%s'%i)