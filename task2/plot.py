import matplotlib.pyplot as plt

numbers = [0, 5, 32, 64, 127, 255, 256]
volts   = [12.7, 76.5, 415, 820, 1620, 3240, 12.7]

plt.plot(numbers, volts)
plt.scatter(numbers, volts, 30, "r", "^")

plt.grid()
plt.show()