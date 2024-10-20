import pandas as pd

def flows_per_capita():
    # This function creates a new dataframe with a new calculated column 'Public Flows per Capita (2021 USD)'
    # by combining information about public investments from IRENA with population statistics from the World Bank.
    irena_flows = pd.pivot_table(irena_data, values="Public Flows (2021 USD M)", index=["ISO3 code", "Country", "Year"],
                                 aggfunc="sum").reset_index()
    irena_flows.rename(columns={"ISO3 code": "Country Code"}, inplace=True)
    flows_per_capita = pd.merge(irena_flows, pop_data, how="left", on=['Country Code', 'Year'])

    # (b) Calculate Public Flows per Capita
    flows_per_capita['Public Flows per Capita (2021 USD)'] = ((flows_per_capita['Public Flows (2021 USD M)'] * 1000000)
                                                              / flows_per_capita['Population'])
    return flows_per_capita

def percent_renewable(df):
    # This function calculates a new column 'Renewable Electricity Generation as % of Total' and adds it to the
    # previously created dataframe. It shows the proportion of electricity generation coming from renewable sources.
    irena_gen = pd.pivot_table(irena_data, values="Electricity Generation (GWh)", index=["ISO3 code", "Country", "Year"],
                               columns=["RE or Non-RE"], aggfunc="sum").reset_index()
    irena_gen.rename(columns={"ISO3 code": "Country Code"}, inplace=True)
    irena_gen['Renewable Electricity Generation as % of Total'] = (irena_gen['Total Renewable'] /
                                                                   (irena_gen['Total Non-Renewable'] + irena_gen['Total Renewable']))
    percent_renewable = pd.merge(df, irena_gen, how="left", on=["Country Code", "Country", "Year"])
    return percent_renewable

def cap_per_capita(df):
    # This function adds the field 'RE capacity per capita' to the previously created dataframe.
    irena_cap = pd.pivot_table(irena_data, values="SDG 7b1 RE capacity per capita (W/inhabitant)",
                               index=["ISO3 code", "Country", "Year"], aggfunc="sum").reset_index()
    irena_cap.rename(columns={"ISO3 code": "Country Code"}, inplace=True)
    irena_flows_and_cap = pd.merge(df, irena_cap, how="left", on=['Country Code', 'Country', 'Year'])
    return irena_flows_and_cap

def epi(df):
    # This function creates a filtered version of the previous dataframe to display data for 2022,
    # and adds the EPI and CDA 2024 indicators to this filtered dataframe.
    # EPI = Environmental Performance Index
    # CDA = Adjusted emissions growth rate for carbon dioxide
    epi_cda = epi_data.filter(items=["iso", "EPI.old", "EPI.new", "CDA.old", "CDA.new"])
    epi_cda.rename(columns={"iso" : "Country Code"}, inplace=True)
    irena_epi = df.loc[df["Year"] == 2022]
    irena_epi = pd.merge(irena_epi, epi_cda, how="left", on=['Country Code'])
    return irena_epi

if __name__ == '__main__':
    # 1) Open the population file. Erase the first three rows from population data and melt. The melt operation will transpose the years into rows.
    pop_file = "data_original\API_SP.POP.TOTL_DS2_en_csv_v2_31753.csv"
    pop_data = pd.read_csv(pop_file, skiprows=4)
    years_array = pop_data.columns[4:-1].astype(str).tolist()
    pop_data = pop_data.melt(id_vars=['Country Code'], value_vars=years_array, var_name='Year', value_name="Population")
    pop_data['Year'] = pop_data['Year'].astype(int)

    # 2) Open IRENA 2024
    irena_file = "data_original\IRENA_Stats_extract_2024 H2.xlsx"
    irena_data = pd.read_excel(irena_file, sheet_name="All data")

    # 3) Open EPI 2024
    epi_file = "data_original\epi2024results.csv"
    epi_data = pd.read_csv(epi_file)

    # 4) Create proc_irena Dataframe with Flows Per Capita
    proc_irena = flows_per_capita()

    # 5) Add RE Production / Total Production % to proc_irena
    proc_irena = percent_renewable(proc_irena)

    # 6) Add Installed RE Capacity Per Capita to proc_irena
    proc_irena = cap_per_capita(proc_irena)

    # 7) Create Second Dataframe with Most Recent IRENA and EPI Results
    proc_irena_epi = epi(proc_irena)

    # 8) Export Both Dataframes to .csv
    proc_irena.to_csv('data_processing/proc_irena.csv', index=False)
    proc_irena_epi.to_csv('data_processing/proc_irena_epi.csv', index=False)
