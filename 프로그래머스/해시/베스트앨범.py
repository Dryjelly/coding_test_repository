def solution(genres, plays):
    answer = []

    music_dict = dict()

    for i, g in enumerate(genres):
        if g in music_dict:
            music_dict[g][0].append(i)
            music_dict[g][1] += plays[i]
        else:
            music_dict[g] = [[i], plays[i]]

    sorted_dict = sorted(music_dict.items(), key=lambda x : x[1][1], reverse=True)

    print(sorted_dict)
    
    for item in sorted_dict:
        # print('item', item, item[1][0])
        if len(item[1][0])==1: answer += item[1][0]
        else: answer += sorted(item[1][0], key=lambda x: plays[x], reverse=True)[:2]
        # print(answer)
        # print(sorted(item[1][0], key=lambda x: plays[x], reverse=True)[:2])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))
print(solution(["classic", "pop", "classic", "classic", "pop", "shit"],[500, 600, 150, 800, 2500, 90]))