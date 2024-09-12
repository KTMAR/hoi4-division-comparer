import tkinter as tk

def show_comparison_result(differences, weapon1, weapon2):
    translations = {
        'strength': 'Прочность',
        'organization': 'Организация',
        'recovery_speed': 'Скорость восстановления',
        'reconnaissance': 'Разведка',
        'suppression': 'Подавление',
        'weight': 'Вес',
        'ammo_consumption': 'Расход боеприпасов',
        'avg_reliability': 'Средняя надежность',
        'infantry_attack': 'Противопехотная атака',
        'anti_tank_attack': 'Противотанковая атака',
        'air_attack': 'Воздушная атака',
        'defense': 'Защита',
        'breakthrough': 'Прорыв',
        'armor': 'Броня',
        'piercing': 'Бронебойность',
        'initiative': 'Инициатива',
        'fortification': 'Укрепленность',
        'front_width': 'Ширина фронта',
        'manpower_cost': 'Людские ресурсы',
        'training_time': 'Время на обучение',
        'fuel_consumption': 'Потребление горючего',
        'infantry_equipment': 'Пехотное снаряжение',
        'support_equipment': 'Снаряжение поддержки'
    }

    comparison_window = tk.Toplevel()
    comparison_window.title("Результат сравнения")

    # Создание заголовков столбцов
    tk.Label(comparison_window, text="Параметр").grid(row=0, column=0, sticky="ew")
    tk.Label(comparison_window, text=weapon1.name).grid(row=0, column=1, sticky="ew")
    tk.Label(comparison_window, text=weapon2.name).grid(row=0, column=2, sticky="ew")

    for i, (field, (current_value, other_value, is_better)) in enumerate(differences.items(), start=1):
        tk.Label(comparison_window, text=translations[field]).grid(row=i, column=0, sticky="e")

        current_value_label = tk.Label(comparison_window, text=f"{current_value}")
        current_value_label.grid(row=i, column=1, sticky="w")

        other_value_label = tk.Label(comparison_window, text=f"{other_value}")
        other_value_label.grid(row=i, column=2, sticky="w")

        if is_better:
            current_value_label.config(fg="green")
            other_value_label.config(fg="red")
        else:
            current_value_label.config(fg="red")
            other_value_label.config(fg="green")
