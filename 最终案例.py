# 练习变量、f-string、time、type的使用
# 新增【运算符】知识点

import time

# ===== 1. 定义个人信息：名字、性别、年龄、身高、爱好 =====
xingming = "开阳"
nianling = 18
shengao = 182.5
aihao = "唱跳、rap、python"

# ===== 2. 打印信息 =====
print(f"大家好，我叫{xingming}")
time.sleep(1)
print(f"我曾经{nianling}岁")
time.sleep(1)
print(f"我的身高是{shengao},我觉得我还能再长长")
time.sleep(1)
print(f"我的爱好是{aihao}, 希望能交到志同道合的朋友")
time.sleep(1)

# ===== 3. 展示信息的数据类型 =====
print("数据类型检验报告：")
print(f"姓名是：{type(xingming)}")
print(f"年龄是：{type(nianling)}")
print(f"身高是：{type(shengao)}")
print(f"爱好是：{type(aihao)}")

# ===== 4. 游戏开始·展示你的信息 =====
print("系统启动中，请稍后...")
time.sleep(1)
# 逐渐显示个人信息
print(f"[ {xingming} ] 身份验证通过")
time.sleep(0.5)
print("正在加载年龄数据...")
time.sleep(0.5)
print(f"年龄：{nianling}岁")
time.sleep(0.5)
print("身高数据校准中...")
time.sleep(0.5)
print(f"身高：{shengao}cm" )
time.sleep(0.5)


# ===== 5. 计算隐藏信息(出生年份) =====
birth_year = 2026 - nianling
print("推算出生年份：", birth_year)
print("出生年份数据类型：", type(birth_year))

# 身高转换成米    / 除法
shengao_m = shengao / 100
print("身高（米）：", shengao_m)
print("身高（米）数据类型：", type(shengao_m))

# ===== 6. 终极彩蛋：模拟AI分析你的理想身高 =====
print("AI 正在分析你的理想身高...")
time.sleep(1)
print("分析中.")
time.sleep(0.5)
print("分析中..")
time.sleep(0.5)
print("分析中...")
time.sleep(0.5)

# 用变量运算计算理想身高：年龄 * 7 + 70
dream_shengao = nianling * 7 + 70
print("你的理想身高是：", dream_shengao)

print("系统关闭...")
time.sleep(0.5)
print("再见！")