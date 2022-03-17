#while05-05.py
cnt=1
col = int(input('col number=>'))
row = int(input('row number=>'))

if col<=0 or row<=0:
	print('invalid')
else:
	while cnt<=row:
		cnt_c =1
		while cnt_c<=col:
			if cnt==1 or cnt== row:
				if cnt_c==1 or cnt_c==col:
					print('■', end ='')
				else:
					print('□',end='')	
			else:
				print('□',end='')
			cnt_c=cnt_c+1
		cnt=cnt+1
		print()