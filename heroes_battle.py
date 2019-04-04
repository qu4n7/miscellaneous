# начну с генерации статистик - предлагаю либо забить их пользователю, иначе генерирую случайно

import random
import time

player_name = input('Введите имя player: ')
enemy_name = input('Введите имя enemy: ')
request = input('Хотите ли Вы сами ввести характеристики(y/n): ')
if request == 'y':
    player_health = int(input('player health (целое число): '))
    player_damage = int(input('player damage (целое число): '))
    player_armor = round(float(input('player armor (дробное число): ')), 1)
    enemy_health = int(input('enemy health (целое число): '))
    enemy_damage = int(input('enemy damage (целое число): '))
    enemy_armor = round(float(input('enemy armor (дробное число): ')), 1)
    player = {'name' : player_name,
              'health' : player_health,
              'damage' : player_damage,
              'armor' : player_armor}
    enemy = {'name' : enemy_name,
              'health' : enemy_health,
              'damage' : enemy_damage,
              'armor' : enemy_armor}
else:
    player = {'name' : player_name,
              'health' : random.randrange(50, 200),
              'damage' : random.randrange(5, 51),
              'armor' : round(random.uniform(1.0, 1.9), 1)}
    enemy = {'name' : enemy_name,
              'health' : random.randrange(50, 200),
              'damage' : random.randrange(5, 51),
              'armor' : round(random.uniform(1.0, 1.9), 1)}

# чтобы записывать статы в файл с именем игрока, создаю функцию, которая будет генерировать имя файла
def file_name(person_name):
    file = ('').join([person_name['name'],'.txt'])
    return file

# функция записи стат в файл
def dict_to_file(file, dictionary):
    with open(file, 'w') as fout:
        for key in dictionary.keys():
            fout.write('%s - %s\n' % (key,dictionary[key]))

# записываю статы в файл
dict_to_file(file_name(player), player)
dict_to_file(file_name(enemy), enemy)

# балуюсь, делаю вид, что сохраняю
print('подождите, пожалуйста, сохраняю файлы')
for i in range(3):
    print('///' * i)
    time.sleep(1)
print('файлы сохранены')

# по условию задачи я должен записать их из файлов => запршиваю, каких игроков загрузить
player_name = input('Введите имя player: ')
enemy_name = input('Введите имя enemy: ')

# функция выгрузки стат из файла
def file_to_dict(file, dictionary):
    with open(file) as file:
        lines = file.readlines()
    for i in lines:
        i = i.split(' - ')
        dictionary.append(i)
    dictionary = dict(dictionary)

# выгружаю статы из файла
dict_to_file(file_name(player), player)
dict_to_file(file_name(enemy), enemy)

# балуюсь, делаю вид, что выгружаю
print('подождите, пожалуйста, выгружаю файлы')
for i in range(3):
    print('///' * i)
    time.sleep(1)
print('данные загружены, статистики игроков')
print(player, '\n', enemy)

# функция нападения
def attack(person1, person2):
    person1['health'] = person1['health'] - person2['damage'] / person1['armor']

# итерация функции, пока у кого то не кончится здоровье
game_round = 0

# из условия не понял, кто бьет первым, поэтому предлагаю выбрать пользователю
player_name = player['name']
enemy_name = enemy['name']
try:
    turn = int(input(f'Кто бьет первым (1 - если {enemy_name} / 2 - если {player_name})?'))
except:
    turn = int(input('Введите число - 1 или 2'))

if turn == 1:
    while player['health'] > 0 and enemy['health'] > 0:
        game_round += 1
        attack(player, enemy)
        print(f'бьет {enemy_name}')
        time.sleep(1)
        print('раунд: {}, player health: {}, enemy health: {}'.format(game_round,
                                                                      player['health'],
                                                                      enemy['health']))
        attack(enemy, player)
        print(f'бьет {player_name}')
        time.sleep(1)
        print('раунд: {}, player health: {}, enemy health: {}'.format(game_round,
                                                                      player['health'],
                                                                      enemy['health']))
        if player['health'] <= 0:
            player['health'] = 0
        elif enemy['health'] <= 0:
            enemy['health'] = 0
elif turn == 0:
    while player['health'] > 0 and enemy['health'] > 0:
        game_round += 1
        attack(enemy, player)
        print(f'бьет {player_name}')
        time.sleep(1)
        print('раунд: {}, player health: {}, enemy health: {}'.format(game_round,
                                                                      player['health'],
                                                                      enemy['health']))
        attack(player, enemy)
        print(f'бьет {enemy_name}')
        time.sleep(1)
        print('раунд: {}, player health: {}, enemy health: {}'.format(game_round,
                                                                      player['health'],
                                                                      enemy['health']))
        if player['health'] <= 0:
            player['health'] = 0
        elif enemy['health'] <= 0:
            enemy['health'] = 0

if enemy['health'] <=0:
    print(f'\nпобедил {player_name}'.upper())
else:
     print(f'\nпобедил {enemy_name}'.upper())

# ПОДКАЖИТЕ, ПЖЛ, ПОЧЕМУ КОГДА БЬЕТ ПЕРВЫМ PLAYER, ИГРА ИДЕТ НОРМАЛЬНО, А КОГДА ENEMY - СРАЗУ ПОБЕЖДАЕТ ENEMY?
# весь вечер ломаю голову, не могу понять ((