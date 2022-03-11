def solution(phone_book):
    answer = True

    # for p in phone_book:
    #     if len(phone_book) != len(set([i[:len(p)] for i in phone_book])):
    #         print(set([i[:len(p)] for i in phone_book]))
    #         answer = False
    #         break

    phone_book.sort()
    # print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break

    # for p in phone_book:
    #     if p in [i[:len(p)] for i in phone_book]

    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))