# Fridge Friend: Milestone 3
Saloni Sharma, Patrick Conley, Kara Wolley

# Automated Unit Tests
<<<<<<< HEAD
Unit tests are located in the script named MatchRecipes_Test.py in directory [Match Ingredients to Recipes](https://github.com/KWolley/Fridge-Friend/tree/master/Match%20Ingredients%20to%20Recipes).\
The entire directory should be cloned to run the testing file. Then, after using the command "chomd +x MatchRecipes_Test.py", the test can be run using ./MatchRecipes_Test.py.

# User Acceptance Testing

## 1. User views recipes for ideas on what food to make 
#### Description
     Test recipe matching with ingredient
#### Pre-conditions
     User has valid user name and password
#### Test steps
     1. Navigate to "Recipes" page via button
     2. Provide ingredient(s) name(s)
     3. Click search button
#### Expected result
     User can view a list of recipes that utilize the ingredient(s)
#### Actual result
     User is shown names and links to recipes
#### Status (Pass/Fail)
     Pass
#### Post-conditions
     Search through database of recipes and output matching recipes.
     User can click and view specific recipes for more information.
    
## 2. Website traversal - link management
=======
Unit tests in script called MatchRecipes_Test.py in directory [Match Ingredients to Recipes](https://github.com/KWolley/Fridge-Friend/tree/master/Match%20Ingredients%20to%20Recipes).\
The entire directory should be cloned to run the testing file.

# User Acceptance Testing

## User views recipes for ideas on what food to make 
#### Description
   Test recipe matching with ingredient
#### Pre-conditions
    User has valid user name and password
#### Test steps
      1. Navigate to ‘recipes’ page\
      2. Provide ingredient(s) name(s)
      3. Click search button
#### Expected result
    - User can view a list of recipes that utilize the ingredient(s)
#### Actual result
    - User is shown names and links to recipes
#### Status (Pass/Fail)
      Pass
#### Post-conditions
    - Search through database of recipes and output matching recipes.
    - User can click and view specific recipes for more information.
    
## Website traversal - link management
>>>>>>> KW,edits
#### Description
    Test that all links traverse pages accurately, and that user can return to home at any time
#### Pre-conditions
    All html, css and image files are uploaded correctly
#### Test steps
    1. Navigate to the home page
    2. select the Pantry button in the header
    3. select the Logo (carrot button) in the header
    4. select Recipes in the header
    5. select Pantry in the footer
<<<<<<< HEAD
    6. select Account in the header
    7. select Contact Us in the footer
    8. select Recipes in the footer
    9. select Pantry in the header
    10. select Account in the footer
=======
    6. selct Account in the header
    7. select Contact Us in the footer
    8. select Recipes in the footer
    9. select Pantry in the header
    10. selct Account in the footer
>>>>>>> KW,edits
    11. return home using the Logo  in the header
#### Expected result
    User should be directed to pages with the following text
    1. What would you like to do today?
    2. Welcome to your pantry
    3. What would you like to do today?
    4. Recipes
    5. Welcome to your pantry
    6. Account Management
    7. Contact Us
    8. Recipes
    9. Welcome to your pantry
    10. Account Management
    11. What would you like to do today?
#### Actual result
    User is through each webpage
#### Status (Pass/Fail)
    Pass
#### Notes
    N/A
#### Post-conditions
<<<<<<< HEAD
    User is able to successfully traverse through pages 

## 3. User interaction
#### Description
    Allow the user to interact with owner by submitting a form with a name, email and text fields
=======
    User is able to succesfully traverse through pages 

## User interaction
#### Description
    Allow the user to interact with owner by submitting a form with a name, emial and text fields
>>>>>>> KW,edits
#### Pre-conditions
    User is able to traverse to Contact Us page
#### Test steps
    1. Navigate to Contact Us page
    2. Provide name in the "Name" field
    3. Provide E-mail in the "E-mail" field
    4. Type "hello fridge friend" in "Message" field
#### Expected result
    User should be able to submit form without error
#### Actual result
<<<<<<< HEAD
    Data not passed correctly 
#### Status (Pass/Fail)
    Fail
#### Notes
    Need to improve where data is being stored for owner to use
=======
    data not passed correctly 
#### Status (Pass/Fail)
    fail
#### Notes
    need to improve where data is being stored for owner to use
>>>>>>> KW,edits
