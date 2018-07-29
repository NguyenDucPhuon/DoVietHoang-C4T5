prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total = 0
for key, value in prices.items():
    print(key)
    print("price : ", value)
    print("stock : ", stock[key])
    print(20 * '*')
    money = value * stock[key]
    total += money

print(f"The amount of money you would earn if you sold all of your food is {total}")