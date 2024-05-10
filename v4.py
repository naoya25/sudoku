from question import Question
import time


def main():
    q = Question()
    q.set_q_str("800000000003600000070090200050007000000045700000100030001000068008500010090000400")
    q.display_s(q.q_str)

    if not q.check_all():
        print("正しいナンプレを入力してね")
        return

    s_t = time.time()
    ans = q.get_ans()
    for a in ans:
        q.display_s(a)
    e_t = time.time()
    print(f"タイム: {e_t - s_t}s")


if __name__ == "__main__":
    main()
