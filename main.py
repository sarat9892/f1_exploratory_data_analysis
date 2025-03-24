import pandas as pd
from bokeh.plotting import figure, show, save
from bokeh.models import ColumnDataSource, HoverTool
from collections import defaultdict


def dominant_driver_chart(data_frame):

    source_list = defaultdict(list)

    source_list["years"] = list(data_frame["Season"])
    source_list["win_count"] = list(data_frame["No_of_Wins"])
    source_list["race_count"] = list(data_frame["No_of_Races"])
    source_list["world_champion"] = list(data_frame["World_Champion"])
    source_list["max_winning_drivers"] = list(data_frame["MaxWin_Drivers"])

    source = ColumnDataSource(source_list)

    plot = figure(title="Dominant Drivers", x_axis_label="Season", y_axis_label="Races", frame_width=1000)

    race_bar = plot.vbar(x="years", top="race_count", legend_label="Number of Races", width=0.8, bottom=0, color="blue", source=source)
    win_bar = plot.vbar(x="years", top="win_count", legend_label="Number of Wins", width=0.8, bottom=0, color="red", source=source)

    tooltip = HoverTool()
    tooltip.tooltips = [("World Champion", "@world_champion"), ("Driver With Most Wins", "@max_winning_drivers")]
    tooltip.renderers = [race_bar]
    plot.add_tools(tooltip)

    plot.legend.location = "top_left"

    save(plot, "f1_dominant_drivers.html", resources="cdn", title="F1 Dominant Drivers")
    show(plot)


if __name__ == '__main__':

    file_path = r"sample_data\dominantDrivers.csv"
    dominant_drivers = pd.read_csv(file_path)

    dominant_driver_chart(dominant_drivers)


