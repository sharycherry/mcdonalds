## Usage

1.install required packages (bs4, requests)

```
pip install -r requirements.txt
```

2.run crawler.py to automatically extract food nutrition information from the McDonald's website. And the output is 'data.json'.

```
python crawler.py
```
3.run db.py to save the data into database (7 columns: product, category, calories, calories_from_fat, protein, carbohydrates, sugars). And the executed result is the data of category 'desserts & shakes'.

```
python db.py
```

4.run recommendation.py to get the demo recommendations (
recommendation for breakfast under 350 calories and recommendation for burgers and drinks under 400 calories)

```
python recommendation.py
```

5.run router.py, and the server will run on http://127.0.0.1:5000/.

```
python router.py
```
You can visit the following urls for corresponding functions:

* Get product details

Given product category, and/or the nutrition type to be sorted, and/or the sort order, show corresponding results

Example:

```
http://127.0.0.1:5000/get?product=breakfast
http://127.0.0.1:5000/get?product=burgers&sortby=sugars
http://127.0.0.1:5000/get?product=breakfast&sortby=calories&reverse=false
```
* Get Recommendation for one category

Given product category, nutrition type, and its threshold, show the recommendations.

Example:

```
http://127.0.0.1:5000/recommend_one?category=burgers&type=calories&max=500
http://127.0.0.1:5000/recommend_one?category=drinks&type=sugars&max=30
```

* Get Recommendation for one category

Given product category1, product category2, nutrition type, and its threshold, show the recommendations.

Example:

```
http://127.0.0.1:5000/recommend_two?category1=burgers&category2=drinks&type=calories&max=300
```
