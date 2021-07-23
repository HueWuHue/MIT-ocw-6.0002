###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    # This isn't dynamic coding thus 0 marks
    # It is actually greedy
    # However the dynamic solutions does not sound better than greedy
    # Dynamic solution 1: Similar to Fib solution,save 1-98 solutions
    # basically memoization but it does not fit in this case
    # Dynamic solution 2: Recursion but how?
    # thus I went for greedy
    curr_weight = 0
    egg_num = 0
    while curr_weight < target_weight:
        for egg in egg_weights:
            if curr_weight + egg <= target_weight:
                max_weight = egg
        curr_weight += max_weight
        egg_num += 1
    return egg_num

if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 199
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 199")
    print("Expected ouput: 13 (7 * 25 + 2 * 10 + 4 * 1)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
