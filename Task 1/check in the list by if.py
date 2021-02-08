# if we have this list [2,4,6,8,10]
List = [2,4,6,8,10]

# check to see if 4 in this list or not
if 4 in List:
    print("4 is in the list")
else:
    print("4 isn't in the list")

# check to see if 4 & 6 in this list on not
if all([4 in List, 6 in List]):
    print("4 & 6 aren't in the list")
else:
    print("4 & 6 not in the list")


# check to see if 3 or 6 in this list
if any([3 in List, 6 in List]):
    print("4 or 6 in the list")
else:
    print(" 4 or 6 aren't in the list")


#  check to see if 2 , 4 and 5 in this list
if all([2 in List, 4 in List, 5 in List]):
    print("2, 4 & 5 are in the list")
else:
    print("2, 4 & 5 aren't in the list")