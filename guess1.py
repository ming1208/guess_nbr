import random
start = input('請輸入隨機數字範圍的起始直: ')
end = input('請輸入隨機數字範圍的結束直: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1
	nbr = input('請猜個數字: ')
	nbr = int(nbr)
	if nbr == r:
		print('恭喜!你在第', count, '次猜中了!')
		break
	elif nbr > r:
		print('比答案大!再猜小一點!')
	elif nbr < r:
		print('比答案小!再猜大一點!')
	print('這是你猜的第', count, '次了!')