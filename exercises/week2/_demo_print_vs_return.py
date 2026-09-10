def add_print(a, b):
    print(a + b)      # 函数内部 print：会执行！打印出 13.0

result = add_print(10, 3)          # 调用它
print("函数的返回值是：", result)   # 看看它"交"了什么

print(f"结果：{add_print(10, 3)}")  # 放进 f-string 里会怎样？
