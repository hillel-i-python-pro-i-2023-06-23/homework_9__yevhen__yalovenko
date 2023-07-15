import csv

from app.loggers.loggers import get_custom_logger
from app.services.processing_json import getting_request


# 'https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt'

def read_csv(url):
    logger = get_custom_logger(__name__)
    response = getting_request(url)
    content = response.text.splitlines()

    reader = csv.reader(content)
    next(reader)

    return reader


def calculate_average_height_weight(reader):
    total_height = 0
    total_weight = 0
    count = 0

    for row in reader:
        height = float(row[2])
        weight = float(row[4])
        total_height += height
        total_weight += weight
        count += 1

    average_weight = total_weight / count
    average_height = total_height / count
    return f"Average height = {average_height}, Average weight = {average_weight}"
