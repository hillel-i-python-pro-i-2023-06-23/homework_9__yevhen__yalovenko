from app.loggers.loggers import get_core_logger
from app.services.processing_users import format_users, output_user_info
from app.services.read_file import read_file


def main():
    logger = get_core_logger()
    logger.info(msg="Start First task")
    text = read_file()
    print(text)
    logger.info(msg="End First task")
    logger.info(msg="Start Second task")
    formatted_users = format_users()
    output = output_user_info(formatted_users)
    print(output)
    logger.info(msg="End Second task")
