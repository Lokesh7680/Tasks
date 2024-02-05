alphabets = {}.fromkeys("abcdy","consonant")

print(alphabets)

for key,value in alphabets.items():
    print(key,value)

m = fast_food_items = {"McDonald's": "Big Mac",
                        "Burger King": "Whopper",
                        "Chick-fil-A": "Original Chicken Sandwich"}

print(fast_food_items.pop("McDonald's"))

fast_food_items.popitem()
print(fast_food_items)