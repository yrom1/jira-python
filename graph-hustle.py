import matplotlib.pyplot as plt
from main import DAYS, COUNTS

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar([f'{x}-{y}-{z}' for x,y,z in DAYS], COUNTS)
plt.show()
