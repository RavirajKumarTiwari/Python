import numpy as np
import matplotlib.pyplot as plt
# x = np.arange(0, 3*np.pi, 0.1)
x = np.linspace(-20, 20, 100)

def fun(x):
    y = []
    for elem in x:
        result = 1-(elem**2)/2
        y.append(result)
    return y

y = fun(x)

plt.plot(x, y)

# y_sin = np.sin(x)
# y_cos = np.cos(x)



# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.xlabel('x asis label')
# plt.ylabel('y axis label')
# plt.title('Sine and Cosine')
# plt.legend(['Sine', 'Cosine'])
# plt.show()
# print("I am here")

# Create the first subplot
plt.subplot(1, 1, 1)
plt.plot(x, y)

# Create the second subplot
# plt.subplot(2, 1, 2)
# plt.plot(x, y)

plt.xlabel('x asis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.show()