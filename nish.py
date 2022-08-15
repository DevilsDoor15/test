# l1 = [1,2,3,4,5]
# opt = [1,3,6,10,15]
# temp = 0
# l2 = []
# for i in l1:
#     temp=temp+i
#     l2.append(temp)
# print(l2)
# 0
# 0+1=1
# 1+2=3
# 3+3=6
# 6+4=10
# 10+5=15



l1 = [1,16,81,256,625]
opt =[1,2,3,4,5]
l2 = []
for i in l1:
    i= i**(1/4)
    l2.append(i)
print(l2)
