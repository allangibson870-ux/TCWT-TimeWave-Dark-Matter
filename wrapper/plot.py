import glob
import os
import numpy as np
import matplotlib.pyplot as plt

# Find latest sweep folder
sweeps = sorted(glob.glob("results/sweep_*"))
if not sweeps:
    print("No sweep folders found in results/")
    raise SystemExit(1)

latest = sweeps[-1]
print(f"Using latest sweep folder: {latest}")

# Find all run subfolders inside that sweep
runs = sorted(
    d for d in glob.glob(os.path.join(latest, "*"))
    if os.path.isdir(d)
)

if not runs:
    print("No run folders found inside latest sweep.")
    raise SystemExit(1)

plt.figure()

for run in runs:
    bg_file = os.path.join(run, "00_background.dat")
    if not os.path.exists(bg_file):
        print(f"Skipping {run}: no 00_background.dat")
        continue

    data = np.loadtxt(bg_file)
    if data.ndim != 2 or data.shape[1] < 2:
        print(f"Skipping {run}: unexpected data shape {data.shape}")
        continue

    x = data[:, 0]  # first column
    y = data[:, 1]  # second column

    label = os.path.basename(run)
    plt.plot(x, y, label=label)

plt.xlabel("x")
plt.ylabel("y")
plt.legend()

os.makedirs("../project_contents/plots", exist_ok=True)
out_path = os.path.join("../project_contents/plots", os.path.basename(latest) + "_background.png")
plt.savefig(out_path, dpi=150)
print(f"Saved plot to {out_path}")
