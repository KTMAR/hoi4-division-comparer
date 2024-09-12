import tkinter as tk
from tkinter import messagebox, ttk
from database import init_db
from models import WeaponStats
from utils import show_comparison_result

session = init_db()

def load_divisions():
    """Загружает список существующих дивизий для отображения в выпадающих списках."""
    divisions = session.query(WeaponStats.name).distinct().all()
    return [division[0] for division in divisions]

def add_record():
    try:
        weapon = WeaponStats(
            name=name_entry.get(),
            strength=float(strength_entry.get()),
            organization=float(organization_entry.get()),
            recovery_speed=float(recovery_speed_entry.get()),
            reconnaissance=float(reconnaissance_entry.get()),
            suppression=float(suppression_entry.get()),
            weight=float(weight_entry.get()),
            ammo_consumption=float(ammo_consumption_entry.get()),
            avg_reliability=float(avg_reliability_entry.get()),
            infantry_attack=float(infantry_attack_entry.get()),
            anti_tank_attack=float(anti_tank_attack_entry.get()),
            air_attack=float(air_attack_entry.get()),
            defense=float(defense_entry.get()),
            breakthrough=float(breakthrough_entry.get()),
            armor=float(armor_entry.get()),
            piercing=float(piercing_entry.get()),
            initiative=float(initiative_entry.get()),
            fortification=float(fortification_entry.get()),
            front_width=float(front_width_entry.get()),
            manpower_cost=float(manpower_cost_entry.get()),
            training_time=float(training_time_entry.get()),
            fuel_consumption=float(fuel_consumption_entry.get()),
            infantry_equipment=float(infantry_equipment_entry.get()),
            support_equipment=float(support_equipment_entry.get())
        )
        session.add(weapon)
        session.commit()
        messagebox.showinfo("Успех", "Запись успешно добавлена!")
        clear_entries()
        update_division_lists()  # Обновить выпадающие списки после добавления новой дивизии
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

def clear_entries():
    name_entry.delete(0, tk.END)
    strength_entry.delete(0, tk.END)
    organization_entry.delete(0, tk.END)
    recovery_speed_entry.delete(0, tk.END)
    reconnaissance_entry.delete(0, tk.END)
    suppression_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    ammo_consumption_entry.delete(0, tk.END)
    avg_reliability_entry.delete(0, tk.END)
    infantry_attack_entry.delete(0, tk.END)
    anti_tank_attack_entry.delete(0, tk.END)
    air_attack_entry.delete(0, tk.END)
    defense_entry.delete(0, tk.END)
    breakthrough_entry.delete(0, tk.END)
    armor_entry.delete(0, tk.END)
    piercing_entry.delete(0, tk.END)
    initiative_entry.delete(0, tk.END)
    fortification_entry.delete(0, tk.END)
    front_width_entry.delete(0, tk.END)
    manpower_cost_entry.delete(0, tk.END)
    training_time_entry.delete(0, tk.END)
    fuel_consumption_entry.delete(0, tk.END)
    infantry_equipment_entry.delete(0, tk.END)
    support_equipment_entry.delete(0, tk.END)

def compare_divisions():
    name1 = division1_combobox.get()
    name2 = division2_combobox.get()

    weapon1 = session.query(WeaponStats).filter_by(name=name1).first()
    weapon2 = session.query(WeaponStats).filter_by(name=name2).first()

    if weapon1 and weapon2:
        differences = weapon1.compare_with(weapon2)
        show_comparison_result(differences, weapon1, weapon2)
    else:
        messagebox.showerror("Ошибка", f"Одна или обе дивизии не найдены: {name1}, {name2}")

def update_division_lists():
    """Обновляет выпадающие списки с дивизиями."""
    divisions = load_divisions()
    division1_combobox['values'] = divisions
    division2_combobox['values'] = divisions

