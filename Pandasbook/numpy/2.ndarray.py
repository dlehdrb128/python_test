import numpy as np

data2 = [
    [1, 2, 5],
    [3, 4, 7],
    [5, 8, 9],
    [5, 8, 5]
]

data5 =[5] 
    



arr2 = np.array(data2)
arr5 = np.array(data5)
# print(arr2)

# print(arr5.shape, "얍")


# data = [
#     [1],
#     [2],
#     [3],
#     [4]    
# ]
# c = np.array(data)
# print( c.shape )


# (2행, 2열)
# print(arr2.shape)  
# # 데이터 차원
# print(arr2.ndim)
# # 데이터 자료형
# print(arr2.dtype)

# # 0부터 4까지 길이가 5인
# print(np.arange(5))
# # 1부터 4까지 길이가 4인   마지막 제외      
print(np.arange(1, 5),"ㅇㅇㅇ")
# # 1부터 4까지 2씩 증가하는 데이터 생성
# print(np.arange(1, 5, 3))



# ndarr1 = np.arange(6)
# # [0,1,2,3,4,5] / 2
# ndarr2 = ndarr1.reshape(2, 3) 
# #
# print(ndarr2)