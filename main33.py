# Задача 3.
# Для выполнения работы будет использован csv файл “shopping_habits”, содержащий данные о различных покупках, которые совершаются покупателями в разных штатах США.
# Каждое из наблюдений в файле имеет следующие характеристики:
# Customer ID – порядковый номер строки в таблице
# Age – возраст покупателя
# Gender – пол покупателя
# Item Purchased – приобретенный товар
# Category - категория
# Purchase Amount (USD) – сумма покупки (в долларах)
# Location – локация покупки
# Size – размер (одежды)
# Color – цвет
# Season – время года совершения покупки
# Review Rating – полученный в отзыве рейтинг
# Subscription Status – статус подписки покупателя
# Shipping Type – тип доставки
# Discount Applied – применена ли скидка
# Promo Code Used – применен ли промокод
# Previous Purchases – были ли у данного покупателя предыдущие покупки
# Payment Method – способ оплаты
# Frequency of Purchases – частота покупок.
# Задание: провеcти разведочный анализ данных, выявить обычные взаимосвязи между значениями столбцов таблицы, выполнить визуализацию, сделать выводы.



# Решение

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных
df = pd.read_csv('dataset/shopping_habits.csv')

# Получение списка категориальных признаков
categorical_features = ['Gender', 'Item Purchased', 'Category', 'Location', 'Size', 'Color', 'Season', 'Subscription Status', 'Shipping Type', 'Discount Applied', 'Promo Code Used', 'Payment Method', 'Frequency of Purchases']

# 1. Основные статистики и распределения:
# Вывод основных статистик для числовых признаков
print("Основные статистики для числовых признаков:")
print(df.describe())

# Распределение категориальных признаков
print("\nРаспределение категориальных признаков:")
for feature in categorical_features:
    print(f"{feature}:\n", df[feature].value_counts())


# 2. Визуализация взаимосвязей:
# Парные графики числовых признаков
sns.pairplot(df[['Age', 'Purchase Amount (USD)', 'Review Rating']])
plt.title('Pairplot of Numerical Features')
plt.show()

# Построение сводной таблицы для анализа взаимосвязи между категориальными признаками
for feature1 in categorical_features:
    for feature2 in categorical_features:
        if feature1 != feature2:
            table = pd.crosstab(df[feature1], df[feature2])
            print(f"Cross-tabulation between {feature1} and {feature2}:\n")
            print(table)
            print("\n")

# Boxplot для категориальных признаков
for feature in categorical_features:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=feature, y='Purchase Amount (USD)', data=df)
    plt.title(f'Purchase Amount by {feature}')
    plt.show()



# 3. Корреляция признаков:
# Матрица корреляции для числовых признаков
corr_matrix = df[['Age', 'Purchase Amount (USD)', 'Review Rating']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Numerical Features')
plt.show()


# 4. Взаимосвязь между всеми категориальными признаками:
# Создание тепловой карты для корреляции между категориальными признаками
plt.figure(figsize=(12, 10))

# Кодирование категориальных признаков
encoded_df = pd.get_dummies(df[categorical_features], drop_first=True)

# Создание тепловой карты
sns.heatmap(encoded_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Categorical Features')
plt.show()

# Парные столбчатые диаграммы для всех комбинаций категориальных признаков
for i in range(len(categorical_features)):
    for j in range(i+1, len(categorical_features)):
        plt.figure(figsize=(12, 6))
        sns.countplot(x=categorical_features[i], hue=categorical_features[j], data=df)
        plt.title(f'{categorical_features[i]} vs {categorical_features[j]}')
        plt.xlabel(categorical_features[i])
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.legend(title=categorical_features[j])
        plt.show()
