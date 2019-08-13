# 문제 설명
# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

# 제한 사항
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.


def solution(s):
    s = s.split(' ')  # s.split()으로 할 경우 공백이 2칸이상이어도 공백을 인덱스로 인식하지 않음
    answer = []
    for w in s:
        result = ''
        for i, c in enumerate(w):
            if i % 2 == 0:
                result += c.upper()
            else:
                result += c.lower()
        answer.append(result)
    return ' '.join(answer)


# 한 줄 코딩

def solution(s):
    return ' '.join([''.join([j.upper() if i % 2 == 0 else j.lower() for i, j in enumerate(w)])
                     for w in s.split(' ')])
