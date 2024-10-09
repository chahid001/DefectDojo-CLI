from datetime import datetime

def get_date():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")

    return date