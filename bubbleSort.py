# bubble sort

def bubble_sort(numList):
    for i in range(len(numList) -1 ,0, -1):
        for j in range(i):
            if numList[j] > numList[j+1]:
                temp = numList[j]
                numList[j] = numList[j+1] 
                numList[j+1] = temp

    return numList



print(bubble_sort([6,2,5,8,1,9]))

