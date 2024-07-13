import mysql.connector
import csv

def extract_data():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234Test*',  # my root password
        database='hackathoncodeiam'  # replace with your database name
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM problemstatements")
    rows = cursor.fetchall()

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in cursor.description])  # column headers
        writer.writerows(rows)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    extract_data()
