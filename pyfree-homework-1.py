# Бортников Арсений для Нетология
# Домашнее задание к занятию 1. Знакомство с Python
# Дата выполнения: 14.05.2022

# Задание 1
date_today = input('Введите дату:\n')
objective_today = input('Введите задачу:\n')

print(date_today, objective_today);

# Задание 2
date_today = input('Введите дату:\n')
objective_today = input('Введите задачу:\n')

date_tomorrow = input('Введите дату:\n')
objective_tomorrow = input('Введите задачу:\n')

today = date_today + " " + objective_today
tomorrow = date_tomorrow + " " + objective_tomorrow

print(today);
print(tomorrow);

# Задание 3
date_today_input = input('Введите дату:\n')
objective_today_input = input('Введите задачу:\n')

date_tomorrow_input = input('Введите дату:\n')
objective_tomorrow_input = input('Введите задачу:\n')

dictionary = {
   'date_today': date_today_input,
   'objective_today': objective_today_input,
   'date_tomorrow': date_tomorrow_input,
   'objective_tomorrow': objective_tomorrow_input
}
