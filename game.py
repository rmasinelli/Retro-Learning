import random

# Define the Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10
        self.defense = 5
        self.position = 0

    def attack(self, enemy):
        damage = self.attack_power - enemy.defense
        enemy.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

# Define the Enemy class
class Enemy:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, player):
        damage = self.attack_power - player.defense
        player.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

# Define a simple map
rooms = ["Forest", "Cave", "Mountain", "Village"]

# Game loop
def game_loop(player):
    while player.is_alive():
        print(f"You are in the {rooms[player.position]}")
        action = input("Choose an action (move, rest, quit): ").lower()

        if action == "move":
            player.position = (player.position + 1) % len(rooms)
            print(f"You moved to the {rooms[player.position]}")
            encounter(player)
        elif action == "rest":
            player.health += 10
            print("You rested and gained 10 health.")
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Try again.")

def encounter(player):
    if random.random() < 0.5:
        enemy = Enemy("Goblin", 50, 8, 3)
        print(f"A wild {enemy.name} appears!")
        while enemy.is_alive() and player.is_alive():
            action = input("Choose an action (attack, flee): ").lower()
            if action == "attack":
                damage = player.attack(enemy)
                print(f"You dealt {damage} damage to the {enemy.name}.")
                if enemy.is_alive():
                    damage = enemy.attack(player)
                    print(f"The {enemy.name} dealt {damage} damage to you.")
            elif action == "flee":
                print("You fled the battle.")
                break
            else:
                print("Invalid action. Try again.")

        if not player.is_alive():
            print("You have been defeated!")
        elif not enemy.is_alive():
            print(f"You defeated the {enemy.name}!")
    else:
        print("The area is quiet. Nothing happens.")

# Main game function
def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    print(f"Welcome to the game, {player.name}!")
    game_loop(player)

if __name__ == "__main__":
    main()
