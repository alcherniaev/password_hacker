from datetime import datetime


def get_release_date(release_str):
    str_date = release_str.replace('Day of release: ', '')
    return datetime.strptime(str_date, "%d %B %Y")
