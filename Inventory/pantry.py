from datetime import date
from datetime import timedelta
import pandas as pd


#read in truncated fruit .csv with names as dataframe index
#note: conversion from .xslx to .csv added one trailing space to fruit names TO DO
store = pd.read_csv("fruits.csv", index_col="Name")


class Pantry:
#User inventory class, contains all ingredients on hand

    #dict storing at home ingredients
    pantry = {}
    
    def __init__(self):
        return
    
    #the argument as text is initially for testing purposes
    #how this is passed in by the application interface can be modified later
    #to match with valid entries in store
    def add_item(self, text):
        new_item = Ingredient(text)
        self.pantry[text] = new_item

        
        
class Ingredient:
    
    def __init__(self, text):
        
        self.purchase_date = date.today()
        self.Fridge1 = int(store.at[text,'Fridge1'][0])         #using only lower-end fridge expiration dates for initial testing
        self.Fridge2 = int(store.at[text,'Fridge2'][0])         #only handles one integer TO DO parse all leading ints
        self.expiration_date = date.today() + timedelta(days = self.Fridge1)
        #manual expiration date for testing only. inflexible. TO DO set using if statements below with correct timedelta keyword (days,weeks,months)
        self.qty = 1 
    
    def update_qty(self, qty):
        self.qty = qty
        
#         set type of time unit for calculating expiration date
#         timedelta keyword days,months etc cant be variables TO DO
# 
#         self.date_type1 = self.Fridge1[1] #TO DO parse for trailing char (allow 1 - 2 ints for time)
#         if self.date_type1 == 'd':
#             self.date_type1 = 'days'
#         elif self.date_type1 == 'w':
#             self.date_type1 = 'weeks'
#         elif self.date_type1 == 'm':
#             self.date_type1 = 'months'

# #can't handle duplicate indices in store currently
# #duplicates in simple store need differentiation TO DO