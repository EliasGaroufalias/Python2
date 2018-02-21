from __future__ import print_function
import os

source_path=raw_input('\n\nGive the name of the brainfuck code file:\n\n\t')
source_path1=list(source_path)
if source_path1[len(source_path1)-4]!='.' or source_path1[len(source_path1)-3]!='t' or source_path1[len(source_path1)-2]!='x' or source_path1[len(source_path1)-1]!='t':
	source_path=source_path+'.txt'
source_path2='./'+source_path

if os.path.isfile(source_path2):
	print('\n\nProgram is being executed.\n\n\tInput-Output:\n\n\n')
	input_file=open(source_path,'r')
	source_code=list(input_file.read())
	l=len(source_code)
	registry1=[0]*30000
	i=0
	j=0
	while j<l:
		if source_code[j]=='>' and i<29999:
			i+=1
		elif source_code[j]=='<' and i>0:
			i-=1
		elif source_code[j]=='+' and registry[i]:
			registry1[i]+=1
		elif source_code[j]=='-':
			registry1[i]-=1
		elif source_code[j]==',':
			#print('make input pretty? no?')
			registry1[i]=ord(raw_input())
		elif source_code[j]=='.':
			print(chr(registry1[i]),end='')
		elif source_code[j]=='[':
			loop_start=j
		elif source_code[j]==']':
			if registry1[i]!=0:
				j=loop_start
		j+=1
	print('\n\n\n')
else:
	print('\n\nThere is no such file\n', end='\n')

#to do: a proper compiler must have custom error messages, so should this translator.