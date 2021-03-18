import glob
import numpy as np
import matplotlib

# matplotlib.use('agg')
import matplotlib.pyplot as plt

files = glob.glob("data/*.csv")
times = np.zeros([len(files), 445])
for i, f in enumerate(files):
    arr = np.genfromtxt(f, dtype=object)
    times[i] = arr[:, 1].astype(float)


style = {"linestyle": "--", "color": "k", "alpha": 0.25}
fig, ax = plt.subplots()
ax.plot(times, **style)
ax.set_xlabel('Run number')
ax.set_ylabel('Time (s)')
ax.set_title('Absolute Times')

# normalized by means
means = times.mean(axis=0, keepdims=True)
fig, ax = plt.subplots()
ax.plot(times / means, **style)
ax.set_title('Time normalized by mean time')
ax.set_xlabel('Run number')
ax.set_ylabel('Relative Time')
plt.show()


# # most and least consistent
# fig, axs = plt.subplots(2, 1)
# CVs = times.std(axis=0)  / times.mean(axis=0)
# max_idx = np.argmax(CVs)
# min_idx = np.argmin(CVs)
# axs[0].plot(times[:, max_idx])
# axs[1].plot(times[:, min_idx])
# plt.show()
