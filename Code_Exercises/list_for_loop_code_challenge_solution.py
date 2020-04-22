## List and loops code challenge

numberList = []

# Version #1
#numberList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

# Version #2
for i in range(51):
    numberList.append(i)

# Version #3
# stop number is 51 b/w the range stops at 51

for i in range(0, 51):
    numberList.append(i)

for eachNumber in numberList: 
    print(eachNumber)
