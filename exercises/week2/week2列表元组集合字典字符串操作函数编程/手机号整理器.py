raw = input("请输入手机号(带横线)")
number = raw.strip()
cleaned = number.replace('-','')
print(f"清洗后手机号:{cleaned}")
print(f"号码长度是:{len(cleaned)}")
print(f"区号（前三位）:{cleaned[:3]}")
print(f"中间四位:{cleaned[3:7]}")
print(f"尾号（后四位）:{cleaned[-4:]}")
print(f"拆分结果:（{cleaned[:3]},{cleaned[3:7]},{cleaned[-4:]}）")


