##### 2021 MCM/ICM E

## FSMM: The Analysis of Food System Re-optimization


## Summary

The unstability of global food system have aroused growing attention worldwide. Althrough
there is sufficient food produced to feed every person, many people in the world are suffering
from hunger. Moreover, the current food system is harmful to the environment. As our
global population continues to rise, the ability to produce more food while sustaining, and even
improving, the health of our environment counts.

The FSMM(Food System Monitoring Model) provides score rank using entropy weight and
subjective weight to evaluate the current state of the food system for most countries in the world.
It contains 9 individual features to measure multiple aspects, including efficiency, profitability,
sustainability and equity.

Considering the future trend of the food system, we apply Gray Forecast Model to forecast
the next 5 years of the development of the food system to figure out the time for each country
to change into equity and sustainability.

To find out the relation between external factors and food system, The FSMM uses Boosting
Regression Model to find the correlation between the scores and 10 indicators which represent
the influences of energy use, government, agriculture, social factors and population ratio. The
FSMM fits the data from 178 countries from 2000 to 2019. After simulating and adjusting the
parameters to decrease the loss of the model, we gets the importance rate of each indicator.

We find the indicators whose importance rate change significantly when the food system
is optimized for equity and sustainability. And we use these indicatos as dependent variable
and apply Linear Regression to fit by using the yields of the wheat, meat and vegetables as
independent variable. By doing this, We find out the direct impact of re-optimization on the
food system.

We finally get the importance rate and the coefficient of two regression model and analyze
the specific influence of various factors on the food system and compare the differences between
the influence on developing and developed countries.

After the overall analysis of the influence on developed and developing countries, we pick
some specific developing and developed countries to analyze and discuss the scalability and
adaptability of the model.

**Keywords** : Boosting Regression, Linear Regression, FSMM, Entropy Weight, data mining,
supervised learning, energy use.


## Contents


- 1 Introduction
- 2 Data Processing
   - 2.1 Data Sources
   - 2.2 Data Cleaning
      - 2.2.1 Missing Data and Outliers
      - 2.2.2 Data Decomposition
- 3 Assumptions and Justification
- 4 Notations
- 5 Equity and Sustainability Oriented Model
   - 5.1 Entropy Weights
   - 5.2 Gray Forecast Model
   - 5.3 Taking Systems into Effect
- 6 Analysing Benefits and Costs
   - 6.1 Boosting Regression
   - 6.2 Parameter Adjustment.
   - 6.3 Result of Regression
   - 6.4 Internal Impact
   - 6.5 Further Analysis of Different Countries
- 7 Further Extension and Case Study
   - 7.1 FSMM Extension for Developed and Developing Countries
   - 7.2 Case Study:China and the United States
- 8 Sensitivity Analysis
- 9 Strength and Weakness
   - 9.1 Strength
   - 9.2 Weakness
- 10 Conclusion
