class productBuyingError(Exception):
    pass


class Product:
    def __init__(self, price, p_id, quantity):
        self.price = price
        self.p_id = p_id
        self.quantity = quantity

    def __repr__(self):
        return "Details of the product: Price - {}, Product ID - {}, Product quantity - {}".format(self.price, self.p_id,
                                                                                              self.quantity)

    def buy(self, buying_count):
        if type(buying_count) == int and buying_count <= self.quantity:
            self.quantity -= buying_count

        else:
            raise productBuyingError("Please insert an integer which is equal or les than the product quantity")

    def get_by_id(self, new_id):
        if self.p_id == new_id:
            return self


class Inventory:
    def __init__(self, p_list: list):
        self.p_list = p_list

    def __repr__(self):
        return 'List of products by their ID-s: {}'.format(self.p_list)

    def sum_of_products(self):
        my_sum = 0
        for i in self.p_list:
            my_sum += Product.get_by_id(i).quantity
        return my_sum


p1 = Product(4000, 1, 50)
p2 = Product(7000, 2, 20)
p3 = Product(1000, 3, 55)
i1 = Inventory([p1.p_id, p2.p_id, p3.p_id])
# print(i)
# print(p1)
# p1.buy(6)
# print(p1)
# p2.buy(30)

p1.get_by_id(1)
print(i1.sum_of_products())

