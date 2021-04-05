# This Python file uses the following encoding: utf-8

import random
print("Тест по математике для 1 класса")
print("Сколько примеров будет в тесте?")
number_of_tasks = int(input())

score = 0
max_ball_for_task = 2

for i in range(number_of_tasks):
    print('Решите задачу/пример')
    if i == 0:
        print("В одном пенале 6 карандашей, а во втором -  2 каранадаша. Сколько карандашей в двух пеналах?")
        answer = 8

    elif i == 1:
        print('В связке 5 красных шариков и 2 синих. Сколько всего в связке красных и синих шариков?')
        answer = 7

    elif i == 2:
        print("Брату 8 лет. А сестра старше брата на 2 года. Сколько лет сестре?")
        answer = 10

    elif i == 3:
        print("В корзине было 8 мячей. Из корзины взяли 2 мяча. Сколько мячей осталось в корзине?")
        answer = 6

    elif i == 4:
        print("На большой льдине 6 пингвинов. А на маленькой 2. Сколько пингвинов на большой льдине?")
        answer = 6
    else:
        # generate and print the plus task
        a = random.randrange(0, 10)
        b = random.randrange(0, 10)

        print(str(a) + "+" + str(b) + "=")
        answer = a + b

    print('Введите ответ')
    # wait for input and validate

    attempts = max_ball_for_task
    while attempts >= 1:
        if int(input()) == answer:
            score += attempts
            print("Ответ верный. У вас {} баллов".format(score))
            break
        else:

            attempts -= 1
            if attempts != 0:
                print("Ответ неверный. Попробуйте еще раз.")
    if attempts == 0:
        print("Ответ неверный. Верный ответ" + " " + str(answer))




# print the total score
print(str(score * 100 / (max_ball_for_task * number_of_tasks)) + "% решено верно")