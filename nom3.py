import random as rnd


def my_int_input():
    while 1:
        try:
            inp = int(input())
            if 0 >= inp or inp > 3:
                print("Введенное число долно быть в диапозоне от 0 до 3")
                continue
            if col_kam - inp <= 0:
                print("Вы обязаны оставить хотя бы 1 камень в куче")
                continue
        except ValueError:
            print("Некорктный ввод. Введите число от 0 до 3")
            continue
        return inp


def step_ai(kucha):
    if kucha == 2:
        return 1
    if kucha == 3:
        return 2
    if kucha == 4:
        return 3

    return rnd.randint(1, 3)


def check_to_win(sbkt, kucha):
    if kucha == 1:
        print(sbkt, "Win!")
        exit()


col_kam = rnd.randint(4, 30)

while 1:
    print("Колоичество камней:", col_kam, "\nДелайте ход. Сколько камнй возмёте?")

    col_kam -= my_int_input()
    check_to_win("Игрок", col_kam)

    ai_hod = step_ai(col_kam)
    col_kam -= ai_hod
    print("Ход  компютера: ", ai_hod)
    check_to_win("Конмпютер", col_kam)

#dddsdfssdfs
#g