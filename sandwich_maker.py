class SandwichMaker:
    def __init__(self):
        self.resources = {
            "bread": 5,
            "chicken": 3,
            "beef": 5,
            "tuna": 2
        }

    def report(self):
        print(f"Bread: {self.resources['bread']}")
        print(f"Chicken: {self.resources['chicken']}")
        print(f"Beef: {self.resources['beef']}")
        print(f"Tuna: {self.resources['tuna']}")

    def is_resource_sufficient(self, sandwich):
        can_make = True
        for item in sandwich.ingredients:
            if sandwich.ingredients[item] > self.resources[item]:
                print(f"Sorry there isn't enough {item}.")
                can_make = False
        return can_make

    def make_sandwich(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}🥪 . Enjoy!")