import random
import time


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.is_stunned = False  # Флаг оглушения после получения крита

    def attack(self, other):
        # Если герой оглушен после получения крита, ограничиваем урон
        if self.is_stunned:
            damage_multiplier = random.uniform(0, 0.5)  # 0-50% при оглушении
            self.is_stunned = False  # Снимаем оглушение после атаки
        else:
            damage_multiplier = random.uniform(0, 1.5)  # 0-150% обычная атака

        damage = int(self.attack_power * damage_multiplier)

        # Проверяем на увертывание (урон меньше 20% от базового)
        if damage_multiplier < 0.2:  # 20% от 20 = 4 урона
            print(f"{self.name} атакует и наносит {damage}% урона! {other.name} увернулся! 🤸")
            return

        other.health -= damage

        # Проверяем, был ли это критический удар для противника
        if damage_multiplier > 1.0:  # >100% - критический удар
            other.is_stunned = True  # Противник оглушен на следующий ход
            emoji = "💥"
            comment = " МОЩНЫЙ УДАР!"
        elif damage_multiplier > 0.7:
            emoji = "⚔️"
            comment = ""
        else:
            emoji = "🗡️"
            comment = " Слабовато..."

        print(f"{self.name} атакует {emoji} и наносит {damage}% урона!{comment}")

        # Проверяем, не убил ли этот удар противника
        if not other.is_alive():
            print(f"💀 {other.name} погиб!")

        # Если противник убит, сбрасываем его оглушение
        if not other.is_alive():
            other.is_stunned = False

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("=== НАЧАЛО БОЯ ===")
        print(f"{self.player.name} vs {self.computer.name}")
        print(f"Здоровье игрока: {self.player.health}")
        print(f"Здоровье компьютера: {self.computer.health}")
        print("Урон возможен от 0% до 150% от стандартного (20)")
        print("После ПОЛУЧЕНИЯ мощного удара (>100%) противник оглушен и бьет слабее")
        print("Противник может увернуться! - тогда урон < 4")
        print("-" * 60)

        round_number = 1

        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n--- Раунд {round_number} ---")

            # Ход игрока (всегда первый)
            self.player.attack(self.computer)
            if self.computer.is_alive() and self.computer.health < 100:
                print(f"❤️ У {self.computer.name} осталось {max(0, self.computer.health)} здоровья")
            elif not self.computer.is_alive():
                break

            # Ход компьютера
            self.computer.attack(self.player)
            if self.player.is_alive() and self.player.health < 100:
                print(f"❤️ У {self.player.name} осталось {max(0, self.player.health)} здоровья")

            round_number += 1

            time.sleep(1)   # небольшая задержка для читаемости

        # Определение победителя
        print("\n" + "=" * 60)
        print("=== БОЙ ЗАВЕРШЕН ===")
        if self.player.is_alive():
            print(f"🏆 {self.player.name} ПОБЕДИЛ!")
            print("🎉 Поздравляем с победой!")
        else:
            print(f"🏆 {self.computer.name} ПОБЕДИЛ!")
            print("💻 Попробуй ещё раз!")


# Запуск игры
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()