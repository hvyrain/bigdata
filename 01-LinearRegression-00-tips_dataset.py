import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.rc('font', family='Gulim')
# 결제금액, 팁, 성별, 흡연여부, 요일, 시간, 동반손님수 
tips = sns.load_dataset('tips')
sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex').set(title='남녀별 음식값과 팁의 상관관계')
plt.show()
sns.boxplot(data=tips, x='sex', y='tip').set(title='남녀별 박스플롯')
plt.show()

x = tips.total_bill
y = tips.tip

n = len(x)
a = 0
b = 0
mses = []
lr = 0.001
epochs=1000
colors = ['red','green','blue','cyan','magenta','yellow','gray','black','orange','purple']
plt.figure(figsize=(10,5))
plt.subplot(121)
plt.grid(True)
plt.scatter(x,y)

for i in range(epochs) :
    mse = sum((y-(a*x+b))**2) / n
    mses.append(mse)
    delta_a = sum(-x*(y-(a*x+b))) / n
    delta_b = sum(-(y-(a*x+b))) / n
    a = a - lr * delta_a
    b = b - lr * delta_b
    if i % (epochs // 10) == 0 :
        print(f'{i:>6,d}회 - mse:{mse:.4f}, a:{a:.4f}, b:{b:.4f}')    
        plt.plot(x, a*x+b, color=colors.pop(), linestyle='dashed')

print(f'최종 mse:{mse:.4f}, a:{a:.4f}, b:{b:.4f}')
plt.subplot(122)
plt.grid(True)
plt.plot(mses)
plt.show()