def run_length_encoding(item):
    count, result, i = 1, "", 0
    while i < len(item):
        char = item[i]
        while i+1 < len(item) and item[i+1] == char:
            count += 1
            i += 1
        result += char + str(count)
        count = 1
        i += 1
    print(result)

run_length_encoding("wwwwaaadexxxxxx")