def create_gui():
    global name_entry, strength_entry, organization_entry, recovery_speed_entry, reconnaissance_entry
    global suppression_entry, weight_entry, ammo_consumption_entry, avg_reliability_entry, infantry_attack_entry
    global anti_tank_attack_entry, air_attack_entry, defense_entry, breakthrough_entry, armor_entry, piercing_entry
    global initiative_entry, fortification_entry, front_width_entry, manpower_cost_entry, training_time_entry
    global fuel_consumption_entry, infantry_equipment_entry, support_equipment_entry
    global division1_combobox, division2_combobox

    root = tk.Tk()
    root.title("Управление характеристиками оружия")

    # Создание и размещение виджетов для ввода данных
    tk.Label(root, text="Название дивизии:").grid(row=0, column=0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)

    tk.Label(root, text="Прочность:").grid(row=1, column=0)
    strength_entry = tk.Entry(root)
    strength_entry.grid(row=1, column=1)

    tk.Label(root, text="Организация:").grid(row=2, column=0)
    organization_entry = tk.Entry(root)
    organization_entry.grid(row=2, column=1)

    tk.Label(root, text="Скорость восстановления:").grid(row=3, column=0)
    recovery_speed_entry = tk.Entry(root)
    recovery_speed_entry.grid(row=3, column=1)

    tk.Label(root, text="Разведка:").grid(row=4, column=0)
    reconnaissance_entry = tk.Entry(root)
    reconnaissance_entry.grid(row=4, column=1)

    tk.Label(root, text="Подавление:").grid(row=5, column=0)
    suppression_entry = tk.Entry(root)
    suppression_entry.grid(row=5, column=1)

    tk.Label(root, text="Вес:").grid(row=6, column=0)
    weight_entry = tk.Entry(root)
    weight_entry.grid(row=6, column=1)

    tk.Label(root, text="Расход боеприпасов:").grid(row=7, column=0)
    ammo_consumption_entry = tk.Entry(root)
    ammo_consumption_entry.grid(row=7, column=1)

    tk.Label(root, text="Средняя надежность:").grid(row=8, column=0)
    avg_reliability_entry = tk.Entry(root)
    avg_reliability_entry.grid(row=8, column=1)

    tk.Label(root, text="Противопехотная атака:").grid(row=9, column=0)
    infantry_attack_entry = tk.Entry(root)
    infantry_attack_entry.grid(row=9, column=1)

    tk.Label(root, text="Противотанковая атака:").grid(row=10, column=0)
    anti_tank_attack_entry = tk.Entry(root)
    anti_tank_attack_entry.grid(row=10, column=1)

    tk.Label(root, text="Воздушная атака:").grid(row=11, column=0)
    air_attack_entry = tk.Entry(root)
    air_attack_entry.grid(row=11, column=1)

    tk.Label(root, text="Защита:").grid(row=12, column=0)
    defense_entry = tk.Entry(root)
    defense_entry.grid(row=12, column=1)

    tk.Label(root, text="Прорыв:").grid(row=13, column=0)
    breakthrough_entry = tk.Entry(root)
    breakthrough_entry.grid(row=13, column=1)

    tk.Label(root, text="Броня:").grid(row=14, column=0)
    armor_entry = tk.Entry(root)
    armor_entry.grid(row=14, column=1)

    tk.Label(root, text="Бронебойность:").grid(row=15, column=0)
    piercing_entry = tk.Entry(root)
    piercing_entry.grid(row=15, column=1)

    tk.Label(root, text="Инициатива:").grid(row=16, column=0)
    initiative_entry = tk.Entry(root)
    initiative_entry.grid(row=16, column=1)

    tk.Label(root, text="Укрепленность:").grid(row=17, column=0)
    fortification_entry = tk.Entry(root)
    fortification_entry.grid(row=17, column=1)

    tk.Label(root, text="Ширина фронта:").grid(row=18, column=0)
    front_width_entry = tk.Entry(root)
    front_width_entry.grid(row=18, column=1)

    tk.Label(root, text="Людские ресурсы:").grid(row=19, column=0)
    manpower_cost_entry = tk.Entry(root)
    manpower_cost_entry.grid(row=19, column=1)

    tk.Label(root, text="Время на обучение:").grid(row=20, column=0)
    training_time_entry = tk.Entry(root)
    training_time_entry.grid(row=20, column=1)

    tk.Label(root, text="Потребление горючего:").grid(row=21, column=0)
    fuel_consumption_entry = tk.Entry(root)
    fuel_consumption_entry.grid(row=21, column=1)

    tk.Label(root, text="Пехотное снаряжение:").grid(row=22, column=0)
    infantry_equipment_entry = tk.Entry(root)
    infantry_equipment_entry.grid(row=22, column=1)

    tk.Label(root, text="Снаряжение поддержки:").grid(row=23, column=0)
    support_equipment_entry = tk.Entry(root)
    support_equipment_entry.grid(row=23, column=1)

    tk.Button(root, text="Добавить запись", command=add_record).grid(row=24, column=0, columnspan=2)

    # Создание и размещение виджетов для сравнения данных
    tk.Label(root, text="Выберите первую дивизию:").grid(row=25, column=0)
    division1_combobox = ttk.Combobox(root)
    division1_combobox.grid(row=25, column=1)

    tk.Label(root, text="Выберите вторую дивизию:").grid(row=26, column=0)
    division2_combobox = ttk.Combobox(root)
    division2_combobox.grid(row=26, column=1)

    tk.Button(root, text="Сравнить дивизии", command=compare_divisions).grid(row=27, column=0, columnspan=2)

    # Инициализация выпадающих списков
    update_division_lists()

    root.mainloop()
