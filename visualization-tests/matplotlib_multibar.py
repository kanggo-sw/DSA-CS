from matplotlib import pyplot as plt

topics = ['A', 'B', 'C', 'D', 'E']
value_a = [69, 74, 58, 77, 85]
value_b = [60, 70, 50, 70, 80]


def create_x(t, w, n, d):
    return [t * x + w * n for x in range(d)]


value_a_x = create_x(2, 0.8, 1, 5)
value_b_x = create_x(2, 0.8, 2, 5)

ax = plt.subplot()
ax.bar(value_a_x, value_a)
ax.bar(value_b_x, value_b)

middle_x = [(a + b) / 2 for (a, b) in zip(value_a_x, value_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(topics)

plt.show()
