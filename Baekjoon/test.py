def selectsort(lst):
    for i in range(len(lst)-1):
        min_idx = i

        for j in range(1+i,len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j

        lst[min_idx],lst[i] = lst[i], lst[min_idx]
    return lst



print(selectsort([1,2,5,3,4,7]))

def maxilen(lst):
    maxi = 0
    hao =[]
    for idx in range(len(lst)-1):
        tem = lst[idx+1]-lst[idx]
        hao.append(tem)
    print(hao)

maxilen([1, 2, 3, 4, 5, 7])