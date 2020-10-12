import pandas as pd

import bokeh.plotting as bp
import bokeh.models as bm
import bokeh.layouts as blay
import bokeh.palettes as bpal

class CovidPlotter(object):

	def __init__(self, metric):
		self.metric = metric
		self.df = pd.read_csv('data/Covid19CountyStatisticsHPSCIreland.csv')
		self.df['TimeStamp'] = pd.to_datetime(self.df['TimeStamp'])
		self.counties = self.df.groupby('CountyName')
		self.dailies = self.identify_daily_figures(self.counties, 7)
		self.daily_counties = self.dailies.groupby('CountyName')
		
		self.create_plot(self.daily_counties)

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
		dailies = pd.DataFrame(holder, columns=["TimeStamp", "CountyName", "ConfirmedCovidCases"])
		if roll > 0:
			rolling = dailies['ConfirmedCovidCases'].rolling(roll).mean()
			dailies['ConfirmedCovidCases'] = rolling

		return dailies


	def create_plot(self, counties):
		colors = bpal.Category20[14]
		dash = ['solid', 'dashed']
		i = 0
		j = 0
		filename = "".join(["plots/", self.metric, ".html"])
		bp.output_file(filename, title="Covid Cases")
		p = bp.figure(title="Covid Cases",
			x_axis_type="datetime",
			width=1024,
			height=768)
		for a, b in counties:
			if a == "Dublin":
				continue
			temp = b.copy()
			temp['StrDate'] = temp['TimeStamp'].apply(lambda x: x.strftime("%a, %b %d"))
			source = bp.ColumnDataSource(temp)
			p.line("TimeStamp",
				self.metric,
				source=source,
				line_width=3,
				line_color=colors[i],
				line_dash=dash[j],
				legend_label=a)
			if i < 12:
				i += 1
			else:
				i = 0
				j += 1

		p.legend.click_policy="hide"
		p.legend.label_text_font_size = '12px'
		p.legend.label_text_font = 'Arial'
		p.legend.location = "top_left" #(15, 700)

		tools = bm.HoverTool(tooltips=[("Date","@StrDate"),
										("County","@CountyName"),
										("Cases","@ConfirmedCovidCases")])
		p.add_tools(tools)
		bp.show(p)

if __name__ == "__main__":
	x = CovidPlotter('ConfirmedCovidCases')