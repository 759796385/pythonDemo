#psutil = process and system utilities 一般用来实现系统监控 跨平台使用
import psutil
print(psutil.cpu_count()) #cpu逻辑数量
print(psutil.cpu_count(logical=False)) # 物理核心

for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

#具体使用 https://github.com/giampaolo/psutil