import csv
with open('train_file_del_list.txt','w')as my_output_file:
	with open('train_file_del.csv','r',errors='ignore')as my_input_file:
		[my_output_file.write('-'.join(row)+'\n')for row in csv.reader(my_input_file)]
	my_output_file.close()