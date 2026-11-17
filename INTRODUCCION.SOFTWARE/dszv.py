class Patron:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone

class FoodItem:
    def __init__(self, name, price,):
        self.name = name
        self.price = price
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price

class MealOrder:
    def __init__(self, patron, FoodItems):
        self.patron = patron
        self.item = [FoodItem]
    def get_patron(self):
        return self.patron
    def get_items(self):
        return self.item

FoodItem1 = FoodItem("Vegetable soup", 45.0)
FoodItem2 = FoodItem("Chicken sandwich", 65.0)

patron1 = Patron ("Daniel", "Daniel@example.com", "4941186065")
patron2 = Patron("Diego", "Diego@example.com", "4942256895")

order1 = MealOrder (patron1, FoodItem1)

print ("objeto, patron1")
print ("nombre:" + patron1.name)
print ("email:" + patron1.email)
print ("phone:" + patron1.phone)

print ("objeto, patron2")
print ("nombre:" + patron2.name)
print ("email:" + patron2.email)
print ("phone:" + patron2.phone)

print ("objeto, patron1")
print ("nombre:" + patron1.get_name())
patron1.set_name("Hector Daniel")
print ("nombre:"+ patron1.get_name())

print ("objeto, patron2")
print ("nombre:" + patron2.get_name())
patron2.set_name("Diego Guijarro")
print ("nombre:"+ patron2.get_name())

print ("objeto, patron1")
print ("email:" + patron1.get_email())
patron1.set_email("dani@gmail.com")
print ("email:"+ patron1.get_email())

print ("objeto, patron2")
print ("email:" + patron2.get_email())
patron2.set_email("die@gmail.com")
print ("email:"+ patron2.get_email())

print ("objeto, patron1")
print ("phone:" + patron1.get_phone())
patron1.set_phone("4925563265")
print ("phone:"+ patron1.get_phone())

print ("objeto, patron2")
print ("phone:" + patron2.get_phone())
patron2.set_phone("4956325687")
print ("phone:"+ patron2.get_phone())

print ("nombre:" + FoodItem1.name)
print ("price:" + str(FoodItem1.price))

print ("nombre:" + FoodItem2.name)
print ("price:" + str(FoodItem2.price))

order1 = MealOrder (patron1, FoodItem1)
order_patron = order1.get_patron()
print(order_patron.get_name())

order_items = order1.get_items()
first_item = order_items[0]
print(first_item.get_name())
print(first_item.get_price())

