from app.loggers.loggers import get_core_logger
from app.services.csv_reader import read_csv, calculate_average_height_weight
from app.services.processing_json import output_json
from app.services.processing_users import format_users, output_user_info
from app.services.read_file import read_file


def main():
    logger = get_core_logger()
    logger.info(msg="START FIRST TASK")
    text = read_file()
    print(text)
    logger.info(msg="END FIRST TASK")
    logger.info(msg="START SECOND TASK")
    formatted_users = format_users()
    output = output_user_info(formatted_users)
    print(output)
    logger.info(msg="END SECOND TASK")
    logger.info(msg="START THIRD TASK")
    cosmonauts_num = output_json('http://api.open-notify.org/astros.json')
    print(cosmonauts_num)
    logger.info(msg="END THIRD TASK")
    logger.info(msg="START FOURTH TASK")
    csv_file = read_csv('https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt')
    average = calculate_average_height_weight(csv_file)
    print(average)
    logger.info(msg="END FOURTH TASK")
