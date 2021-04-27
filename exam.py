

x = 5
y = 10
days = 1

def km (days,x, y):
    while x < y :
        x = x + x*0.1
        days +=1
    return days

print(km(5,x,y))


def erankyuni (a,b,c):
    if a == b == c:
        print ("isoclase")
    elif a != b & b != c & c != a:
        print ("simple")
    elif a == b or b == c & a != c:
        print("2 side equal")
    elif a == c or b == c & b != c:
        print("2 side equal")
    elif b == c or a == c & b != a:
        print ("2 side equal")
    else:
        print ("not possible")

erankyuni(10,10,10)

def year (number):
    if number %4 == 0 or number %400 == 0 & number%100 != 0:
        return "yes"
    else:
        return "no"
print (year(1800))

x=2
y=3
x1=4
y1=5





