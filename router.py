from flask import Flask, flash, redirect, render_template, request, url_for, g
import json
from pprint import pprint
from cons import DATA
import random


app = Flask(__name__)
app.debug = True

# create a global variable to store the recommendations(because we need to use it in two routes)
choices = []

@app.route('/')
def display():
	food_types = ['Vegetarian', 'Chicken', 'Beef']
	nutrition_types = ['Calories', 'Protein', 'Carbohydrates', 'Sugars']
	dessert_types = list(DATA["desserts & shakes"].keys())
	dessert_types.append("None")
	drink_types = list(DATA["drinks"].keys())
	drink_types.append("None")

	# pass the data food_types, nutrition_types, dessert_types, and drink_types to 'display.html' as options
	return render_template('display.html', food_types=food_types, nutrition_types=nutrition_types, 
		dessert_types=dessert_types, drink_types=drink_types)

@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
	dic = {'Beef': 'burgers', 'Chicken': 'chicken & sandwiches', 'Vegetarian': 'snacks & sides'}
	# get data from form options in 'recommendations.html'
	food_type = request.form.get('food_types')
	nutrition_type = request.form.get('nutrition_types').lower()
	threshold = float(request.form['text'])
	category = dic[food_type]

	dessert_type = request.form.get('dessert_types')
	drink_type = request.form.get('drink_types')

	# only choose the drink_type, so set the dessert_nutrition to zero
	if dessert_type == 'None':
		dessert_nutrition = 0
	else:
		dessert_nutrition = float(DATA["desserts & shakes"][dessert_type][nutrition_type])

	if drink_type == 'None':
		drink_nutrition = 0
	else:
		drink_nutrition = float(DATA["drinks"][drink_type][nutrition_type])

	# import global variable to use it
	global choices
	choices = []
	products = DATA[category]
	
	# calculate the sum of nutrition value, if less than threshold, add to choics
	if dessert_nutrition == 0 and drink_nutrition == 0:
		for product, nutrition in products.items():
			if nutrition[nutrition_type] < threshold:
				choices.append([product])
	elif drink_nutrition == 0:
		for product, nutrition in products.items():
			if nutrition[nutrition_type] + dessert_nutrition < threshold:
				choices.append([product, dessert_type])
	elif dessert_nutrition == 0:
		for product, nutrition in products.items():
			if nutrition[nutrition_type] + drink_nutrition < threshold:
				choices.append([product, drink_type])
	else:
		for product, nutrition in products.items():
			if nutrition[nutrition_type] + drink_nutrition + dessert_nutrition < threshold:
				choices.append([product, drink_type, dessert_type])
	return render_template('result.html', choices=choices)


@app.route('/random', methods=['GET', 'POST'])
def random_recom():
	global choices
	# index from 0 to len(choices) - 1
	index = random.randint(0,len(choices))
	print(index)
	return render_template('random.html', choice=choices[index])


if __name__ == '__main__':
	app.run()