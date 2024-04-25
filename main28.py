#Погружение в невероятный мир Pandas
#Используя базу данных фильмов из практической части урока, проверте следующие гипотезы: #Большинство фильмов выпускаются по пятницам


#Решение

import pandas as pd
import matplotlib.pyplot as plt  # Библиотека для построения графиков

# Папка с распакованным датасетом
FILE_PATH = './the_movies_dataset'

# Чтение CSV файла с указанием типов данных
df = pd.read_csv(f'{FILE_PATH}/movies_metadata.csv', low_memory=False)

# Преобразование столбца с датой выпуска в формат даты
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Извлечение дня недели из даты выпуска фильма
df['release_day_of_week'] = df['release_date'].dt.day_name()

# Подсчет количества фильмов по дням недели
movies_per_day = df['release_day_of_week'].value_counts()

# Сортировка по порядку дней недели
movies_per_day = movies_per_day.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Построение графика
plt.figure(figsize=(10, 6))
movies_per_day.plot(kind='bar', color='skyblue')
plt.title('Количество фильмов по дням недели')
plt.xlabel('День недели')
plt.ylabel('Количество фильмов')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Нахождение дня недели с наибольшим количеством фильмов
max_movies_day = movies_per_day.idxmax()

# Получение количества фильмов в этот день
max_movies_count = movies_per_day.max()

# Вывод наибольшего значения и количество фильмов
print(f"Наибольшее количество фильмов выпущено в {max_movies_day}: {max_movies_count} фильмов.")
