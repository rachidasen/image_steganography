# read first ar


import argparse
import os
message=''
name_count=0
parser=argparse.ArgumentParser()
parser.add_argument("-a","--add",nargs="+",help="hi freing")
args=parser.parse_args()
flag=0
if args.add:
	print args.add
	name_count=1
	for u in args.add:
		if flag==0:
			image_name=u
			flag=1
		else:
			print "reading_file",u
			# with open(u,'r') as myfile:
			message=u
			print message

			# message.encode('unicode-escape')
			# message.encode("ascii","ignore")
			# message.dencode('string-escape')
			# mess=str(message)
			# print type(mess)
			# cmd = 'python image_scale.py '+message+' '+str(name_count)+' '
			cmd='python correct.py '+image_name+' "'+message+'" ' + str(name_count)
			# cmd=str(cmd)
			print cmd
			cmd.decode('string-escape')
			# print cmd
			os.system(cmd)
			print "Allah is the forgiver"
			# os.system("python image_scale.py "+mess+' '+str(name_count))
			# print u
			cmd='python de_stgano.py '+image_name+" "+str(name_count)
			os.system(cmd)
			name_count+=1
			# myfile.close()