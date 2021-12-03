from random import randrange

def password_gen(select,easy,middle,difficult):
    
    easy_list = []
    middle_list = []
    difficult_list = []

    easy = 4
    middle = 6
    difficult = 8

    if select == "lvl1":
        for i in range(easy):
            num = randrange(1,6)
            while num in easy_list:
                num = randrange(1,6)
        easy_list.append(num)
        return easy_list

    if select == "lvl2":
        for i in range(middle):
            num = randrange(1,9)
            while num in middle_list:
                num = randrange(1,6)
        middle_list.append(num)
        return middle_list

    if select == "lvl3":
        for i in range(difficult):
            num = randrange(1,9)    
        difficult_list.append(num)
        return difficult_list
