from mart_class import Mart

mart1 = Mart("Продукты", "ул.Горького, 14", {})

mart1.add_item('молоко', 100)
mart1.add_item('хлеб', 50)

print("Магазин:", mart1.name)
print("Товары:", mart1.items)
print("Цена молока:", mart1.get_item_price('молоко'))
print("Цена сыра:", mart1.get_item_price('сыр'))

mart1.update_item_price('молоко', 120)

print("Цена молока:", mart1.get_item_price('молоко'))

#************************
mart2 = Mart("ГастроГном", "ул. Кукушкинда,1", {"колбаса":700, 'хлеб':55, "сок":120, "сыр": 1200} )

print("Магазин:", mart2.name)
print("Товары:", mart2.items)
print("Цена молока:", mart2.get_item_price('молоко'))
print("Цена сыра:", mart2.get_item_price('сыр'))

mart2.update_item_price('молоко', 120)

#************************
mart3 = Mart("ГастроОй", "ул. Рабочего Класса,8", {"колбаса":777, 'хлеб':55, "сок":123, "сыр": 1234} )

print("Магазин:", mart2.name)
print("Товары:", mart2.items)
print("Цена молока:", mart2.get_item_price('молоко'))
print("Цена сыра:", mart2.get_item_price('сыр'))

mart2.update_item_price('молоко', 120)

