def get_questions() -> list:
    with open("questions.txt", "r") as f:
        text = f.read()
        data = text.split("\n")

    # データ整形
    questions = []
    for q in data:
        if not q.strip():
            continue
        q_arr = q.split("\t")
        r_dict = {}
        r_dict["id"] = int(q_arr[0])
        r_dict["blank"] = int(q_arr[1].split(": ")[-1])
        r_dict["ans"] = q_arr[2]
        r_dict["question"] = q_arr[3]
        questions.append(r_dict)
    # for a in questions[:10]:
    #     print(a)

    # # 空欄の分布表示用
    # distribution = {i: 0 for i in range(81)}
    # for q in questions:
    #     distribution[q["blank"]] += 1

    # for k, v in distribution.items():
    #     if not (50 <= k <= 64):
    #         continue
    #     print(f"blank: {k} --> {v}  {round(v / len(questions) * 100, 2)}%")
    return questions
