import random

def RandomNick(length: int):
    alpha_first = 'AEIOUYaeiouy'
    alpha_second = 'BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz'
    s = ''; i = 1

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

def nigen():
    choice = input("Please, choice:\n1. Male nick.\n2. Female nick.\n3. Nick from random chars.\n4. Exit.\n")
    if (choice == "4"):
        exit()
    limit = int(input("\nHow many nicks you want?\n"))
    file = ''; i = 1

    print('\n')
    if (choice == "1"):
        file = 'boy_users.txt'
    elif (choice == "2"):
        file = 'girl_users.txt'

    elif (choice == "3"):
        length = int(input('\nChoice nick length.\n'))
        while limit >= i:
            nick = RandomNick(length)
            print(f"{i}. {nick}")
            i += 1

    if (file != ''):
        fl = open(file, 'r', encoding='UTF-8')
        lines = fl.readlines()
        while limit >= i:
            nick = random.choice(lines)
            print(f"{i}. {nick}")
            i += 1

    nigen()

print("nigen is loading...\n")
nigen()
