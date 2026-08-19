# 简单的加减法
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    print("=== 迷你计算器 ===")
    print(f"3 + 2 = {add(3, 2)}")
    print(f"5 - 1 = {sub(5, 1)}")