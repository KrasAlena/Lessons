def write_log_message(message):
    with open('log.txt', 'w') as file:
        file.write(message)