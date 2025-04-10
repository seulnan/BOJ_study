n = int(input())
arr = [int(input()) for _ in range(n)]

# 버블 정렬: 인접한 두 수를 비교해서 큰 수를 뒤로 보내는 방식으로 정렬하는 알고리즘

# 최악: O(n^2) 최선: O(n)
for i in range(n - 1): # i는 몇번째 반복중인지를 나타내며 한번 돌때마다 가장 큰 수가 맨뒤로 정렬됨. 하나의 수를 골라서 나머지들이랑 하나씩 비교하니까 n-1
    for j in range(n - 1 - i): # 이미 뒤쪽에 정렬된 숫자는 다시 비교할 필요없으니 그만큼 줄여서 반복함
        if arr[j] > arr[j + 1]: # 왼쪽이 더 크면 swap해야함
            # swap
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 출력
for num in arr:
    print(num)