##카운터에는 거스름돈으로 사용할 500원 100원 50원 10원짜리 동전이 무한히 존재
##손님에게 거슬러 줘야 할 돈이 N원일때 거슬러 줘야할 동전의 최소 개수를 구하라
##단, 거슬러 줘야할 돈 N은 10의 배수이다

print("N을 입력하세요")
N=input()
N=int(N)

count=0

type=[500,100,50,10]
for coin in type:
    count+=N//coin
    N%=coin

print(count)    

##최초 알고리즘 (bad)
##print("N을 입력하세요")
##N=input()
##N=int(N)
##N500=N//500
##N100=(N%500)//100
##N50=(N%100)//50
##N10=(N%50)//10
##
##answer= N500+N100*N50+N10
##print(answer)

##피드백 : 처음에는 배열에 넣지 않고 하나하나 계산해 넣음 배열에 넣어서 for문 사용하면 간단해짐!!!!!!!왜 안했을까..
