from datetime import datetime


def convert_to_standard(datetime_obj):
    date_standart = datetime_obj.strftime("%Y-%m-%d")
    return date_standart
