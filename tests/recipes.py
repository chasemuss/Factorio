import json

def get_raw(product):
    with open('./database/recipes.json') as recipes_file:
        recipes = json.loads(recipes_file.read())
    
    print(f'Looking for {product}')
    raw = []
    
    # Check for product
    recipe = {}
    for r in recipes:
        if r['name'] == product:
            recipe = r
            break
    if recipe == {}:
        print(f'No recipe found for {product}')
        return -1
    
    for ingredient in recipe['ingredients']:
        next_level_down = get_raw(ingredient['name'])
        print('Next Level', ingredient['name'], next_level_down)
        if next_level_down == -1:
            print(f"Adding {ingredient['name']} to {product}'s raw")
            raw.append(ingredient)
            
    print(f'Raw Ingredients for {product} = {raw}')
    return raw

if __name__=='__main__':
    get_raw('automation-science-pack')