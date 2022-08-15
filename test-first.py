# is_rider= False
# is_licence = False
# if is_rider and is_licence:
#     print("aniket is licenced rider")
# elif is_rider and not is_licence:
#     print("aniket is rider")
# elif is_licence and is_rider or not is_licence and not is_rider:
#     print("aniket has no right to ride a bike")


# l1 = [1,2,3,4,5,6,7,8,9]
# def evn(temp):
#     return temp%2 == 0

# x = lambda evn(x) : x

# evenList = list(filter(evn,l1))
# evenList = list(map(evn,l1))
# evenList = list(filter(lambda evn: evn % 2 == 0,l1))
# evenList = list(filter(lambda evn: evn % 2 == 1,l1))
# evenList = list(filter(lambda evn: evn % 2 != 0,l1))

# print(evenList)
# print(evn(l1[2]))

def countD(i,l2):
    count = 0
    for li in l2:
        if i == li:
            count = count + 1
    return count



l2 = [1,2,5,1,2,5,7,8,9,5,6,6,6,4,4,5,2,1,0]
temp = 1
expOp = [1,2,4,5,6]
l3 = []
for i in l2:
    if(countD(i,l2) > 1 and i not in l3):
        l3.append(i)

print(l3)

def mult(pric,qnt):
    return pric * qnt

price = 10
qnt = 5
totalPrice = 0
# totalPrice = price * qnt
print(mult(price,qnt))