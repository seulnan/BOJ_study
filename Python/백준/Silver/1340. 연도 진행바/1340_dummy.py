# 일단 날짜를입력받아야함
# , 로 구분후 공백제거 해야하는것보다 그냥 어차피 분단위로 다바꿀거니까 공백기준으로 다 나누고 그안에서 ,랑 :제거
string = input().split(" ") # 공백제거후 리스트로 넣기

month = string[0]
dd = int(string[1].strip(","))
print(dd)
yyyy = int(string[2])
hh, mm = map(int, string[3].split(":"))
print(month,dd,yyyy,hh,mm)

# month 를 상수화해서 리스트의 인덱스값으로 접근
MONTH = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# 평년일때 각 달의 막날숫자도 다름(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31일)
# 윤년일때는 또 따로 고려해야(31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31일) -> 2월이 29인것만 다름
DAY = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if yyyy % 400 == 0 or (yyyy % 4 == 0 and yyyy % 100 != 0):
    DAY[1] +=1

# 전체 일자가 몇개인지 알아야함. 일자로 하면 불편하니까 그냥 모든 날짜랑 시간을 분단위로 바꾸는것이 포인트!!(단위통일)
all_time = sum(DAY)*24*60 # 그해의 전체시간을 분으로 바꾸기(일자기준)

month_idx = MONTH.index(month) # 아니걍 순회안하고 month랑 일치하는거 index찾기로 바로하면되네

current_time = (sum(DAY[:month_idx])++dd-1)*24*60+hh*60+mm
print(current_time/all_time*100)

# dMay 10, 1981 00:31ummy시도들
"""
아니 무한 If문 하지말고 month가 MONTH 리스트 순회하면서 인덱스를 출력시키면안됨??
for m in MONTH:
    if month == m:
        print(MONTH.index(m))
2월 제외하고 홀수는 31일 짝수는 30일,
아니근데 결론은 이번해가 몇프로지났는지 출력하는건데
일단 그전달까지 일을 모두 더해야하고,
"""
