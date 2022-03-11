def solution(key, lock):
    key_size = len(key)
    lock_size = len(lock)
    key_loc =[]
    lock_loc =[]

    for i in range(key_size):
        for j in range(key_size):
            if key[i][j]: key_loc.append((i,j))

    for i in range(lock_size):
        for j in range(lock_size):
            if not lock[i][j]: lock_loc.append((i,j))

    def rotate_90_loc(key_loc):
        for idx, (i, j) in enumerate(key_loc):
            key_loc[idx] = (j, key_size-1-i)

    def match(key_loc, lock_loc):
        s, e = 1-key_size, lock_size+key_size-1
        for m_i in range(s,e):
            for m_j in range(s,e):
                # if m_i == 1 and m_j == 1:
                #     print('ha')
                count = 0
                for k_loc in key_loc:
                    k_m_i = k_loc[0] + m_i
                    k_m_j = k_loc[1] + m_j
                    # 자물쇠 바깥에 있으면 continue
                    if k_m_i >= lock_size or k_m_i < 0 or k_m_j >= lock_size or k_m_j < 0: continue
                    # 자물쇠와 맞으면 count ++
                    if (k_m_i, k_m_j) in lock_loc: count+=1
                    # 자물쇠와 맞지 않으면 break
                    else: break
                if count == len(lock_loc): return True
        return False

    for _ in range(4):
        # print(key_loc)
        if match(key_loc, lock_loc): return True
        rotate_90_loc(key_loc)

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))