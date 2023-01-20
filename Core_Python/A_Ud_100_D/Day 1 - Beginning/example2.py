
def solv(A):
    ele_len = len(A)
    for i in range(0, ele_len - 1):
        for j in range(i + 1, ele_len - 1):
            if A[i] == A[j]:
                return A[i]
    else:
        return -1

A = [10, 5, 3, 4, 3, 6, 9, 10]
ret_res = solv(A)
print(ret_res)



