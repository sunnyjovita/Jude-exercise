# exercises 1
inventory = {'gold' : 500, 'pouch' : ['flint', 'twine', 'gemstone'], 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}
# list = ["seashell", "strange berry", "lint"]
# inventory["pocket"] = list
inventory["pocket"] = ["seashell", "strange berry", "lint"]
inventory["backpack"].sort()
print(inventory)
inventory["backpack"].remove("dagger")
inventory["gold"] += 50
print(inventory)

# exercises 2
prices = {}
prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3

stock = {}
