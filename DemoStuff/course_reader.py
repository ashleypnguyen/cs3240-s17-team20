# Ashley Nguyen (apn2my)
import csv
import psycopg2

# read data from the CSV file and load it
# into the database table. This file must define a method called load_course_database(db_name,
# csv_filename) that takes two strings as parameters, the name of the database and the name of the
# CSV file with the data.

def load_course_database(db_name, csv_filename):
    with open('seas-courses-5years.csv', 'rU') as csvfile: reader = csv.reader(csvfile, delimiter=',').tuple()
    for row in reader:
        deptID = [0]
        courseNum = [1]
        sem = [2]
        meetingType = [3]
        seats = [4]
        instructor = [5]

    PG_USER = "postgres"
    PG_USER_PASS = "sarahxxxx"
    PG_DATABASE = "Berkeley"
    PG_HOST_INFO = "localhost"
    conn = psycopg2.connect("dbname=" + PG_DATABASE + " user=" + PG_USER + " password=" + PG_USER_PASS + PG_HOST_INFO)
    print("** Connected to database.")
    cur = conn.cursor()
    cur.execute(deptID, courseNum,sem,meetingType,seats,instructor)




