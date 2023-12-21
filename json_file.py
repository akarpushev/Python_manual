# Сериализация
import json
# Сериализуем Python объект в json строку
a = json.dumps([1, 2, 3, {'4': 5, '6': 7}])
print(a)

print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], indent=4))

print(json.dumps({"english text": "русский текст"}, ensure_ascii=False))
# флаг ensure_ascii дает ожидаемый вид текста

# Десериализация
def check_code_decode_json(src):
    json_str = json.dumps(src)
    python_obj = json.loads(json_str)

    print('Исходный python объект:', repr(src))
    print('json строка при сериализации:', repr(json_str))
    print('python объект при десериализации', repr(python_obj))

    return src == python_obj

src = [1, 2, 3, {"4": 5, '6': 7}]
print(check_code_decode_json(src))