# x만큼 간격이 있는 n개의 숫자 
"""
문제 설명 
함수 solution은 정수 x와 자연수 n을 입력 받아, 
x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
  
제한 조건
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.
  
  
"""
def solution(x, n):
    answer = []
    a_x = x 
    for i in range(n):
        answer.append(a_x)
        a_x += x 
        
        
    return answer
  
  

  
# 문자열 내p와 y의 개수 
"""
문제 설명
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

제한사항
문자열 s의 길이 : 50 이하의 자연수
문자열 s는 알파벳으로만 이루어져 있습니다.
  
"""

def solution(s):
    answer_p = 0
    answer_y = 0
    
    for i in s.lower():
        if i == 'p':
            answer_p += 1
        elif i == 'y':
            answer_y += 1 
    
    if answer_p == answer_y:
        return True

    return False



# 자릿수 더하기
"""
문제 설명
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

제한사항
N의 범위 : 100,000,000 이하의 자연수
"""
def solution(n):
    sum_h = 0
    for i in str(n):
        sum_h += int(i)
    
    return sum_h


# 핸드폰 번호 가리기 
"""
문제 설명
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
phone_number는 길이 4 이상, 20이하인 문자열입니다.    
    
    
"""

def solution(phone_number):
    answer = ''
    
    for i in range(len(phone_number)-4):
        answer += '*'
    answer += phone_number[-4:]
    
    
    return answer