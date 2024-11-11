# Выполнил: Мальцев Георгий Павлович

def just_num():


    for i in range(2, 51):
        t = 0
        for j in range(2, 50):
            if i % j == 0:
                t += 1
        if t == 1:
            print(i)
just_num()
