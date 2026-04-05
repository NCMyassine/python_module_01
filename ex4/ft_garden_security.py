class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        if height < 0:
            self._height = 0
        else:
            self._height = height
        if age < 0:
            self._age = 0
        else:
            self._age = age

    def show(self) -> str:
        return f"{self._name}: {self._height}cm, {self._age} days old"

    def set_height(self, newdata: int):
        if newdata < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = newdata
            print(f"Height updated: {newdata}")

    def set_age(self, newdata: int) -> None:
        if newdata < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = newdata
            print(f"Age updated: {newdata}")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age


def main() -> None:
    rose = Plant("Rose", round(15, 1), 10)
    print("=== Garden Security System ===")
    print("Plant created: ", rose.show())
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    print("Current state: ", rose.show())


if __name__ == "__main__":
    main()
