from functions.create_structure import create_dirs

log = 0
path = "log/execution.log"
create_dirs()


def start_log():
    from datetime import datetime
    import getpass
    global log
    global path

    log = open(path, "w+")
    username = getpass.getuser()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    log.write(f'File generation by {username}. Date: {dt_string}\n\n')
    log.close()


def write_log(statement):
    global log
    global path
    log = open(path, "a+")
    log.write(statement)
    log.close()



