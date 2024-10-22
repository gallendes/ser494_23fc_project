import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy
import seaborn as sns

def compound_stats(df, feature_name):
    result = pd.pivot_table(df, values=feature_name, index=['Year'],
                            aggfunc={f'{feature_name}':['max','median','min']})
    result.columns = ['Max', 'Median', 'Min']
    result = result[['Min', 'Median', 'Max']]
    return result

def simple_stats(df, feature_name):
    min = df[feature_name].min()
    median = df[feature_name].median()
    max = df[feature_name].max()
    result = pd.DataFrame([[min, median, max]], columns=['Min', 'Median', 'Max'],
                          index=[feature_name])
    return result

def qual_stats(df):
    num_categories = pd.pivot_table(df, values='Country', index=['Year'],
                            columns=['Region'], aggfunc='count')
    min = num_categories.idxmin(axis='columns')
    max = num_categories.idxmax(axis='columns')
    df_min = pd.DataFrame(min)
    df_max = pd.DataFrame(max)
    stats = pd.merge(df_min, df_max, how='outer', on='Year').reset_index()
    stats = stats.rename(columns={
        '0_x': 'Least Frequent',
        '0_y': 'Most Frequent'
    })
    merged_stats = pd.merge(num_categories, stats, how='left', on='Year')
    return merged_stats


