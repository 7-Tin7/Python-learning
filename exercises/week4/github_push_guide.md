# 🚀 GitHub 上传指南（第 4 周收官）

> 目标：把你的项目推到 GitHub（或 Gitee），建立求职作品集。
> 这份指南覆盖新手最容易卡住的坑：认证、网络、分支名。

════════════════════════════════════
一、先想清楚：GitHub 还是 Gitee？
════════════════════════════════════

| | GitHub（github.com）| Gitee 码云（gitee.com）|
|--|---------------------|----------------------|
| 地位 | 全球标准，外企/大厂看 | 国内主流，速度快 |
| 网络 | 国内直连可能慢/不稳 | 国内速度快 ✅ |
| 求职 | 面试官都认 ⭐ | 国内公司也认可 |
| 建议 | **有梯子/能直连 → 首选** | **网络不稳 → 用这个** |

💡 两个都注册不冲突，作品集可以双份。

════════════════════════════════════
二、⚠️ 最大的坑：push 时的"密码"不是密码！
════════════════════════════════════

GitHub 从 2021 年起【不再接受账号密码】做 git push。
如果你用命令行 push，要求输入密码时，必须输入【个人访问令牌 Token】：

  ① 登录 GitHub → 右上角头像 → Settings
  ② 左侧最下 → Developer settings
  ③ Personal access tokens → Tokens (classic) → Generate new token
  ④ 勾选权限：至少勾 repo（仓库读写）
  ⑤ 生成后【立刻复制保存】（只显示一次！）
  ⑥ push 提示密码时，粘贴这个 Token

❌ 直接输账号密码 → 报错 "Support for password authentication was removed"

════════════════════════════════════
三、路线 A：PyCharm 一键上传（新手最省心 ⭐推荐）
════════════════════════════════════
PyCharm 会帮你处理登录和认证，不用手动搞 Token：

  ① PyCharm 打开你的项目
  ② 顶部菜单：Git → GitHub → Share Project on GitHub
     （或 VCS → Import into Version Control → Share Project on GitHub）
  ③ 弹窗登录 GitHub（浏览器点授权即可）
  ④ 填仓库名（英文，如 python-practice）和描述
  ⑤ 点 Share → 自动帮你建远程仓库 + push！✅

之后的日常更新：
  PyCharm 右上角 √ 提交 → 菜单 Git → Push（或 Ctrl+Shift+K）

════════════════════════════════════
四、路线 B：命令行上传（理解原理）
════════════════════════════════════
  ① 网页上新建仓库：github.com → New repository
     仓库名英文，不要勾选 "Add README"（避免冲突）

  ② 本地关联远程仓库（在项目文件夹里敲）：
     git remote add origin https://github.com/你的用户名/仓库名.git

  ③ 把分支改成 main（GitHub 默认名）：
     git branch -M main

  ④ 第一次推送（-u 记住关联）：
     git push -u origin main
     → 提示输入用户名和密码时，密码填【Token】！

  ⑤ 以后每次更新：
     git add .  →  git commit -m "说明"  →  git push

════════════════════════════════════
五、上传前必须做：加 .gitignore
════════════════════════════════════
在项目根目录新建文件 `.gitignore`（开头有个点），内容：

  .idea/
  __pycache__/
  *.pyc
  任务清单.txt
  学习内容.txt
  日记.txt

作用：忽略编辑器配置、缓存、个人数据文件，不让它们上传。
（这些是"你电脑上的东西"，不该进公开仓库）

════════════════════════════════════
六、作品集怎么整理（求职加分项）
════════════════════════════════════
建议仓库结构：
  python-practice/          ← 一个总仓库
    ├── README.md           ← 首页说明（写你学了什么、有哪些项目）
    ├── week1_基础/
    ├── week2_数据结构/
    ├── week3_面向对象/
    └── week4_进阶/

README.md 写法（简明）：
  # 我的 Python 学习之路
  ## 项目列表
  - 猜数字游戏：random + while 循环
  - 学生成绩管理系统：字典 + 函数 + 文件持久化
  - 待办事项管理器：面向对象 + 文件读写
  ...

════════════════════════════════════
七、完成检查清单
════════════════════════════════════
  [ ] 注册了 GitHub（或 Gitee）账号
  [ ] 创建了远程仓库
  [ ] 成功 push 第一个项目
  [ ] 网页上能看到自己的代码
  [ ] 加了 .gitignore
  [ ] （加分）写了 README.md
