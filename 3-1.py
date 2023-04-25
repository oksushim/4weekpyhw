#학생들 이름 입력
name = list(input("학생들의 이름을 순서대로 입력해 주세요 :").split(","))

#학생들 점수 입력
num = list(map(int, input("학생들의 성적을 순서대로 입력해 주세요 :").split(",")))

score = dict(zip(name,num))   #스코어가 dic인것 정의
av = sum(num)/len(num)   #평균 구하기

print(score)
print(av)
