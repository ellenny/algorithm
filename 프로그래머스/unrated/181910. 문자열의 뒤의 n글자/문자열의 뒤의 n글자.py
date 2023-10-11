def solution(my_string, n):
    answer = ''
    for i in my_string[len(my_string)-n::]:
        answer += i
    return answer