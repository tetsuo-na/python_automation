# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 14:25:58 2021

@author: Tetsuo Nakano
"""

import tkinter
from tkinter import messagebox

# メッセージボックス表示
def hello_window(event):
    messagebox.showinfo('注意', '社内ネットワークでは実行できません。\n外部ネットワークに接続して実行してください。')
    messagebox.showinfo('注意', 'ダウンロードを開始します。\n（ダウンロード完了には数分かかります。）')
    import download_csv
    download_csv.download_csv()
    messagebox.showinfo('Finish', 'ダウンロードが完了しました')
    messagebox.showinfo('Next', 'Step2に進んでください')


def get_text(event):
    import sum_csv2
    get_path = entry.get()
    sum_csv2.csv_marge(get_path)
    messagebox.showinfo('Finish', 'データの統合が完了しました')
    messagebox.showinfo('', 'ウィンドウを閉じてください')


# ウィンドウ
window = tkinter.Tk()
window.title('アンケート結果取得')
window.geometry('480x480')

# ラベル
label = tkinter.Label(text='Step1:ネクプロサイトからアンケート結果CSVを一括取得')
label.place(x=25, y=25)
label_2 = tkinter.Label(text='Step2：取得した全てのCSVを移動')
label_2.place(x=25, y=150)
label_3 = tkinter.Label(text='手動でフォルダを作成し、全CSVを移動してください')
label_3.place(x=100, y=200)

label_4 = tkinter.Label(text='Step3：取得した全てのCSVをマージ')
label_4.place(x=25, y=300)

label_5 = tkinter.Label(text='フォルダパス:')
label_5.place(x=50, y=350)

# ボタン
button1 = tkinter.Button(text='CSV一括ダウンロード', width=20)
button1.bind('<Button-1>', hello_window)
button1.place(x=170, y=75)

button2 = tkinter.Button(text='CSV統合', width=10)
button2.bind('<Button-1>', get_text)
button2.place(x=190, y=400)


# ボックス
entry = tkinter.Entry(width=40)
entry.place(x=140, y=350)

window.mainloop()
