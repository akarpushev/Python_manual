import json

russian_data = {
    "Фамилия": "Петров",
    "Имя": "Петр",
}

filename = "russian.json"
with open(filename, "w") as f:
    json.dump(russian_data, f)


filename = "russian_ensure_ascii.json"
with open(filename, "w", encoding="utf8") as f:
    json.dump(russian_data, f, ensure_ascii=False)

with open(filename, 'r') as f:
    print(f)
x = json.load(f)
print(x)
