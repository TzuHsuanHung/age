driving = input('你有開過車嗎？')
if driving != '有' and driving!='沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = input('今年幾歲？')
age = int(age)

if driving == '有':
	if age >= 18:
		print(age , '歲了，行車注意安全，安心上路')
	else:
		print('為什麼你開過車了？！')
elif driving == '沒有':
	if age >= 18:
		print('要試著考看看嗎？會方便很多喔！')
	else:
		print('等你18歲就可以考了')

else:
	print('只能輸入 有/沒有')