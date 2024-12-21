import pandas as pd

# Читаем исходный файл
df = pd.read_csv('input.csv')

# Убираем одну колонку
df = df.drop(columns=['ColumnToRemove'])

# Сохраняем файл
df.to_csv('filtered.csv', index=False)

# Фильтруем по значению 'USD' в столбце1
filtered_df = df[df['Column1'] == 'USD']
filtered_df.to_csv('final.csv', index=False)
print("Обработка завершена. Результаты сохранены в final.csv.")