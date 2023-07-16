class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name: str, price: float, quantity: int, author: str):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f'Book name: {self.name}')
        print(f'Price: {self.price}')
        print(f'Rest: {self.quantity}')
        print(f'Author: {self.author}')


book = Book('The Selfish Gene', 10.99, 10, 'Richard Dawkins')
book.read()
