import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# --------------------------------------------------------------
# Load data
# --------------------------------------------------------------

df = pd.read_pickle("../../data/interim/01_dataprocessed.pkl")

# --------------------------------------------------------------
# Plot single columns
# --------------------------------------------------------------

set_df = df[df['set'] == 1]
plt.plot(set_df['acc_y'])
plt.savefig('../../reports/figures/visualizations/plot1.png')
plt.close()

# --------------------------------------------------------------
# Plot firstt 100 values of all exercises
# --------------------------------------------------------------

for label in df['label'].unique():
    subset = df[df['label'] == label]
    fig, x = plt.subplots()
    plt.plot(subset[:100]['acc_y'].reset_index(drop = True), label = label)
    plt.legend()
    plt.savefig(f'../../reports/figures/visualizations/{label}.png')
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
    plt.savefig(f'../../reports/figures/visualizations/{label}.png')
    plt.close()

# --------------------------------------------------------------
# Compare medium vs. heavy sets
# --------------------------------------------------------------


category_df = df.query("label == 'squat'").query("participant == 'A'").reset_index()

fig, ax = plt.subplots()
category_df.groupby(["category"])["acc_y"].plot()
ax.set_xlabel("samples")
ax.set_ylabel("acc_y")
plt.legend()
plt.savefig(f'../../reports/figures/visualizations/category.png')

# --------------------------------------------------------------
# Compare participants
# --------------------------------------------------------------

participant_df = df.query("label == 'bench'").sort_values("participant").reset_index()

fig, ax = plt.subplots()
participant_df.groupby(["participant"])["acc_y"].plot()
ax.set_xlabel("samples")
ax.set_ylabel("acc_y")
plt.legend()
plt.savefig(f'../../reports/figures/visualizations/participant.png')


# --------------------------------------------------------------
# Plot multiple axis
# --------------------------------------------------------------

label = "squat"
participant = "A"
all_axis_df = df.query(f"label == '{label}'").query(f"participant == '{participant}'").reset_index()

fig, ax = plt.subplots()
all_axis_df[["acc_x","acc_y","acc_z"]].plot(ax = ax)
plt.legend()
plt.savefig(f'../../reports/figures/visualizations/all_axis.png')


# --------------------------------------------------------------
# Create a loop to plot all combinations per sensor
# --------------------------------------------------------------

labels = df['label'].unique()
participants = df['participant'].unique()

for label in labels:
    for participant in participants:
        all_axis_df =(
            df.query(f"label == '{label}'")
            .query(f"participant == '{participant}'")
            .reset_index()
        )
        
        if len(all_axis_df) > 0:
            fig, ax = plt.subplots()
            all_axis_df[["acc_x","acc_y","acc_z"]].plot(ax = ax)
            ax.set_xlabel("samples")
            plt.legend()
            plt.title(f"acc {label} ({participant})".title())
            plt.savefig(f"../../reports/figures/visualizations/acc_{label}_({participant}).png")

for label in labels:
    for participant in participants:
        all_axis_df =(
            df.query(f"label == '{label}'")
            .query(f"participant == '{participant}'")
            .reset_index()
        )
        
        if len(all_axis_df) > 0:
            fig, ax = plt.subplots()
            all_axis_df[["gyr_x","gyr_y","gyr_z"]].plot(ax = ax)
            ax.set_xlabel("samples")
            plt.legend()
            plt.title(f"gyr {label} ({participant})".title())
            plt.savefig(f"../../reports/figures/visualizations/gyr_{label}_({participant}).png")


# --------------------------------------------------------------
# Combine plots in one figure
# --------------------------------------------------------------

label = 'row'
participant = 'A'
combined_plot_df =(
    df.query(f"label == '{label}'")
    .query(f"participant == '{participant}'")
    .reset_index(drop = True)
)
fix, ax = plt.subplots(nrows=2, sharex=True, figsize = (20,10))
combined_plot_df[["acc_x","acc_y","acc_z"]].plot(ax = ax[0])
combined_plot_df[["gyr_x","gyr_y","gyr_z"]].plot(ax = ax[1])
ax[0].set_ylabel("acc")
ax[1].set_ylabel("gyr")
plt.legend()
plt.savefig(f'../../reports/figures/visualizations/test.png')

# --------------------------------------------------------------
# Loop over all combinations and export for both sensors
# --------------------------------------------------------------

labels = df['label'].unique()
participants = df['participant'].unique()

for label in labels:
    for participant in participants:
        combined_plot_df =(
            df.query(f"label == '{label}'")
            .query(f"participant == '{participant}'")
            .reset_index(drop = True)
        )
        
        if len(combined_plot_df) > 0:
            
            fix, ax = plt.subplots(nrows=2, sharex=True, figsize = (20,10))
            combined_plot_df[["acc_x","acc_y","acc_z"]].plot(ax = ax[0])
            combined_plot_df[["gyr_x","gyr_y","gyr_z"]].plot(ax = ax[1])
            ax[0].set_ylabel("acc")
            ax[1].set_ylabel("gyr")
            plt.legend()
            plt.savefig(f'../../reports/figures/{label}_{participant}.png')
            