
# number1 = 50
# number2 = 30
# case2_umber1 = 40
# case2_number2 = 30
#
# case_1 = number1 * number2
# sum = number1 + number2
# if case_1 <= 1000:
#     print(case_1)
# else:
#     print(sum)
#
# def product(x, y):
#     pro= x* y
#     return pro
#
# def sum(x,y):
#     sum = x + y
#     return sum
#
# def evaluate_number(x, y):
#     p = product(x,y)
#     print(" Product of "+str(x)+" and "+ str(y) + " is "+ str(p))
#     s = sum(x, y)
#     print(" Sum of " + str(x) + " and " +str(y) + " is " + str(s))
#     if p <= 1000:
#         return p
#     else:
#         return s
#
#
# print("pls enter x value")
# x=input()
# print("pls enter y value")
# y=input()
#
# result = evaluate_number(int(x), int(y))
#
# print("Result is " + str(result))
# =================================================================



sentence_1 = input("what would you like to order sir or madam: ")
sentence_2 = float(input("i forgot the price of that could u say the price of it again?: "))
sentence_3 = int(input("great, how many of it would you like?:"))

total = sentence_2 * sentence_3

print(f"ok so you want {sentence_3} {sentence_1} and the price for each {sentence_1} is {sentence_2} so your total will be {round(total, 2)} ")


