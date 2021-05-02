#My name is Kelly
list1 = ["M" , "na", "i", "Ke"]
list2 = ["y", "me" ,"s" , "lly"]

print([list1[0]+list2[0], list1[1]+list2[1], list1[2]+list2[2], list1[3]+list2[3]])

list3 = [5,74,85,1]
print(list3[0]**2, list3[1]**2, list3[2]**2, list3[3]**2)

#Write a program that will calculate sum of lists members.

list4 = [5,8,6,4,7,8]

print(sum(list4))


#Write a Python program to remove duplicates from a list.
list4 = [1,5,4,99,6,5,4,1,2,5]
final_list = []

def dublicate_numbers (list4):
    for symbol in list4:
        if symbol in final_list:
            continue
        else:
         final_list.append (symbol)
    print(final_list)

dublicate_numbers(list4)

#Write a Python program to get unique values from a list.
list5 = [1,1,2,2,3,3,4,4,5,5]
unique_numbers = []

def find_unique_numbers (list5):
    unique_numbers = []
    for symbol in list5:
        if symbol in unique_numbers:
            continue
        else:
            unique_numbers.append(symbol)
    return unique_numbers
print (find_unique_numbers (list5))


