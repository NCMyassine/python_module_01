class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

    def grow(self, growth) -> float:
        self.height = round(self.height + 0.8, 1)
        growth += 0.8
        return round(growth, 1)

    def Age(self) -> None:
        self.age += 1


def main() -> None:
    print("=== Plant Factory Output ===")
    plnts = [
        Plant("Rose", round(25, 1), 30),
        Plant("Oak", round(200, 1), 365),
        Plant("Cactus", round(5, 1), 90),
        Plant("Sunflower", round(80, 1), 45),
        Plant("Fern", round(15, 1), 120),
    ]
    for e in plnts:
        print("Created: ", e.show())


if __name__ == "__main__":
    main()
