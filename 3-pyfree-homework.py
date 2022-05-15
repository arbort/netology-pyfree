HELP = """
help - напечатать справку по программе
add_word - добавить слово в список
add_letter - добавить букву
show - напечатать все слова и зафиксированную букву
check - проверить список слов на наличие в них буквы """

print("""Привет! Список доступных команд:
help - напечатать справку по программе
add_word - добавить слово в список
add_letter - добавить букву
show - напечатать все слова и зафиксированную букву
check - проверить список слов на наличие в них буквы""")

list = []
the_letter = str()
list_for_review = []

def count_letter(list, char):
  count = 0
  for word in list:
    for letter in word:
      if letter == char:
        count += 1
  return count
  
while True:
 command = input("Введите команду: ")
 if command == "help":
   print(HELP)
 elif command == "show":
   print(list)
   print(the_letter)
 elif command == "add_word":
   word = input("Введите слово: ")
   list.append(word)
   print("Слово добавлено")
 elif command == "add_letter":
   add_letter = input("Введите букву: ")
   the_letter = add_letter
   print("Буква добавлена")
 elif command == "check":
   result = count_letter(list, the_letter)
   print(result)
 elif command == "exit":
   break
 else: 
   print("Неизвестная команда")
   break
