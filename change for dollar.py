# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 17:36:43 2023

@author: kpenaalvarez
"""

def make_change(amount, coins):
    # Base cases
    if amount == 0:
        return 1  # Valid combination found
    if amount < 0 or not coins:
        return 0  # Invalid combination
    
    # Recursive cases
    return make_change(amount - coins[0], coins) + make_change(amount, coins[1:])


coins = [1, 5, 10, 25, 50]
num_ways = make_change(100, coins)
print("Number of ways to make change for a dollar:", num_ways)
