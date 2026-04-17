class Product:
    total_products = 0

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        Product.total_products += 1

    def info(self):
        return f"Mahsulot: {self.name} - {self.price} so‘m | Jami mahsulotlar: {Product.total_products}"

p1 = Product("P001", "Telefon", 2500000)
print(p1.info())
