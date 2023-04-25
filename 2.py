n, x = map(int,input("n,x :").split(","))  
li = list(map(int,input("n개의 숫자를 입력해 주세요 :").split(",")))  

i = 0
for i in range(0,n) :
    if li[i] > x :
        print(li[i], end=",")
