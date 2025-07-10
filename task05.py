class product:
    def __init__(self, name, price, category, in_stock):
        self.name = name 
        self.price = price
        self.category = category
        self.in_stock = in_stock

narx_str = "300$"
narx = int(narx_str.replace("$", ""))
new_product = product("Telefon", narx, "elektronika", True)
print(f"Mahsulot: {new_product.name}")
print(f"Mahsulot narxi: {new_product.price}")
print(f"Mahsulot turi: {new_product.category}")
print(f"Mahsulot bormi: {new_product.in_stock}")
        