#### SER494: Exploratory Data Munging and Visualization
#### Title: Analyzing Global Trends in Renewable Energy Adoption
#### Author: Gonzalo Allendes
#### Date: October 17th, 2024

### **Data File 1**: [IRENA (2024), Renewable energy statistics 2024](data_original/IRENA_Stats_extract_2024 H2.xlsx)

#### 1. Basic Questions

> **Dataset Author(s):** IRENA. Prepared by Julian Prime, Iman Abdulkadir Ahmed, Dennis Akande, Nazik Elhassan, Gerardo Escamilla, Akshay Jamdade, Yury
Melnikov, Adrian Whiteman.
>
> 
> **Dataset Construction Date:** July 2024
> 
> 
> **Dataset Record Count:** 90,553
> 
> 
> **Dataset Field Meanings:**
>   - ***Region***: Composition of geographical regions used by the Statistics Division of the United Nations. 
>   - ***Sub-region***: Subcategory within geographical region. Also used by the UN. 
>   - ***Country***: Name of the country.
>   - ***ISO3 code***: Three-digit alphabetical country code assigned by the International Organization for Standardization (ISO)
>   - ***M49 code***: Standard country or area code issued for statistical use by the Statistics Division of the UN. 
>   - ***RE or Non-RE***: Renewable or non-renewable energy label for the data in this row.
>   - ***Group Technology***: High-level category of the type of technology used.
>   - ***Technology***: Mid-level category of the type of technology used.
>   - ***Sub-Technology***: Low-level category of the type of technology used.
>   - ***Producer Type***: Type of producer, whether it is on-grid, off-grid, heat, or a combination of heat and power.
>   - ***Year***: Year of row data collection.
>   - ***Electricity Generation (GWh)***: Total electricity generation in gigawatt-hours.
>   - ***Electricity Installed Capacity (MW)***: Total installed capacity in megawatts.
>   - ***Heat Generation (TJ)***: Heat generation in terajoules.
>   - ***Off-grid Biogas for Cooking (1,000 inhabitants)***: Number of inhabitants using off-grid biogas for cooking, measured in 1,000's.
>   - ***Off-grid Biogas Production (1,000 m3)***: Amount of biogas produced off-grid measured in thousands of cubic meters.
>   - ***Off-grid Electricity Access (1,000 inhabitants)***: Number of inhabitants with access to electricity through off-grid systems in thousands of people.
>   - ***Public Flows (2021 USD M)***: Financial flows including public investments and aid related to energy development in millions of USD (2021).
>   - ***SDG 7a1 Intl. Public Flows (2021 USD M)***: Sustainable development goal (SDG) indicator that shows international public flows to finance sustainable energy in developing countries, in USD (2021).
>   - ***SDG 7b1 RE capacity per capita (W/inhabitant)***: Renewable energy installed capacity per capita measured in watts per inhabitant. 
>
> 
> **Dataset URL:** https://www.irena.org/Publications/2024/Jul/Renewable-energy-statistics-2024 (Click on 'Download data', it's a free download)
> 
> **Dataset File Hash(es):** 77524de3d458e8bce36ace669fdbf900

#### 2. Interpretable Records

