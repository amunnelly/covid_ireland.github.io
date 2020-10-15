# Plotting Irish Covid Cases

## Data

The data is sourced from [the official government source](https://covid19ireland-geohive.hub.arcgis.com/datasets/d9be85b30d7748b5b7c09450b8aede63_0).

## `covid_plotter.py`

The program reads the data and creates two sets of data. The first has the data as is, with cumulative counts of cases broken by down county. The second set has individual counts of cases by day by county, averaged over seven days.

### Graphs
From these two data sets, five sets of graphs are created:
1. Cumulative cases by day by county, including Dublin
2. Cumulative cases by day by county, excluding Dublin
3. Seven-day-average count of cases by day by county, including Dublin
4. Seven-day-average count of cases by day by county, excluding Dublin
5. The official "Population Proportion of cases per 100,000 people" statistic.