import datetime

def logged(msg,type):
    if type == 1:
        tp = "[INFO] - "
    elif type == 2:
        tp = "[WARNING] - "
    elif type == 3:
        tp = "[ERROR] - "
    else:
        tp == " - "
    now = datetime.datetime.now()
    current_time = "[" + now.strftime("%d/%m/%y %H:%M:%S") + "]"
    to_log = current_time + tp + msg + "\n"
    with open("log", "a") as file:
        file.write(to_log)