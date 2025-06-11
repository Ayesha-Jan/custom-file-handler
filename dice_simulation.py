import random
import matplotlib.pyplot as plt


def plot_graph(func):
    """
    Decorator to plot the frequency distribution of dice rolls.
    """

    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        rolls = list(results)
        counts = [rolls.count(i) for i in range(1, 7)]

        plt.figure(figsize=(8, 4))
        plt.bar(range(1, 7), counts, color="pink", edgecolor="black")
        plt.xticks(range(1, 7))
        plt.xlabel("Dice Face")
        plt.ylabel("Frequency")
        plt.title(f"Distribution for {len(rolls):,} Rolls (Seed=40)")
        plt.grid(True, axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()

        return rolls

    return wrapper


@plot_graph
def dice_roll(n):
    """
    Generator function to yield n random dice rolls.
    """
    for _ in range(n):
        yield random.randint(1, 6)


if __name__ == "__main__":
    random.seed(40)

    for n in [10, 100, 1000, 10000, 100000, 500000]:
        dice_roll(n)
