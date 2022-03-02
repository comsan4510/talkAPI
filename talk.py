import tkinter as tk
from tkinter import *;
import SendApi as sp

frame = tk.Tk()
frame.geometry('600x400')
frame.title('チャットボット')
frame.iconbitmap('icon48.ico')

def senda3rt(event=None):
    soushin_text = entry.get()
    msgs.insert(END,"あなた：%s" %soushin_text)

    #テキストの送信
    text = sp.send_talkapi(soushin_text)

    #表示エリアに結果を反映
    msgs.insert(END,"A3RT：%s" %text)
    entry.delete(0,END)


frame.bind('<Return>',senda3rt)

#スクロールバーの作成
sc = Scrollbar(frame)
sc.pack(side=RIGHT, fill=Y)

#表示エリアの作成
msgs = tk.Listbox(frame, width=80, height=15, yscrollcommand=sc.set)
msgs.pack(side='top', fill=tk.BOTH, pady=10,padx=50)

#送信ボタンの作成
btn = tk.Button(frame,text="送信",height=3,command=senda3rt)
btn.pack(fill='x',padx=100,pady=10,side='bottom')

#入力ボックスの作成
entry = tk.Entry(width=20,font=('',20))
entry.pack(fill='x',padx=100,pady=10,side='bottom',ipady=10)



#ウィンドウの描画
frame.mainloop()
