import json
import sqlite3
import os.path

data = json.load(open('data.json'))
db = sqlite3.connect('data.db')

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

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute('select * from nutrition where category = "desserts & shakes"; ')
print(cursor.fetchall())
cursor.close()