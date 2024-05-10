class ReportGenerator:
    @staticmethod
    def generate_annual_report(weather_data):
        highest_temp = {'value': float('-inf'), 'day': ''}
        lowest_temp = {'value': float('inf'), 'day': ''}
        highest_humidity = {'value': 0, 'day': ''}

        for entry in weather_data:
            max_temp = entry.max_temp
            min_temp = entry.min_temp
            humidity = entry.humidity
            date = entry.date

            if max_temp is not None and min_temp is not None:
                if max_temp > highest_temp['value']:
                    highest_temp['value'] = max_temp
                    highest_temp['day'] = date
                if min_temp < lowest_temp['value']:
                    lowest_temp['value'] = min_temp
                    lowest_temp['day'] = date

            if humidity is not None and humidity > highest_humidity['value']:
                highest_humidity['value'] = humidity
                highest_humidity['day'] = date

        report = []
        report.append(f"Highest: {highest_temp['value']}C on {highest_temp['day']}")
        report.append(f"Lowest: {lowest_temp['value']}C on {lowest_temp['day']}")
        report.append(f"Humidity: {highest_humidity['value']}% on {highest_humidity['day']}")

        return report

    @staticmethod
    def generate_monthly_report(weather_data):
        highest_temp = {'value': float('-inf'), 'day': ''}
        lowest_temp = {'value': float('inf'), 'day': ''}
        highest_humidity = {'value': 0, 'day': ''}
        data = {
            "total_high_temp" : 0,
            "total_min_temp" : 0,
            "total_humidity" : 0,
            "count_entries" : 0
        }

        for entry in weather_data:
            max_temp = entry.max_temp
            min_temp = entry.min_temp
            humidity = entry.humidity
            date = entry.date

            if max_temp is not None and min_temp is not None:
                data["total_high_temp"] += max_temp
                data["total_min_temp"] += min_temp
                data["count_entries"] += 1
                if max_temp > highest_temp['value']:
                    highest_temp['value'] = max_temp
                    highest_temp['day'] = date
                if min_temp < lowest_temp['value']:
                    lowest_temp['value'] = min_temp
                    lowest_temp['day'] = date

            if humidity is not None and humidity > highest_humidity['value']:
                data["total_humidity"] += humidity
                highest_humidity['value'] = humidity
                highest_humidity['day'] = date

        average_max_temp = data["total_high_temp"] / data["count_entries"]
        average_min_temp = data["total_min_temp"] / data["count_entries"]
        average_humidity = data["total_humidity"] / len(weather_data)

        report = []
        report.append(f"Average Highest: {average_max_temp}C")
        report.append(f"Average Lowest: {average_min_temp}C")
        report.append(f"Average Mean Humidity: {average_humidity}%")

        return report
    
    @staticmethod
    def generate_monthly_report_with_chart(weather_data):
        lowest_min_temp = float('inf')
        highest_min_temp = float('-inf')
        lowest_max_temp = float('inf')
        highest_max_temp = float('-inf')

        for entry in weather_data:
            min_temp = entry.min_temp
            max_temp = entry.max_temp

            if min_temp is not None:
                lowest_min_temp = min(lowest_min_temp, min_temp)
                highest_min_temp = max(highest_min_temp, min_temp)

            if max_temp is not None:
                lowest_max_temp = min(lowest_max_temp, max_temp)
                highest_max_temp = max(highest_max_temp, max_temp)

        highest_temp_bars = '+' * int(highest_max_temp)
        lowest_temp_bars = '+' * int(lowest_max_temp)
        highest_color = "\033[91m"  # Red color
        lowest_color = "\033[94m"  # Blue color
        reset_color = "\033[0m"     # Reset color

        report = []
        report.append(f"{lowest_min_temp}C {highest_color}{highest_temp_bars}{reset_color} {highest_min_temp}")
        report.append(f"{lowest_min_temp}C {lowest_color}{lowest_temp_bars}{reset_color} {lowest_max_temp}")

        return report