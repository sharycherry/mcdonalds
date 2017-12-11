import json
import sqlite3
import os.path

# create database
def create_database(data, db):
	c = db.cursor()
	c.execute('CREATE TABLE nutrition (product varchar(20) , category varchar(20), calories, calories_from_fat, protein, carbohydrates, sugars)')

	query = 'INSERT INTO nutrition (product, category, calories, calories_from_fat, protein, carbohydrates, sugars) VALUES(?,?,?,?,?,?,?)'
	columns = ['calories', 'calories from fat', 'protein', 'carbohydrates', 'sugars']

	for category, itemlists in data.items():
		for product, nutrition in itemlists.items():
			keys = (product, category,) + tuple(nutrition[c] for c in columns)
			# print(keys)
			c = db.cursor()
			c.execute(query, keys)
			c.close() 

	db.commit()
	db.close()  


# retrieve data from database
if os.path.isfile('data.db') == False:
	data = json.load(open('data.json'))
	db = sqlite3.connect('data.db')
	create_database(data, db)
else:
	conn = sqlite3.connect('data.db')
	cursor = conn.cursor()
	print("category: desserts & shakes\n")
	print("product, category, calories, calories_from_fat, protein, carbohydrates, sugars\n")
	for row in cursor.execute('select * from nutrition where category = "desserts & shakes"; '):
		print(row)
	cursor.close()