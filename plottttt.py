import glob
import numpy as np
import matplotlib

# matplotlib.use('agg')
import matplotlib.pyplot as plt

files = glob.glob("data/*.csv")
times = np.zeros([len(files), 234])
print(times.shape)
for i, f in enumerate(files):
    arr = np.genfromtxt(f, dtype=object)
    times[i] = arr[:, 1].astype(float)


style = {"linestyle": "--", "color": "k", "alpha": 0.75}
fig, ax = plt.subplots()
ax.plot(times, **style)
# ax.plot(times[:,0], **style)
# ax.plot(times[:,10], **style)
# plt.show()

# normalized by means
means = times.mean(axis=0, keepdims=True)
print(means)
print(means.shape)
fig, ax = plt.subplots()
ax.plot(times / means, **style)
# ax.plot(times[:,0], **style)
# ax.plot(times[:,10], **style)
plt.show()
