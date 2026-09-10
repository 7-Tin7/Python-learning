# 第 3 周 · 第 3 课：面向对象（class）—— 把"数据+功能"打包

## 一、为什么需要类

你之前写程序的方式是"**数据**归数据（字典/列表），**功能**归功能（函数）"：
```python
students = {"小明": 92}          # 数据散着放
def add_student(...): ...        # 功能单独写
def show_stats(...): ...
```

但现实世界的东西是**一体**的：
- 学生：有属性（名字、成绩）+ 有行为（自我介绍、考试）
- 宠物：有属性（名字、饥饿值、快乐值）+ 有行为（喂食、玩耍）

**类（class）就是把"属性 + 行为"打包成一体** —— 这就是面向对象。

## 二、类 vs 对象（模具比喻）

- **类** = 蛋糕模具（定义了蛋糕长什么样）→ 一个
- **对象** = 用模具做出来的蛋糕（具体的、能吃的）→ 可以很多个

```python
class Student:            # 定义"类"（模具）—— 不产生任何学生
    ...

s1 = Student(...)         # 创建"对象"（用模具做蛋糕）→ s1
s2 = Student(...)         # 再做第二个 → s2（互不影响）
```

**类名习惯用大驼峰**（每个单词首字母大写）：`Student`、`Pet`、`Car`。

## 三、三个新东西：__init__ / self / 方法

### 1. __init__（构造方法）—— 创建对象时自动执行
```python
class Student:
    def __init__(self, name, score):   # 创建对象时自动调用
        self.name = name                # 把参数存成"属性"
        self.score = score
```
创建对象：`s = Student("小明", 92)` ← 参数自动传给 __init__

### 2. self —— 指"当前这个对象自己"
- 类里每个方法第一个参数都是 self
- self.name = name：把传进来的值"贴"到这个对象身上（变成属性）
- 以后想用这个属性：还是 self.name

### 3. 方法 —— 类里的函数
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):                       # 方法（必须带 self）
        print(f"我是{self.name}，成绩{self.score}分")

    def is_pass(self):
        return self.score >= 60                # 方法里能用自己的属性

s = Student("小明", 92)
s.introduce()        # 我是小明，成绩92分     ← 调用方法
print(s.is_pass())   # True
print(s.name)        # 小明                  ← 直接访问属性
```

## 四、完整例子：宠物类

```python
class Pet:
    def __init__(self, name):      # 创建时设置初始属性
        self.name = name
        self.hunger = 30           # 饥饿值
        self.happiness = 70        # 快乐值

    def feed(self):                # 方法：喂食
        self.hunger = self.hunger - 20     # 修改自己的属性！
        self.happiness = self.happiness + 10

    def show(self):
        print(f"{self.name}：饥饿{self.hunger}，快乐{self.happiness}")

p1 = Pet("咪咪")
p2 = Pet("旺财")       # 两个对象，互不影响！
p1.feed()              # 只影响咪咪
p1.show()              # 咪咪：饥饿10，快乐80
```

## 五、对照你的旧写法（感受升级）

**之前**（函数 + 字典，数据功能分离）：
```python
students = {"小明": 92}
def add_student(students, name, score): ...
```

**之后**（类，学生自带一切）：
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def add_score(self, n):          # 改成绩
        self.score = self.score + n

s = Student("小明", 92)
s.add_score(5)                       # 小明 97 —— 方法自己操作自己的数据
```

## 六、记忆口诀

> 类是模具，对象是产品；
> __init__ 造物时初始化；
> self 指自己，属性贴身上；
> 方法自带 self，调对象点一下；
> 一个类，无数对象，互不干扰。
