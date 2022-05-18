import sys

def search_value(d, val):
	for key, value in d.items():
		if val == value:
			return key
	return 'Unknown state'

def state():
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

	if len(list(sys.argv)) == 2:
		capital = sys.argv[1]
		short_state = search_value(capital_cities, capital)
		state = search_value(states, short_state)
		print(state)

if __name__ == '__main__':
	state()