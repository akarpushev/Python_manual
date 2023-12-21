student = {
    'имя': 'Алексей',
    'возраст': 25,
    'группа': 'ИТ-42'
}
# Проверка наличия ключа с использованием оператора in
if 'возраст' in student:
    print('Ключ "возраст" присутствует в словаре student')
else:
    print('Ключ "возраст" отсутствует в словаре student')

#Проверка наличия ключа с использованием метода get()
if student.get('возраст') is not None:
    print('Ключ "возраст" присутствует в словаре student')
else:
    print('Ключ "возраст" отсутствует в словаре student')

# Проверка наличия ключа с использованием try/except
try:
    value = student['возраст']
    print("Значение:", value)
except KeyError:
    print("Ключ не найден в словаре")

def in_dictionary(key, dict):
    return key in dict
print(in_dictionary('имя', student))