# 第 2 周 · 第 5 课：函数（def）—— 把代码打包

## 一、为什么需要函数
- 把**重复使用**的代码打包成一个"工具"
- 以后需要时**调用一次**，不用复制粘贴
- 例子：仓库项目的"显示资产"在两个分支重复 → 打包成函数

## 二、三步理解函数：定义 → 调用 → 结果

### 1. 定义（def = define，定义一个函数）
```python
def greet():              # def 函数名():  ← 冒号不能忘！
    print("你好！")        # 函数体（缩进 4 空格）
    print("欢迎学习函数！")
```
**定义函数时，里面的代码不会执行**——只是"写好菜谱"。

### 2. 调用（函数名 + 括号）
```python
greet()    # 执行函数里的代码
greet()    # 可以反复调用
```

### 3. 参数：把"变化的部分"变成变量
```python
def greet(name):                    # name 是参数（占位符）
    print(f"你好，{name}！")

greet("小明")    # 你好，小明！
greet("小红")    # 你好，小红！
```

### 4. return：把结果"还给"调用者
```python
def add(a, b):
    return a + b          # return 把计算结果交出去

result = add(3, 5)        # result = 8
print(result)             # 8
```

**return 和 print 的区别**：
```python
def f1():
    return 100            # 能存进变量：x = f1() → x = 100
def f2():
    print(100)            # 只是显示，x = f2() → x = None（啥也没有）
```

## 三、默认参数（可选）
```python
def greet(name="朋友"):    # 不传就用默认值
    print(f"你好，{name}！")

greet()           # 你好，朋友！
greet("小明")     # 你好，小明！
```

## 四、仓库项目重构示例
```python
# 之前：每个分支里重复 2 行
print(f"您的总资产为{property}")
print(f"您的现金为{cash}")

# 之后：定义一次，到处调用
def show_assets():
    print(f"您的总资产为{property}")
    print(f"您的现金为{cash}")

# 添加分支里：show_assets()
# 出售分支里：show_assets()
```

## 五、记忆口诀

> def 定函数，冒号缩进好；
> 参数是占位，调用填实料；
> return 交结果，print 只显示；
> 定义不执行，调用才生效。
