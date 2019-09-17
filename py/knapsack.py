class Item(object):
    weight = 0
    value = 0

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return 'Item \n' + 'weight: ' + str(self.weight) + '\n' + 'value: ' + str(self.value) + '\n'


def basic_knapsack(availableWeight, items, numItems):
    maxValue = 0
    for i, item in enumerate(items):
        if item.weight <= availableWeight:
            tempValue = basic_knapsack(availableWeight - item.weight, items, numItems)
            possibleMaxValue = tempValue + item.value
            if possibleMaxValue > maxValue:
                maxValue = possibleMaxValue
    return maxValue


# Returns the maximum value that can be put in a knapsack with capacity availableWeight
def knapsack_01(availableWeight, items, n):
    if n == 0 or availableWeight == 0 : 
        # base case
        return 0
  
    if (items[n-1].weight > availableWeight): 
        # If weight of the nth item weighs more than the current knapsack capacity,
        # move on to the next item
        return knapsack_01(availableWeight, items, n-1) 
  
    else: 
        # return the maximum of two cases: 
        # (1) nth item included 
        # (2) not included 
        # get combs with the nth item, making sure to subtract it's weight from the sack capacity
        temp1 = items[n-1].value + knapsack_01(availableWeight-items[n-1].weight, items, n-1)
        # get combs w/o the nth item
        temp2 = knapsack_01(availableWeight, items, n-1)
        return max(temp1, temp2)


# originally i wanted to use a dictionary for faster lookup, but couldn't decide on what to use as a key
# i dont think you can use availableWeight + n, because of a case where 2 different items have the same sum(availableWeight +n)
# for ex. <Item>[Item(weight: 10, value: 1), Item(weight: 9, value: 200)]
# the first item's availableWeight is 10, n is 0. 10 + 0 = 10.
# the second item's availableWeight is 9, n is 1. 9 + 1 = 10.
# so, the memoization lookup would resolve to the value of whichever was computed first, totally ignoring the different values associated with them
# maybe n * c, or another function would work? look into this laterrr

# just use array for now
def knapsack_01_memoized(availableWeight, items, n, memo):
    if memo[availableWeight][n] != None:
        # before doiGng any calculation, check if the memo has done it already
        return memo[availableWeight][n]

    if n == 0 or availableWeight == 0 : 
        # base case
        result = 0
  
    if (items[n-1].weight > availableWeight): 
        # If weight of the nth item weighs more than the current knapsack capacity,
        # move on to the next item
        result = knapsack_01(availableWeight, items, n-1) 
  
    else: 
        # return the maximum of two cases: 
        # (1) nth item included 
        # (2) not included 
        # get combs with the nth item, making sure to subtract it's weight from the sack capacity
        temp1 = items[n-1].value + knapsack_01(availableWeight-items[n-1].weight, items, n-1)
        # get combs w/o the nth item
        temp2 = knapsack_01(availableWeight, items, n-1)
        result = max(temp1, temp2)
    # memoize this return value before returning it
    memo[availableWeight][n] = result
    return result



if __name__ == '__main__':
    capacity = 165
    items1 = [
        Item(39, 92),
        Item(22, 57),
        Item(29, 49),
        ]
    print(basic_knapsack(capacity, items1, len(items1)))    

    # source: p01
    # https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
    items2 = [
        Item(23, 92),
        Item(31, 57),
        Item(29, 49),
        Item(44, 68),
        Item(53, 60),
        Item(38, 43),
        Item(63, 67),
        Item(85, 84),
        Item(89, 87),
        Item(82, 72)
        ]
    # solution = [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
    # total val: 309
    print(knapsack_01(capacity, items2, len(items2)))

    memo = [[None for i in range(capacity)] for i in range(len(items2))]
    print(knapsack_01_memoized(capacity, items2, len(items2), memo))