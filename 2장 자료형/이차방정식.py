import tkinter as tk
from tkinter import messagebox
import cmath

# 이차방정식의 해를 계산하는 함수
def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        # 판별식 계산
        d = cmath.sqrt(b**2 - 4*a*c)
        
        # 두 근 계산
        x1 = (-b + d) / (2*a)
        x2 = (-b - d) / (2*a)
        
        result = f"근1: {x1}\n근2: {x2}"
        messagebox.showinfo("결과", result)
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 숫자를 입력하세요")

# Tkinter 창 설정
root = tk.Tk()
root.title("이차방정식 풀이기")

# 입력 레이블 및 엔트리
label_a = tk.Label(root, text="a:")
label_a.grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

label_b = tk.Label(root, text="b:")
label_b.grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

label_c = tk.Label(root, text="c:")
label_c.grid(row=2, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1)

# 계산 버튼
button_solve = tk.Button(root, text="계산", command=solve_quadratic)
button_solve.grid(row=3, columnspan=2)

# Tkinter 이벤트 루프 시작
root.mainloop()