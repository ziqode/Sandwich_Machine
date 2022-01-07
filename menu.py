class MenuItem:
    def __init__(self, name, bread, chicken, beef, tuna, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "bread": bread,
            "chicken": chicken,
            "beef": beef,
            "tuna": tuna
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="chicken", bread=1, chicken=1, beef=0, tuna=0, cost=3.5),
            MenuItem(name="beef", bread=1, chicken=0, beef=1, tuna=0, cost=5.0),
            MenuItem(name="tuna", bread=1, chicken=0, beef=0, tuna=1, cost=4.2),
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_sandwich(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