>**Record 1:**
> - **Raw Data**:
>  
>| Region | Sub-region     | Country | ISO3 code | M49 code | RE or Non-RE    | Group Technology | Technology          | Sub-Technology      | Producer Type       | Year | Electricity Generation (GWh) | Electricity Installed Capacity (MW) | Heat Generation (TJ) | Off-grid Biogas for Cooking (1,000 inhabitants) | Off-grid Biogas Production (1,000 m³) | Off-grid Electricity Access (1,000 inhabitants) | Public Flows (2021 USD M) | SDG 7a1 Intl. Public Flows (2021 USD M) | SDG 7b1 RE capacity per capita (W/inhabitant) |
>|--------|----------------|---------|-----------|----------|-----------------|------------------|---------------------|---------------------|---------------------|------|------------------------------|-------------------------------------|----------------------|-------------------------------------------------|---------------------------------------|-------------------------------------------------|---------------------------|-----------------------------------------|-----------------------------------------------|
>| Europe | Western Europe | Austria | AUT       | 40       | Total Renewable | Wind energy      | Onshore wind energy | Onshore wind energy | On-grid electricity | 2022 | 7245.134                     | 3579.236                            |                      |                                                 |                                       |                                                 |                           |                                         |                                               |
>
> - **Interpretation**: This record in the data displays the installed capacity and the amount of electricity generated from onshore wind energy in 2022 in the country of Austria. [This Wikipedia article](https://en.wikipedia.org/wiki/Wind_power_in_Austria) confirms the installed capacity, making it a reasonable data record. 
>
> 
>**Record 2**
>  - **Raw Data:**
> 
> | Region | Sub-region     | Country | ISO3 code | M49 code | RE or Non-RE    | Group Technology | Technology          | Sub-Technology      | Producer Type | Year | Electricity Generation (GWh) | Electricity Installed Capacity (MW) | Heat Generation (TJ) | Off-grid Biogas for Cooking (1,000 inhabitants) | Off-grid Biogas Production (1,000 m³) | Off-grid Electricity Access (1,000 inhabitants) | Public Flows (2021 USD M) | SDG 7a1 Intl. Public Flows (2021 USD M) | SDG 7b1 RE capacity per capita (W/inhabitant) |
> |--------|----------------|---------|-----------|----------|-----------------|------------------|---------------------|---------------------|---------------|------|------------------------------|-------------------------------------|----------------------|-------------------------------------------------|---------------------------------------|-------------------------------------------------|---------------------------|-----------------------------------------|-----------------------------------------------|
> | Europe | Western Europe | Austria | AUT       | 40       | Total Renewable | Wind energy      | Onshore wind energy | Onshore wind energy | All types     | 2022 |                              |                                     |                      |                                                 |                                       |                                                 | 2.990235202               |                                         | 417.8938538                                   |
> 
> 
> 
>  - **Interpretation:** This record in the data displays the public investments and aid dedicated to financing on-grid and off-grid wind energy (all of it was onshore) and per-capita installed capacity of this type of energy, for the year 2022. Considering an installed capacity of approximately 3.580 MW in 2022 and a population of around 9M, the per capita RE capacity in this record is reasonable. 

### **Data File 2**: [Environmental Performance Index 2024](data_original/epi2024results.csv)

#### 1. Basic Questions

> **Dataset Author(s):** Block, S., Emerson, J. W., Esty, D. C., de Sherbinin, A., Wendling, Z.A., et al. 
>
> 
> **Dataset Construction Date:** 3 June 2024. Corrigendum: 7 October 2024.
> 
> 
> **Dataset Record Count:** 180
>
> **Dataset Fields 1-3:**
>   - ***code***: Standard country or area code issued for statistical use by the Statistics Division of the UN.
>   - ***iso***: Three-digit alphabetical country code assigned by the International Organization for Standardization (ISO)
>   - ***country***: Name of the country.
> 
> **Dataset Fields 4-150 Suffixes:**
>   - ***.new***: Most recent indicator scores calculated using the 2024 methodology.
>   - ***.old***: Baseline scores representing values from approximately 10 years ago, also calculated using the 2024 methodology (backcasted).
>
> **Dataset Fields 4-150 Meanings:**
>   - ***EPI***: Environmental Performance Index: The 2024 EPI combines 58 indicators across 11 issue categories, ranging from climate change mitigation and air pollution to waste management, sustainability of fisheries and agriculture, deforestation, and biodiversity protection.
>   - ***ECO***: Ecosystem Vitality
>   - ***BDH***: Biodiversity & Habitat
>   - ***MKP***: Marine KBA Protection
>   - ***MHP***: Marine Habitat Protection
>   - ***MPE***: Marine Protection Stringency
>   - ***PAR***: Protected Areas Representativeness Index
>   - ***SPI***: Species Protection Index
>   - ***TBN***: Terrestrial Biome Protection (national weights)
>   - ***TKP***: Terrestrial KBA Protection
>   - ***PAE***: Protected Area Effectiveness
>   - ***PHL***: Protected Human Land
>   - ***RLI***: Red List Index
>   - ***SHI***: Species Habitat Index
>   - ***BER***: Bioclimatic Ecosystem Resilience
>   - ***ECS***: Forests
>   - ***PFL***: Primary Forest Loss
>   - ***IFL***: Intact Forest Landscape Loss
>   - ***FCL***: Tree cover loss weighted by permanency
>   - ***TCG***: Net change in tree cover
>   - ***FLI***: Forest Lanscape Integrity
>   - ***FSH***: Fisheries
>   - ***FSS***: Fish Stock Status
>   - ***FCD***: Fish Catch Discarded
>   - ***BTZ***: Bottom Trawling in EEZ
>   - ***BTO***: Bottom Trawling in Global Ocean
>   - ***RMS***: Regional Marine Trophic Index
>   - ***APO***: Air Pollution
>   - ***OEB***: Ozone exposure KBAs
>   - ***OEC***: Ozone exposure croplands
>   - ***NXA***: Adjusted emissions growth rate for nitrous oxides
>   - ***SDA***: Adjusted emissions growth rate for sulfur dioxide
>   - ***AGR***: Agriculture
>   - ***SNM***: Sustainable Nitrogen Management Index
>   - ***PSU***: Phosphorus Surplus
>   - ***PRS***: Pesticide Pollution Risk
>   - ***RCY***: Relative Crop Yield
>   - ***WRS***: Water Resources
>   - ***WWG***: Wastewater generated
>   - ***WWC***: Wastewater collected
>   - ***WWT***: Wastewater treated
>   - ***WWR***: Wastewater reused
>   - ***HLT***: Environmental Health
>   - ***AIR***: Air Quality
>   - ***HPE***: Anthropogenic PM2.5 exposure 
>   - ***HFD***: Household solid fuels
>   - ***OZD***: Ozone exposure
>   - ***NOD***: NO2 exposure
>   - ***SOE***: SO2 exposure
>   - ***COE***: CO exposure
>   - ***VOE***: VOC exposure
>   - ***H2O***: Sanitation & Drinking Water
>   - ***USD***: Unsafe sanitation 
>   - ***UWD***: Unsafe drinking water
>   - ***HMT***: Heavy Metals
>   - ***LED***: Lead exposure
>   - ***WMG***: Solid Waste
>   - ***WPC***: Waste Generated Per Capita
>   - ***SMW***: Controlled Solid Waste
>   - ***WRR***: Waste Recovery Rate
>   - ***PCC***: Climate Change 
>   - ***CCH***: Climate Change Mitigation
>   - ***CDA***: Adjusted emissions growth rate for carbon dioxide
>   - ***CDF***: Adjusted emissions growth rate for carbon dioxide (country-specific targets)
>   - ***CHA***: Adjusted emissions growth rate for methane
>   - ***FGA***: Adjusted emissions growth rate for F-gases
>   - ***NDA***: Adjusted emissions growth rate for nitrous oxide
>   - ***BCA***: Adjusted emissions growth rate for black carbon
>   - ***LUF***: Net carbon fluxes due to land cover change
>   - ***GTI***: GHG growth rate adjusted by emissions intensity
>   - ***GTP***: GHG growth rate adjusted by per capita emissions
>   - ***GHN***: Projected emissions in 2050
>   - ***CBP***: Projected cumulative emissions to 2050 relative to carbon budget
>
>
> **Dataset URL:** https://epi.yale.edu/downloads/epi2024results.csv
> 
> **Dataset File Hash(es):** 50f3b9020aed3aa27d118498b31f3e8b

#### 2. Interpretable Records

>**Record 1:**
> - **Raw Data**:
>  
>  
>  | code | iso | country | EPI.old | EPI.new | ECO.old | ECO.new | BDH.old | BDH.new | MKP.old | MKP.new | MHP.old | MHP.new | MPE.old | MPE.new | PAR.old | PAR.new | SPI.old | SPI.new | TBN.old | TBN.new | TKP.old | TKP.new | PAE.old | PAE.new | PHL.old | PHL.new | RLI.old | RLI.new | SHI.old | SHI.new | BER.old | BER.new | ECS.old | ECS.new | PFL.old | PFL.new | IFL.old | IFL.new | FCL.old | FCL.new | TCG.old | TCG.new | FLI.old | FLI.new | FSH.old | FSH.new | FSS.old | FSS.new | FCD.old | FCD.new | BTZ.old | BTZ.new | BTO.old | BTO.new | RMS.old | RMS.new | APO.old | APO.new | OEB.old | OEB.new | OEC.old | OEC.new | NXA.old | NXA.new | SDA.old | SDA.new | AGR.old | AGR.new | SNM.old | SNM.new | PSU.old | PSU.new | PRS.old | PRS.new | RCY.old | RCY.new | WRS.old | WRS.new | WWG.old | WWG.new | WWC.old | WWC.new | WWT.old | WWT.new | WWR.old | WWR.new | HLT.old | HLT.new | AIR.old | AIR.new | HPE.old | HPE.new | HFD.old | HFD.new | OZD.old | OZD.new | NOD.old | NOD.new | SOE.old | SOE.new | COE.old | COE.new | VOE.old | VOE.new | H2O.old | H2O.new | USD.old | USD.new | UWD.old | UWD.new | HMT.old | HMT.new | LED.old | LED.new | WMG.old | WMG.new | WPC.old | WPC.new | SMW.old | SMW.new | WRR.old | WRR.new | PCC.old | PCC.new | CCH.old | CCH.new | CDA.old | CDA.new | CDF.old | CDF.new | CHA.old | CHA.new | FGA.old | FGA.new | NDA.old | NDA.new | BCA.old | BCA.new | LUF.old | LUF.new | GTI.old | GTI.new | GTP.old | GTP.new | GHN.old | GHN.new | CBP.old | CBP.new |
>  |------|-----|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
>  | 152  | CHL | Chile   | 46.6    | 49.6    | 53.7    | 57.4    | 39.7    | 42.5    | 13.4    | 28.4    | 17.4    | 37.8    | 100     | 87.7    | 34.6    | 34.6    | 30.4    | 33.6    | 48.7    | 54.9    | 60.5    | 63.9    | 64.8    | 64.8    | 95.6    | 95.6    | 30      | 20.6    | 69.9    | 46.8    | 100     | 100     | 50.6    | 70.3    | NA      | NA      | 46.1    | 83.6    | 51.9    | 62.1    | 49.6    | 49.6    | 73.5    | 73.5    | 82.7    | 81.9    | 31      | 22.7    | 85.5    | 88.8    | 100     | 100     | 96.5    | 94.3    | 57.7    | 55.2    | 75.7    | 80.9    | 74.2    | 71.1    | 93.3    | 86.6    | 32.2    | 63.4    | 100     | 99.1    | 69.1    | 66.3    | 39.7    | 45.4    | 30.7    | 29.5    | 60.6    | 43.2    | 91      | 100     | 85.4    | 85.5    | 0       | 0       | 99.9    | 99.9    | 99.9    | 100     | 84      | 84      | 45.3    | 45.1    | 31.8    | 29.2    | 21      | 8.3     | 40.4    | 48      | 55.6    | 62.3    | 12      | 12.6    | 0       | 0       | 25.2    | 22.4    | 25.8    | 27.5    | 75.4    | 80.8    | 70.5    | 78.5    | 75.9    | 82.3    | 92.2    | 98.1    | 90.8    | 98.1    | 31.9    | 31      | 34      | 31.3    | 90.7    | 91.3    | 0.4     | 0.5     | 37      | 41.5    | 37      | 41.5    | 36.5    | 46.7    | 21.8    | 37.5    | 55.5    | 49.5    | 0       | 0       | 45.3    | 56      | 14      | 66.6    | 49.3    | 49.5    | 34.3    | 42.3    | 30.2    | 38.1    | 12.3    | 13.5    | 54.8    | 54.8    |
>
> - **Interpretation**: This record displays current versus baseline indicator scores in the EPI (2024) for the country of Chile. With a score of 49.6, Chile ranks 64th in this year's EPI ranking. This can be confirmed by [downloading the PDF report here](https://epi.yale.edu/downloads/2024epireport.pdf).
>
> 
>**Record 2**
>  - **Raw Data:**
> 
>  | code | iso | country                  | EPI.old | EPI.new | ECO.old | ECO.new | BDH.old | BDH.new | MKP.old | MKP.new | MHP.old | MHP.new | MPE.old | MPE.new | PAR.old | PAR.new | SPI.old | SPI.new | TBN.old | TBN.new | TKP.old | TKP.new | PAE.old | PAE.new | PHL.old | PHL.new | RLI.old | RLI.new | SHI.old | SHI.new | BER.old | BER.new | ECS.old | ECS.new | PFL.old | PFL.new | IFL.old | IFL.new | FCL.old | FCL.new | TCG.old | TCG.new | FLI.old | FLI.new | FSH.old | FSH.new | FSS.old | FSS.new | FCD.old | FCD.new | BTZ.old | BTZ.new | BTO.old | BTO.new | RMS.old | RMS.new | APO.old | APO.new | OEB.old | OEB.new | OEC.old | OEC.new | NXA.old | NXA.new | SDA.old | SDA.new | AGR.old | AGR.new | SNM.old | SNM.new | PSU.old | PSU.new | PRS.old | PRS.new | RCY.old | RCY.new | WRS.old | WRS.new | WWG.old | WWG.new | WWC.old | WWC.new | WWT.old | WWT.new | WWR.old | WWR.new | HLT.old | HLT.new | AIR.old | AIR.new | HPE.old | HPE.new | HFD.old | HFD.new | OZD.old | OZD.new | NOD.old | NOD.new | SOE.old | SOE.new | COE.old | COE.new | VOE.old | VOE.new | H2O.old | H2O.new | USD.old | USD.new | UWD.old | UWD.new | HMT.old | HMT.new | LED.old | LED.new | WMG.old | WMG.new | WPC.old | WPC.new | SMW.old | SMW.new | WRR.old | WRR.new | PCC.old | PCC.new | CCH.old | CCH.new | CDA.old | CDA.new | CDF.old | CDF.new | CHA.old | CHA.new | FGA.old | FGA.new | NDA.old | NDA.new | BCA.old | BCA.new | LUF.old | LUF.new | GTI.old | GTI.new | GTP.old | GTP.new | GHN.old | GHN.new | CBP.old | CBP.new |
>  |------|-----|--------------------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
>  | 840  | USA | United States of America | 57      | 57.2    | 53.5    | 53.5    | 41.3    | 40.7    | 58.7    | 58.7    | 46.1    | 46.1    | 77.9    | 76.9    | 14.6    | 14.6    | 27      | 39.9    | 37.5    | 37.8    | 36.9    | 36.9    | 71.5    | 71.5    | 89.4    | 89.4    | 47.7    | 45.5    | 61.1    | 20.8    | 31.1    | 30.5    | 53.6    | 51.9    | 92.2    | 87.6    | 24      | 18.1    | 50.3    | 49.9    | 43.9    | 43.9    | 66.5    | 66.5    | 42.5    | 46.5    | 38.4    | 38      | 37      | 45.1    | 36      | 46.4    | 41      | 50.6    | 51.5    | 49.1    | 89      | 89.1    | 28.6    | 31.7    | 35.5    | 36.9    | 100     | 100     | 100     | 100     | 78.5    | 83      | 68      | 76.6    | 62.8    | 80.7    | 56.9    | 57.8    | 77.6    | 100     | 63.9    | 63.9    | 5.6     | 5.6     | 78.2    | 78.2    | 67.7    | 67.7    | 67.7    | 67.7    | 69.7    | 72.3    | 62.9    | 65.8    | 56.3    | 61.5    | 88.9    | 91.6    | 27.1    | 33.8    | 1.9     | 7       | 29.1    | 35.7    | 53.5    | 60.3    | 38.5    | 35.5    | 94.1    | 96.2    | 84.6    | 90.5    | 98.1    | 100     | 79.1    | 82.5    | 78.3    | 82.5    | 45.3    | 41.7    | 15.6    | 13.3    | 100     | 93.9    | 47.7    | 44      | 51.6    | 50.1    | 51.6    | 50.1    | 60.8    | 57.7    | 37.4    | 33.3    | 60.7    | 50.5    | 38      | 46.7    | 53.8    | 55.2    | 100     | 100     | 50.5    | 50.2    | 52.6    | 52.5    | 35.3    | 35.5    | 0       | 0       | 50.1    | 50.1    | 
> 
> - **Interpretation**: This record displays current versus baseline indicator scores in the EPI (2024) for the United States of America. With a score of 57.2, the U.S. ranks 35th in this year's EPI ranking. This can be confirmed by [downloading the PDF report here](https://epi.yale.edu/downloads/2024epireport.pdf).

### **Data File 3**: [Population, total.](data_original/API_SP.POP.TOTL_DS2_en_csv_v2_31753.csv)

#### 1. Basic Questions

> **Dataset Author(s):** World Bank Group
>
> 
> **Dataset Construction Date:** Last updated on 09/19/2024.
> 
> 
> **Dataset Record Count:** 266
> 
>
> **Dataset Field Meanings:**
>   - ***Country Code***: Country ISO3 code.
>   - ***Indicator Name***: World Bank's indicator name, which is 'Population, total' in this data set.
>   - ***Indicator Code***: World Bank's indicator code, which is 'SP.POP.TOTL' in this data set.
>   - ***Columns '1960' to '2023'***: Columns labeled with years ranging from 1960 until 2023 containing total population by country. Total population is based on the de facto definition of population, which counts all residents regardless of legal status or citizenship. The values shown are midyear estimates.
>
>
> **Dataset URL:** https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv
> 
> **Dataset File Hash(es):** bd6f43cc84e4d83208b6ad5e79247ce0

#### 2. Interpretable Records

>**Record 1:**
> - **Raw Data**:
>  
>
> | Country Name | Country Code | Indicator Name    | Indicator Code | 1960 | 1961  | 1962  | 1963  | 1964  | 1965  | 1966  | 1967  | 1968  | 1969  | 1970  | 1971  | 1972  | 1973  | 1974  | 1975  | 1976  | 1977  | 1978  | 1979  | 1980  | 1981  | 1982  | 1983  | 1984  | 1985  | 1986  | 1987  | 1988  | 1989  | 1990  | 1991  | 1992  | 1993  | 1994  | 1995  | 1996  | 1997  | 1998  | 1999  | 2000  | 2001  | 2002  | 2003  | 2004  | 2005  | 2006  | 2007  | 2008  | 2009  | 2010  | 2011  | 2012  | 2013  | 2014  | 2015  | 2016  | 2017  | 2018  | 2019  | 2020  | 2021  | 2022  | 2023  |
> |--------------|--------------|-------------------|----------------|------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
> | Andorra      | AND          | Population, total | SP.POP.TOTL    | 9443 | 10216 | 11014 | 11839 | 12690 | 13563 | 14546 | 15745 | 17079 | 18449 | 19860 | 21322 | 22832 | 24393 | 26003 | 27640 | 29294 | 30949 | 32574 | 34142 | 35611 | 36987 | 38598 | 40432 | 42181 | 43809 | 45605 | 47635 | 49654 | 51639 | 53569 | 55434 | 57283 | 59156 | 61037 | 62928 | 64147 | 64682 | 65186 | 65655 | 66097 | 67820 | 70849 | 73907 | 76933 | 79826 | 80221 | 78168 | 76055 | 73852 | 71519 | 70567 | 71013 | 71367 | 71621 | 71746 | 72540 | 73837 | 75013 | 76343 | 77700 | 79034 | 79824 | 80088 |
>
> - **Interpretation**: This record displays the country of Andorra's population within the years 1960 - 2023. Considering that it is a very small nation in between Spain and France, it displays very reasonable numbers.
>
> 
>**Record 2**
>  - **Raw Data:**
> 
> | Country Name              | Country Code | Indicator Name    | Indicator Code | 1960      | 1961      | 1962      | 1963      | 1964      | 1965      | 1966      | 1967      | 1968      | 1969      | 1970      | 1971      | 1972      | 1973      | 1974      | 1975      | 1976      | 1977      | 1978      | 1979      | 1980      | 1981      | 1982      | 1983      | 1984      | 1985      | 1986      | 1987      | 1988      | 1989      | 1990      | 1991      | 1992      | 1993      | 1994      | 1995      | 1996      | 1997      | 1998      | 1999      | 2000      | 2001      | 2002      | 2003      | 2004      | 2005      | 2006      | 2007      | 2008      | 2009      | 2010      | 2011      | 2012      | 2013      | 2014      | 2015      | 2016      | 2017      | 2018      | 2019      | 2020      | 2021      | 2022      | 2023      |
> |---------------------------|--------------|-------------------|----------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
> | Latin America & Caribbean | LCN          | Population, total | SP.POP.TOTL    | 219142626 | 225304612 | 231638540 | 238127927 | 244742056 | 251458185 | 258225265 | 265030167 | 271885703 | 278797542 | 285779012 | 292852914 | 300036114 | 307345195 | 314759757 | 322249100 | 329807630 | 337531513 | 345450768 | 353452209 | 361451180 | 369321289 | 377189872 | 385189898 | 393227113 | 401251731 | 409259052 | 417266298 | 425320442 | 433393694 | 441597528 | 449847635 | 458008075 | 466139063 | 474258790 | 482331291 | 490304061 | 498199382 | 506010566 | 513714410 | 521281149 | 528688278 | 535935546 | 542976557 | 549897638 | 556739532 | 563424119 | 569972223 | 576386180 | 582738079 | 588873862 | 595510008 | 602139396 | 608642242 | 615046755 | 621390109 | 627667493 | 633795231 | 639626265 | 645293844 | 650533026 | 654978670 | 659306928 | 664155299 |
> 
> - **Interpretation**: This record displays the total population of the subregion of Latin American & the Caribbean. 

## Background Domain Knowledge
TODO

## Dataset Generality
TODO

## Data Transformations
### Transformation N
**Description:** TODO

**Soundness Justification:** TODO

(duplicate above as many times as needed; remove this line when done)


## Visualizations
### Visual N
**Analysis:** TODO

(duplicate above as many times as needed; remove this line when done)