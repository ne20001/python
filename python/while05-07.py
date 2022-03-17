#while05-07.py
cnt_r =0
cnt_c =0

number = int(input('input number=>'))

row =number //5+1
while cnt_r<row:
	str_output =''
	col =1
	while col <=5:
		cnt_c = cnt_c+1
		if cnt_c>number:
			break
		elif cnt_c%2==1:
			str_output = str_output+'〇'
		elif cnt_c%2==0:
			str_output=str_output+'●'
		col=col+1
	print(str_output)
	cnt_r=cnt_r+1
