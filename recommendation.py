import json
from pprint import pprint
from cons import DATA

def recommend_one(category, nutrition_type, threshold):
	choices = []
	products = DATA[category]
	for product, nutrition in products.items():
		if nutrition[nutrition_type] < threshold:
			choices.append(product)
	pprint(choices)

def recommend_two(category1, category2, nutrition_type, threshold):
	choices = []
	products1 = DATA[category1]
	products2 = DATA[category2]
	for product1, nutrition1 in products1.items():
		for product2, nutrition2 in products2.items():
			if nutrition1[nutrition_type] + nutrition2[nutrition_type] < threshold:
				choices.append((product1, product2, nutrition1[nutrition_type] + nutrition2[nutrition_type]))
	pprint(choices)

recommend_one('breakfast', 'calories', 500)

recommend_two('burgers', 'drinks', 'calories', 800)