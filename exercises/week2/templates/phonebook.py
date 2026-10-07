# ============================================
# 第 2 周 练习：手机通讯录 📒
#
# 功能：
#   1. 添加联系人（名字 + 电话）
#   2. 查找联系人的电话
#   3. 查看所有联系人
#   4. 退出
#
# 新知识：字典 dict（创建 / 赋值 / in 判断 / items() 遍历）
# 旧知识：while True / input / if-elif-else / break / f-string
# ============================================

contacts = {}   # 空字典：名字 → 电话

while True:
    print("1.添加联系人  2.查找电话  3.查看所有  4.退出")
    choice = input("请选择：")

    # ---- TODO 1：添加联系人 ----
    # 如果 choice == "1"：
    #   1. name = input("请输入联系人名字：")
    #   2. phone = input("请输入电话号码：")
    #   3. contacts[name] = phone      ← 字典添加/修改的写法！
    #   4. print(f"已添加联系人：{name}")

    # ---- TODO 2：查找电话 ----
    # 如果 choice == "2"：
    #   1. name = input("请输入要查找的名字：")
    #   2. 如果 name in contacts：打印 f"{name} 的电话是 {contacts[name]}"
    #   3. 否则：打印"通讯录里没有这个人"
    # 提示：contacts[name] 取值，键不存在会报错，所以要先 in 判断！

    # ---- TODO 3：查看所有 ----
    # 如果 choice == "3"：
    #   用 for name, phone in contacts.items(): 遍历
    #   打印 f"{name}: {phone}"
    # 提示：items() 返回键值对，name 拿键，phone 拿值 —— 又是元组拆包！

    # ---- TODO 4：退出 ----
    # 如果 choice == "4" 或 choice == "q"：打印"再见！"然后 break

    # 加个兜底：
    # 否则：打印"无效的选择，请重新输入"

# 提示：
# - contacts[name] = phone 这一行"又添加又修改"——键不存在就是添加，存在就是覆盖
# - 整个结构和购物清单几乎一样，只是把"列表"换成了"字典"
# ============================================
