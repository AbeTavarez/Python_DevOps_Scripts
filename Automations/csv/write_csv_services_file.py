import csv

hosts = [["workstation.local", "192.168.25.46"],
         ["webserver.cloud", "10.2.5.6"]]

with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)


with open("sofware.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))


# DictReader() allows us to convert the data in a CSV file into a standard dictionary
# DictWriter() \ allows us to write data from a dictionary into a CSV file

# with list of dictionaries
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
         {"name": "Lio Nelson", "username": "lion", "department": "Development"},
         {"name": "Charlie Grey", "username": "greyc", "department": "UX"}
         ]
# we set they keys we want to write to the file
keys = ["name", "username", "department"]
# open the file for writing
with open("by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()  # writes csv header
    writer.writerows(users)  # turn list of dictionaries into lines
