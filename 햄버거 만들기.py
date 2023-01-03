def solution(ingredient):
    answer, start_search_idx = 0, 0
    str_ingredient = "".join(str(ingredient)[1:-1].split(", "))
    while True:
        find_idx = str_ingredient.find("1231", start_search_idx)
        if find_idx == -1:
            break
        else:
            answer += 1
            str_ingredient = str_ingredient[0:find_idx] + str_ingredient[find_idx+4:]
            if find_idx < 3:
                start_search_idx = 0
            else:
                start_search_idx = find_idx - 3
    return answer

ingredient = list(map(int, (input()[1:-1]).split(",")))
print(solution(ingredient))