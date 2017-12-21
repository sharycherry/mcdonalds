## Usage

1.install required packages (bs4, requests)

```
pip install -r requirements.txt
```

2.run crawler.py to automatically extract food nutrition information from the McDonald's website. And the output is 'data.json'.

```
python crawler.py
```
3.run db.py to save the data into database (7 columns: product, category, calories, calories\_from_fat, protein, carbohydrates, sugars). And the executed result is the data of category 'desserts & shakes'.

```
python db.py
```

4.run router.py, and the server will run on http://127.0.0.1:5000/.

```
python router.py
```
You will see a page showing some drop-down options.

1.food type(Beef, Chicken, Vegetarian)

2.nutrition type

3.dessert or shake (you can select 'None')

4.drink (you can select 'None')

5.input the nutrition threshold

After selecting what you want, click the 'go' button to get recommendations. Then you can click the roll image in the recommendation page to get a random recommendation.