def solution(n, lost, reserve):
    n = list(range(1,n+1))
    lost.sort()
    reserve.sort()
    cnt = len(n) - len(lost)
    save = []
    for i in lost:
        if n[i-1] in reserve:
            cnt += 1
            save.append(n[i-1])
            continue

        if n[i-1] == n[0]:
            if n[i] in reserve and n[i] not in lost:
                cnt += 1
                save.append(n[i])

        elif n[i-1] == n[-1]:
            if n[i-2] in reserve and n[i-2] not in lost and n[i-2] not in save:
                cnt += 1
                save.append(n[i-2])

        else:
            if n[i-2] in reserve and n[i-2] not in lost and n[i-2] not in save:
                cnt += 1
                save.append(n[i-2])

            elif n[i] in reserve and n[i] not in lost and n[i] not in save:
                cnt += 1
                save.append(n[i])
            else:
                pass

    return(cnt)