HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = []
today = []
tomorrow = []
other = []

while True:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(tasks, today, tomorrow, other)
  elif command == "add":
    task = input("Введите название задачи: ")
    tasks.append(task)
    date = input("Введите дату выполнения задачи: ").lower().lstrip().rstrip()
    if date == "сегодня":
      today.append(date)
    elif date == "завтра":
      tomorrow.append(date)
    else:
      other.append(date)
    print("Задача добавлена")
  elif command == "exit":
    break
  else: 
    print("Неизвестная команда")
    break

print("Спасибо за использование! До свидания!")
