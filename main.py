import tomllib
import json

def make_recipe_tree(target_item, layer = 0):
  print(f'{'\t' * layer}{target_item = }')
  recipe_tree = {}
  for machine in recipes[target_item]:
    
    if recipes[target_item][machine]["Type"] == "Resource":
      return { "Time": recipes[target_item][machine]["Time"], "Output": recipes[target_item][machine]["Output"] }
    
    for ingredient in recipes[target_item][machine]["Ingredients"]:
      next_layer = make_recipe_tree(ingredient, layer + 1)
      
  

with open('Recipes.toml', 'rb') as items_fin:
  recipes = tomllib.load(items_fin)

# print(json.dumps(recipes, indent=4))

item_to_make = "Automation_Science_Pack"
make_recipe_tree(item_to_make)