
#Write a function that will return the count of given character in the given string

def character (string):
    print (len(string))
character("jone")



#Write a function that will return count of characters till the given one

def character (string):
        if len(string)>4:
            print("doesn't satisfy the requirement ")
        else:
            print(len(string))
character("how are you")

#Write a function that will return the factorial of a given number
def factorial(n):
    a = 1
    for i in range(2, n + 1):
        a *= i
    return a
print(factorial(5))

#Write a function that will return true if the number is bouquet and false if not.
def bouquet (number):
        if number % 5 == 0:
            return True
        else:
            return False
print(bouquet(10))

#powerup if the number is bouquet
def power_up (num):
    if bouquet (num) == True:
        return num**3
print(power_up(10))






