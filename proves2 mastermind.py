from random import randrange

print()

easy_list = []
middle_list = []
difficult_list = []

easy = 4
middle = 6
difficult = 8

for i in range(easy):
    num = randrange(1,7)
    easy_list.append(num)
print(easy_list)
print()

for i in range(middle):
    num = randrange(1,7)
    middle_list.append(num)
print(middle_list)
print()

for i in range(difficult):
    num = randrange(1,7)
    difficult_list.append(num)
print(difficult_list)
print()
