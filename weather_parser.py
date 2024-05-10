import os

class WeatherRecord:
    def __init__(self, date, max_temp, min_temp, humidity):
        self.date = date
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.humidity = humidity

class WeatherDataParser:
    @staticmethod
    def parse_line(*args):
        cols = args[0].strip().split(',')
        date = cols[0]
        max_temp = float(cols[1]) if cols[1] else None
        min_temp = float(cols[3]) if cols[3] else None
        humidity = float(cols[7 if not args[1] else 8]) if cols[7 if not args[1] else 8] else None
        return WeatherRecord(date, max_temp, min_temp, humidity)

    @staticmethod
    def parse_file(*args):
        weather_data = []
        with open(args[0], 'r') as file:
            next(file)
            for line in file:
                weather_data.append(WeatherDataParser.parse_line(line,args))
        return weather_data

    @staticmethod
    def data_loader(weather_data, month, year, args):
        if month:
            for filename in os.listdir(args.data_dir):
                if filename.endswith(".txt"):
                    file_year = filename.split("_")[2]
                    file_month = filename.split("_")[3].split('.')[0]
                    if file_year == year and file_month == month:
                        file_path = os.path.join(args.data_dir, filename)
                        weather_data += WeatherDataParser.parse_file(file_path,month)
            return weather_data