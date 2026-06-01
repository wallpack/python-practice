s = input()

min_str = s
max_str = s

while s != 'КОНЕЦ':
    if s < min_str:
        min_str = s
    if s > max_str:
        max_str = s

    s = input()

print(f'Минимальная строка ⬇️: {min_str}')
print(f'Максимальная строка ⬆️: {max_str}') 