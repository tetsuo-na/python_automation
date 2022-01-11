# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:35:40 2021

@author: Tetsuo Nakano
"""

def csv_marge(path):

    # CSV結合
    import pandas as pd
    import glob

    # パスで指定したファイルの一覧をリスト形式で取得. （ここでは一階層下のtestファイル以下）
    csv_files = glob.glob(path + '/*.csv')

    #読み込むファイルのリストを表示
    for a in csv_files:
        print(a)

    #csvファイルの中身を追加していくリストを用意
    data_list = []

    #読み込むファイルのリストを操作
    for file in csv_files:
        data_list.append(pd.read_csv(file))

    #リストを全ての行方向に結合
    #axis=0:行方向に結合, sort
    df = pd.concat(data_list, axis=0, sort=False)

    df.to_csv(path + "/summary.csv",encoding='utf_8_sig')
