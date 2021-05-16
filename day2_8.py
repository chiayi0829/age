driving = input('你有沒有開過車（有/沒有）？')
if driving != '有' and driving != '沒有':
	print('請回答有或沒有！')
	raise SystemExit
age = input('請問你的年齡是？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了！')
	else:
		print('偷開車ㄛ！')
elif driving == '沒有':
	if age >= 18:
		print('你怎麼沒去考駕照呢？')
	else:
		print('真是個乖寶寶！')