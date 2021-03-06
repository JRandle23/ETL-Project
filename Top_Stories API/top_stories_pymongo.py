from bs4 import BeautifulSoup
import requests
import pymongo
import json
import datetime 

# Establish connection 
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.top_stories_nyt
collection = db.business

# URL of page to be scraped - PLEASE USE YOUR API HERE
business_url = "https://api.nytimes.com/svc/topstories/v2/business.json?api-key=YOURAPI"

# Retrieve Business top stories 
response = requests.get(business_url)

# Load results as json document
result = json.loads(response.content)
results = result['results']
results = [{'api': 'topstories' ,'title': x['title'], 'published_date': x['published_date'].split(";")} for x in results]


# Add results to business collection 
collection.insert_many(results)


# ---------------------------------------- #
# POLITICS
db = client.top_stories_nyt
collection = db.politics

# Politics top stories url PLEASE USE YOUR API HERE
politics_url = "https://api.nytimes.com/svc/topstories/v2/politics.json?api-key=YOURAPI"

# Retrieve Politics top stories 
response = requests.get(politics_url)

# Load results as json document
result = json.loads(response.content)
results = result['results']
results = [{'api': 'topstories' ,'title': x['title'], 'published_date': x['published_date'].split(";")} for x in results]

# Add results to politics collection 
collection.insert_many(results)

# ---------------------------------------- #
# US 
db = client.top_stories_nyt
collection = db.us

# US top stories URL - PLEASE USE YOUR API HERE
us_url = "https://api.nytimes.com/svc/topstories/v2/us.json?api-key=YOURAPI"

# Retrieve US top stories 
response = requests.get(us_url)

# Load results as json document
result = json.loads(response.content)
results = result['results']
results = [{'api': 'topstories' ,'title': x['title'], 'published_date': x['published_date'].split(";")} for x in results]

# Add results to US collection 
collection.insert_many(results)

# ---------------------------------------- #
# TECHNOLOGY
db = client.top_stories_nyt
collection = db.technology 

# Technology top stories URL - PLEASE USE YOUR API HERE
tech_url = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=YOURAPI"

# Retrieve Technology top stories 
response = requests.get(tech_url)

# Load results into a json document 
result = json.loads(response.content)
results = result['results']
results = [{'api': 'topstories' ,'title': x['title'], 'published_date': x['published_date'].split(";")} for x in results]

# Add results to technology collection 
collection.insert_many(results)

# ---------------------------------------- #
# OPINION
db = client.top_stories_nyt
collection = db.opinions

# Opinion top stories URL - PLEASE USE YOUR API HERE
opinion_url = "https://api.nytimes.com/svc/topstories/v2/opinion.json?api-key=YOURAPI"

# Retrieve Opinion top stories 
response = requests.get(opinion_url)

# Load results into a json document 
result = json.loads(response.content)
results = result['results']
results = [{'api': 'topstories' ,'title': x['title'], 'published_date': x['published_date'].split(";")} for x in results]

# Add results to Opinion collection 
collection.insert_many(results)

