# Погружение в невероятный мир Pandas
# Используя базу данных фильмов из практической части урока, проверте следующие гипотезы: Известные актеры снимаются в самыx дорогих фильмах


# Решение

import pandas as pd
import matplotlib.pyplot as plt  # Библиотека для построения графиков
import ast

# Папка с распакованным датасетом
FILE_PATH = './the_movies_dataset'

# Чтение CSV файла с указанием типов данных
df = pd.read_csv(f'{FILE_PATH}/movies_metadata.csv', low_memory=False)

# Сортировка фильмов по бюджету и взятие топ-100 самых дорогих
top_100_expensive_movies = df.sort_values(by='budget', ascending=False).head(100)

# Создание пустого словаря для подсчета актеров
actors_count = {}

# Подсчет количества фильмов для каждого актера
for actors_list in top_100_expensive_movies['genres']:
    actors = eval(actors_list)  # Преобразование строки в список актеров
    for actor in actors:
        actor_name = actor['name']
        actors_count[actor_name] = actors_count.get(actor_name, 0) + 1

# Сортировка актеров по количеству фильмов
sorted_actors_count = sorted(actors_count.items(), key=lambda x: x[1], reverse=True)

# Построение графика
plt.figure(figsize=(10, 6))
actors, num_movies = zip(*sorted_actors_count[:20])  # Выведем только 20 самых часто встречающихся актеров
plt.bar(actors, num_movies, color='skyblue')
plt.title('Количество фильмов для каждого актера в топ-100 самых дорогих фильмов')
plt.xlabel('Актер')
plt.ylabel('Количество фильмов')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Вывод количества известных актеров
print(f"Количество известных актеров в результатах: {len(sorted_actors_count)}")