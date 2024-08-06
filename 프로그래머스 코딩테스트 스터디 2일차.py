#프로그래머스 코딩테스트 스터디 2일차.python
'''
문제: x만큼 간격이 있는 n개의 숫자

문제 설명
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

제한 조건
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.

입출력 예
x  |    n	| answer
2  |	5	| [2,4,6,8,10]
4  |	3	| [4,8,12]
-4 |	2	| [-4, -8]
'''

def solution(x, n):
    # 만약 x가 양수라면?
    if x > 0:
        # answer 리스트에 x부터 x*n+1까지 x간격으로 담습니다.
        answer = [i for i in range(x,x*n+1,x)]    
        
    # 만약 x가 음수라면?
    elif x < 0:
        # answer 리스트에 x부터 x*n-1까지 x간격으로 담습니다.
        answer = [i for i in range(x,x*n-1,x)]
    
    # 만약 x가 0이라면?
    else:
        # answer 리스트에 0을 n개 담습니다.
        answer = [0]*n
    
    return answer