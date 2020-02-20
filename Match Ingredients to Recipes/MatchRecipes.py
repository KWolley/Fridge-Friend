#!/usr/bin/python3

#Script: matching ingredients in kitchen with recipes

#INGREDIENTS 
ingredients_file = open('ItemsInKitchen.txt') #open file with ingredients
ingredients_file.readline() #moving read cursor to third line where ingredients start

#read in each line with ingredient name and store in list
ingredients = []
for ing in ingredients_file.readlines():
    if (ing == '\n' or ing == 'Staple Items:\n'):
        break
    else:
        ingredients.append(ing[3:-1]) #removing ' -' and '/n' to get word only
#Output
print('\nCurrent ingredients in your kitchen:')
i_string = ' '
for i in ingredients:
    i_string += i + ", "
print(i_string[:-2])


#RECIPES
#Names of all recipe files
recipes = ["SnickerdoodleCookies.txt", 'Enchiladas.txt', 'Rabokki.txt', 'Tiramisu.txt',
        'TomatoMozSandwich.txt', 'VegStirFry.txt', 'ChanaMasala.txt']


#MATCHING
import re
def IngredientToRecipe():
    #Search each ingredient in each recipe file
    matched_recipes = []
    for ingredient in ingredients:
        #takes ingredient string as regex pattern
        item = re.compile(ingredient, re.IGNORECASE)
        
        #search through all recipes
        for current_recipe in recipes:
            #open each recipe file and read in recipe name
            r = open(('Recipes/' + current_recipe), 'r')
            recipe_name = (r.readline())[8:-1] #slice 'Recipe:' from line to get name
            r.seek(0) #brings read cursor back to start of file
            
            #match ingredient name regex in recipe file
            if item.search(r.read()):
                #check if recipe name has already been added to list
                if recipe_name not in matched_recipes:
                    matched_recipes.append(recipe_name) #add recipe name to options
            r.close() #close each recipe file when done

    
    #OUTPUT FOR USER
    if len(matched_recipes) == 0: #when no recipes matched the ingredient
        print("\nOh no! No recipes in the library include this ingredient. ")
    if len(matched_recipes) == 1:
        print('\nYou can try out this recipe!')
        print('-' + matched_recipes[0])
    else:
        print("\nHere are recipes you can try:")
        for option in matched_recipes:
            print('- ' + option)
    print("\n")


#RUN PROGRAM
IngredientToRecipe()
