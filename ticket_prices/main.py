def main():
    price = 0

    count_ticket = int(input("Введите количество билетов: "))
    for num_ticket in range(1, count_ticket + 1):
        age = int(input(f"Билет №{num_ticket} - Введите возраст посетителя: "))

        if age < 18:
            continue
        elif 18 <= age < 25:
            price += 990
        else:
            price += 1390

    if count_ticket > 3:
        price *= 0.9

    print(f"Общая стоимость билетов: {price}")


if __name__ == '__main__':
    main()
