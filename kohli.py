#7th class
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

print(df)

print(df.head(10)) # see first 10 rows
print(df.tail(10)) # see last 10 rows

df.info()

print(df.shape)
print(df["Opposition"].describe())

run_frequency = df["Runs"].value_counts()
print(run_frequency)

run_frequency = df["Opposition"].value_counts()
print(run_frequency)

new_df = df[["Runs", "SR", "Opposition"]]
print(df)

vs_aussies = df[df["Opposition"] == "v Australia"]
print(vs_aussies)

# Find all the matches where Virat scored a century
tons = df[df["Runs"] >= 100]
print(tons)

ton_sr = df[df["SR"] > 100]
print(ton_sr)

sril_cent = df[
    (df["Opposition"] == "v Sri Lanka") & (df["Runs"])
]
print(sril_cent)

def find_centuries(x):
    if x >= 100:
        return "OG"
    else:
        return "NOOB"
df["Centuries"] = df["Runs"].apply(find_centuries)
print(df.tail(10))

# Number of matches he has played at position
print(df["Pos"].head(10))

positions = df["Pos"].unique()
print(positions)
df["Pos"] = df["Pos"].map({
    3.0: "Batting at 3",
    4.0: "Batting at 4",
    2.0: "Batting at 2",
    1.0: "Batting at 1",
    7.0: "Batting at 7",
    5.0: "Batting at 5",
    6.0: "Batting at 6",
})
# print(df[["Runs", "Pos"]])
print(df.head(10))
pos_counts = df["Pos"].value_counts()
print(pos_counts)
print(type(pos_counts))

pos_counts_value = pos_counts.values
pos_counts_labels = pos_counts.index

fig = plt.figure(figsize=(10, 5))
plt.pie(pos_counts_value, labels=pos_counts_labels)
plt.show()


def show_pie_plots(df, key):
    counts = df[key].value_counts()
    print(counts)
    count_values = counts.values
    count_labels = counts.index
    fig = plt.figure(figsize=(10, 5))
    plt.pie(count_values,labels= count_labels)
    plt.show()

# Total matches played in different grounds
show_pie_plots(df, "Ground")

# Total matches played different countries
show_pie_plots(df, "Opposition")

# total sixes scored in different positions
print("\nTotal sixes scored in different positions : ")
runs_at_pos =df.groupby("Pos")["6s"].sum()
print(runs_at_pos, type(runs_at_pos))
runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos.index

fig = plt.figure(figsize=(10, 5))
plt.bar(
    runs_at_pos_labels,
    runs_at_pos_values,
    color = "green",
    width = 0.3
)
plt.show()
#Total runs scored in different countries
print("\nTotal runs scored in different positions : ")
runs_at_opp = df.groupby("Opposition")["Runs"].sum()
print(runs_at_opp, type(runs_at_opp))
runs_at_opp_values = runs_at_opp.values
runs_at_opp_labels = runs_at_opp.index

fig = plt.figure(figsize=(10, 7))
plt.bar(
    runs_at_opp_labels,
    runs_at_opp_values,
    color="black",
    width=0.2
)
plt.show()

# Number of centuries scored by him
centuries = df.query("Runs >= 100")
print(centuries)

innings = centuries["Inns"].value_counts()
print(innings)

plt.pie(innings.values, labels=innings.index)
plt.show()

# calcualate the dismissals of Kohli
dis = df.query("Dismissal" == True)
dis_count = dis["Dismissal"].value_counts()
print(dis_count)

# againsst which teams he has scored the most century
# against with teams he has xeored the most 
