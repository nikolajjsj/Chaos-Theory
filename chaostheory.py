import matplotlib.pyplot as plt

## equation: 
# x(n+1) = r * x(n) * (1 - x(n))
x = .5
r = 3

# first ans
first_val = r * x * (1 - x)

# list for points
x_points = [1]
y_points = [first_val]

# for lops to make graph points
for i in range(1, 100):
    x_points.append(i)
    y_points.append(r * y_points[i - 1] * (1 - y_points[i - 1]))

# plot
plt.plot(x_points , y_points , "-", lw=1, color="black", alpha=0.3)
plt.show()