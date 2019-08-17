
__author__ = 'Зиновьев Максим Игоревич'

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
patronymic = input('Введите ваше отчество: ')
patName = input('Введите имя вашего питомца: ')

while True:
    likePlay = input('Вы любите играть? (Да/Нет) ')
    if likePlay == 'Да':
        likePlayBool = True
        break
    elif likePlay == 'Нет':
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
    elif playerAge > 90:
        playerAnswer = input('Для вас игра может быть утомительной, вы уверены, что хотите играть? (Да/Нет) ')
        if playerAnswer == 'Да':
            playerAnswer = input('Вы точно уверены, что хотите играть? (Да/Нет) ')
            if playerAnswer == 'Да':
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

