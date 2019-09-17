def find_missing_with_set_in(shortList, bigList):
    set1 = set(shortList)
    for x in list2:
        if x not in set1:
            return x

def find_missing_meme_solution(lilMeme, bigMeme):
    return sum(bigMeme) - sum(lilMeme)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 3, 4, 5]

    print(find_missing_with_set_in(list1, list2))
    print(find_missing_meme_solution(list1, list2))