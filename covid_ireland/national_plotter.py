import pandas as pd

import bokeh.plotting as bp
import bokeh.models as bm


class NationalPlotter(object):

	def __init__(self, metric, title):
		self.metric = metric
		self.title = title
		self.df = pd.read_csv('data/Covid19CountyStatisticsHPSCIreland.csv')
		self.df['TimeStamp'] = pd.to_datetime(self.df['TimeStamp'])
		self.dailies = self.identify_daily_figures(7)
		print(self.dailies.tail())
		self.create_plot(self.dailies)


	def identify_daily_figures(self, roll=0):
		"""

		"""
		holder = []
		bydate = self.df.groupby('TimeStamp')
		for a, b in bydate:
			holder.append([a, b.ConfirmedCovidCases.sum()])

		single_days = [holder[0][1]]
		for i in range(1, len(holder)):
			today = holder[i][1] - holder[i-1][1]
			single_days.append(today)

		dailies = pd.DataFrame(holder, columns=["TimeStamp", "Cumulative"])
		dailies['Daily'] = single_days
		if roll > 0:
			rolling = dailies['Daily'].rolling(roll).mean()
			dailies['Average'] = rolling
		return dailies


	def create_filename(self):
		return "".join(["plots/national_", self.metric.lower(), ".html"])


	def create_plot(self, data):
		filename = self.create_filename()
		bp.output_file(filename, title=self.title)
		p = bp.figure(title=self.title,
			x_axis_type="datetime",
			width=1200,
			height=700)
		temp = data.copy()
		temp['StrDate'] = temp['TimeStamp'].apply(lambda x: x.strftime("%a, %b %d"))
		temp['Base'] = 0
		source = bp.ColumnDataSource(temp)
		p.varea("TimeStamp",
			"Daily",
			"Base",
			source=source,
			fill_color="pink",
			fill_alpha=0.5,
			legend_label="Daily Cases")

		p.line("TimeStamp",
			"Average",
			source=source,
			line_width=3,
			line_color="crimson",
			legend_label="Average Daily Cases")


		tools = bm.HoverTool(tooltips=[("Date","@StrDate"),
										("Daily Cases","@Daily{0, 0}"),
										("Average Cases","@Average{0, 0}")])
		p.add_tools(tools)

		p.legend.location = "top_left"
		p.legend.click_policy = "hide"

		p.title.text_font = "Helvetica"
		p.title.text_font_size = "18px"
		p.background_fill_color = 'slategray'
		# p.background_fill_alpha = 0.25
		p.xaxis.formatter = bm.DatetimeTickFormatter(months=["%b, %Y"], days=["%b, %d"], hours=["%H:%M"])

		bp.show(p)

if __name__ == "__main__":
	x = NationalPlotter('ConfirmedCovidCases',
		"Confirmed Cases by Day")
