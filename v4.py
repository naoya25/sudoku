from question import Question
import time


def main():
    q = Question(
        s="800000000003600000070090200050007000000045700000100030001000068008500010090000400"
    )
    q_str = q.q_str

    if not check_all(q_str):
        print("正しいナンプレを入力してね")
        return

    # dfs
    s_t = time.time()
    stack = [(0, q_str)]
    while stack:
        i, t = stack.pop()

        if i == q_str.count("0"):
            print(t)
            print("正解" if t in q.get_ans() else "不正解")
            continue

        k, next_options = find_next(t)
        for j in next_options:
            new_t = t[:k] + j + t[k + 1 :]
            stack.append((i + 1, new_t))

    e_t = time.time()
    print(f"タイム: {e_t - s_t}s")


# 全マスチェック
def check_all(s):
    # 横
    for i in range(9):
        ss = s[i * 9 : (i + 1) * 9]
        for j in range(1, 10):
            if ss.count(str(j)) > 1:
                return False
    # 縦
    for i in range(9):
        ss = [s[i % 9 + 9 * j] for j in range(9)]
        for j in range(1, 10):
            if ss.count(str(j)) > 1:
                return False
    # 3 x 3
    for i in range(9):
        ss = [s[i // 3 * 27 + i % 3 * 3 + j // 3 * 9 + j % 3] for j in range(9)]
        for j in range(1, 10):
            if ss.count(str(j)) > 1:
                return False
    return True


def check_i(s, i):
    # 横
    r = i // 9
    ss = s[r * 9 : (r + 1) * 9]
    for j in range(1, 10):
        if ss.count(str(j)) > 1:
            return False
    # 縦
    ss = [s[i % 9 + 9 * j] for j in range(9)]
    for j in range(1, 10):
        if ss.count(str(j)) > 1:
            return False
    # 3 x 3
    ss = [s[i // 27 * 27 + i % 9 // 3 * 3 + j // 3 * 9 + j % 3] for j in range(9)]
    for j in range(1, 10):
        if ss.count(str(j)) > 1:
            return False
    return True


def find_next(s):
    i, max_n, cannot_set = 0, 0, set()
    for k in range(81):
        if s[k] != "0":
            continue

        r_arr = list(s[k // 9 * 9 : k // 9 * 9 + 9])  # 横
        c_arr = [s[k % 9 + 9 * j] for j in range(9)]  # 縦
        b_arr = [s[k // 27 * 27 + k % 9 // 3 * 3 + j // 3 * 9 + j % 3] for j in range(9)]  # 3x3

        now_set = set(r_arr + c_arr + b_arr)
        n = len(now_set)
        if max_n < n:
            max_n = n
            i = k
            cannot_set = now_set
    return i, set(map(str, range(1, 10))) - cannot_set


if __name__ == "__main__":
    main()
