def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        row = []

        for j in range(len(arr2[i])):
            row.append(arr1[i][j] + arr2[i][j])

        answer.append(row)

    return answer


arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

print(solution(arr1, arr2))


# 헷갈린 부분:
# len(arr2)는 행의 개수이고, len(arr2[i])는 현재 행의 열 개수이다.

# 실수한 점:
# 열을 반복하는 안쪽 반복문에서 len(arr2)를 사용해
# 열의 개수보다 큰 인덱스에 접근했다.