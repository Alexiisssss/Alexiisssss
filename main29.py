# Погружение в невероятный мир Pandas
# Используя базу данных фильмов из практической части урока, проверте следующие гипотезы: Известные актеры снимаются в самых кассовых фильмах


# Решение

import pandas as pd
import matplotlib.pyplot as plt  # Библиотека для построения графиков
import ast

# Папка с распакованным датасетом
FILE_PATH = './the_movies_dataset'

# Чтение CSV файла с указанием типов данных
df = pd.read_csv(f'{FILE_PATH}/movies_metadata.csv', low_memory=False)

# Преобразование столбца 'revenue' в числовой формат и сортировка по убыванию
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
df = df.sort_values(by='revenue', ascending=False)

# Определение самых кассовых фильмов
top_movies = df[['title', 'genres', 'revenue']].head(100)  # Возьмем топ-100 самых кассовых фильмов

# Создание словаря для подсчета упоминаний актеров
actor_count = {}

# Подсчет упоминаний каждого актера в самых кассовых фильмах
for cast_list in top_movies['genres']:
    if isinstance(cast_list, str):
        for actor in cast_list.split(','):
            actor = actor.strip()  # Убираем лишние пробелы
            if actor in actor_count:
                actor_count[actor] += 1
            else:
                actor_count[actor] = 1

# Преобразование словаря в DataFrame для построения графика
actor_count_df = pd.DataFrame(list(actor_count.items()), columns=['Actor', 'Count'])
actor_count_df = actor_count_df.sort_values(by='Count', ascending=False).head(10)  # Возьмем топ-10 актеров

# Построение графика
plt.figure(figsize=(10, 6))
plt.bar(actor_count_df['Actor'], actor_count_df['Count'], color='skyblue')
plt.title('Наиболее часто встречающиеся актеры в самых кассовых фильмах')
plt.xlabel('Актеры')
plt.ylabel('Количество упоминаний')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Преобразование строк JSON в списки
top_movies['genres'] = top_movies['genres'].apply(ast.literal_eval)

# Создание пустого словаря для подсчета жанров
genre_counts = {}

# Подсчет количества фильмов для каждого жанра
for genres_list in top_movies['genres']:
    for genre in genres_list:
        genre_name = genre['name']
        genre_counts[genre_name] = genre_counts.get(genre_name, 0) + 1

# Нахождение наиболее часто встречающегося жанра
most_common_genre = max(genre_counts, key=genre_counts.get)

# Получение количества фильмов в наиболее часто встречающемся жанре
movies_in_most_common_genre = genre_counts[most_common_genre]

# Вывод наиболее часто встречающегося жанра и количество фильмов в этом жанре
print(f"Наиболее часто встречающийся жанр в топ-100 самых кассовых фильмов: {most_common_genre}")
print(f"Количество фильмов в жанре '{most_common_genre}': {movies_in_most_common_genre}")
