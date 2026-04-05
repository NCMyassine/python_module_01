class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self, growth) -> int:
        self.height = round(self.height + 0.8, 1)
        growth += 0.8
        return round(growth, 1)

    def Age(self) -> None:
        self.age += 1


def main() -> None:
    i: int = 2
    growth: int = 0
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(f"{rose.show()}")
    for i in range(2, 8):
        print(f"=== Day {i} ===")
        growth = + rose.grow(growth)
        rose.Age()
        print(f"{rose.show()}")
    print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    main()
