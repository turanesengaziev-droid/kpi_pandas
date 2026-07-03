import pandas as pd
df = pd.read_excel('students (1).xlsx')

# print(df.head(10))

# ================================

# ЗАДАЧИ ПО PANDAS (СТУДЕНТЫ)
# Файл: students.xlsx
# Столбцы:
# id, first_name, last_name, age, gender, group, q1, q2, q3, q4

# q1,q2,q3,q4 - это столбцы которые хранят оценки за четверть

# ================================

# 1. Загрузить Excel файл в DataFrame и вывести первые 10 строк
# --------------------------------
# 2. Добавить новый столбец avg_score (средний балл q1-q4)
df['avg_score'] = df[['q1', 'q2', 'q3', 'q4']].mean(axis=1)
# df.to_excel('students (1).xlsx', index=False)
# print(df)

# --------------------------------
# 3. Вывести студентов, у которых avg_score >= 4.5 (отличники)

# print(df[df['avg_score'] >= 4.5])

# --------------------------------
# 4. Отфильтровать студентов по группе (например group == "A1")
a1 = df[df['group'] == 'A1']
b1 = df[df['group'] == 'B1']
c1 = df[df['group'] == 'C1']
a2 = df[df['group'] == 'A2']
b2 = df[df['group'] == 'B2']


# print(a1, a2)

# --------------------------------
# 5. Найти максимальный балл по каждой четверти (q1, q2, q3, q4)
# max_score = df[['q1','q2','q3','q4']].max()
# print(max_score)


# --------------------------------
# 6. Найти самого младшего студента (min age)
# min_age = df[df['age'] == df['age'].min()]
# print(min_age)
# --------------------------------
# 7. Посчитать средний avg_score по каждой группе (groupby group)
# avg_group = df.groupby('group')['avg_score'].mean()
# print(avg_group)
# --------------------------------
# 8. Посчитать количество студентов по полу (gender)
# group_gender = df.groupby('gender')['id'].count()
# print(group_gender)
# --------------------------------
# 9. Найти сумму всех оценок по каждой четверти (q1-q4)
# sum_q = df[['q1','q2','q3', 'q4']].sum()
# print(sum_q)

# --------------------------------
# 10. Вывести топ-3 студентов в каждой группе по avg_score
# top_3 = df.sort_values(['group','avg_score'], ascending=[True, False]).groupby('group').head(3)
# print(top_3)

# top_3 = df.sort_values(['avg_score'], ascending=False).head(3))

# top_3 = df.sort_values(['avg_score'], ascending=False).head(3)
# =================================

print('hello')

def func():
    ...

