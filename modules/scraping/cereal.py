from typing import Dict


class Nutrition:
    def __init__(
        self,
        protein: float,
        carbohydrates: float,
        fiber: float,
        fat: float,
        salt: float,
        calories: str,
    ) -> None:
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fiber = fiber
        self.fat = fat
        self.salt = salt
        self.calories = calories


class Cereal:
    def __init__(
        self,
        name: str,
        brand: str,
        price: Dict[str, float],
        grams: float,
        is_original: bool,
        nutrition: Nutrition,
    ) -> None:
        self.name = name
        self.brand = brand
        self.price = price
        self.grams = grams
        self.is_original = is_original
        self.nutrition = nutrition