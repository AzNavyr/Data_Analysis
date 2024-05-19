import matplotlib.pyplot as plt

professions = [
    "Кардиолог", "Петролеум инженер", "Облачный архитектор",
    "HR-профессионал", "Фармацевт", "Стоматолог",
    "Медицинская сестра (RN)", "Техник мед. оборудования", "LPN"
]

salaries = [
    324760, 130523, 144000,
    67061, 152308, 170910,
    80820, 60780, 48070
]

plt.figure(figsize=(10, 6))
plt.bar(professions, salaries, color='skyblue')
plt.xlabel('Профессии')
plt.ylabel('Средняя годовая зарплата ($)')
plt.title('Зависимость зарплат от профессий в 2024 году')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()