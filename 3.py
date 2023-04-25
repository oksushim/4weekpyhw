#학생들 이름 입력
name = list(input("학생들의 이름을 순서대로 입력해 주세요 :").split(","))

#학생들 점수 입력
num = list(map(int, input("학생들의 성적을 순서대로 입력해 주세요 :").split(",")))

#스코어가 dic인것 정의
score = {}

for i in range (0, len(name)) :   #학생 수만큼 반복
    score[name[i]] = num[i]   #하나씩 추가해서 딕셔너리로 생성
    av = sum(num)/len(name)   #평균 구하기

print(score)
print(av)

