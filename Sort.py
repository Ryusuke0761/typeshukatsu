    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sorted(array)
    # 結果出力
    [print(sortedArray[i-1]) for i in sortedArray]
