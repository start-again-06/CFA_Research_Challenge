import seaborn as sns
import matplotlib.pyplot as plt


class SensitivityHeatmap:

    def plot(self, sensitivity_matrix):

        plt.figure(figsize=(8,6))

        sns.heatmap(
            sensitivity_matrix,
            annot=True,
            fmt=".2f",
            cmap="viridis"
        )

        plt.title("DCF Sensitivity Analysis")

        plt.xlabel("Terminal Growth")

        plt.ylabel("WACC")

        plt.show()
