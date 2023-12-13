start=input("Starting Numbers: ")
rows=input("Amount of Rows: ")
if not start.isnumeric() or not rows.isnumeric():
    raise Exception("Input has to be Integers")
curList=list(map(int,start))
rows=int(rows)
print(curList)
for i in range(rows-1):
    curNum=curList[0]
    amount=0
    newList=[]
    for j in curList:
        if curNum != j:
            newList.append(amount)
            newList.append(curNum)
            curNum=j
            amount=1
        else:
            amount+=1
    newList.append(amount)
    newList.append(curNum)
    curList=newList
    print(curList) 
