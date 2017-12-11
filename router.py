from flask import Flask
from flask import g
from flask import request
import json
from pprint import pprint
from cons import DATA


app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Welcome to the Recommendation System for McDonald!'

@app.route('/get')
def get_products():
	product = request.args.get('product')
	sortby = request.args.get('sortby')
	reverse = request.args.get('reverse')
	if sortby == None:
		products = list(DATA.get(product).keys()) 
	else:
		products = DATA.get(product)
		products = [(p, n[sortby]) for p, n in products.items()]
		products = sorted(products, key=lambda x: x[1], reverse=(not reverse==None))
		pprint(products)
		# products = sorted(products.items(), key=lambda x: x[1][sortby])
		# products = ['{} ({})'.format(p, n) for p, n in products]
	return json.dumps(products)

@app.route('/recommend_one')
def recommend_one():
	category = request.args.get('category')
	nutrition_type = request.args.get('type')
	threshold = float(request.args.get('max'))
	choices = []
	products = DATA[category]
	for product, nutrition in products.items():
		if nutrition[nutrition_type] < threshold:
			choices.append((product, nutrition[nutrition_type]))
	return json.dumps(choices)

@app.route('/recommend_two')
def recommend_two():
	choices = []
	category1 = request.args.get('category1')
	category2 = request.args.get('category2')
	nutrition_type = request.args.get('type')
	threshold = float(request.args.get('max'))

	products1 = DATA[category1]
	products2 = DATA[category2]
	for product1, nutrition1 in products1.items():
		for product2, nutrition2 in products2.items():
			if nutrition1[nutrition_type] + nutrition2[nutrition_type] < threshold:
				choices.append((product1, product2, nutrition1[nutrition_type] + nutrition2[nutrition_type]))
	return json.dumps(choices)

if __name__ == '__main__':
	app.run()