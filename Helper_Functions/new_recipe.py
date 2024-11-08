import json

def new_recipe():
    with open('./Database/recipes.json') as recipe_file:
        recipes = json.load(recipe_file)
    
    recipes.append({
        "Name": input('What are we making? '),
        "Ingredients": [
            {"Name": input(f'Ingredient {x} Name: '), "Quantity": float(input(f"How much is needed? "))}
            for x in range(int(input('How many ingredients? ')))],
        "Base Time (Seconds)": float(input('How long does it take to make this? ')),
        "Produced By": [
            input('Machine Name: ') 
            for x in range(int(input('How many machines can make this? ')))
        ]
    })

    with open('./Database/recipes.json', 'w') as recipe_file:
        recipe_file.write(json.dumps(recipes, indent=4))
    
    


if __name__ == '__main__':
    new_recipe()