# ナンプレの解答作成アルゴリズム

https://qiita.com/S_Kaji/items/c76f3732cd4e00644719

# v1振り返り
全探索\
1マスごとに盤面をチェックし、いけてたら次のマス\
結果5分くらいかかった長すぎ\
改善策：check関数が無駄に走ってる\