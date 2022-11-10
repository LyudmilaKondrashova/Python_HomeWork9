#"Крестики-нолики"
def PrintTickTackToe(r1, r2, r3): # Печатаем Крестики-нолики
    print(f'|{r1[0]}|{r1[1]}|{r1[2]}|')
    print(f'|{r2[0]}|{r2[1]}|{r2[2]}|')
    print(f'|{r3[0]}|{r3[1]}|{r3[2]}|')

def Krestick(r1, r2, r3, row_kr, col_kr): #Заносим крестик
    import emoji
    fl = False
    if row_kr == 1:
        if r1[col_kr - 1] == '-':
            r1[col_kr - 1] = 'X'
            fl = True
        else:
            print('Эта позиция уже занята! Введите другие значения! ' + emoji.emojize(':no_entry_sign:', language='alias'))
    if row_kr == 2:
        if r2[col_kr - 1] == '-':
            r2[col_kr - 1] = 'X'
            fl = True
        else:
            print('Эта позиция уже занята! Введите другие значения! ' + emoji.emojize(':no_entry_sign:', language='alias'))
    if row_kr == 3:
        if r3[col_kr - 1] == '-':
            r3[col_kr - 1] = 'X'
            fl = True
        else:
            print('Эта позиция уже занята! Введите другие значения! ' + emoji.emojize(':no_entry_sign:', language='alias'))
    return fl

def Win(r1, r2, r3):    #Определяем, является текущая ситуация выигрышной
    winner = ''
    if r1 == ['X', 'X', 'X']:
        winner = 'Победили крестики!'
    if r1 == ['O', 'O', 'O']:
        winner = 'Победили нолики!'
    if r2 == ['X', 'X', 'X']:
        winner = 'Победили крестики!'
    if r2 == ['O', 'O', 'O']:
        winner = 'Победили нолики!'
    if r3 == ['X', 'X', 'X']:
        winner = 'Победили крестики!'
    if r3 == ['O', 'O', 'O']:
        winner = 'Победили нолики!'
    if r1[0] == 'X' and r2[0] == 'X' and r3[0] == 'X':
        winner = 'Победили крестики!'
    if r1[0] == 'O' and r2[0] == 'O' and r3[0] == 'O':
        winner = 'Победили нолики!'
    if r1[1] == 'X' and r2[1] == 'X' and r3[1] == 'X':
        winner = 'Победили крестики!'
    if r1[1] == 'O' and r2[1] == 'O' and r3[1] == 'O':
        winner = 'Победили нолики!'
    if r1[2] == 'X' and r2[2] == 'X' and r3[2] == 'X':
        winner = 'Победили крестики!'
    if r1[2] == 'O' and r2[2] == 'O' and r3[2] == 'O':
        winner = 'Победили нолики!'  
    if r1[0] == 'X' and r2[1] == 'X' and r3[2] == 'X':
        winner = 'Победили крестики!'
    if r1[0] == 'O' and r2[1] == 'O' and r3[2] == 'O':
        winner = 'Победили нолики!'
    if r1[2] == 'X' and r2[1] == 'X' and r3[0] == 'X':
        winner = 'Победили крестики!'
    if r1[2] == 'O' and r2[1] == 'O' and r3[0] == 'O':
        winner = 'Победили нолики!'
    if len(winner) > 0:
        return winner
    else:
        return 'Next step'

def Nolick(r1, r2, r3, row_nol, col_nol): #Заносим нолик
    import emoji
    fl = False
    if row_nol == 1:
        if r1[col_nol - 1] == '-':
            r1[col_nol - 1] = 'O'
            fl = True
        else:
            print('Эта позиция уже занята! Введите другие значения! ' + emoji.emojize(':no_entry_sign:', language='alias'))
    if row_nol == 2:
        if r2[col_nol - 1] == '-':
            r2[col_nol - 1] = 'O'
            fl = True
        else:
            print('Эта позиция уже занята! Введите другие значения! ' + emoji.emojize(':no_entry_sign:', language='alias'))
    if row_nol == 3:
        if r3[col_nol - 1] == '-':
            r3[col_nol - 1] = 'O'
            fl = True
        else:
            print('Эта позиция уже занята! Введите другие значения! ' + emoji.emojize(':no_entry_sign:', language='alias'))
    return fl

def TickTackToe():
    import emoji
    from progress.bar import Bar
    import time

    row1 = ['-','-', '-']
    row2 = ['-','-', '-']
    row3 = ['-','-', '-']
    
    print('Начало игры: ' + emoji.emojize(':smiley:', language='alias'))
    PrintTickTackToe(row1, row2, row3)

    
    count_tick_tack = 0
    flag_game = False
    while not flag_game:
        winner_game = Win(row1, row2, row3)
        if winner_game == 'Next step' and count_tick_tack < 9: 
            flag_krest = False
            while not flag_krest:
                print('Введите позицию крестика:')
                row_krest = int(input('строка (от 1 до 3): \n'))
                col_krest = int(input('столбец (от 1 до 3): \n'))
                if row_krest < 1 or row_krest > 3 or col_krest < 1 or col_krest > 3:
                    print('Введите значения позиции крестика в пределах от 1 до 3!')
                else:
                    with Bar('Обрабатываем ход!', max=2) as bar:
                        for i in range(2):
                            bar.next()
                            time.sleep(0.5)
                    if Krestick(row1, row2, row3, row_krest, col_krest):
                        flag_krest = True
                        count_tick_tack += 1
            PrintTickTackToe(row1, row2, row3)
        elif count_tick_tack == 9:
            print('НИЧЬЯ! ' + emoji.emojize(':handshake:', language='alias'))
            exit()
        else:
            print(winner_game + emoji.emojize(':glowing_star::glowing_star::glowing_star:', language='alias'))
            exit()
                    
        winner_game = Win(row1, row2, row3)
        if winner_game == 'Next step' and count_tick_tack < 9:
            flag_nol = False
            while not flag_nol:
                print('Введите позицию нолика:')
                row_nolick = int(input('строка (от 1 до 3): \n'))
                col_nolick = int(input('столбец (от 1 до 3): \n'))
                if row_nolick < 1 or row_nolick > 3 or col_nolick < 1 or col_nolick > 3:
                    print('Введите значения позиции крестика в пределах от 1 до 3!')
                else:
                    with Bar('Обрабатываем ход!', max=2) as bar:
                        for i in range(2):
                            bar.next()
                            time.sleep(0.5)
                    if Nolick(row1, row2, row3, row_nolick, col_nolick):
                        flag_nol = True
                        count_tick_tack += 1
            PrintTickTackToe(row1, row2, row3)
        elif count_tick_tack == 9:
            print('НИЧЬЯ! ' + emoji.emojize(':handshake:', language='alias'))
            exit()
        else:
            print(winner_game + emoji.emojize(':glowing_star::glowing_star::glowing_star:', language='alias'))
            exit()

TickTackToe()