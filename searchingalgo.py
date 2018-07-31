#===========================Linear search algorithm=============================
#def search(a, item):
#    found = False
#    i = 0
#    for ele in a :
#        if ele == item:
#            found = True
#        else:
#            i = i+1
#    return found
#a = [10,20,30,40,50,"ram",42.3,64]
#print(search(a,10))

#=========================Binary Search algorithm===============================
def binarySearch(mylist,item):
    first = 0
    last = len(mylist)-1
    found = False
    while first <= last and found == False:
        mid = (first+last)/2
        if mylist[mid] == item:
            found = True
        else:
            if item < mylist[mid]:
                last = mid - 1
            else:
                first = mid +1
    return found
mylist = [10,20,30,40,50,60,70,80,90]
print(binarySearch(mylist,100))
