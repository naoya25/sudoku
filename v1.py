from question import Question


def main():
    q = Question()
    q_str = q.q_str

    if not check(q_str):
        print("正しいナンプレを入力してね")
        return

    # dfs
    stack = [(0, q_str)]
    while stack:
        i, t = stack.pop()

        if i == 81:
            print(t)
            continue

        if t[i] != "0":
            stack.append((i + 1, t))
            continue

        for j in range(1, 10):
            new_t = t[:i] + str(j) + t[i + 1 :]
            if check(new_t):
                stack.append((i + 1, new_t))


def check(s):
    # 横
    for i in range(9):
        ss = [s[i * 9 + j] for j in range(9)]
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


if __name__ == "__main__":
    main()
