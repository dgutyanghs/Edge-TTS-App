import re
from datetime import datetime, timedelta

def shift_time(match):
    time_format = '%H:%M:%S.%f'
    time_str = match.group(0)
    original_time = datetime.strptime(time_str, time_format)
    shifted_time = original_time + timedelta(seconds=50, minutes=0, hours=0) #time shift for 50 seconds.
    return shifted_time.strftime(time_format)[:-3]

def shift_subtitle_times(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        content = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3}', shift_time, content)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Replace 'mulanCN3.vtt' with the path to your subtitle file
shift_subtitle_times('mulanCN3.vtt')
