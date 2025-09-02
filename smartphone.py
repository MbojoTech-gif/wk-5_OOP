# Smartphone Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def call(self, contact):
        print(f"{self.brand} {self.model} is calling {contact}... 📞")

    def charge(self, amount):
        self.battery += amount
        print(f"{self.brand} {self.model} charged to {self.battery}% 🔋")

    def info(self):
        print(f"📱 {self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}%")

# Inheritance: GamingPhone (child of Smartphone)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system  # extra feature

    # Polymorphism: Override call() method
    def call(self, contact):
        print(f"{self.brand} {self.model} starts a VOICE CHAT with {contact} 🎧 (Gaming Mode)")

    def play_game(self, game):
        print(f"{self.brand} {self.model} is playing {game} 🎮 with {self.cooling_system} cooling system!")


# Testing classes
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 85)
phone2 = GamingPhone("Asus", "ROG Phone 8", 512, 95, "Liquid Cooling")

phone1.info()
phone1.call("Alice")
phone1.charge(10)

print("-----")

phone2.info()
phone2.call("Bob")
phone2.play_game("PUBG Mobile")
