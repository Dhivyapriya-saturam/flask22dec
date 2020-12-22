import csv
from flask import request


def render():
    """
    Writing the user details into the csv file
    :return:
    """
    if request.method == 'POST':
        name = request.args.get['name']
        email = request.args.get['email']
        fieldnames = ['name', 'email']

        with open('list.csv', 'w') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow({'name': name, 'email': email})
    return 'Thanks for your input!'


def check():
    """
    Login check whether the user already registered  or not
    :return:
    """
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        details = [name, email]
        with open('list.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row == details:
                    return 'User found!'
                else:
                    return 'User not found!'
