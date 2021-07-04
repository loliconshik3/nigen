from pyfzf.pyfzf import FzfPrompt
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
    choice = fzf.prompt(["Exit", "Nick from random chars", "Female nick", "Male nick"])[0]

    if (choice == "Exit"):
        exit()

    limit_list = []; index = 1
    while index < 101:
        limit_list.append(f"Count: {index}")
        index += 1
    limit = int(fzf.prompt(limit_list)[0].replace("Count: ", ""))

    file = ''
    if (choice == "Male nick"):
        file = 'boy_users.txt'
    elif (choice == "Female nick"):
        file = 'girl_users.txt'

    elif (choice == "Nick from random chars"):
        length_list = []; index = 1
        while index < 101:
            length_list.append(f"Length: {index}")
            index += 1
        length = int(fzf.prompt(length_list)[0].replace("Length: ", ""))

        #length = int(input('\nChoice nick length.\n'))
        index = 1
        while limit >= index:
            nick = RandomNick(length)
            print(f"{index}. {nick}")
            index += 1

    if (file != ''):
        fl = open(file, 'r', encoding='UTF-8')
        lines = fl.readlines(); index = 1
        while limit >= index:
            nick = random.choice(lines)
            print(f"{index}. {nick}")
            index += 1

    #nigen()

print("nigen is loading...\n")
fzf = FzfPrompt()
nigen()
