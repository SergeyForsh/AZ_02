import pandas as pd
# 1. Создание DataFrame с данными
data = {
    'Имя': ['Аня', 'Борис', 'Вика', 'Денис', 'Елена', 'Федор', 'Галя', 'Игорь', 'Кира', 'Леонид'],
    'Математика': [5, 4, 3, 4, 5, 2, 3, 4, 5, 4],
    'Русский язык': [4, 5, 3, 3, 4, 5, 4, 4, 5, 4],
    'Физика': [5, 3, 4, 5, 4, 3, 5, 4, 4, 4],
    'Химия': [3, 4, 4, 5, 5, 3, 4, 3, 4, 5],
    'История': [4, 5, 3, 4, 3, 3, 5, 5, 4, 4]
}
df = pd.DataFrame(data)
# 2. Вывод первых нескольких строк DataFrame
print("Первые несколько строк DataFrame:")
print(df.head())
# 3. Вычисление средней оценки по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("\nСредние оценки по предметам:")
print(mean_scores)
# 4. Вычисление медианной оценки по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианные оценки по предметам:")
print(median_scores)
# 5. Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(f"\nQ1 по математике: {Q1_math}")
print(f"Q3 по математике: {Q3_math}")
print(f"IQR по математике: {IQR_math}")
# 6. Вычисление стандартного отклонения
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по предметам:")
print(std_deviation)
### Объяснение кода:
# 1. **Создание DataFrame**: Мы создаем DataFrame с именами учеников и их оценками по 5 предметам.
# 2. **Вывод первых строк**: Используем `head()`, чтобы вывести первые 5 строк DataFrame.
# 3. **Средние оценки**: Используем метод `mean()` для вычисления средних оценок по всем предметам.
# 4. **Медианные оценки**: Используем метод `median()` для вычисления медианных оценок
# по всем предметам.
# 5. **Q1, Q3 и IQR**: Вычисляем первый (Q1) и третий (Q3) квартили для оценок по математике
# и рассчитываем интерквартильный размах (IQR).
# 6. **Стандартное отклонение**: Используем метод `std()` для вычисления стандартного отклонения
# по всем предметам.
#       Запустив этот код, вы получите все необходимые результаты анализа.