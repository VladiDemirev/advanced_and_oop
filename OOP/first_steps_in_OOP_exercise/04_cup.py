class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity: int) -> None:
        new_quantity = self.quantity + quantity
        if new_quantity <= self.size:
            self.quantity = new_quantity

    def status(self) -> int:
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
