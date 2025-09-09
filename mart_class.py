class Mart:
    def __init__(self, name, address, items):
        self.name = name
        self.address = address
        self.items = items if items is not None else {}  # берёт переданный или создаёт пустой словарь: {name: price}
        ''' 
        - `name`: название магазина.
        - `address`: адрес магазина.
        - `items`: словарь, где ключ - название товара, значение - цена. типа `{'apples': 0.5, 'bananas': 0.75}`.
        '''

# -  метод добавления товара
    def add_item(self, item_name, price):
        self.items[item_name] = price

# - метод удаления товара
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

# - метод получения цены товара по названию. Если товара нет, возвращает `None`.
    def get_item_price(self, item_name):
        price = self.items.get(item_name, "товар не найден")
        return price

# - метод обновления цены товара.
    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"товар '{item_name}' не найден")


