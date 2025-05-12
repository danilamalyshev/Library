import csv

file_path = '../DATABASE/customer.csv'
customers = []

with open(file_path, mode="w", newline='', encoding='utf-8') as customersfile:
    reader = csv.reader(customersfile)
    for row in reader:
        customers.append(input())