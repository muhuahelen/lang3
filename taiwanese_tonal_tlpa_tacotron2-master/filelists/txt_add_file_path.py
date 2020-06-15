import csv
with open('eval-file.txt','w')as output_file:
	with open('pre_test.txt','r')as change_file:
		lines=change_file.readlines()
		for i in range(0,len(lines)):
			lines[i]='/home/mu/tacotron2/test-shuf/%d.wav'%(i+1) + '|' +lines[i].strip()+'\n'
			output_file.write(lines[i])