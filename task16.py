class Product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock

product1 = Product("AirPods", 129.99, True)
product2 = Product("iPhone 13", 999.99, True)
product3 = Product("MacBook", 1499.99, True)
product4 = Product("iPad", 399.50, True)
product5 = Product("Apple Watch", 299.00, True)

products = [product1, product2, product3, product4, product5]

total_price = sum(p.price for p in products if p.in_stock)
print(f"Ombordagi mahsulotlar narxi: {total_price.:f}")
