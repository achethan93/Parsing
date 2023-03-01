# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# def print_hi(name):
#  Use a breakpoint in the code line below to debug your script.
#  print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import re
import smtplib

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Algorithm,
# 1. parse the given file, read line by line and apply regex
# 2. get the matched line list and convert to file
# 3. attach file and send email using smtp
def send_execution_count(file):
    logs = parse_log_file(file)
    # txt file
    target_file = 'report.txt'
    matched_logs_file(logs, target_file)
    send_email(target_file)


# 1. to split the log file into line by line
# 2. for these each line, try and match my regex
# 3. if matched, add it to a list
# 4. if not, continue with the next line in the log
# 5. once the entire file is read, I am expected have matching list of lines
def parse_log_file(file):
    logs = []
    # read line by line
    with open(file, 'r') as file:
        for line in file:
            # call parse_log_line(line)
            log = parse_log_line(line)
            # if matched, add it to the list
            if log:
                logs.append(log)

    return logs


# below functions are like library functions to us, it simply checks if given line matches our regex or not
# and returns the matched line
def parse_log_line(line):
    match = re.match(r'(.*) (.*) : (.*7474)', line)
    if match:
        timestamp, level, message = match.groups()
        return timestamp, level, message
    else:
        return None


# write logs to target file
def matched_logs_file(logs, target_file):
    with open(target_file, 'w') as file:
        file.writelines('\n')
        for log in logs:
            file.writelines(str(log) + '\n')


def send_email(emailable_file):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("achethan93@gmail.com", "qtdrjbuzrkmlazbg")

    file = open(emailable_file, 'r')
    for_mail = file.read()
    print(for_mail)
    # message to be sent
    # message = str(for_mail)
    # print(message)
    # sending the mail
    s.sendmail("achethan93@gmail.com", "wukiw@inboxbear.com", for_mail)

    # terminating the session
    s.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    send_execution_count('//Topgrep_Sample_log.txt')
