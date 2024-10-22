import pandas as pd

def flows_per_capita():
    # This function creates a new dataframe with a new calculated column 'Public Flows per Capita (USD)'
    # by combining information about public investments from IRENA with population statistics from the World Bank.
    irena_flows = pd.pivot_table(irena_data, values='Public Flows (2021 USD M)', index=['Region', 'ISO3 code', 'Country', 'Year'],
                                 aggfunc='sum').reset_index()
    irena_flows.rename(columns={'ISO3 code': 'Country Code'}, inplace=True)
    flows_per_capita = pd.merge(irena_flows, pop_data, how='inner', on=['Country Code', 'Year'])
    flows_per_capita['Public Flows per Capita (USD)'] = ((flows_per_capita['Public Flows (2021 USD M)'] * 1000000)
                                                              / flows_per_capita['Population'])
    flows_per_capita = flows_per_capita[flows_per_capita['Year'] != 2023]
    return flows_per_capita

def percent_renewable(df):
    # This function calculates a new column 'Renewable Energy Share of Electricity Production (%)' and adds it to the
    # previously created dataframe. It shows the proportion of electricity generation coming from renewable sources.
    # Electricity Generation data has blank cells instead of zeroes. To avoid problems while aggregating into
    # pivot tables, nan's must be replaced with zeroes.
    irena_gen = pd.pivot_table(irena_data, values='Electricity Generation (GWh)', index=['ISO3 code', 'Country', 'Year'],
                               columns=['RE or Non-RE'], aggfunc='sum').reset_index()
    irena_gen.fillna({'Total Non-Renewable': 0}, inplace=True)
    irena_gen.fillna({'Total Renewable': 0}, inplace=True)
    irena_gen.rename(columns={'ISO3 code': 'Country Code'}, inplace=True)
    irena_gen['Renewable Energy Share of Electricity Production (%)'] = (irena_gen['Total Renewable'] /
                                                                   (irena_gen['Total Non-Renewable'] + irena_gen['Total Renewable']))
    percent_renewable = pd.merge(df, irena_gen, how='left', on=['Country Code', 'Country', 'Year'])
    return percent_renewable

def cap_per_capita(df):
    # This function adds the field 'RE capacity per capita' to the previously created dataframe.
    irena_cap = pd.pivot_table(irena_data, values='SDG 7b1 RE capacity per capita (W/inhabitant)',
                               index=['ISO3 code', 'Country', 'Year'], aggfunc='sum').reset_index()
    irena_cap.rename(columns={'ISO3 code': 'Country Code'}, inplace=True)
    irena_flows_and_cap = pd.merge(df, irena_cap, how='left', on=['Country Code', 'Country', 'Year'])
    return irena_flows_and_cap

def epi(df):
    # This function creates a filtered version of the previous dataframe to display data for 2022,
    # and adds the EPI and CDA 2024 indicators to this filtered dataframe.
    # Missing scores for EPI and CDA in 2024 were replaced with the mean of the dataset.
    epi_cda = epi_data.filter(items=['iso', 'EPI.old', 'EPI.new', 'CDA.old', 'CDA.new'])
    epi_cda.rename(columns={'iso' : 'Country Code'}, inplace=True)
    irena_epi = df.loc[df['Year'] == 2022]
    irena_epi = pd.merge(irena_epi, epi_cda, how='left', on=['Country Code'])

    # This list of countries / territories do not have EPI and CDA scores.
    # To fill in missing values, territories that depend on other nations will borrow EPI and CDA scores from their
    # parent nations. For independent countries in this list, missing values will be replaced with dataset averages.
    territories = {
        "American Samoa": "USA",
        "Andorra": "Independent",
        "Aruba": "NLD",
        "British Virgin Islands": "GBR",
        "Cayman Islands": "GBR",
        "China Hong Kong Special Administrative Region": "CHN",
        "Curaçao": "NLD",
        "Democratic People's Republic of Korea": "Independent",
        "Faroe Islands": "DNK",
        "French Polynesia": "FRA",
        "Greenland": "DNK",
        "Guam": "USA",
        "Kosovo": "Independent",
        "Libya": "Independent",
        "Nauru": "Independent",
        "New Caledonia": "FRA",
        "Palau": "Independent",
        "Puerto Rico": "USA",
        "Saint Kitts and Nevis": "Independent",
        "Saint Martin (French Part)": "FRA",
        "Sint Maarten (Dutch Part)": "NLD",
        "Somalia": "Independent",
        "South Sudan": "Independent",
        "State of Palestine": "Independent",
        "Syrian Arab Republic": "Independent",
        "Turks and Caicos Islands": "GBR",
        "Tuvalu": "Independent",
        "United States Virgin Islands": "USA",
        "Yemen": "Independent"
    }

    irena_epi = update_epi_cda_scores(irena_epi, territories)
    return irena_epi

