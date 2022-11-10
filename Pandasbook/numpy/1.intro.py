import numpy as np
data = [1,2,3]
arr = np.array(data)

# print(arr)


# 넘파이는 행렬이나 다차원 배열을 관리하기 위한 ndarray 객체를 사용
# array 함수에 파이썬 리스트를 넘겨주면 ndarray 타입의 객체를 반환

print(type(arr))


data2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(data2d[2])

arr=np.array(data2d)
        # arr[행 인덱스, 열 인덱스]
print(arr[0: ,2])