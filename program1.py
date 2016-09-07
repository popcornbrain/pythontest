robot = {"price": 900, "count": 2, "tax": 1.25}
book = {"price": 100, "tax": 1.06}

print(robot["price"] * robot["count"] * robot["tax"] + book["price"] * book["tax"])