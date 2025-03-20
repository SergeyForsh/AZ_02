import pandas as pd

data = {
    'Набор А': [85, 90, 95, 100, 105],
    'Набор Б': [70, 80, 95, 110, 120],
}
df = pd.DataFrame(data)
stdA = df['Набор А'].std()
stdB = df['Набор Б'].std()
print(f"Стандартное отклонение 1 набор - {stdA}")
print(f"Стандартное отклонение 2 набор - {stdB}")

print()

data1 = {
    'Возраст': [23, 22, 21, 27, 23, 20, 29, 28, 22, 25],
    'Зарплата': [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 61000],
}
df = pd.DataFrame(data1)
print(df.describe())

print(f"Средний возраст - {df['Возраст'].mean()}")
print(f"Медианный возраст - {df['Возраст'].median()}")
print(f"Стандартное отклонение возраста - {df['Возраст'].std()}")
print()
print(f"Средняя зарплата - {df['Зарплата'].mean()}")
print(f"Медианная зарплата - {df['Зарплата'].median()}")
print(f"Стандартное отклонение зарплата - {df['Зарплата'].std()}")
