def isSublist(larger, smaller):
    # print('smaller is : ',smaller)
    lt_smaller = len(smaller)
    result_is_sublist = False

    for index,item in enumerate(smaller):
        for idx,itm in enumerate(larger):
            # print('-----', larger[idx:idx+len(smaller)])
            if item == item and smaller == larger[idx:idx+len(smaller)]:
                result_is_sublist = True
                return result_is_sublist


    return result_is_sublist

larger_list = [1,2,3,4,5,6,7,8]
smaller_list = [3,4,5]

result = isSublist(larger_list, smaller_list)
print('is sublist exists ? ', result)