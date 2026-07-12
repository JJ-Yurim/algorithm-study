def solution(phone_number):

    hidden = '*' * (len(phone_number) -4)
    last_number = phone_number[-4:]

    answer = hidden + last_number

    return answer


# phone_number = "01033334444"
phone_number = "027778888"

print(solution(phone_number))



# 헷갈린 점
# 1. 문자열은 불변 자료형이어서 문자 하나를 직접 변경할 수 없다.
# 2. for문의 i를 변경해도 원본 phone_number는 변경되지 않는다.
# 3. 마지막 4자리를 제외한 개수는 len(phone_number) - 4이다.
# 4. 문자열 곱셈과 슬라이싱을 사용하면 반복문 없이 해결할 수 있다.