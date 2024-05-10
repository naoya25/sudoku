from question import Question
import time


def main():
    q = Question()
    q_str = q.q_str

    if not check_all(q_str):
        print("正しいナンプレを入力してね")
        return

    # dfs
    s_t = time.time()
    stack = [(0, q_str)]
    while stack:
        i, t = stack.pop()

        if i == 81:
            print(t)
            print("正解" if t in q.get_ans() else "不正解")
            continue

        if t[i] != "0":
            stack.append((i + 1, t))
            continue

        for j in range(1, 10):
            new_t = t[:i] + str(j) + t[i + 1 :]
            if check_i(new_t, i):
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


if __name__ == "__main__":
    main()
