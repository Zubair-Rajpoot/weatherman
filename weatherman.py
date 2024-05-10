import argparse
import os
from weather_parser import WeatherDataParser
from report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description="Generate weather reports for a given year.")
    parser.add_argument("data_dir", type=str, help="Path to the directory containing weather data files")
    parser.add_argument("-e", "--year", type=str, help="Year for which to generate reports")
    parser.add_argument("-a", "--month", type=str, help="specify year/month for which you want to generate average reports")
    parser.add_argument("-c", "--chart", type=str, help="specify year/month for which you want to generate bar chart from low to high")
    args = parser.parse_args()

    month_dict = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }

    if(args.year):
        weather_data = []
        for filename in os.listdir(args.data_dir):
           if filename.endswith(".txt"):
               file_year = filename.split("_")[2]
               if file_year == args.year:
                   file_path = os.path.join(args.data_dir, filename)
                   weather_data += WeatherDataParser.parse_file(file_path)

        report = ReportGenerator.generate_annual_report(weather_data)
        for line in report:
            print(line)

    if(args.month):
        weather_data = []
        year, m = args.month.split("/")
        month = month_dict[int(m)]
        weather_data = WeatherDataParser.data_loader(weather_data, month, year, args)
        report = ReportGenerator.generate_monthly_report(weather_data)
        for line in report:
            print(line)

    if(args.chart):
        weather_data = []
        year, m = args.chart.split("/")
        month = month_dict[int(m)]
        weather_data = WeatherDataParser.data_loader(weather_data, month, year, args)
        report = ReportGenerator.generate_monthly_report_with_chart(weather_data)
        for line in report:
            print(line)


if __name__ == "__main__":
    main()
