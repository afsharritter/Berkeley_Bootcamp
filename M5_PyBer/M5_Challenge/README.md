# Module 5: PyBer with MatPlotLib

## Overview of the Analysis

In this challenge, a python-based ridesharing company, PyBer, is requesting an analysis of data for 2,375 trips and 120 cities using Python Pandas and MatPlotLib.

## Results

This project aims to identify and visualize the effect of city type (rural, suburban, or urban) on ridership.

### Summary DataFrame

The data was first summarized to show Rider, Driver, and Fare specifics for Rural, Suburban, and Urban city types. See Table 1

![Table 1](/M5_Challenge/Analysis/Table1_PyBer_Summary_DataFrame.png "Table 1: Summary DataFrame")

Urban city types had the greatest number of rides and drivers (1,625 and 2,405, respectively). Urban cities had the lowest fares, averaging $24.53 per ride and $16.57 per driver. Given the volume of trips taken, urban cities had the highest revenue among city types, with fares totaling $39,854.38. 

Rural areas had the lowest ridership and driver counts (totaling 125 and 78, respectively). In contrast, Rural areas had the highest fares, averaging $34.62 per ride and $55.49 per driver. This low volume of trips resulted in the lowest revenue among city types, with fares totaling $4,327.93. 

Suburban areas fell between urban and rural city types in all parameters noted above. 

### Multi-Line Chart

The ridesharing data was then grouped to create a pivot chart that listed fare amounts for each day based on the trip's city type, which was then visualized in the graph in Figure 1. 

![Figure 1](/M5_Challenge/Analysis/Figure1_PyBer_Fare_Summary.png "Figure 1: PyBer Fare Summary")

From January to April 2019, Urban rides had the highest total weekly fares. All city types saw a surge in total fares during the week ending on February 24th. This week saw the highest gross fares for Suburban areas. Urban city types had the highest fares during the week ending on March 10th, while Rural areas saw their peak during the week ending on April 7th. 

## Data Summary and Recommendations

The graph in figure 1 shows a discrepancy between major holidays and total fares, indicating that PyBer might need to implement a "Surge" system that increases a rider's fare during peak travel times. For example, the week of January 6th, which includes the New Year holiday, has relatively low total fare amounts across all city types. One would expect that ridership on holidays would increase compared to other days of the year. Similarly, Valentine's Day (during the week ending on February 17th) and St. Patricks Day (the week ending on March 17th) did not have high total fare amounts compared to other weeks in the year. By adding a Surge-Pricing, PyBer could significantly increase its revenue during peak travel times. 

PyBer can also consider increasing fares across-the-board in Urban areas since the demand for ridesharing apps is significantly increased. Small fare increases would not likely affect ridership, given the challenges and competitiveness of the rideshare market in urban areas.  

PyBer might also want to increase location-based advertising, perks, or discounts in Rural areas to increase visibility and ridership. The high average fares in rural areas might be a barrier for residents of those communities, who may not have the disposable income to spend on ridesharing apps. If balanced properly, a decrease in average fares for Rural residents might increase ridership enough to improve revenue in those regions.  
