import tkinter as tk
from tkinter import messagebox
import keyboard
import pyautogui
import time

# 读取文件中的句子并保存到全局变量
file_path = "savedFile.txt"  # 你的文本文件路径
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
sentences = content.split('.')  # 以句号分隔文本

# 初始化句子索引
current_sentence_index = 0

def send_message(message):
    time.sleep(0.2)  # Add a 0.5-second delay
    pyautogui.write(message, interval=0.01)

def send_next_sentence():
    global current_sentence_index

    if current_sentence_index < len(sentences):
        sentence = sentences[current_sentence_index].strip()
        send_message(sentence)
        current_sentence_index += 1
    else:
        messagebox.showinfo("End of Text", "No more sentences to send.")

def send_multiple_sentences():
    for _ in range(10):
        send_next_sentence()
        keyboard.press_and_release('enter')
        #time.sleep(0.001)

def reset_progress():
    global current_sentence_index
    current_sentence_index = 0


# 注册全局热键 Ctrl+Alt+S
keyboard.add_hotkey('ctrl+alt+s', send_next_sentence)

# 注册全局热键 Ctrl+Alt+A
keyboard.add_hotkey('ctrl+alt+a', send_multiple_sentences)

# 注册全局热键 Ctrl+Alt+R
keyboard.add_hotkey('ctrl+alt+r', reset_progress)

# 创建主窗口
root = tk.Tk()
root.title("Text Sender")

# 添加文本提示标签
label = tk.Label(root, text="Press Ctrl + Alt + S to send the next sentence.\nPress Ctrl + Alt + A to send the multiple sentence.\nPress Ctrl + Alt + R to reset progress.")
label.pack(pady=10)

# 运行主循环
root.mainloop()
