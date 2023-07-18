from application.services.getting_request import getting_request


def processing_json_file(url) -> dict:
    json_file = getting_request(url).json()
    return json_file


def output_json(url) -> str:
    json_file = processing_json_file(url)
    number = json_file['number']
    return f"Numbers of cosmonauts for now is: {number}"
