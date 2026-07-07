def solution(num):
    answer = 0

    while num != 1:

        if num % 2 == 0:
            num = num // 2
            answer += 1
        else:
            num = (num * 3)+1
            answer += 1

        if answer == 500:
            return -1
                
    return answer


num = 6
print(solution(num))


# 실수한 점
# 1. num이 1이 될 때까지 반복해야 하는데 while 조건을 반대로 작성함
# 2. 짝수 판별에 몫 연산자(//)를 사용함 → 나머지 연산자(%)를 사용해야 함
# 3. 홀수 계산식에서 + 1을 빠뜨림
# 4. 정수 나눗셈이므로 / 대신 //를 사용해야 함