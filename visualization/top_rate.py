from matplotlib import font_manager, rc
from matplotlib import pyplot as plt

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

topics = ["모데카이저", "다리우스", "피오라"]

# Global
value_a = [14.80, 10.10, 9.35]

# USA
value_b = [14.89, 13.25, 8.87]


def create_x(t, w, n, d):
    return [t * x + w * n for x in range(d)]


value_a_x = create_x(2, 0.8, 1, 3)
value_b_x = create_x(2, 0.8, 1, 3)

ax = plt.subplot()
ax.plot(value_a_x, value_a, ls="--", label="Global")
ax.plot(value_b_x, value_b, ls=":", label="USA")

plt.legend(loc=2)

middle_x = [(a + b) / 2 for (a, b) in zip(value_a_x, value_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(topics)

plt.ylabel("Pick rate (%)")

plt.show()
