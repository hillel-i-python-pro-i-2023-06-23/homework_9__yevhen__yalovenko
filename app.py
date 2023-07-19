from flask import Flask, send_file
from webargs import fields
from webargs.flaskparser import use_args

from application.config import FILES_OUTPUT_DIR
from application.services.csv_reader import read_csv, calculate_average_height_weight
from application.services.processing_json import output_json, getting_request
from application.services.processing_users import format_users, output_user_info
from application.services.read_file import read_file

app = Flask(__name__)


@app.route("/")
def home_page():
    return "This is homepage"


@app.route("/get-content/")
def get_content():
    return read_file()


# Альтернативна реалізація для перегляду вмісту файла
@app.route("/new.txt")
def download():
    file = FILES_OUTPUT_DIR / "new.txt"
    if not file.is_file():
        read_file()
    return send_file(file)


@app.route("/generate-users/")
@use_args({"amount": fields.Int(missing=100)}, location="query")
def users_generate(args):
    amount = args["amount"]
    formatted_users = format_users(amount)
    output = output_user_info(formatted_users)
    return f"<ol>{output}</ol>"


@app.route("/space/")
def cosmonauts():
    json_file = getting_request("http://api.open-notify.org/astros.json")
    return output_json(json_file)


@app.route("/mean/")
def average_h_w():
    # Getting data - START #
    url = "https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"
    # Getting data - END #

    read = read_csv(url)
    return calculate_average_height_weight(read)


if __name__ == "__main__":
    app.run()
