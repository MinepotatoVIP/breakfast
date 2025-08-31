import time as real_time
from datetime import datetime

class Breakfast:
    # Dictionnaire des calories approximatives pour chaque aliment
    food_calories = {
        "egg": 72,  # calories par œuf
        "tomato": 22,  # calories par tomate
        "sausage": 150,  # calories par saucisse
        "bread": 80,  # calories par tranche de pain
        "butter": 102  # calories par cuillère de beurre
    }

    def __init__(self, name=None):
        self.name = name
        self.food = []
        self.time = None
        self.served_time = None
        self.total_calories = 0

    def set_name(self, name):
        """Définir le nom du petit-déjeuner"""
        self.name = name

    def add_food(self, food):
        """Ajouter des aliments au petit-déjeuner, sous forme de chaîne séparée par des virgules"""
        self.food = food.split(', ')
        self.calculate_calories()

    def set_time(self):
        """Enregistrer l'heure de préparation"""
        self.time = datetime.now().strftime('%I:%M %p')

    def serve_breakfast(self):
        """Simuler le service du petit-déjeuner"""
        self.served_time = datetime.now().strftime('%I:%M %p')
        print("Breakfast served!")

    def calculate_calories(self):
        """Calculer les calories totales du petit-déjeuner"""
        self.total_calories = 0
        for item in self.food:
            if item in Breakfast.food_calories:
                self.total_calories += Breakfast.food_calories[item]
            else:
                print(f"Warning: No calorie information for {item}!")
        
    def wait_until_served(self, delay_seconds):
        """Attendre un certain nombre de secondes avant de servir le petit-déjeuner"""
        print(f"Waiting for {delay_seconds} seconds before serving breakfast...")
        real_time.sleep(delay_seconds)
        self.serve_breakfast()

    def __str__(self):
        """Affichage des détails du petit-déjeuner"""
        food_list = ', '.join(self.food)
        return (f"Breakfast: {self.name}\n"
                f"Ingredients: {food_list}\n"
                f"Calories: {self.total_calories} kcal\n"
                f"Prepared at: {self.time}\n"
                f"Served at: {self.served_time if self.served_time else 'Not served yet'}")


class BreakfastManager:
    def __init__(self):
        self.breakfasts = []

    def create_breakfast(self, name, food, delay_seconds=0):
        """Créer un petit-déjeuner et ajouter à la liste de gestion"""
        breakfast = Breakfast(name)
        breakfast.add_food(food)
        breakfast.set_time()
        self.breakfasts.append(breakfast)

        # Servir après un délai si spécifié
        if delay_seconds > 0:
            breakfast.wait_until_served(delay_seconds)
        return breakfast

    def show_all_breakfasts(self):
        """Afficher tous les petits-déjeuners créés"""
        for breakfast in self.breakfasts:
            print("\n" + str(breakfast))

