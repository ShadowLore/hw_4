films = ['Во все тяжкое', 'Трансформеры', 'Приколи', 'Форсаж', 'Непосредственно Каха', 'Люди в черном', 'Довод']

print(films[5])

print(films[len(films) - 3])
print(films[-3])

print(films[-1])
print(films[len(films) - 1])

films.append('Смурфики')
print(films)

films.insert(2, 'Игра эндера')
print(films)

last_film = films.pop()
print(last_film)
print(films)

print(films.count('Довод'))

print(films.index('Непосредственно Каха'))
