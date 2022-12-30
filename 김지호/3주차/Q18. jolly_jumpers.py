num = input("input=")
num_list0 = num.split(',')

for j in range(2):
    num_list = num_list0[j].split(' ')

    num_set = set()

    for i in range(1, int(num_list[0])):
        num_set.add(i)

    for i in range(2, int(num_list[0])+1):
        num_set2= {abs(int(num_list[i])-int(num_list[i-1]))}
        num_set= num_set - num_set2

    if len(num_set) == 0:
        print("joly")
    else:
        print("not joly")

num = input("input=")
num_list0 = num.split(',')

for j in range(2):
    num_list = num_list0[j].split(' ')

    num_set = set()

    for i in range(1, int(num_list[0])):
        num_set.add(i)

    for i in range(2, int(num_list[0])+1):
        num_set2= {abs(int(num_list[i])-int(num_list[i-1]))}
        num_set= num_set - num_set2

    if len(num_set) == 0:
        print("joly")
    else:
        print("not joly")

print(num_list0[2])