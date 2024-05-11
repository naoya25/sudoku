import random
import time
from created_questions import get_questions
from question import Sudoku


def play_game():
    questions = get_questions()  # 過去に生成した問題一覧
    n = random.randint(0, len(questions) - 1)

    q = Sudoku()
    q.set_q_str(s=questions[n]["question"])
    q.set_ans(s=questions[n]["ans"])

    if q.q_ans not in q.get_ans():
        print("問題に不備があります。")
        return
    user_ans = q.q_str

    print(" - Start - ")
    print("縦は上から何番目か、横は左から何番目か、それぞれ 0~8 の数字で指定してください")
    print("値は、1~9 の値を入力してください")
    print("以下のコマンドも試してみてね！")
    print("a → 答えを表示するよ")
    print("q → ゲーム終了")
    print("h → ヒントを表示するよ")
    q.display_s(user_ans)

    t = 1
    s_t = time.time()
    while user_ans.count("0") > 0:
        print(f"< {t} >")
        s = input("縦 横 値 を入力してください -> ")
        if not s.strip():
            continue
        if s == "a":
            q.display_s(q.q_ans)
            return
        if s == "q":
            return
        if s == "h":
            i, _ = q.find_next(user_ans)
            r = i // 9
            c = i % 9
            print(f"{r} {c} {q.q_ans[i]} ←これ入力してみてね！！")
            continue

        r, c, num = map(int, s.split())
        if not (0 <= r < 9 and 0 <= c < 9 and 1 <= num < 10):
            print("正しい値を入力してね")
            continue
        i = r * 9 + c
        if q.q_ans[i] == str(num):
            print("正解!")
            user_ans = user_ans[:i] + str(num) + user_ans[i + 1 :]
            q.display_s(user_ans)
        else:
            print("残念")
        t += 1
    print("正解 !!!\nおめでとう !!!")
    print(f"タイム: {time.time() - s_t}")
    return


if __name__ == "__main__":
    play_game()
