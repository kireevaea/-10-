import os
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Указываем путь к файлу
file_path = 'events.json'

# Проверяем, существует ли файл
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Файл {file_path} не найден!")

# Открываем и читаем JSON
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read().strip()

    if not content:
        raise ValueError(f"Файл {file_path} пуст!")

    data = json.loads(content)

# Проверяем наличие ключа "events"
if 'events' not in data:
    raise KeyError("Ключ 'events' не найден в JSON-файле")

# Создаем DataFrame
df = pd.json_normalize(data['events'])

# Вывод первых строк датафрейма
print(df.head())

# Анализ типов событий
signature_counts = df['signature'].value_counts()
print("Количество событий по типам:\n", signature_counts)

# Визуализация
plt.figure(figsize=(10, 6))
sns.countplot(y='signature', data=df, order=signature_counts.index)
plt.title('Распределение событий по типам')
plt.xlabel('Количество событий')
plt.ylabel('Тип события')
plt.show()
