from _future_ import print_function

source_code=list(raw_input('\n\nGive the brainfuck code:\n\n\t'))
print('\n\nProgram is being executed.\n\n\tInput-Output:\n\n\n')
l=len(source_code)
registry1=[0]*30000
i=0
j=0
k=0
loop_start=[]
while j<l:
	if source_code[j]=='>':
		if i<29999:
			i+=1
		else:
			print("\nError 1: Registry index out of range.")
	elif source_code[j]=='<':
		if i>0:
			i-=1
		else:
			print("\nError 1: Registry index out of range.")
			break
	elif source_code[j]=='+':
		if registry1[i]<255:
			registry1[i]+=1
		else:
			print("\nError 2: Registry value overflow.")
			break
	elif source_code[j]=='-':
		if registry1[i]>0:
			registry1[i]-=1
		else:
			print("\nError 3: Registry value can't be negative.")
			break
	elif source_code[j]==',':
		#print('make input pretty? no?')
		try:
			registry1[i]=ord(raw_input())
		except:
			print("\nError 4: Invalid value.")
			break
	elif source_code[j]=='.':
		print(chr(registry1[i]),end='')
	elif source_code[j]=='[':
		k+=1
		if len(loop_start)<k:
			loop_start.append(j)
		else:
			loop_start[k-1] = j
	elif source_code[j]==']':
		if registry1[i]!=0:
			j=loop_start[k-1]
		else:
			k-=1
	j+=1
print('\n\n\n')
