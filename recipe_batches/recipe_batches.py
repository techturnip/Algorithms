#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batch_nums = []

    for key in recipe:
        # base case:
        # if a recipe key doesn't exist in
        # ingredients then you can't make
        # the recipe
        if key not in ingredients:
            # return 0
            return 0

        # ingredient value devided by recipe value
        batch_nums.append(ingredients[key] // recipe[key])

    for i in range(0, len(batch_nums)):
        if batch_nums[i] == 0:
            return 0

        for num in batch_nums:
            if batch_nums[i] <= num:
                lowest_num = batch_nums[i]
                return lowest_num

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
