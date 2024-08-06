#프로그래머스 코딩테스트 스터디 2일차-(2).python
'''
문제 - 문자열 내 p와 y의 개수

문제 설명
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

제한사항
문자열 s의 길이 : 50 이하의 자연수
문자열 s는 알파벳으로만 이루어져 있습니다.
'''

def solution(s):
    answer = True
    
    # p를 셀 함수 p_count, y를 셀 함수 y_count를 정의 합니다.
    p_count, y_count = 0, 0
    
    for i in s:
        # i 가 p이거나 P면 p_count에 1을 더합니다.
        if i == "p" or i == "P":
            p_count += 1
        # i 가 y이거나 Y면 y_count에 1을 더합니다.
        if i == "y" or i == "Y":
            y_count += 1
    
    #만약 p_count와 y_count가 같다면 True, 아니면 False를 반환합니다.
    if p_count == y_count:
        return True
    return False