# program 1
# if __name__ == '__main__':
#     n = int(input())
#     arr =list(map(int, input().split()))
#     s1=set(arr)
#     s2= list(s1)
#     s2.sort()
#     print(s2[-2])

# # program 2
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Berry
# Harry
# if __name__ == '__main__':
#     ghelist=[]
#     temp=[]
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         temp = [name,score]
#         s1= set(temp)
#         ghelist.append(s1)
#         # ghelist.sort()
       
#     print(temp)
#     print(s1)

# Function calling
def dictionairy():

	# Declaring hash function
	key_value = {}

# Initializing the value
	key_value['sa'] = 56
	key_value['sm'] = 2
	key_value['ak'] = 12
	key_value['ns'] = 24
	key_value['ae'] = 18
	key_value['ds'] = 323
	
	# Note that it will sort in lexicographical order
	# For mathematical way, change it to float
	print(sorted(key_value.items(), key=lambda kv:
				(kv[1], kv[0]))[-2])


def main():
	# function calling
	dictionairy()


# main function calling
if __name__ == "__main__":
	main()
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
