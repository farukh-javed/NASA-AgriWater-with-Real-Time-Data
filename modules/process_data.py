def process_et_data(data):
    dates, et_values = [], []
    for entry in data:
        dates.append(entry['time'])
        et_values.append(entry['et'])
    return dates, et_values
