from random import randint


def attack(chName, char_class):
    """Это функция один."""
    if char_class == 'warrior':
        return (f'{chName} нанёс урон противнику равный '
                f'{5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{chName} нанёс урон противнику равный'
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{chName} нанёс урон противнику равный '
                f'{5 + randint(-3, -1)}')


def defence(chName, char_class):
    """Это функция два."""
    if char_class == 'warrior':
        return (f'{chName} блокировал '
                f'{10 + randint(5, 10)} урона)')
    if char_class == 'mage':
        return (f'{chName} блокировал '
                f'{10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{chName} блокировал '
                f'{10 + randint(2, 5)} урона')


def special(chName, char_class):
    """Это функция три."""
    if char_class == 'warrior':
        return (f'{chName} применил специальное умение'
                f'«Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{chName} применил специальное умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{chName} применил специальное умение «Защита {10 + 30}»')


def start_training(chName, char_class):
    """Это функция четыре."""
    if char_class == 'warrior':
        print(f'{chName}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{chName}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{chName}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или'
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(chName, char_class))
        if cmd == 'defence':
            print(defence(chName, char_class))
        if cmd == 'special':
            print(special(chName, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    """Это функция пять."""
    appChoice = None
    char_class = None
    while appChoice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: '
                           'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя.'
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.'
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель.'
                  'Черпает силы из природы, веры и духов.')
        appChoice = input('Нажми (Y), чтобы подтвердить выбор,'
                          'или любую другую кнопку,'
                          'чтобы выбрать другого персонажа ').lower()
    return char_class
