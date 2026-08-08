#      0 1 2 3 4 5 6 7 8 9 10 11
blist = [2, 3, 4, 5, 6, 7, 8, 9, 7, 7, 31, 3]
clist = [2, 3, 4, 5, 6, 7, 3]
dlist = [2, 6, 7, 8, 9, 7, 7, 31, 3]
elist = [2, 3, 4, 5, 6, 3]


def house(alist):
    previous_num = 0
    print("                                                        ")
    print("Printing current and previous number sum in a range(10)")
    for current_index in range(len(elist)):
        current_num = elist[current_index]
        sum = previous_num + current_num
        print(f"current number {current_num} previous number {previous_num} sum {sum}")
        previous_num = current_num

#
# house(elist)
# house(dlist)
# house(blist)


def printing_sum(alist):
    previous_num = 0
    print("                                                        ")
    print("Printing current and previous number sum in a range(10)")
    for current_index in range(len(alist)):
        current_num = alist[current_index]
        sum = previous_num + current_num
        print(f"current number {current_num} previous number {previous_num} sum {sum}")
        previous_num = current_num

# printing_sum(blist)
# printing_sum(clist)
# printing_sum(dlist)
# printing_sum(elist)



word1 = "MuazEroglu"

def print_even_index(astring):
    print(f"original string is {astring}")
    print("Printing only even index chars")
    for index in range(len(astring)):
        if index %2 == 0:
            print(astring[index])
        # else:
            # print("")print

print_even_index(word1)

