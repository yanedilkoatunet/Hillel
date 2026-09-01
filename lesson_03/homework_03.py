# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
    "Would you tell me, please, which way I ought to go from here?\n"
    "That depends a good deal on where you want to get to, said the Cat.\n"
    "I don't much care where —— said Alice.\n"
    "Then it doesn't matter which way you go, said the Cat.\n"
    "—— so long as I get somewhere, Alice added as an explanation.\n"
    "Oh, you're sure to do that, said the Cat, if you only walk long enough."
)
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
print(alice_in_wonderland.count("'"))
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)
"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
azov_sea_area = 37800
black_sea_area = 436402
full_area = azov_sea_area + black_sea_area
print(full_area)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
first_second_storage = 250449
second_third_storage = 222950
all_storage = 375291
third = all_storage - first_second_storage
print(third)
first = all_storage - second_third_storage
print(first)
second = all_storage - (third + first)
print(second)


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
pc_price = 1179 * 18
print(pc_price)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(8019 % 8)
print(9907 % 9)
print(2789 % 5)
print(7248 % 6)
print(7128 % 5)
print(19224 % 9)
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza = 274
medium_pizza = 218
juice = 35
cake = 350
water = 21

final_price = (big_pizza*4) + (medium_pizza*2) + (juice*4) + cake + (water*3)
print(final_price)
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
pictures = 232
one_page = 8
all_pages = 232 // 8
print(all_pages)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
fuel_per_hundred = 9
tank_capacity = 48
all_fuel = (distance // 100) * fuel_per_hundred
print(all_fuel)
fuel_stop = all_fuel // tank_capacity
print(fuel_stop)