def update_epi_cda_scores(df, territories):
    for territory, parent in territories.items():
        # Skip if the parent is 'Independent', as there is no parent country to reference
        if parent != 'Independent':
            # Find the parent country's values
            parent_values = df.loc[df['Country Code'] == parent, ['EPI.new', 'EPI.old', 'CDA.new', 'CDA.old']].values
            if len(parent_values) > 0:  # Ensure the parent country exists in the dataset
                # Update the territory's values with the parent country's values
                df.loc[df['Country'] == territory, ['EPI.new', 'EPI.old', 'CDA.new', 'CDA.old']] = parent_values[0]
            else:
                print(f"Parent country {parent} not found in dataset for {territory}.")
        else:
            averages = df[['EPI.new', 'EPI.old', 'CDA.new', 'CDA.old']].mean().values
            df.loc[df['Country'] == territory, ['EPI.new', 'EPI.old', 'CDA.new', 'CDA.old']] = averages
    return df

def main():
    # 1) Open the population file. Erase first three rows from population data
    #    (they are just headers) and melt data to transpose years into rows.
    global pop_data
    pop_file = 'data_original\API_SP.POP.TOTL_DS2_en_csv_v2_31753.csv'
    pop_data = pd.read_csv(pop_file, skiprows=4)
    years_array = pop_data.columns[4:-1].astype(str).tolist()
    pop_data = pop_data.melt(id_vars=['Country Code'], value_vars=years_array, var_name='Year', value_name='Population')
    pop_data['Year'] = pop_data['Year'].astype(int)

    # 2) Open IRENA 2024
    global irena_data
    irena_file = 'data_original\IRENA_Stats_extract_2024 H2.xlsx'
    irena_data = pd.read_excel(irena_file, sheet_name='All data')

    # 3) Open EPI 2024
    global epi_data
    epi_file = 'data_original\epi2024results.csv'
    epi_data = pd.read_csv(epi_file)

    # 4) Calculate Quantitative Feature 1: 'Public Flows per Capita (USD)'
    proc_irena = flows_per_capita()

    # 5) Calculate Quantitative Feature 2: 'Renewable Energy Share of Electricity Production (%)'
    proc_irena = percent_renewable(proc_irena)

    # 6) Include Quantitative Feature 3: 'RE capacity per capita'
    proc_irena = cap_per_capita(proc_irena)

    # 7) Calculate Quantitative Features 4 and 5:
    #    EPI 2024 (Environmental Performance Index) and
    #    CDA 2024 (Adjusted emissions growth rate for carbon dioxide)
    proc_irena_epi = epi(proc_irena)

    # 8) Export Quantitative Features 1 to 3 to .csv
    proc_irena.to_csv('data_processing/proc_irena.csv', index=False)

    # 9) Export Quantitative Features 4 and 5 to .csv
    proc_irena_epi.to_csv('data_processing/proc_irena_epi.csv', index=False)

    print('Exported data files to csv in directory data_processing/')

if __name__ == '__main__':
    main()