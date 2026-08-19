# 简单的加减法
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: 除数不能为零"
    return a / b

if __name__ == "__main__":
    print("=== 迷你计算器 ===")
    print(f"3 + 2 = {add(3, 2)}")
    print(f"5 - 1 = {sub(5, 1)}")
    print(f"3 * 4 = {mul(3, 4)}")
    print(f"10 / 2 = {div(10, 2)}")