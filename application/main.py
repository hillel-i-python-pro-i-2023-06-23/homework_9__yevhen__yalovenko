from application.services.csv_reader import read_csv, calculate_average_height_weight
from application.services.processing_json import output_json
from application.services.processing_users import format_users, output_user_info
from application.services.read_file import read_file


def main():
    text = read_file()
    print(text)

    formatted_users = format_users()
    output = output_user_info(formatted_users)
    print(output)

    cosmonauts_num = output_json('http://api.open-notify.org/astros.json')
    print(cosmonauts_num)

    csv_file = read_csv('https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt')
    average = calculate_average_height_weight(csv_file)
    print(average)
