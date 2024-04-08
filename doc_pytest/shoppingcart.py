class ShoppingCart:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def add(self, item):
        if self.size() == self.max_size:
            raise OverflowError("cart is full, can't add more")
        self.items.append(item)

    def size(self):
        return len(self.items)

    def prize(self, prize_map):
        total_prize = 0
        for item in self.items:
            total_prize += prize_map.get(item)
        return total_prize