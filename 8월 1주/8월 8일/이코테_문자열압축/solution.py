def solution2(s):
    length = len(s)
    answer = int(length)

    for step in range(1, length // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1

        for j in range(step, length, step):
            if prev == s[j : j + step]:
                count += 1
            else:
                if count > 1:
                    compressed = compressed + str(count) + prev
                else:
                    compressed = compressed + prev
                prev = s[j : j + step]
                count = 1

        if count > 1:
            compressed = compressed + str(count) + prev
        else:
            compressed = compressed + prev

        answer = min(answer, len(compressed))

    return answer


def solution(s):
    length = len(s)
    answer = int(length)

    for step in range(1, length // 2 + 1):
        start, end = 0, step
        next_start, next_end = step, step + step
        word, value = "", 1

        while True:
            current_word = s[start:end]
            next_word = s[next_start:next_end]

            if current_word == next_word:
                value += 1
            else:
                if value > 1:
                    # aa / aa
                    word = word + str(value) + current_word
                else:
                    # aa / ac
                    word = word + current_word

                value = 1

            start, end = start + step, end + step
            next_start, next_end = start + step, end + step

        if value > 1:
            word = word + str(value) + current_word
        else:
            word = word + current_word

        print(word, step)
        answer = min(answer, len(word))

    return answer
