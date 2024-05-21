import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import argparse

def plot_cost_distribution(expected_value, std_deviation):
    p10 = norm.ppf(0.10, loc=expected_value, scale=std_deviation)
    p50 = norm.ppf(0.50, loc=expected_value, scale=std_deviation)
    p90 = norm.ppf(0.90, loc=expected_value, scale=std_deviation)
    p99 = norm.ppf(0.99, loc=expected_value, scale=std_deviation)
    x = np.linspace(expected_value - 3 * std_deviation, expected_value + 3 * std_deviation, 1000)
    pdf = norm.pdf(x, loc=expected_value, scale=std_deviation)
    cdf = norm.cdf(x, loc=expected_value, scale=std_deviation)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.fill_between(x, pdf, where=(x >= -10000000) & (x <= p90), alpha=0.1, color='gray')
    plt.fill_between(x, pdf, where=(x >= -10000000) & (x <= p50), alpha=0.2, color='gray')
    plt.fill_between(x, pdf, where=(x >= -10000000) & (x <= p10), alpha=0.3, color='gray')
    plt.plot(x, pdf, color='blue')
    plt.axvline(p10, color='red', linestyle='--', label=f'p10 = {round(p10/1000000,2)} mill. kr')
    plt.axvline(p50, color='green', linestyle='--', label=f'p50 = {round(p50/1000000,2)} mill. kr')
    plt.axvline(p90, color='purple', linestyle='--', label=f'p90 = {round(p90/1000000,2)} mill. kr')
    plt.axhline(0, color="black")
    plt.ylabel('Probability Density')
    plt.title('PDF')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(x, cdf, color='orange')
    plt.fill_between(x, cdf, where=(x >= -10000000) & (x <= p90), alpha=0.1, color='gray')
    plt.fill_between(x, cdf, where=(x >= -10000000) & (x <= p50), alpha=0.2, color='gray')
    plt.fill_between(x, cdf, where=(x >= -10000000) & (x <= p10), alpha=0.3, color='gray')
    plt.axvline(p10, color='red', linestyle='--', label=f'p10 = {round(p10/1000000,2)} mill. kr')
    plt.axvline(p50, color='green', linestyle='--', label=f'p50 = {round(p50/1000000,2)} mill. kr')
    plt.axvline(p90, color='purple', linestyle='--', label=f'p90 = {round(p90/1000000,2)} mill. kr')
    plt.axhline(0, color="black")
    plt.ylabel('Cumulative Probability')
    plt.title("CDF")
    plt.legend()

    print(f'p10: {p10}')
    print(f'p50: {p50}')
    print(f'p90: {p90}')
    print(f"p99: {p99}")
    plt.savefig('cost_est_plot.png', dpi=300)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot cost distribution.')
    parser.add_argument('expected_value', type=float, help='Expected value of the cost')
    parser.add_argument('std_deviation', type=float, help='Standard deviation of the cost')
    args = parser.parse_args()
    plot_cost_distribution(args.expected_value, args.std_deviation)
