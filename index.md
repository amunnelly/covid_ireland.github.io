# Covid-19 and Ireland

_Latest data point: January 20, 2021._

## Graphs

The raw data is taken from [the official government source](https://covid19ireland-geohive.hub.arcgis.com/datasets/d9be85b30d7748b5b7c09450b8aede63_0).

### Confirmed Covid Cases

* [Cumulative Cases Nationally](/covid_ireland/plots/national_confirmedcovidcases.html). Confirmed cases per day, seven-day-average of confirmed cases per day.


* [Cumulative Cases by County](/covid_ireland/plots/confirmedcovidcases_cumulative.html). The data broken down by day and by county.

* [Cumulative Cases by County, excluding Dublin](/covid_ireland/plots/confirmedcovidcases_cumulative_excluding_dublin.html). Because Dublin is so much bigger than any other county, the detail of the other twenty-five counties gets lost. This the data above minus Dublin.

* [Seven-Day Average of Cases by County](/covid_ireland/plots/confirmedcovidcases_seven_day_average.html). Again, from the official data, with a seven-day-average replacing the cumulative count. A seven-day-average because a daily count makes for a very noisy graph.

* [Seven-Day Average of Cases by County, excluding Dublin](/covid_ireland/plots/confirmedcovidcases_seven_day_average_excluding_dublin.html). Again, Dublin excluded to make the other counties' data clearer.

### Cases per Population Unit

The official data's preferred rate of change metric is `Population Proportion by County`, which is fine as far as it goes. However, neither population nor area is even distributed across the country, and this makes it a little less than satisfactory.

* [Population Proportion of Cases by County, cumulative](/covid_ireland/plots/populationproportioncovidcases_cumulative.html) is the graph of this offical metric.

* In an effort to even things out, I divided the county population by the county area as recorded in [Wikipedia](https://en.wikipedia.org/wiki/List_of_Irish_counties_by_area), and then expressed the number of cases divided by this population per square kilometre as `Case Density`. It's fine as far as it goes, but it doesn't really tell us that much more than the earlier graph. I include it for the sake of it, as much as anything. [Case Density](/covid_ireland/plots/casedensity_cumulative.html)

## Interacting with the Graphs

* Click counties on and off by clicking on the county name in the legend
* Hover over a line to see the county, date, and number of cases at that date.

## Usefulness of the Data
The data is a record of what happened over the past six months broken down by county. It cannot tell us anything about the next six months, or year, or however long this is going to take. Sadly, the difficulties experienced in testing and tracing make that more or less impossible in the Irish case.
