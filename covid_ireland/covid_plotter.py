import pandas as pd

import bokeh.plotting as bp
import bokeh.models as bm
import bokeh.layouts as blay
import bokeh.palettes as bpal
import json

class CovidPlotter(object):

	def __init__(self, metric, cumulative, dublin):
		self.metric = metric
		self.cumulative = cumulative
		self.dublin = dublin
		self.df = pd.read_csv('data/Covid19CountyStatisticsHPSCIreland.csv')
		with open('colors.json') as f:
			self.colors = json.load(f)
		self.df['TimeStamp'] = pd.to_datetime(self.df['TimeStamp'])
		self.counties = self.df.groupby('CountyName')
		self.dailies = self.identify_daily_figures(self.counties, 7)
		self.daily_counties = self.dailies.groupby('CountyName')
		
		if cumulative:
			self.create_plot(self.counties)
		else:
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
		dailies = pd.DataFrame(holder, columns=["TimeStamp", "CountyName", self.metric])
		if roll > 0:
			rolling = dailies[self.metric].rolling(roll).mean()
			dailies[self.metric] = rolling
		return dailies


	def create_filename(self):
		count_ = "_seven-day_average"
		dublin = "_excluding_dublin"
		if self.cumulative:
			count_ = "_cumulative"
		if self.dublin:
			dublin = ""
		filename = "".join([self.metric.lower(), count_, dublin])
		return "".join(["plots/", filename, ".html"])
		


	def create_plot(self, counties):
		filename = self.create_filename()
		bp.output_file(filename, title="Covid Cases")
		p = bp.figure(title="Covid Cases",
			x_axis_type="datetime",
			width=1200,
			height=600)
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
				line_color=self.colors[a]['color'],
				line_dash=self.colors[a]['dash'])
				# legend_group='CountyName')
				# legend_label=a)
			legend_items.append((a, [leg]))



		# p.add_layout(bm.LinearAxis(), "right")


		legend = bm.Legend(items=legend_items,
					location='top_right',
					orientation='vertical',
					border_line_color="black")

		p.add_layout(legend, 'right')

		# p2 = bp.figure(height=600,
		# 	width=400)
		# for legend in legend_items:
		# 	legend = bm.Legend(items=legend_items,
		# 						orientation='vertical',
		# 						location='top_right')
		# 	p.add_layout(legend)

		p.legend.click_policy="hide"
		p.legend.label_text_font_size = '12px'
		p.legend.label_text_font = 'FreeSans'
		p.legend.location = "top_left" #(15, 700)

		tools = bm.HoverTool(tooltips=[("Date","@StrDate"),
										("County","@CountyName"),
										("Cases","@ConfirmedCovidCases")])
		p.add_tools(tools)

		p.title.text_font = "FreeSans"
		p.title.text_font_size = "18px"

		p.background_fill_color = 'gray'
		p.background_fill_alpha = 0.5



		bp.show(p)

if __name__ == "__main__":
	x = CovidPlotter('ConfirmedCovidCases', True, True)
	x = CovidPlotter('ConfirmedCovidCases', True, False)
	x = CovidPlotter('ConfirmedCovidCases', False, False)
	x = CovidPlotter('ConfirmedCovidCases', False, True)
	x = CovidPlotter('PopulationProportionCovidCases', True, True)
	x = CovidPlotter('PopulationProportionCovidCases', False, True)
	