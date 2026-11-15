count = 0       # Кол-во принятых оценок
sum_grade = 0   # Сумма всех принятых оценок
min_g = 10      # Нач значение мин оценки
max_g = 0       # Нач значение макс оценки

print("Программа анализа оценок студентов")
print("Доступные команды: add 2, add 3, add 4, add 5")
print("Также доступны команды: avg, min, max, exit")

while True: #бесконечн цикл

    command = input("Введите команду: ")  # Получаем команду пользователя

    # оценка
    if command == "add 2":
        grade = 2
    elif command == "add 3":
        grade = 3
    elif command == "add 4":
        grade = 4
    elif command == "add 5":
        grade = 5

    # Если введена команда добавления оценки
    if command == "add 2" or command == "add 3" or command == "add 4" or command == "add 5":

        count = count + 1  # Увеличиваем счетчик на 1
        sum_grade = sum_grade + grade  # Добавляем оценку к общей сумме

        # Проверяем, является ли оценка мин
        if grade < min_g:
            min_g = grade

        # Проверяем, является ли оценка макс
        if grade > max_g:
            max_g = grade

        print("Оценка добавлена:", grade)

    # Вычисляем среднюю оценку
    elif command == "avg":
        if count > 0:
            print("Средняя оценка:", sum_grade / count)
        else:
            print("Оценки ещё не добавлены")

    # Выводим минимальную оценку
    elif command == "min":
        if count > 0:
            print("Минимальная оценка:", min_g)
        else:
            print("Оценки ещё не добавлены")

    # Выводим максимальную оценку
    elif command == "max":
        if count > 0:
            print("Максимальная оценка:", max_g)
        else:
            print("Оценки ещё не добавлены")

    # Завершаем программу
    elif command == "exit":
        print("Программа завершена")
        break

    # Обрабатываем неизвестную команду
    else:
        print("Ошибка: неправильная команда или оценка")
