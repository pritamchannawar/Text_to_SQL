import sqlite3

## Connect to SQLite
connection = sqlite3.connect("hospital.db")

# Create a cursor object to insert record, create table
cursor = connection.cursor()

## Create the table
table_info = """
Create table PATIENTS(
    PATIENT_ID INT PRIMARY KEY,
    NAME VARCHAR(50),
    AGE INT,
    GENDER VARCHAR(10),
    CONTACT_NUMBER VARCHAR(15),
    ADDRESS VARCHAR(100)
);

Create table DOCTORS(
    DOCTOR_ID INT PRIMARY KEY,
    NAME VARCHAR(50),
    SPECIALIZATION VARCHAR(50),
    EXPERIENCE INT
);

Create table APPOINTMENTS(
    APPOINTMENT_ID INT PRIMARY KEY,
    PATIENT_ID INT,
    DOCTOR_ID INT,
    APPOINTMENT_DATE DATE,
    TIME_SLOT VARCHAR(10),
    FOREIGN KEY (PATIENT_ID) REFERENCES PATIENTS(PATIENT_ID),
    FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTORS(DOCTOR_ID)
);
"""

cursor.executescript(table_info)

## Insert Some records

cursor.execute('''Insert Into PATIENTS values(1, 'John Doe', 35, 'Male', '1234567890', '123 Main St')''')
cursor.execute('''Insert Into PATIENTS values(2, 'Jane Doe', 30, 'Female', '9876543210', '456 Elm St')''')
cursor.execute('''Insert Into PATIENTS values(3, 'Bob Smith', 40, 'Male', '5555555555', '789 Oak St')''')
cursor.execute('''Insert Into PATIENTS values(4, 'Alice Johnson', 25, 'Female', '1111111111', '321 Maple St')''')
cursor.execute('''Insert Into PATIENTS values(5, 'Mike Brown', 45, 'Male', '2222222222', '901 Pine St')''')
cursor.execute('''Insert Into PATIENTS values(6, 'Emily Davis', 28, 'Female', '3333333333', '234 Cedar St')''')
cursor.execute('''Insert Into PATIENTS values(7, 'Tom Harris', 38, 'Male', '4444444444', '567 Spruce St')''')
cursor.execute('''Insert Into PATIENTS values(8, 'Lily White', 32, 'Female', '5555555555', '890 Walnut St')''')
cursor.execute('''Insert Into PATIENTS values(9, 'James Martin', 42, 'Male', '6666666666', '345 Hickory St')''')
cursor.execute('''Insert Into PATIENTS values(10, 'Sophia Patel', 29, 'Female', '7777777777', '678 Oak St')''')

cursor.execute('''Insert Into DOCTORS values(1, 'Dr. Smith', 'Cardiology', 10)''')
cursor.execute('''Insert Into DOCTORS values(2, 'Dr. Johnson', 'Neurology', 15)''')
cursor.execute('''Insert Into DOCTORS values(3, 'Dr. Williams', 'Oncology', 12)''')
cursor.execute('''Insert Into DOCTORS values(4, 'Dr. Thompson', 'Orthopedics', 8)''')
cursor.execute('''Insert Into DOCTORS values(5, 'Dr. Lee', 'Pediatrics', 10)''')
cursor.execute('''Insert Into DOCTORS values(6, 'Dr. Kim', 'Dermatology', 12)''')
cursor.execute('''Insert Into DOCTORS values(7, 'Dr. Brown', 'Gastroenterology', 15)''')
cursor.execute('''Insert Into DOCTORS values(8, 'Dr. Davis', 'Endocrinology', 10)''')
cursor.execute('''Insert Into DOCTORS values(9, 'Dr. Martin', 'Nephrology', 12)''')
cursor.execute('''Insert Into DOCTORS values(10, 'Dr. Patel', 'Pulmonology', 8)''')

cursor.execute('''Insert Into APPOINTMENTS values(1, 1, 1, '2023-03-01', '10:00 AM')''')
cursor.execute('''Insert Into APPOINTMENTS values(2, 2, 2, '2023-03-02', '11:00 AM')''')
cursor.execute('''Insert Into APPOINTMENTS values(3, 3, 3, '2023-03-03', '12:00 PM')''')
cursor.execute('''Insert Into APPOINTMENTS values(4, 4, 4, '2023-03-04', '1:00 PM')''')
cursor.execute('''Insert Into APPOINTMENTS values(5, 5, 5, '2023-03-05', '2:00 PM')''')

cursor.execute('''Insert Into APPOINTMENTS values(6, 6, 6, '2023-03-06', '3:00 PM')''')
cursor.execute('''Insert Into APPOINTMENTS values(7, 7, 7, '2023-03-07', '4:00 PM')''')
cursor.execute('''Insert Into APPOINTMENTS values(8, 8, 8, '2023-03-08', '5:00 PM')''')
cursor.execute('''Insert Into APPOINTMENTS values(9, 9, 9, '2023-03-09', '6:00 PM')''')
cursor.execute('''Insert Into APPOINTMENTS values(10, 10, 10, '2023-03-10', '7:00 PM')''')
cursor.execute('''Insert Into APPOINTMENTS values(11, 1, 2, '2023-03-11', '8:00 PM')''')
cursor.execute('''Insert Into APPOINTMENTS values(12, 2, 3, '2023-03-12', '9:00 PM')''')
cursor.execute('''Insert Into APPOINTMENTS values(13, 3, 4, '2023-03-13', '10:00 PM')''')
cursor.execute('''Insert Into APPOINTMENTS values(14, 4, 5, '2023-03-14', '11:00 PM')''')
cursor.execute('''Insert Into APPOINTMENTS values(15, 5, 6, '2023-03-15', '12:00 AM')''')

## Display All the records

print("The inserted records are")
data = cursor.execute('''Select * from PATIENTS''')
print("Patients:")
for row in data:
    print(row)

data = cursor.execute('''Select * from DOCTORS''')
print("Doctors:")
for row in data:
    print(row)

data = cursor.execute('''Select * from APPOINTMENTS''')
print("Appointments:")
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()