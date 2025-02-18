import tkinter as tk
from tkinter import messagebox
import cmath

def f(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

def df(x, a, b, c):
    return 3 * a * x**2 + 2 * b * x + c

def newton_raphson(a, b, c, d, x0, tol=1e-6, max_iter=1000):
    x = x0
    for i in range(max_iter):
        fx = f(x, a, b, c, d)
        dfx = df(x, a, b, c)
        if dfx == 0:
            raise ValueError("도함수가 0입니다. 다른 초기값을 시도하세요.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("수렴하지 않습니다. 다른 초기값을 시도하세요.")

def solve_cubic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        d = float(entry_d.get())
        x0 = float(entry_x0.get())
        
        root = newton_raphson(a, b, c, d, x0) 
        result = f"근: {root}"
        messagebox.showinfo("결과", result)
    except ValueError as e:
        messagebox.showerror("오류", str(e))
    except Exception as e:
        messagebox.showerror("입력 오류", "유효한 숫자를 입력하세요")

# Tkinter 창 설정
root = tk.Tk()
root.title("삼차방정식 풀이기")

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

label_d = tk.Label(root, text="d:")
label_d.grid(row=3, column=0)
entry_d = tk.Entry(root)
entry_d.grid(row=3, column=1)

label_x0 = tk.Label(root, text="초기값 x0:")
label_x0.grid(row=4, column=0)
entry_x0 = tk.Entry(root)
entry_x0.grid(row=4, column=1)

# 계산 버튼
button_solve = tk.Button(root, text="계산", command=solve_cubic)
button_solve.grid(row=5, columnspan=2)

# Tkinter 이벤트 루프 시작
root.mainloop()