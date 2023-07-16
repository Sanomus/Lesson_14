class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict) -> None:
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name: str, cuisine: str, menu: dict, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish: dict, quantity: int) -> float:
        if menu_dict.get(dish):
            if menu_dict[dish]['quantity'] - quantity >= 0:
                menu_dict[dish]['quantity'] = menu_dict[dish]['quantity'] - quantity
                cost = menu_dict[dish]['price'] * quantity
                return print(f'Your order cost: {cost}')
            else:
                return print('Requested quantity not available')
        else:
            return print('Dish not available')
     

menu_dict = {
    'Khung Pao Chicken': {'price': 20.00, 'quantity': 5},
    'Laksa Shiritaki': {'price': 15.50, 'quantity': 5},
    'Miso Butter Roast Chicken': {'price': 25.50, 'quantity': 12},
    'Indonesian Nasi Goreng': {'price': 12.50, 'quantity': 7},
    'Korean Bibimbab': {'price': 17.50, 'quantity': 6},
    'Double Beef Humburger': {'price': 3.95, 'quantity': 13}, 
    'Cheeseburger': {'price': 2.80, 'quantity': 8},
    'French fries': {'price': 1.85, 'quantity': 15}, 
}

mixed_restaurant = FastFood('AsianBurgerMix', 'FastFood', menu_dict, True)
mixed_restaurant.order('Khung Pao Chicken', 5)
mixed_restaurant.order('Korean Bibimbab', 7)
mixed_restaurant.order('Pepsi', 7)
