from semantics3 import Products
import keys
import json

def recommendation_data(name, brand):
    k = keys.Keys()
    sem3 = Products(
        api_key = k.get_semantics_api_key(),
        api_secret = k.get_semantics_secret_key()
    )

    sem3.products_field("search", "iphone")
    sem3.products_field("brand", "apple")
    sem3.products_field("limit", 10)
    results = sem3.get()

    output = []

    for r in results["results"]:
        data = {}
        data['image'] = r["images"][0]
        data['url'] = r['sitedetails'][0]["url"]
    
        try:
            data['price'] = r['sitedetails'][0]["latestoffers"][0]["price"]
        except:
            pass
        
        data['brand'] = r['brand']
        data['name'] = r['name']
        output.append(data)
        print(data)
    return output

recommendation_data("macbook", "apple")
