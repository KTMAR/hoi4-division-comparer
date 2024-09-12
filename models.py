from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WeaponStats(Base):
    __tablename__ = 'weapon_stats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True, unique=True)

    # Базовые параметры
    strength = Column(Float, nullable=False)
    organization = Column(Float, nullable=False)
    recovery_speed = Column(Float, nullable=False)
    reconnaissance = Column(Float, nullable=False)
    suppression = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    ammo_consumption = Column(Float, nullable=False)
    avg_reliability = Column(Float, nullable=False)

    # Боевые параметры
    infantry_attack = Column(Float, nullable=False)
    anti_tank_attack = Column(Float, nullable=False)
    air_attack = Column(Float, nullable=False)
    defense = Column(Float, nullable=False)
    breakthrough = Column(Float, nullable=False)
    armor = Column(Float, nullable=False)
    piercing = Column(Float, nullable=False)
    initiative = Column(Float, nullable=False)
    fortification = Column(Float, nullable=False)
    front_width = Column(Float, nullable=False)

    # Стоимость
    manpower_cost = Column(Float, nullable=False)
    training_time = Column(Float, nullable=False)
    fuel_consumption = Column(Float, nullable=False)
    infantry_equipment = Column(Float, nullable=False)
    support_equipment = Column(Float, nullable=False)

    def __str__(self):
        return (f"Дивизия: {self.name}\n"
                f"Прочность: {self.strength}\n"
                f"Организация: {self.organization}\n"
                f"Скорость восстановления: {self.recovery_speed}\n"
                f"Разведка: {self.reconnaissance}\n"
                f"Подавление: {self.suppression}\n"
                f"Вес: {self.weight}\n"
                f"Расход боеприпасов: {self.ammo_consumption}\n"
                f"Средняя надежность: {self.avg_reliability}\n"
                f"Противопехотная атака: {self.infantry_attack}\n"
                f"Противотанковая атака: {self.anti_tank_attack}\n"
                f"Воздушная атака: {self.air_attack}\n"
                f"Защита: {self.defense}\n"
                f"Прорыв: {self.breakthrough}\n"
                f"Броня: {self.armor}\n"
                f"Бронебойность: {self.piercing}\n"
                f"Инициатива: {self.initiative}\n"
                f"Укрепленность: {self.fortification}\n"
                f"Ширина фронта: {self.front_width}\n"
                f"Людские ресурсы: {self.manpower_cost}\n"
                f"Время на обучение: {self.training_time}\n"
                f"Потребление горючего: {self.fuel_consumption}\n"
                f"Пехотное снаряжение: {self.infantry_equipment}\n"
                f"Снаряжение поддержки: {self.support_equipment}\n")

    def compare_with(self, other_weapon):
        fields = ['strength', 'organization', 'recovery_speed', 'reconnaissance', 'suppression',
                  'weight', 'ammo_consumption', 'avg_reliability', 'infantry_attack', 'anti_tank_attack',
                  'air_attack', 'defense', 'breakthrough', 'armor', 'piercing', 'initiative',
                  'fortification', 'front_width', 'manpower_cost', 'training_time', 'fuel_consumption',
                  'infantry_equipment', 'support_equipment']

        differences = {}

        for field in fields:
            current_value = getattr(self, field)
            other_value = getattr(other_weapon, field)

            if current_value != other_value:
                if current_value > other_value:
                    differences[field] = (current_value, other_value, True)
                else:
                    differences[field] = (current_value, other_value, False)

        return differences
