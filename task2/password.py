import random as R

print("Welcome to password generator:")

def num():
    value = R.randint(0, 9)
    return value

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def alpha():
    value = R.choice(alphabets)
    return value


x = R.randint(8, 15)
y = 0
i = 0


password = []
while i < x:
    if y % 2 == 0:
        password.append(str(num()))
    else:
        password.append(alpha())
    y += 1
    i += 1


print("Generated password:", ''.join(password))
