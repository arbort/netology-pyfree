HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = dict()

def showTasks():
  print(f'Всего задач {len(tasks)}\n\n')
  for task, date in tasks.items():
    print(f'{task}: {date}\n')

while True:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    showTasks()
  elif command == "add":
    task = input("Введите название задачи: ")
    date = input("Введите дату выполнения задачи: ").lower().lstrip().rstrip()
    tasks[task] = date
    print("Задача добавлена")
  elif command == "exit":
    break
  else: 
    print("Неизвестная команда")
    break

print("Спасибо за использование! До свидания!")
