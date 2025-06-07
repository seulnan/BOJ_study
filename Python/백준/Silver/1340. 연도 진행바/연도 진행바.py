# 공백으로 한번 나누고 , 나 : 제거 하는방향이 좋음
string = input().split(" ")
# 입력받기
month = string[0]
dd = int(string[1].strip(","))
yyyy = int(string[2])
hh, mm = map(int, string[3].split(":"))

# month,day 를 상수화해서 리스트의 인덱스값으로 접근
MONTH = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
DAY = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if yyyy %400==0 or (yyyy%4==0 and yyyy%100 !=0):
    DAY[1]+=1
    
# 그리고 모든걸 다 분으로 바꿔서 한번에 퍼센트 계산할 수 있도록 단위통일
month_idx=MONTH.index(month)
# 현재시간 계산
current_time = (sum(DAY[:month_idx])+dd-1)*24*60+hh*60+mm # 그전날까지 계산하고 시간분은 따로계산해서더하기 
all_time = sum(DAY)*24*60

print(current_time/all_time*100)