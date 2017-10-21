from semantics3 import Products
import keys
import json

k = keys.Keys()
sem3 = Products(
    api_key = k.get_semantics_api_key(),
    api_secret = k.get_semantics_secret_key()
)

sem3.products_field("search", "iphone")
sem3.products_field("brand", "apple")
sem3.products_field("variation_includeall", 0)
sem3.products_field("limit", 7)
results = sem3.get()

for r in results["results"]:
    print(r["images"][0])
    print(r['sitedetails'][0]["url"])
    print(r['sitedetails'][0]["latestoffers"][0]["price"])
    print(r['brand'])
    print(r['name'])
