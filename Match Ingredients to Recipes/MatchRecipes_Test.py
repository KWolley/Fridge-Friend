#!/usr/bin/python3
# Saloni Sharma

import unittest
import MatchRecipes

class MatchRecipesTesting(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    
    #TEST 1
    #Check whether ingredients (ItemsInKitchen) have been stored correctly
    def test_ingredient_names(self):
        #this is what the ingredients should be
        ingredients_list = ['Tomatoes', 'Cilantro', 'Bread', 'Eggs',\
            'Milk', 'Cheese', 'Carrots', 'Broccoli', 'Onion']
        #list from MatchRecipes to test
        MRList = MatchRecipes.StoreIngredients('ItemsInKitchen.txt')
        #check that both lists have the same ingredients
        for item, MRitem in zip(ingredients_list, MRList):
            self.assertEqual(item, MRitem)


    #TEST 2
    #Check whether recipe names were stored correctly from recipe files
    def test_recipe_filenames(self):
        #this is what the filenames should be
        Filenames = ['Tiramisu.txt', 'Enchiladas.txt', 'VegStirFry.txt', \
            'Rabokki.txt', 'TomatoMozSandwich.txt', 'SnickerdoodleCookies.txt', \
            'ChanaMasala.txt']
        #run function to get filenames from MatchRecipes
        Recipe_files = MatchRecipes.StoreRecipeFilenames('Recipes/')
        if Recipe_files == Filenames:
            result = True
        else:
            result = False
        #Check whether both lists of filenames are the same
        self.assertTrue(result)

    
    #TEST 3
    #Test whether ingredients matched to correct recipes
    def test_matched_recipes(self):
        #create lists to use in IngredientToRecipe() function below
        Recipe_files = MatchRecipes.StoreRecipeFilenames('Recipes/')
        Pantry_list = MatchRecipes.StoreIngredients('ItemsInKitchen.txt')
        #this is what the matched recipe names should be
        recipe_names = ['Chana Masala', 'Cheese Enchiladas with Green Sauce',\
             'Tomato Mozzarella Sandwich', 'Tiramisu Cake','Rabokki - Ramen with Rice Cake',\
             'Snickerdoodle Cookies', 'Vegetable Stir Fry']
        #run function to get list of matched recipes from MatchRecipes 
        MRRecipes = MatchRecipes.IngredientToRecipe(Pantry_list, Recipe_files)
        #check that both lists are the same
        self.assertListEqual(recipe_names, MRRecipes)


#Run test cases
if __name__ == '__main__':
    unittest.main()