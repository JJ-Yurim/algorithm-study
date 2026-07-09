def solution(arr, divisor):
    answer = []

    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    
    if len(answer) == 0:
        answer.append(-1)

    answer.sort()
    return answer



# arr = [5, 9, 7, 10]
# divisor = 5

# arr = [2, 36, 1, 3]	
# divisor = 1

arr = [3,2,6]	
divisor =10

print(solution(arr, divisor))


# ===================================
# 헷갈린 부분:
# 결과 배열을 작은 수부터 정렬하는 방법이 기억나지 않았다.
#
# 틀린 부분:
# 나누어떨어지는 값과 빈 배열 예외 처리는 맞았지만,
# 문제에서 요구한 오름차순 정렬을 하지 않았다.
#
# 해결:
# return 전에 answer.sort()를 사용했다.
#
# 확인할 점:
# 문제에서 결과의 정렬 순서를 요구하는지 확인한다.
# sort()는 원본 리스트를 정렬하고 반환값은 None이다.
# sorted()는 정렬된 새로운 리스트를 반환한다.