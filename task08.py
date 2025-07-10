class product:
    def __init__(self, name, price, category, in_stock):
        self.name = name 
        self.price = price
        self.category = category
        self.in_stock = in_stock


    def chek_stock(self):
        if self.in_stock:
            print(f"{self.name} omborda mavjud ✅")
        else:
            print(f"{self.name} hozirda tugagan ❌")
            
p1 = product("Airpods", 90.0, "electronic", True)
p2 = product("Airpods", 900.0, "electronic", False)

p1.chek_stock()
p2.chek_stock()