def my_var():
	num = 42
	string1 = '42'
	string2 = 'quarante-deux'
	float = 42.0
	bool = True
	l = [42]
	d = {42: 42}
	t = (42, )
	s = set()

	print(num, 'has a type', type(num))
	print(string1, 'has a type', type(string1))
	print(string2, 'has a type', type(string2))
	print(float, 'has a type', type(float))
	print(bool, 'has a type', type(bool))
	print(l, 'has a type', type(l))
	print(d, 'has a type', type(d))
	print(t, 'has a type', type(t))
	print(s, ' has a type ', type(s), sep='')

if __name__ == '__main__':
	my_var()
