import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# --------------------------------------------------------------
# Load data
# --------------------------------------------------------------

df = pd.read_pickle("/mnt/e/projects/fitnessTracker/data/interim/01_dataprocessed.pkl")

# --------------------------------------------------------------
# Plot single columns
# --------------------------------------------------------------

set_df = df[df['set'] == 1]
plt.plot(set_df['acc_y'])
plt.savefig('/mnt/e/projects/fitnessTracker/src/visualization/visualizations/plot1.png')
plt.close()

# --------------------------------------------------------------
# Plot firstt 100 values of all exercises
# --------------------------------------------------------------

for label in df['label'].unique():
    subset = df[df['label'] == label]
    fig, x = plt.subplots()
    plt.plot(subset[:100]['acc_y'].reset_index(drop = True), label = label)
    plt.legend()
    plt.savefig(f'/mnt/e/projects/fitnessTracker/src/visualization/visualizations/{label}.png')
    plt.show()

# --------------------------------------------------------------
# Adjust plot settings
# --------------------------------------------------------------

mpl.style.use('seaborn-v0_8-deep')
mpl.rcParams['figure.figsize'] = (20,5)
mpl.rcParams['figure.dpi'] = 100

for label in df['label'].unique():
    subset = df[df['label'] == label]
    fig, x = plt.subplots()
    plt.plot(subset[:100]['acc_y'].reset_index(drop = True), label = label)
    plt.legend()
    plt.savefig(f'/mnt/e/projects/fitnessTracker/src/visualization/visualizations/{label}.png')
    plt.close()

# --------------------------------------------------------------
# Compare medium vs. heavy sets
# --------------------------------------------------------------

plt.close()
category_df = df.query("label == 'squat'").query("participant == 'A'").reset_index()
plot = category_df.groupby(["category"]).plot()

# --------------------------------------------------------------
# Compare participants
# --------------------------------------------------------------


# --------------------------------------------------------------
# Plot multiple axis
# --------------------------------------------------------------


# --------------------------------------------------------------
# Create a loop to plot all combinations per sensor
# --------------------------------------------------------------


# --------------------------------------------------------------
# Combine plots in one figure
# --------------------------------------------------------------


# --------------------------------------------------------------
# Loop over all combinations and export for both sensors
# --------------------------------------------------------------