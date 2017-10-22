from flask import jsonify
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import http.client
import requests
import ast
import semantics

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

def search_by_product_name(name):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    text = name
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    #sentiment = client.analyze_sentiment(document=document).document_sentiment

    #text_val = ('Text: {}'.format(text))
    #sentiment_score = ('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    return search_backend(text)

def search_backend(text):
    url = "http://6197757d.ngrok.io/api/post/search"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"substring\"\r\n\r\n" + text+ "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "ab6c3b80-1ccb-9138-a34c-875cd2b78733"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    res_list = ast.literal_eval(response.text)
    #rec = semantics.get_recommendations(text)
    #output = res_list + rec['results']
    print(res_list)
   
search_by_product_name("iPhone")