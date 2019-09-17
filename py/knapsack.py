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


# Returns the maximum value that can be put in a knapsack of 
def knapSack01(availableWeight, items, n):
    if n == 0 or availableWeight == 0 : 
        # base case
        return 0
  
    if (items[n-1].weight > availableWeight): 
        # If weight of the nth item weighs more than the current knapsack capacity,
        # move on to the next item
        return knapSack01(availableWeight, items, n-1) 
  
    else: 
        # return the maximum of two cases: 
        # (1) nth item included 
        # (2) not included 
        temp1 = items[n-1].value + knapSack01(availableWeight-items[n-1].weight, items, n-1)
        temp2 = knapSack01(availableWeight, items, n-1)
        return max(temp1, temp2)


# # Returns the maximum value that can be put in a knapsack of 
# def knapSack01(availableWeight, items, n):
#     # base case
#     if n == 0 or availableWeight == 0 : 
#         return 0
  
#     # If weight of the nth item is more than Knapsack of capacity 
#     # availableWeight, then this item cannot be included in the optimal solution 
#     if (items[n-1].weight > availableWeight): 
#         return knapSack01(availableWeight, items, n-1) 
  
#     # return the maximum of two cases: 
#     # (1) nth item included 
#     # (2) not included 
#     else: 
#         return max(items[n-1].value + knapSack01(availableWeight-items[n-1].weight, items, n-1), 
#                    knapSack01(availableWeight, items, n-1)) 


if __name__ == '__main__':
    items1 = [
        Item(39, 92),
        Item(22, 57),
        Item(29, 49),
        ]
    print(basic_knapsack(165, items1, len(items1)))    

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
    print(knapSack01(165, items2, len(items2)))