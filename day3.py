# 크기가 작은 부분문자열 
'''
문제 설명
숫자로 이루어진 문자열 t와 p가 주어질 때, t에서 p와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return하는 함수 solution을 완성하세요.

예를 들어, t="3141592"이고 p="271" 인 경우, t의 길이가 3인 부분 문자열은 314, 141, 415, 159, 592입니다. 이 문자열이 나타내는 수 중 271보다 작거나 같은 수는 141, 159 2개 입니다.

제한사항
1 ≤ p의 길이 ≤ 18
p의 길이 ≤ t의 길이 ≤ 10,000
t와 p는 숫자로만 이루어진 문자열이며, 0으로 시작하지 않습니다.

'''
def solution(t,p):
    answer = ""
    count = 0 
    
    for i in range(len(t)):
        am = t[i:len(p)+i]
        if int(am) <= int(p) and len(p)  == len(am):
            count += 1
            
    return count 
  
  
  # 두 정수 사이의 합 
'''
  문제 설명
 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

 제한 조건
 a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
 a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
 a와 b의 대소관계는 정해져있지 않습니다.
  

'''
  
def solution(a, b):
  answer = 0
  if a <= b :
      for i in range(a,b+1):
          answer += i 
  
  else:
      for i in range(b, a+1):
          answer += i 
      
  return answer

# 나머지가 1이 되는 수 찾기
"""
  문제 설명
자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

제한사항
3 ≤ n ≤ 1,000,000

    
"""
    
def solution(n):
  for i in range(1,n):
      if n % i == 1:
          return i 
  
  
# 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
"""
제한사항
absolutes의 길이는 1 이상 1,000 이하입니다.
absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
signs의 길이는 absolutes의 길이와 같습니다.
signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.
    
"""
def solution(absolutes, signs):
    answer = []
    for i in range(len(signs)):
        if signs[i] == 1 :
            answer.append(absolutes[i])
        elif signs[i] == 0 :
            answer.append(absolutes[i] * -1)
        
    return sum(answer)
  
# 문제 설명
"""
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
  
"""

def solution(answers):
    result = []
    
    answer_1 = [1,2,3,4,5] * 2000
    answer_2 = [2,1,2,3,2,4,2,5] * (10000 // 8)
    answer_3 = [3,3,1,1,2,2,4,4,5,5] * (10000 // 10)
    
    count1 = 0
    count2 = 0
    count3 = 0
    
    for i in range(len(answers)):
        if answer_1[i] == answers[i]:
            count1 += 1 
        if answer_2[i] == answers[i]:
            count2 += 1
        if answer_3[i] == answers[i]:
            count3 += 1 
    
    if max(count1, count2, count3) == count1:
        result.append(1)
    if max(count1, count2, count3) == count2:
        result.append(2)
        
    if max(count1, count2, count3) == count3:
        result.append(3)

    return result
