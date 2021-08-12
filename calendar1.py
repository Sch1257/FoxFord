# This Python file uses the following encoding: utf-8
from tkinter import Tk, Canvas
from datetime import datetime, date

def get_events(filename):
    date_list = []
    name_list = []
    with open(filename, encoding='utf-8') as file:
        for line in file:
            # удаляем символ перевода строки
            line = line.rstrip('\n')
            # разделяем строку на 2 части по запятой
            text = line.split(',')
            #print(text[1], text[0])

            # Преобразуем второй элемент из строки в дату

            # date = datetime.strptime("21/11/06", "%d/%m/%y").date()
            date = datetime.strptime(text[1], '%d/%m/%y').date()
            name = text[0]
            date_list.append(date)
            name_list.append(name)
    return(name_list, date_list)

def days_till_deadline(now, deadline, name):
    if now > deadline:
        period = now - deadline
        message = 'Праздник {} уже прошел {} дней назад.\nЭто был {}.'\
                    .format(name, period.days, wich_weekday(date.weekday(deadline)))
    elif now.day == deadline.day and now.month == deadline.month and now.year == deadline.year:
        message = ("{} сегодня".format(name))
    else:
        period = deadline - now
        message = ("До праздника {} осталось {} дней.\nЭто будет {}."
                   .format(name, period.days, wich_weekday(date.weekday(deadline))))
    return message
def wich_weekday(weekday):
    get_weekday = 0
    if weekday == 0:
        get_weekday = "Понедельник"
    if weekday == 1:
        get_weekday = "Вторник"
    if weekday == 2:
        get_weekday = "Среда"
    if weekday == 3:
        get_weekday = "Четверг"
    if weekday == 4:
        get_weekday = "Пятница"
    if weekday == 5:
        get_weekday = "Суббота"
    if weekday == 6:
        get_weekday = "Воскресенье"
    return get_weekday

event_name_list, event_date_list = get_events("events.txt")

today = date.today()

#for i in range(len(event_name_list)):
#    print(days_till_deadline(today, event_date_list[i], event_name_list[i]))

root = Tk()
root.title("Календарь ожиданий")
#root.geometry("600x600")
canvas = Canvas(root, width=600, height=600, bg="Aqua")
canvas.pack()
canvas.create_text(100, 50, anchor='w', fill='black', font='Timesnewroman 20 bold underline',
                   text = "Первое приложение. \nКалендарь ожидания.")
vertical_space = 120

for i in range(len(event_date_list)):
    display = days_till_deadline(today,event_date_list[i], event_name_list[i])
    canvas.create_text(50, vertical_space, anchor='w', fill='blue', font='Arial 15 bold', text=display)
    vertical_space += 70

root.mainloop()
