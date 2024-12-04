#### SER494: Project Experimentation
#### Title: Renewable Energy and Environmental Progress
#### Author: Gonzalo Allendes
#### Date: November 23rd, 2024

## Explainable Records
### Record 1
**Raw Data:**

| Country | Population    | Public Flows per Capita (USD) | Renewable Energy Share of Electricity Production (%) | SDG 7b1 RE capacity per capita (W/inhabitant) | Total Non-Renewable Generation (GWh) | Total Renewable Generation (GWh) | EPI.new |
|---------|---------------|-------------------------------|------------------------------------------------------|-----------------------------------------------|--------------------------------------|----------------------------------|---------|
| Chile   | 17,309,750.61 | 10.6290                       | 47.01                                                | 477.2715                                      | 35,341.87                            | 30,839.43                        | 49.6    |

**Prediction Explanation:**

The model predicted an EPI of 50.86, which is slightly higher than the actual value of 49.6. The error of 
1.2581 is small and shows that the model is effectively taking into account the different features 
to predict a reasonable output with an error of 2.54%. In terms of the domain, Chile has a balanced energy 
mix with a growing emphasis on renewable energy sources. Its investment in public flows per capita supports
sustainability efforts. However, the country relies on non-renewable energy, which slightly affects its EPI 
score. The model's prediction considered those factors and placed Chile higher than our calculated
median of 47.3, available in data_processing\summary.txt. 

### Record 2
**Raw Data:**

| Country       | Population     | Public Flows per Capita (USD) | Renewable Energy Share of Electricity Production (%) | SDG 7b1 RE capacity per capita (W/inhabitant) | Total Non-Renewable Generation (GWh) | Total Renewable Generation (GWh) | EPI.new |
|---------------|----------------|-------------------------------|------------------------------------------------------|-----------------------------------------------|--------------------------------------|----------------------------------|---------|
| United States | 310,167,213.70 | 0.1796                        | 12.40                                                | 537.4178                                      | 3,740,149.22                         | 533,483.83                       | 57.2    |

**Prediction Explanation:**

The model predicted an EPI of 55.5302, which is slightly lower than the actual value of 57.2. The residual of
1.6698 represents a 2.92% error. In terms of the domain, The United States of America has a large population 
and high energy consumption, so it faces challenges in balancing renewable and non-renewable sources. 
Although there is significant renewable capacity per capita, the country still depends heavily on non-renewable
generation. This lowers its overall environmental performance. The model's predicted EPI is reasonable given
the contrast between the country's high performance in renewable energies versus its reliance on non-renewable. 

## Interesting Features
### Feature A
**Feature:** Renewable Energy Capacity per Capita in Watts per Inhabitant (2000 - 2022 average)

**Justification:** Renewable Energy Capacity per Capita is a key indicator of a countr's investment
and infrastructure in renewable energy. The higher the capacity, the more energy can be generated
from renewable sources on a per-person basis. This feature could strongly impact the model's prediction
of EPI scores because countries that prioritize renewable energy capacity are expected to have
better environmental performance. Therefore, an increase in this factor is expected to positively
influence a country's EPI score.

### Feature B
**Feature:** Public Flows in Renewable Energy per Capita in USD (2000 - 2022 average)

**Justification:** Public Flows in Renewable Energy per Capita in USD reflects government investments
and subsidies in renewable energy infrastructure to promote sustainable energy development. This generally
represents efforts towards transitioning to cleaner energy sources. The need for those investments might
indicate the country is starting from a lower baseline in terms of renewable infrastructure. Therefore,
while public flows can drive long term improvements in environmental performance, they may also
be an indicator of environmental issues that the country is attempting to address, and thus could have
a slight negative trend in predicting the Environmental Performance Index (EPI) scores.

## Experiments 
### Varying A
**Prediction Trend Seen:** Feature A was increased in increments of 66 within the range [377.27, 577.27],
which was chosen to center the variations around Chile's renewable energy capacity of 477.2715 Watts per inhabitant. 
The model predicted the EPI scores [51.7250, 52.1737, 52.8804, 53.7235] in that order. While individual predictions
may vary in each execution because of the stochastic nature of the algorithm, this positive correlation consistently
holds true. Therefore, when varying Feature A, there is a clear upward trend in the predicted EPI values. 
As Feature A increases, the predicted EPI also increases, indicating that higher renewable energy capacity 
per capita leads to a better Environmental Performance Index (EPI) score. 

### Varying B
**Prediction Trend Seen:** Feature B was increased in increments of 1.33 within the range [8.63, 12.63],
selected to center the variations around Chile's public flows in renewable energy per capita of 10.629 USD.
The model predicted the EPI scores [52.1911, 52.3844, 52.5764, 52.7684], suggesting a weak positive
correlation. However, in another run, the model's predictions [51.7154, 51.4690, 51.2393, 51.0095] suggested
a weak negative correlation instead. Unlike Feature A, the direction of the correlation does not consistently 
hold true across multiple executions. These results suggest that while Feature B might influence the EPI, 
the correlation is consistently weak and lacks a clear direction, whether positive or negative—similar
to observing near-zero correlations in a correlation matrix. 

### Varying A and B together
**Prediction Trend Seen:** When both Feature A (SDG 7b1 RE capacity per capita) and Feature B (Public Flows per Capita)
were increased together in the same direction, the predicted EPI scores showed a consistently positive trend. 
With Feature A increasing in increments of 66 W/inhabitant and Feature B increasing in increments of 1.33 USD, 
the model predicted the scores [52.4805, 53.3763, 54.6374, 56.1963]. This behavior aligns with the strong 
positive correlation observed for Feature A, which consistently drives EPI scores upward, while the weak influence 
of Feature B contributes minimally. Even when it has a negative coefficient in certain model executions,
it does not detract from the overall upward trend.

### Varying A and B inversely
**Prediction Trend Seen:** When both Feature A (SDG 7b1 RE capacity per capita) and Feature B (Public Flows per Capita)
were varied inversely in opposite directions, the predicted EPI scores maintained a positive overall trend. 
With Feature A increasing in increments of 66 W/inhabitant and Feature B increasing in increments of 1.33 USD, 
the model predicted the scores [52.4805, 53.1841, 54.2779, 55.6568]. This indicates that the strong positive
correlation of Feature A continues to dominate, driving the upward trend. The opposing effect of 
Feature B, whose influence is weaker and more variable, may reduce or improve the rate of EPI improvement,
depending on the sign of its assigned coefficient. In summary, despite the inverse variation of both features,
the dominant effect of Feature A leads to an overall increase in the predicted EPI, while Feature B's weaker
and more inconsistent impact may cause minor fluctuations in the rate of improvement.