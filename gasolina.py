# código de geração do gráfico 
import matplotlib.pyplot as plt
x = []
y = []
dataset = open('/content/da-ebac-marcia/gasolina.csv', 'r',)
for line in dataset:
  line = line.strip()
  X, Y = line.split(',')
  x.append(X)
  y.append(Y)
dataset.close()

plt.plot(x, y)

plt.title('Preço venda Gasolina por Dia')
plt.xlabel('X  - Dia')
plt.ylabel('Y  - Preço')
plt.show()
