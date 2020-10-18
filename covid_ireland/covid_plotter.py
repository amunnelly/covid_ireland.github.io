import pandas as pd

import bokeh.plotting as bp
import bokeh.models as bm
import bokeh.layouts as blay
import bokeh.palettes as bpal
import json


class CovidPlotter(object):

	def __init__(self, metric, cumulative, dublin, title):
		self.metric = metric
		self.cumulative = cumulative
		self.dublin = dublin
		self.title = title
		self.df = pd.read_csv('data/Covid19CountyStatisticsHPSCIreland.csv')
		with open('data/counties.json') as f:
			self.counties = json.load(f)
		self.df['TimeStamp'] = pd.to_datetime(self.df['TimeStamp'])
		self.find_case_density()
		self.county_group = self.df.groupby('CountyName')
		self.dailies = self.identify_daily_figures(self.county_group, 7)
		self.daily_counties = self.dailies.groupby('CountyName')
		
		if cumulative:
			self.create_plot(self.county_group)
		else:
			self.create_plot(self.daily_counties)

	def find_case_density(self):
		self.df['Area'] = self.df['CountyName'].apply(lambda x: self.counties[x]['area'])
		self.df['PopPerKmSquared'] = self.df['PopulationCensus16'] / self.df['Area']
		self.df['CaseDensity'] = self.df['ConfirmedCovidCases'] / self.df['PopPerKmSquared']


	def identify_daily_figures(self, counties, roll=0):
		"""
		
		args:
			counties (pd groupby object)
		"""
		holder = []
		for a, b in counties:
			temp = b.copy()
			temp.sort_values('TimeStamp', inplace=True)
			for i in range(1, len(temp)):
				date_ = temp['TimeStamp'].iloc[i]
				current = temp['ConfirmedCovidCases'].iloc[i]
				prior = temp['ConfirmedCovidCases'].iloc[i-1]
				cases = current - prior
				holder.append([date_, a, cases])
		dailies = pd.DataFrame(holder, columns=["TimeStamp", "CountyName", self.metric])
		if roll > 0:
			rolling = dailies[self.metric].rolling(roll).mean()
			dailies[self.metric] = rolling
		return dailies


	def create_filename(self):
		count_ = "_seven_day_average"
		dublin = "_excluding_dublin"
		if self.cumulative:
			count_ = "_cumulative"
		if self.dublin:
			dublin = ""
		filename = "".join([self.metric.lower(), count_, dublin])
		return "".join(["plots/", filename, ".html"])
		


	def create_plot(self, counties):
		filename = self.create_filename()
		bp.output_file(filename, title=self.title)
		p = bp.figure(title=self.title,
			x_axis_type="datetime",
			width=1200,
			height=700)
		legend_items = []
		for a, b in counties:
			if self.dublin==False and a =="Dublin":
				continue
			temp = b.copy()
			temp['StrDate'] = temp['TimeStamp'].apply(lambda x: x.strftime("%a, %b %d"))
			source = bp.ColumnDataSource(temp)
			leg = p.line("TimeStamp",
				self.metric,
				source=source,
				line_width=2,
				line_color=self.counties[a]['color'],
				line_dash=self.counties[a]['dash'])
			legend_items.append((a, [leg]))


		legend = bm.Legend(items=legend_items,
					location='top_right',
					orientation='vertical',
					border_line_color="black")

		p.add_layout(legend, 'right')

		p.legend.click_policy="hide"
		p.legend.label_text_font_size = '12px'
		p.legend.label_text_font = 'Helvetica'
		p.legend.location = "top_left"
		p.legend.background_fill_color = 'slategray'
		p.legend.background_fill_alpha = 0.5

		tools = bm.HoverTool(tooltips=[("Date","@StrDate"),
										("County","@CountyName"),
										("Cases","@ConfirmedCovidCases")])
		p.add_tools(tools)

		p.title.text_font = "Helvetica"
		p.title.text_font_size = "18px"

		p.background_fill_color = 'slategray'
		p.background_fill_alpha = 0.5

		bp.show(p)

if __name__ == "__main__":
	x = CovidPlotter('ConfirmedCovidCases',
		True,
		True,
		"Confirmed Cases by County, Cumulative")
	x = CovidPlotter('ConfirmedCovidCases',
		True,
		False,
		"Confirmed Cases by County, Cumulative, Excluding Dublin")
	x = CovidPlotter('ConfirmedCovidCases',
		False,
		True,
		"Confirmed Cases by County, Seven-Day-Average")
	x = CovidPlotter('ConfirmedCovidCases',
		False,
		False,
		"Confirmed Cases by County, Seven-Day-Average, Excluding Dublin")
	x = CovidPlotter('PopulationProportionCovidCases',
		True,
		True,
		"Population Proportion per 100,000, Cumulative")
	x = CovidPlotter('CaseDensity',
		True,
		True,
		"Case Density per County per Square Kilometre, Cumulative")
	x.df.to_csv('data/munged/df.csv')
