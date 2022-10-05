# Visulizantion
import matplotlib.pyplot as mat

print(mat)
fig = mat.figure('Histogram')
ax = fig.add_subplot(1, 1, 1)
ax.hist([21, 12, 23, 35, 45, 60, 33, 22, 56, 34, 28, 40, 41],
        bins=7, facecolor='r', normed=True)

mat.title('Distrubution')
mat.xlabel('Range')
mat.ylabel('Amount')
mat.show()
