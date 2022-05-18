import sys

def search_key(d, val):
	for key, value in d.items():
		if val == key:
			return value
	return 'Unknown state'

def capital_city():
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
		state = sys.argv[1]
		short_state = search_key(states, state)
		capital = search_key(capital_cities, short_state)
		print(capital)

if __name__ == '__main__':
	capital_city()