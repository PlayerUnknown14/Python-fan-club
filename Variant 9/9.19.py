def f(S, h): # "S" - количество камней в куче; "h" - номер текущего хода
    if h == 3 and S >= 88: # если "S" 3-го хода >= 88 (удовлетворяет задаче), то "S" изначальный - искомое значение
        return 1
    elif h == 3 and S < 88: # проверяем "S" для других условий (неудовлетворяющих задаче)
        return 0
    elif h < 3 and S >= 88: # проверяем "S" для других условий (неудовлетворяющих задаче)
        return 0
    else:
        if h % 2 == 0: # проверка на чётность номера хода - в задаче именно 2-ой (чётный) ход должен быть выигрышным
            return f(S + 1, h + 1) or f(S + 4, h + 1) or f(S * 3, h + 1) # если h чётный - делаем проверки для возможных ходов
        else:
            return f(S + 1, h + 1) and f(S + 4, h + 1) and f(S * 3, h + 1)
 
for S in range(1, 88): # проверка для всех "S" в диапазоне от 1 до 87
    if f(S, 1) == 1:
        print(S)
        break #Answer: 29