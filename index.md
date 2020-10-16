## Graphs

There are five graphs in the dataset. They are:
1. [Cumulative Cases by County](/covid_ireland/plots/confirmedcovidcases_cumulative.html). This is the raw data from [the official government source](https://covid19ireland-geohive.hub.arcgis.com/datasets/d9be85b30d7748b5b7c09450b8aede63_0). The most recent date is October 5th, 2020.

2. [Cumulative Cases by County, excluding Dublin](/covid_ireland/plots/confirmedcovidcases_cumulative_excluding_dublin.html). Because Dublin is so much bigger than any other county, the detail of the other twenty-five counties gets lost. This the data above minus Dublin.

3. [Seven-Day Average of Cases by County](/covid_ireland/plots/confirmedcovidcases_seven_day_average.html). Again, from the official data, with a seven-day-average replacing the cumulative count. A seven-day-average because a daily count is very noisy.

4. [Seven-Day Average of Cases by County, excluding Dublin](/covid_ireland/plots/confirmedcovidcases_seven_day_average_excluding_dublin.html). Again, Dublin excluded to make the other counties' data clearer.

5. [Population Proportion of Cases by County](/covid_ireland/plots/populationproportioncovidcases_cumulative.html).

### Interacting with the Graphs

* Click counties on and off by clicking on the county name in the legend
* Hover over a line to see the county, date, and value (cumulative cases/seven-day-average, as appropriate)

### A Note on Population Proportion of Cases

Cavan has the highest `PopulationProportionCovidCases` with 1,526. It's hard to say that particularly matters - different counties have different populations and different sizes. These aren't like-for-like comparisons.

What is may be interesting, however, is the way the graph shows different growth rates for different counties.

Most counties' growth rates show a fast rise in March/April, levelling off from April through to August, and then rising again in September. Some counties don't fit the pattern. Kildare's rate started increasing from the end of July, and hasn't really stopped. Offaly jumped for the first fortnight in August and then settled again. Donegal started rising before Cavan and Monaghan.

These differences may or may not be significant. All we can say from this data is that they happened. Why they happened or how particular trends will continue into the future is impossible to determine from this data.