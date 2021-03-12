# set up maptlotlib to use agg
# taken from sphinx-gallery
# https://github.com/sphinx-gallery/sphinx-gallery/blob/4a026660b2cbb00c3ce8a7e28e957d8ef6320099/sphinx_gallery/scrapers.py#L31
import matplotlib
from warnings import filterwarnings

matplotlib.use("agg")

filterwarnings(
    "ignore",
    category=UserWarning,
    message="Matplotlib is currently using agg, which is a"
    " non-GUI backend, so cannot show the figure.",
)

import matplotlib.pyplot as plt
import glob
import time as _time # apparently at least one example redefines this

files = glob.glob("examples/**/*.py")
times = []
for f in files:
    start = _time.time()
    exec(open(f).read())
    end = _time.time()
    times.append(end - start)
    plt.close("all")
from datetime import datetime

now = "data/" + datetime.now().strftime("%Y-%m-%d_%I-%M") + ".csv"
from matplotlib import __version__ as mpl_version
import sys
import platform

with open(now, "w") as f:
    f.write("# matplotlib version:" + mpl_version + "\n")
    for l in sys.version.splitlines():
        f.write("# " + l + "\n")
    f.write("# " + platform.platform() + "\n")
    for fname, time in zip(files, times):
        f.write(f"{fname}, {time}\n")

