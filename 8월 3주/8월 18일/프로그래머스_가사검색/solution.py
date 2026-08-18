def find_left_index(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left


def find_right_index(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    return right


# https://school.programmers.co.kr/learn/courses/30/lessons/60060
def solution(words, queries):
    answer = []
    array = [[[] for _ in range(2)] for _ in range(100001)]

    for word in words:
        list_word = [x for x in word]
        reverse_list_word = list_word[::-1]

        array[len(word)][0].append("".join(list_word))
        array[len(word)][1].append("".join(reverse_list_word))

    for i in range(100001):
        array[i][0].sort()
        array[i][1].sort()

    for query in queries:

        if query[0] == "?":
            query = "".join([x for x in query][::-1])
            a = find_left_index(array[len(query)][1], query.replace("?", "a"))
            b = find_right_index(array[len(query)][1], query.replace("?", "z"))
            answer.append(b - a + 1)
        else:
            a = find_left_index(array[len(query)][0], query.replace("?", "a"))
            b = find_right_index(array[len(query)][0], query.replace("?", "z"))
            answer.append(b - a + 1)

    return answer
