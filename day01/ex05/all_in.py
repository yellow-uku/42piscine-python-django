import sys


def search_value(d, val):
	for key, value in d.items():
		if val.upper() == value.upper():
			return key
	return 'Unknown city'

def search_key(d, val):
	for key, value in d.items():
		if val.upper() == key.upper():
			return value
	return 'Unknown state'

def get_state_or_capital(token):
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
		}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	value_token = ''
	key_token = ''

	
	if token in capital_cities.values():
		short_state = search_value(capital_cities, token)
		key_token = search_value(states, short_state)
		value_token = token
	elif token in states.keys():
		short_state = search_key(states, token)
		value_token = search_key(capital_cities, short_state)
		key_token = token
	return key_token, value_token

def all_in_py():

	if len(list(sys.argv)) == 2:
		l_input = sys.argv[1].split(',')
	#	print(l_input)
		for token in l_input:
			token = token.strip()
	#		print(token+'$')
			if token:
				state, capital = get_state_or_capital(token)
		#		print(capital, '-', state)
				if token == capital:
					print(capital, 'is the capital of', state)
				elif token == state:
					print(state, 'is the state of', capital)
				else:
					print(token, 'is neither a capital city nor a state')

if __name__ == '__main__':
	all_in_py()