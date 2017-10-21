from semantics3 import Products
import keys

sem3 = Products(
    api_key = keys.get_semantics_api_key(),
    api_secret = keys.get_semantics_secret_key()
)

sem3.products_field("search", "iphone")
results = sem3.get()

print(results)
