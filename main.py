import pandas as pd
from bokeh.plotting import figure, show, save

def dominant_driver_chart(data_frame):
    years = data_frame["Season"]
    win_count = data_frame["No_of_Wins"]
    race_count = data_frame["No_of_Races"]
    world_champion = data_frame["World_Champion"]
    max_winning_drivers = data_frame["MaxWin_Drivers"]

    plot = figure(title="Dominant Drivers", x_axis_label="Season", y_axis_label="Races", frame_width=1000)

    plot.vbar(x=years, top=race_count, legend_label="Number of Races", width=0.8, bottom=0, color="blue")
    plot.vbar(x=years, top=win_count, legend_label="Number of Wins", width=0.8, bottom=0, color="red")

    save(plot, "f1_dominant_drivers.html", resources="cdn", title="F1 Dominant Drivers")
    show(plot)


if __name__ == '__main__':

    file_path = r"sample_data\dominantDrivers.csv"
    dominant_drivers = pd.read_csv(file_path)

    dominant_driver_chart(dominant_drivers)


