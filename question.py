class Question:
    def __init__(self):
        # https://rocketnews24.com/2012/07/03/22654/
        self.q_str = (
            "800000000003600000070090200050007000000045700000100030001000068008500010090000400"
        )

    def set(self, q_str):
        self.q_str = q_str

    def str2list(self):
        q_list = []
        for i in range(9):
            row = list(map(int, list(self.q_str[i * 9 : i * 9 + 9])))
            q_list.append(row)
        return q_list

    # 9 x 9の2次元配列を返す
    def get_q_list(self):
        q_list = self.str2list()
        return q_list
