from typing import List

from matplotlib import font_manager, rc
from matplotlib import pyplot as plt

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

topics = ["야스오", "다이애나", "제드"]

# Global
value_a: List = open("top_rep.csv", 'r', encoding='utf-8').readlines()[1:]
value_a = [vvv for vvv in value_a if len(vvv.split(','))>=3]
for i in range(len(value_a)):
    value_a[i] = value_a[i].split(',')[1]
print(value_a)
# USA
value_b: List = open("top_rep.csv", 'r', encoding='utf-8').readlines()[1:]
value_b = [vvv for vvv in value_b if len(vvv.split(','))>=3]
for i in range(len(value_b)):
    value_b[i] = value_b[i].split(',')[2]

print(value_b)


def create_x(t, w, n, d):
    return [t * x + w * n for x in range(d)]


value_a_x = create_x(2, 0.8, 1, 3)
value_b_x = create_x(2, 0.8, 2, 3)

ax = plt.subplot()
ax.bar(value_a_x, value_a, ls="--", label="Positive")
ax.bar(value_b_x, value_b, ls=":", label="Negative")

plt.legend(loc=2)

middle_x = [(a + b) / 2 for (a, b) in zip(value_a_x, value_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(topics)

plt.ylabel("Pick rate (%)")

plt.show()
