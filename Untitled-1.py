from pprint import pprint


def get_recipes(file_name):
    cook_book = {} # Создаем пустой словарь cook_book
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            dish = file.readline().strip()  # возвращает строку без пробелов
            cook_book[dish] = []

            num = int(file.readline().strip())
            for _ in range(num):
                words = file.readline().strip().split('|')
                cook_book[dish].append(
                    {
                        'ingredient_name': words[0].strip(),
                        'quantity': int(words[1].strip()),
                        'measure': words[2].strip()
                    }
                )

            if not file.readline():
                break

    return cook_book # возвращает словарь

def get_shop_list_by_dishes(dishes, person_count):
    ingr_dict = dict() # создаем пустой словарь

    for dish_name in dishes: # проходим циклом по списку 
        if dish_name in cook_book: # если есть ключ в словаре cook-book
            for ings in cook_book[dish_name]: # проходим циклом по ключу словаря
                meas_quan_list = dict() # создаем еще один словарь
                if ings['ingredient_name'] not in ingr_dict: # если нет ингредиента в словаре 
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_dict[ings['ingredient_name']] = meas_quan_list # формируем словарь ingr_dict
                else:
                    ingr_dict[ings['ingredient_name']]['quantity'] = ingr_dict[ings['ingredient_name']]['quantity'] + \
                        ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_dict # Возвращаем словарь


cook_book = get_recipes('recipes.txt')
pprint(cook_book)

pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))


