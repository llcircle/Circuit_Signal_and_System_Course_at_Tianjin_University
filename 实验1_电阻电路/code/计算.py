# b=0
# a=[1.74,1.41	,1.17	,0.99,	0.87,	0.78,	0.70,	0.63,	0.58]
# for i in range(len(a)):
#     b+=6.97/a[i]-i-1
# print(b/len(a))

# while True:
#     a=float(input("输入：I"))
#     b=int(input("输入：RL"))
#     print(PL：a*a*b)
#     print(效率：a*b/7)

# import pandas as pd
# import matplotlib.pyplot as plt
# #设置中文
# from pylab import mpl
# mpl.rcParams["font.sans-serif"]=["SimHei"]
# mpl.rcParams["axes.unicode_minus"]=False
# # 读取CSV文件
# df = pd.read_csv('d:\\VS_Projects\\VScode_Python\\奇奇怪怪\\计算\\1.csv')

# # 提取第三列（R_L）和第五列（P_L）
# r_l = df['R_L（KΩ）']
# p_l = df['P_L (mW)']
# plt.figure(figsize=(10, 6))

# # 绘制折线图
# plt.title('负载功率随负载电阻变化的曲线',fontsize=30)
# plt.plot(r_l, p_l, marker='o', linestyle='-', color='b')
# plt.xlim(left=0,right=10)  # 设置 X 轴最小值为 0
# plt.ylim(bottom=0,top=5)  
# plt.xticks(r_l)


# # 显示网格
# plt.grid(True)

# # 显示图表
# plt.show()
