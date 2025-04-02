cnt = 0
def recursion(s, l, r):
    global cnt
    cnt +=1 
    if l >= r: return 1 # 0이 길이보다 크거나 같다 -> 단일문자라는 뜻 or 범위가 다 좁혀질때까지 같다는 뜻 -> 무조건 1
    elif s[l] != s[r]: return 0 # 맨 첫글자랑 맨 뒤글자가 다르다고 검증. 무조건 0
    else:
        return recursion(s, l+1, r-1) # 그것도 같다면 앞에서 두번쨰, 뒤에서 두번째로 다시 재귀

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(int(input())):
    cnt = 0
    print(isPalindrome(input().rstrip()), cnt)