def main():
    file_1 = "data_processing\proc_irena.csv"
    proc_irena = pd.read_csv(file_1)
    file_2 = "data_processing\proc_irena_epi.csv"
    proc_irena_epi = pd.read_csv(file_2)

    # (1) Summary Statistics
    # Computes Yearly Min, Median, and Max for Public Flows per Capita (USD)
    quant_stat_1 = compound_stats(proc_irena, "Public Flows per Capita (USD)")
    # Computes Yearly Min, Median, and Max for Renewable Energy Share of Electricity Production (%)
    quant_stat_2 = compound_stats(proc_irena, "Renewable Energy Share of Electricity Production (%)")
    # Computes Yearly Min, Median, and Max for SDG 7b1 RE capacity per capita (W/inhabitant)
    quant_stat_3 = compound_stats(proc_irena, "SDG 7b1 RE capacity per capita (W/inhabitant)")
    # Computes Min, Median, and Max for EPI (Environmental Performance Index) 2024
    quant_stat_4 = simple_stats(proc_irena_epi, "EPI.new")
    # Computes Min, Median, and Max for CDA (Adjusted emissions growth rate for carbon dioxide) 2024
    quant_stat_5 = simple_stats(proc_irena_epi, "CDA.new")
    # Computes Number of Categories, Most Frequent Category, and Least Frequent Category for Geographical Regions
    qual_stat = qual_stats(proc_irena)

    # Print Summary Stats
    summary_filename = "data_processing\summary.txt"
    with open(summary_filename, "w") as summary_file:
        summary_file.write('Quantitative Features')
        summary_file.write('\n')
        summary_file.write('1. Public Flows per Capita (USD) from 2000 to 2022')
        summary_file.write('\n')
        summary_file.write('2. Renewable Energy Share of Electricity Production (%) from 2000 to 2022')
        summary_file.write('\n')
        summary_file.write('3. Renewable Energy Capacity per Capita (W/inhabitant) from 2000 to 2022')
        summary_file.write('\n')
        summary_file.write('4. EPI Scores in 2024')
        summary_file.write('\n')
        summary_file.write('5. CDA Scores in 2024')
        summary_file.write('\n')
        summary_file.write('* Quantitative features 1 to 3 depend on yearly values, which is why they'
                           ' each require separate tables.')
        summary_file.write('\n\n')
        summary_file.write('Qualitative Feature')
        summary_file.write('\n')
        summary_file.write('1. Countries by Region')
        summary_file.write('\n\n')
        summary_file.write('Quantitative 1: Public Flows per Capita (USD) from 2000 to 2022')
        summary_file.write('\n')
        summary_file.write(quant_stat_1.to_string())
        summary_file.write('\n\n')
        summary_file.write('Quantitative 2: Renewable Energy Share of Electricity Production (%GWh) from 2000 to 2022')
        summary_file.write('\n')
        summary_file.write(quant_stat_2.to_string())
        summary_file.write('\n\n')
        summary_file.write('Quantitative 3: Renewable Energy Capacity per Capita (W/inhabitant) from 2000 to 2022')
        summary_file.write('\n')
        summary_file.write(quant_stat_3.to_string())
        summary_file.write('\n\n')
        summary_file.write('Quantitative 4 and 5: EPI and CDA Scores in 2024')
        summary_file.write('\n')
        summary_file.write(pd.concat([quant_stat_4, quant_stat_5]).to_string())
        summary_file.write('\n\n')
        summary_file.write('Qualitative 1: Frequencies of Countries by Region from 2000 to 2022')
        summary_file.write('\n')
        summary_file.write(qual_stat.to_string())

    # (2) Pairwise Correlations
    selected_features = ['Public Flows per Capita (USD)', 'Renewable Energy Share of Electricity Production (%)',
                         'SDG 7b1 RE capacity per capita (W/inhabitant)', 'EPI.new', 'CDA.new']
    correlation_matrix = proc_irena_epi[selected_features].corr()

    correlations_filename = "data_processing\correlations.txt"
    with open(correlations_filename, 'w') as correlations_file:
        correlations_file.write('Correlations were calculated using data from the year 2022 to avoid the complexity of'
                                ' a time dimension.')
        correlations_file.write('\n')
        correlations_file.write('However, for the EPI and CDA scores, the year 2024 was used, as '
                                'the 2022 scores do not fully reflect data from year 2022.')
        correlations_file.write('\n')
        correlations_file.write('Please note that EPI and CDA scores for 2023 are not available, '
                                'as the study is conducted biennially.')
        correlations_file.write('\n\n')
        correlations_file.write(correlation_matrix.to_string())

    # (3) Plots of Distributions

    sns.set_theme()

    # 1 AB
    fig, ax = plt.subplots()
    ax.set(title="Public Flows per Capita and Renewable Share \nin Electricity Production (2022)",
           xlabel="Public Flows in Renewable Energy per Capita (USD)",
           ylabel="Renewable Share of Electricity Production (%)")
    ax.set_xlim(left=-5, right=150)
    ax.set_ylim(bottom=-0.05, top=1.05)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    ax.scatter(proc_irena_epi["Public Flows per Capita (USD)"],
               proc_irena_epi["Renewable Energy Share of Electricity Production (%)"], s=5)
    fig.show()
    fig.savefig("visuals\AB.png")

    # 2 AC
    fig, ax = plt.subplots()
    ax.set(title="Public Flows per Capita and Installed RE \nCapacity Per Capita (2022)",
           xlabel="Public Flows in Renewable Energy per Capita (USD)", ylabel="RE Capacity per Capita (W/inhabitant)")
    ax.set_xlim(left=-5, right=150)
    ax.set_ylim(bottom=-100, top=2700)
    ax.scatter(proc_irena_epi["Public Flows per Capita (USD)"],
               proc_irena_epi["SDG 7b1 RE capacity per capita (W/inhabitant)"], s=5)
    fig.show()
    fig.savefig("visuals\AC.png")

    # 3 AD
    fig, ax = plt.subplots()
    ax.set(title="Public Flows (2022) and Most Recent EPI score",
           xlabel="Public Flows in Renewable Energy per Capita (USD)", ylabel="EPI Score")
    ax.set_xlim(left=-5, right=150)
    ax.scatter(proc_irena_epi["Public Flows per Capita (USD)"],
               proc_irena_epi["EPI.new"], s=5)
    fig.show()
    fig.savefig("visuals\AD.png")

    # 4 AE
    fig, ax = plt.subplots()
    ax.set(title="Public Flows (2022) Most Recent CDA score",
           xlabel="Public Flows in Renewable Energy per Capita (USD)", ylabel="CDA Score")
    ax.set_xlim(left=-5, right=150)
    ax.scatter(proc_irena_epi["Public Flows per Capita (USD)"],
               proc_irena_epi["CDA.new"], s=5)
    fig.show()
    fig.savefig("visuals\AE.png")

    # 5 BC
    fig, ax = plt.subplots()
    ax.set(title="Renewable Energy Share and Installed \n RE Capacity Per Capita (2022)",
           xlabel="Renewable Energy Share of Electricity Production (%)",
           ylabel="RE Capacity per Capita (W/Inhabitant)")
    ax.scatter(proc_irena_epi["Renewable Energy Share of Electricity Production (%)"],
               proc_irena_epi["SDG 7b1 RE capacity per capita (W/inhabitant)"], s=5)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    fig.show()
    fig.savefig("visuals\BC.png")

    # 6 BD
    fig, ax = plt.subplots()
    ax.set(title="Renewable Energy Share (2022) and Most Recent EPI score",
           xlabel="Renewable Energy Share of Electricity Production (%)", ylabel="EPI Score")
    ax.scatter(proc_irena_epi["Renewable Energy Share of Electricity Production (%)"],
               proc_irena_epi["EPI.new"], s=5)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    fig.show()
    fig.savefig("visuals\BD.png")

    # 7 BE
    fig, ax = plt.subplots()
    ax.set(title="Renewable Energy Share (2022) and Most Recent CDA score",
           xlabel="Renewable Energy Share of Electricity Production (%)", ylabel="CDA Score")
    ax.scatter(proc_irena_epi["Renewable Energy Share of Electricity Production (%)"],
               proc_irena_epi["CDA.new"], s=5)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    fig.show()
    fig.savefig("visuals\BE.png")

    # 8 CD
    fig, ax = plt.subplots()
    ax.set(title="Installed RE Capacity Per Capita (2022) and Most Recent EPI score",
           xlabel="RE Capacity per Capita (W/Inhabitant)", ylabel="EPI Score")
    ax.scatter(proc_irena_epi["SDG 7b1 RE capacity per capita (W/inhabitant)"],
               proc_irena_epi["EPI.new"], s=5)
    fig.show()
    fig.savefig("visuals\CD.png")

    # 9 CE
    fig, ax = plt.subplots()
    ax.set(title="Installed RE Capacity Per Capita (2022) and Most Recent CDA score",
           xlabel="RE Capacity per Capita (W/Inhabitant)", ylabel="CDA Score")
    ax.scatter(proc_irena_epi["SDG 7b1 RE capacity per capita (W/inhabitant)"],
               proc_irena_epi["CDA.new"], s=5)
    fig.show()
    fig.savefig("visuals\CE.png")

    # 10 DE
    fig, ax = plt.subplots()
    ax.set(title="Most Recent EPI score and Most Recent CDA score",
           xlabel="EPI Score", ylabel="CDA Score")
    ax.scatter(proc_irena_epi["EPI.new"],
               proc_irena_epi["CDA.new"], s=5)
    fig.show()
    fig.savefig("visuals\DE.png")

    #11 BAR GRAPH
    fig, ax = plt.subplots()
    data = qual_stat[qual_stat['Year'] == 2000].iloc[:, 1:6]
    data = data.T
    ax.set(title='Countries by Region', xlabel="Region", ylabel="Count")
    sns.barplot(data=data, x=data.index, y=data[0])
    ax.bar_label(ax.containers[0], fontsize=10);
    ax.set_ylim(bottom=0, top=60)
    fig.show()
    fig.savefig("visuals\F.png")

    #12 Data Generality
    g = sns.displot(data=proc_irena_epi, x="EPI.new", kde=True)
    g.fig.show()
    g.fig.savefig("visuals\data_generality.png")

    print('Exported visuals directory visuals/')

    # # 11 TIME SERIES A
    # fig, ax = plt.subplots()
    # ax.set(title="Public Flows in Renewable Energy per Capita (2000 - 2022)",
    #        xlabel="Year",
    #        ylabel="Public Flows in Renewable Energy per Capita (USD)")
    # ax.set_ylim(bottom=-5, top=1000)
    # ax.scatter(proc_irena["Year"],
    #            proc_irena["Public Flows per Capita (USD)"], s=5)
    # fig.show()
    # fig.savefig("visuals\A_time_series.png")
    #
    # # 12 TIME SERIES B
    # fig, ax = plt.subplots()
    # ax.set(title="Renewable Energy Share of \nElectricity Production (2000 - 2022)",
    #        xlabel="Year",
    #        ylabel="Renewable Energy Share of Electricity Production (%)")
    # ax.scatter(proc_irena["Year"],
    #            proc_irena["Renewable Energy Share of Electricity Production (%)"], s=5)
    # ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    # fig.show()
    # fig.savefig("visuals\B_time_series.png")
    #
    # # 13 TIME SERIES C
    # fig, ax = plt.subplots()
    # ax.set(title="Installed RE Capacity per Capita (2000 - 2022)",
    #        xlabel="Year",
    #        ylabel="Installed RE Capacity per Capita (W/Inhabitant)")
    # ax.scatter(proc_irena["Year"],
    #            proc_irena["SDG 7b1 RE capacity per capita (W/inhabitant)"], s=5)
    # fig.show()
    # fig.savefig("visuals\C_time_series.png")

if __name__ == '__main__':
    main()