import random
import time


# v4ベースで作成
class Sudoku:
    def __init__(self):
        self.q_str: str = ""
        self.q_ans: list = []

    def set_q_str(self, s: str):
        self.q_str: str = s

    def display_s(self, s: str) -> None:
        print("+-------+-------+-------+")
        for i in range(9):
            b1 = " ".join(map(lambda x: "." if x == "0" else x, s[i * 9 : i * 9 + 3]))
            b2 = " ".join(map(lambda x: "." if x == "0" else x, s[i * 9 + 3 : i * 9 + 6]))
            b3 = " ".join(map(lambda x: "." if x == "0" else x, s[i * 9 + 6 : i * 9 + 9]))
            print(f"| {b1} | {b2} | {b3} |")
            if i % 3 == 2:
                print("+-------+-------+-------+")

    # self.q_strの全マスチェック
    def check_all(self) -> bool:
        # 横
        for i in range(9):
            ss = self.q_str[i * 9 : (i + 1) * 9]
            for j in range(1, 10):
                if ss.count(str(j)) > 1:
                    return False
        # 縦
        for i in range(9):
            ss = [self.q_str[i % 9 + 9 * j] for j in range(9)]
            for j in range(1, 10):
                if ss.count(str(j)) > 1:
                    return False
        # 3 x 3
        for i in range(9):
            ss = [self.q_str[i // 3 * 27 + i % 3 * 3 + j // 3 * 9 + j % 3] for j in range(9)]
            for j in range(1, 10):
                if ss.count(str(j)) > 1:
                    return False
        return True

    # sのi番目のみチェック
    def check_i(self, s: str, i: int) -> bool:
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

    # 探索時に選択肢の少ないものの位置とその選択肢を計算
    def find_next(self, s: str) -> (int, set):
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

    # dfsですべての解答を取得
    def get_set_ans(self) -> list:
        ans = []
        stack = [(0, self.q_str)]
        while stack:
            i, t = stack.pop()

            if i == self.q_str.count("0"):
                ans.append(t)
                continue

            k, next_options = self.find_next(t)
            for j in next_options:
                new_t = t[:k] + j + t[k + 1 :]
                stack.append((i + 1, new_t))
        self.q_ans = ans
        return ans

    # 新しい問題作成時の初期配置を生成
    def get_init_grid(self) -> str:
        s = ""
        arr = list(map(str, range(1, 10)))
        random.shuffle(arr)
        s += "".join(arr[:3]) + "0" * 6
        s += "".join(arr[3:6]) + "0" * 6
        s += "".join(arr[6:]) + "0" * 6
        random.shuffle(arr)
        s += "0" * 3 + "".join(arr[:3]) + "0" * 3
        s += "0" * 3 + "".join(arr[3:6]) + "0" * 3
        s += "0" * 3 + "".join(arr[6:]) + "0" * 3
        random.shuffle(arr)
        s += "0" * 6 + "".join(arr[:3])
        s += "0" * 6 + "".join(arr[3:6])
        s += "0" * 6 + "".join(arr[6:])
        return s

    def create_new_ans(self) -> str:
        stack = [(0, self.get_init_grid())]
        while stack:
            i, t = stack.pop()

            if t.count("0") == 0:
                return t

            k, next_options = self.find_next(t)
            for j in next_options:
                new_t = t[:k] + j + t[k + 1 :]
                stack.append((i + 1, new_t))
        return 0


def create_questions(q):
    new_ans = q.create_new_ans()

    # 穴開けていく
    new_q = new_ans
    i_arr = list(range(81))
    random.shuffle(i_arr)
    for i in i_arr:
        next_s = new_q[:i] + "0" + new_q[i + 1 :]
        q.set_q_str(s=next_s)
        ans_arr = q.get_set_ans()
        if len(ans_arr) == 1:
            new_q = next_s

    return new_ans, new_q


def main():
    q = Sudoku()
    i = 0
    n = 1000
    s_t = time.time()
    with open("questions.txt", "w") as f:
        while i < n:
            q_ans, q_str = create_questions(q)
            f.write(f"{i}\t")
            f.write(f"blank: {q_str.count('0')}\t")
            f.write(f"{q_ans}\t")
            f.write(f"{q_str}\n")
            print(f"< {i} > blank: {q_str.count('0')}")
            if i % 10 == 9:
                print(f"time: {time.time() - s_t}")
            i += 1
    print(f"計算終了 time: {time.time() - s_t}")


if __name__ == "__main__":
    main()
