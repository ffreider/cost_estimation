import pandas as pd
import matplotlib.pyplot as plt
import argparse

def clean_data(file_path, level):
    cost_estimation_data = pd.read_csv(file_path, header=3)
    columns_to_keep = ['Levels', 'WBS Name', 'P10 (NOK)', 'Expected Value (NOK)', 'P90 (NOK)']
    cleaned_data = cost_estimation_data[columns_to_keep]
    cleaned_data = cleaned_data.dropna(subset=['Levels', 'WBS Name', 'P10 (NOK)', 'Expected Value (NOK)', 'P90 (NOK)'])
    cleaned_data = cleaned_data[cleaned_data['Levels'].astype(str).str.count('\.') == (level - 1)]
    cleaned_data = cleaned_data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    cleaned_data['P10 (NOK)'] = cleaned_data['P10 (NOK)'].str.replace(',', '').astype(float)
    cleaned_data['Expected Value (NOK)'] = cleaned_data['Expected Value (NOK)'].str.replace(',', '').astype(float)
    cleaned_data['P90 (NOK)'] = cleaned_data['P90 (NOK)'].str.replace(',', '').astype(float)
    return cleaned_data

def plot_tornado_diagram(cleaned_data):
    cleaned_data['Lower Deviation (NOK)'] = cleaned_data['Expected Value (NOK)'] - cleaned_data['P10 (NOK)']
    cleaned_data['Upper Deviation (NOK)'] = cleaned_data['P90 (NOK)'] - cleaned_data['Expected Value (NOK)']
    cleaned_data['Total Deviation (NOK)'] = cleaned_data['Lower Deviation (NOK)'] + cleaned_data['Upper Deviation (NOK)']
    sorted_data = cleaned_data.sort_values(by='Total Deviation (NOK)', ascending=False)
    plt.style.use('seaborn-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 10))
    for index, row in sorted_data.iterrows():
        ax.plot([-row['Lower Deviation (NOK)'], row['Upper Deviation (NOK)']], 
                 [row['WBS Name'], row['WBS Name']], 
                 color='skyblue', linewidth=10, solid_capstyle='butt')
        ax.scatter(0, row['WBS Name'], color='red', zorder=5)
    ax.axvline(x=0, color='grey', linestyle='--')
    ax.set_xlabel('Deviation from Expected Value (NOK)', fontsize=14)
    ax.set_ylabel('WBS Name', fontsize=14)
    ax.set_title('Tornado Diagram of Cost Estimates (Centered on Expected Value)', fontsize=16, weight='bold')
    plt.tight_layout()
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.grid(True, linestyle='--', alpha=0.7, axis='x')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Clean WBS data and plot a tornado diagram.')
    parser.add_argument('file_path', type=str, help='Path to the CSV file containing the cost estimation data')
    parser.add_argument('level', type=int, help='Level of WBS to include in the plot')
    args = parser.parse_args()
    
    cleaned_data = clean_data(args.file_path, args.level)
    plot_tornado_diagram(cleaned_data)

