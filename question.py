# v4ベースで作成
class Question:
    def __init__(self, s: str):
        self.q_str: str = s
        self.q_ans: list = []

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

    # dfsで解答作成
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


def main():
    q = Question(
        s="800000000003600000070090200050007000000045700000100030001000068008500010090000400",
    )
    q.get_set_ans()
    for a in q.q_ans:
        q.display_s(a)

    return


if __name__ == "__main__":
    main()
