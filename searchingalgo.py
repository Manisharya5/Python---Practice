#===========================Linear search algorithm=============================
def search(a, item):
    found = False
    i = 0
    for ele in a :
        if ele == item:
            found = True
        else:
            i = i+1
    return found
a = [10,20,30,40,50,"ram",42.3,64]
print(search(a,10))
