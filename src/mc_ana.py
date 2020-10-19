import pickle
import matplotlib.pyplot as plt
import seaborn as sns

with open("results_based_on_100_sim.p", "rb") as pickle_file:
    results = pickle.load(pickle_file)


results_to_plot = results.loc[results["epsilon"].isin([0.01, 0.05, 0.1, 0.15, 0.2, 0.3])]
print(results_to_plot)

sns.lineplot(data=results_to_plot, x='T', y='average_won', hue='epsilon')
plt.title("Outcome based on 10^3 simulations for each point")
plt.show()

