
__author__ = 'Зиновьев Максим Игоревич'

import sys
import time

def exitProgramm(text):
    if text == 'exit' or text == 'Exit':
        print('До свидания')
        time.sleep(1)
        sys.exit()

print('Добро пожаловать в игру "My First Game"')
name = input('Введите ваше имя: ')
name.title()
exitProgramm(name)
surname = input('Введите вашу фамилию: ')
surname.title()
exitProgramm(surname)
patronymic = input('Введите ваше отчество: ')
patronymic.title()
exitProgramm(patronymic)
patName = input('Введите имя вашего питомца: ')
patName.title()
exitProgramm(patName)

while True:
    likePlay = input('Вы любите играть? (Да/Нет) ')
    likePlay.lower()
    exitProgramm(likePlay)
    if likePlay == 'да':
        likePlayBool = True
        break
    elif likePlay == 'нет':
        likePlayBool = False
        break
    else:
        print('Я не знаю такой команды')

while True:
    playerAge = int(input('Сколько вам лет? '))
    if playerAge >= 18 and playerAge < 90:
        print('Здравствуйте, ', name)
        break
    elif playerAge < 18:
        print('Извините, но играть можно только с 18 лет, попробуйте поиграть когда станете постарше. ')
    elif playerAge >= 90:
        playerAnswer = input('Для вас игра может быть утомительной, вы уверены, что хотите играть? (Да/Нет) ')
        playerAnswer.lower()
        exitProgramm(playerAnswer)
        if playerAnswer == 'да':
            playerAnswer = input('Вы точно уверены, что хотите играть? (Да/Нет) ')
            playerAnswer.lower()
            exitProgramm(playerAnswer)
            if playerAnswer == 'да':
                print('Хорошо, тогда начнем игру!')
                break
            elif playerAnswer == 'Нет':
                print('До свидания, ', name)
                break
            else:
                print('Неизвестная команда!')
        elif playerAnswer == 'Нет':
            print('До свидания, ', name)
            break
        else:
            print('Неизвестная команда!')
    else:
        print('Вы ввели не корректный возраст, попробуйте ещё раз.')
print('Я могу произнести все буквы алфавита, которых нет в твоем имени: ')
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
for itm in alphabet:
    if itm in name:
        pass
    else:
        print(itm)

print('\nСыграем в игру. Я задумал 16 чисел от 1 - 16 и расположил их в произвольном порядке в строке. '
      'Скажите мне Где какое.')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
question = [8, 3, 1, 2, 15, 4, 10, 14, 6, 16, 5, 12, 13, 7, 9, 11]
table = ['|*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*|']
line2 = '8|3|1|2|15|4|10|14|6|16|5|12|13|7|9|11'
line = '|'.join(table)
for num in numbers:
    ind = question.index(num) + 1
    print(line, '\nВ какой ячейке находится число ', num, '?')
    userAnswer = int(input())
    exitProgramm(userAnswer)
    while userAnswer != ind:
        userAnswer = int(input('Нет, попробуйте ещё раз: '))
        exitProgramm(userAnswer)
        if userAnswer == ind:
            table[ind] = str(num)
            line = '|'.join(table)
    else:
        line = '|'.join(table)
        print('Верно')
        if userAnswer == ind:
            table[ind] = str(num)
            line = '|'.join(table)
    if line == line2:
        break
print('Все числа: ', line2)

