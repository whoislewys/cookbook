''' Given an unsorted list, find the kth smallest number in that list '''


def kth_smallest(nums, k):
  return sorted(nums)[k-1]


def quick_select(nums, k):
  # todo: 
  pass


if __name__ == '__main__':
  list1 = [1, 3, 4, 0, 9]
  print(kth_smallest(list1, 3))
  # solution: 3
  print(quick_select(list1, 3))
