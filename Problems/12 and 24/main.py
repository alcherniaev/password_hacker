from datetime import datetime


def format_time(datetime_obj):
    h_24 = datetime_obj.strftime("%H:%M")
    h_12 = datetime_obj.strftime("%I:%M")
    print(f'24h {h_24}')
    print(f'12h {h_12}')
