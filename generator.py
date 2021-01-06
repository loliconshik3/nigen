import random

def RandomNick(length: int):
    alpha_first = 'AEIOUYaeiouy'
    alpha_second = 'BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz'
    s = ''
    i = 1

    r = random.randint(0.00, 100.00)
    first_char = ''
    if (r > 50.00):
        first_char = random.choice(alpha_first)
    else:
        first_char = random.choice(alpha_second)
    s += first_char
    while (length - 1) >= i:
        char = s[len(s)-1]
        if (char in alpha_first):
            s += random.choice(alpha_second)
        else:
            s += random.choice(alpha_first)
        i += 1

    return s

def NickGenerator():
    choice = input("Выберите что хотите получить:\n1. Мужской ник.\n2. Женский ник.\n3. Ник из случайных букв.\n4. Выход.\n")
    if (choice == "4"):
        exit()
    limit = int(input("\nСколько никнеймов вы хотите получить?\n"))
    file = ''
    s = '\n'
    i = 1

    if (choice == "1"):
        file = 'boy_users.txt'
    elif (choice == "2"):
        file = 'girl_users.txt'
    elif (choice == "3"):
        length = int(input('\nВведите длину ника.\n'))
        while limit >= i:
            s += f"{i}. {RandomNick(length)}\n"
            i += 1


    if (file != ''):
        fl = open(file, 'r', encoding='UTF-8')
        lines = fl.readlines()
        while limit >= i:
            nick = random.choice(lines)
            s += f"{i}. {nick}"
            i += 1

    print(s)

    NickGenerator()

print("Приветствую вас в утилите NickGenerator.\n")
NickGenerator()