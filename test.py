from number_check import check

phone = input("Введите номер: ")

result = check(phone)

if result:
  print(f"Оператор {result[0]}; Регион: {result[1]}")
else:
  print("Не удалось получить информацию")

input("Press any key")