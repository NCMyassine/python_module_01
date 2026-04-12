class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        if height < 0:
            self._height = 0
        else:
            self._height = height
        if age < 0:
            self._days = 0
        else:
            self._days = age

    def show(self) -> str:
        return f"{self._name}: {self._height:.1f}cm, {self._days} days old"

    def grow(self, growth) -> float:
        self._height = round(self._height + 0.8, 1)
        growth += 0.8
        return round(growth, 1)

    def age(self) -> None:
        self._days += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def show(self) -> None:
        res: str = super().show()
        print(f"{res}\n Color: {self.color}")

    def bloom(self) -> None:
        print(f" {self._name} has not bloomed yet")
        print("[asking the rose to bloom]")
        self.show()
        print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = diameter

    def show(self) -> None:
        res: str = super().show()
        print(f"{res}\n Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self):
        print("[asking the oak to produce shade]")
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest
        self.nutritional_value = 0

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        print(super().show())
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


def main() -> None:
    growth: float = 0
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose.bloom()
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    oak.produce_shade()
    print("")
    print("=== Vegetable")
    vege = Vegetable("Tomato", 5, 10, "April")
    vege.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(1, 21):
        vege.age()
        growth += vege.grow(growth)
    vege.show()


if __name__ == "__main__":
    main()
