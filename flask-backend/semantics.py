from semantics3 import Products
import keys
import json

def get_recommendations(name, brand=None):
    k = keys.Keys()

#    categories = Categories(
 #       api_key = k.get_semantics_api_key(),
  #      api_secret = k.get_semantics_secret_key()
  #  )

    products = Products(
        api_key = k.get_semantics_api_key(),
        api_secret = k.get_semantics_secret_key()
    )

    products.products_field("search", name)
    if brand != None:
        products.products_field("brand", brand)
    products.products_field("variation_includeall", 0)
    products.products_field("limit", 10)
    results = products.get()

    output = []

    for r in results["results"]:
        data = {}
        try:
            data['image'] = r["images"][0]
        except:
            pass
        data['url'] = r['sitedetails'][0]["url"]

        try:
            data['price'] = r['sitedetails'][0]["latestoffers"][0]["price"]
        except:
            pass
        try:
            data['brand'] = r['brand']
        except:
            pass
        data['title'] = r['name']
        data['status'] = True
        output.append(data)
    return {"results": output}
