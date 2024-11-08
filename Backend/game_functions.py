import json

def total_raw(target_item):
    with open('./database/recipes.json') as recipe_file:
        recipes = json.loads(recipe_file.read())

    target_recipe = [r for r in recipes if r['Name'] == target_item][0]
    raw_ingredients = {}
    



if __name__ == '__main__':
    total_raw('Automation Science Pack')