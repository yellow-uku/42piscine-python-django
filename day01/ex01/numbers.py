def numbers():
	with open('numbers.txt', 'r') as f:
		l = f.read().strip('\n').split(',')
		for num in l:
			print(num)

if __name__ == '__main__':
	numbers()
