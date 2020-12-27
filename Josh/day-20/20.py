import re

with open("input.txt") as fp:
    lines = fp.readlines()

if __name__ == "__main__":
    possible_allergies = {}
    all_ingredients = set()
    for line in lines:
        ingredients, allergies = line.strip().strip(")").split(" (contains ")
        ingredients = set(ingredients.split(" "))
        all_ingredients = all_ingredients.union(ingredients)
        for allergen in allergies.split(", "):
            if allergen in possible_allergies:
                possible_allergies[allergen] = possible_allergies[
                    allergen
                ].intersection(ingredients)
            else:
                possible_allergies[allergen] = ingredients
    allergens = {}
    while len(allergens) < len(possible_allergies):
        for allergen, ingredient_set in possible_allergies.items():
            if len(ingredient_set) == 1:
                for ingredient in ingredient_set:
                    break
                allergens[allergen] = ingredient
                for other in possible_allergies:
                    if ingredient in possible_allergies[other]:
                        possible_allergies[other].remove(ingredient)
    safe = all_ingredients.difference(allergens.values())

    with open("input.txt") as fp:
        text = fp.read()
        safe_count = sum(
            len(re.findall(rf"\b{ingredient}\b", text)) for ingredient in safe
        )
        print(safe_count)
        print(f"Part 2: {','.join(allergens[k] for k in sorted(allergens))}")
