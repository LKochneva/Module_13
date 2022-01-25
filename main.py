stoimost = []
ticket = int(input("Введите количество билетов:"))
for i in range(1, ticket + 1):
     age = int(input(f"Пожалуйста, укажите возраст {i} покупателя:"))
     if age < 18:
         stoimost.append(0)
     elif 18 <= age < 25:
         stoimost.append(990)
     else:
         stoimost.append(1390)
if ticket > 3:
    itogo_skidka = sum(stoimost) - sum(stoimost) * 10 / 100
    print("Вы выбрали больше 3 билетов, сумма вашей покупки со скидкой составит:", itogo_skidka)
else:
    itogo = sum(stoimost)
    print("Сумма вашей покупки: ", itogo)

