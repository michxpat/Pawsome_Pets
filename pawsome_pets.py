import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('pawsomePets.db')
# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

#Sometimes needed for foreign keys to work
cursor.execute("PRAGMA foreign_keys = 1")

# Develop SQL code to create the entire database schema, reflecting the constraints
# identified in previous steps.
createTables = """  
CREATE TABLE Clinic (
    clinicNo int NOT NULL PRIMARY KEY CHECK (clinicNo > 0),
    cName varchar(40) NOT NULL,
    cAddress varchar(100) NOT NULL,
    cPhone varchar(10) UNIQUE NOT NULL CHECK (cPhone BETWEEN 1000000000 AND 9999999999)
);

CREATE TABLE Staff (
    staffNo int NOT NULL PRIMARY KEY CHECK (staffNo > 0),
    sName varchar(40) NOT NULL,
    sAddress varchar(100) NOT NULL,
    sPhone int UNIQUE NOT NULL CHECK (sPhone BETWEEN 1000000000 AND 9999999999),
    sDOB date NOT NULL CHECK (sDOB <= CURRENT_DATE),
    position varchar(15) NOT NULL CHECK (position IN ('Receptionist','Veterinarian','Groomer','Maintenance','Nurse')),
    salary decimal(10,2) NOT NULL CHECK (salary > 0),
    clinicNo int NOT NULL,
    clinicManaged int,
    FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo),
    FOREIGN KEY (clinicManaged) REFERENCES Clinic(clinicNo),
    CHECK (clinicNo = clinicManaged)
);

CREATE TABLE Owner (
    ownerNo int NOT NULL PRIMARY KEY CHECK (ownerNo > 0),
    oName varchar(40) NOT NULL,
    oAddress varchar(100) NOT NULL,
    oPhone varchar(10) UNIQUE NOT NULL CHECK (oPhone BETWEEN 1000000000 AND 9999999999)
);

CREATE TABLE Pet (
    petNo int NOT NULL PRIMARY KEY CHECK (petNo > 0),
    pName varchar(40) NOT NULL,
    pDOB date NOT NULL CHECK (pDOB <= CURRENT_DATE),
    species varchar(10) NOT NULL CHECK (species In ('Dog','Cat','Reptile','Bird')),
    breed varchar(15) NOT NULL,
    color varchar(15) NOT NULL,
    clinicNo int,
    ownerNo int NOT NULL,
    FOREIGN KEY (clinicNo) references Clinic(clinicNo),
    FOREIGN KEY (ownerNo) references Owner(ownerNo)
    UNIQUE(pName,ownerNo)
);

CREATE TABLE Examination (
    examNo int NOT NULL PRIMARY KEY CHECK (examNo > 0),
    chiefComplaint varchar(100) NOT NULL,
    description varchar(200) NOT NULL,
    examDate date NOT NULL CHECK (examDate <= CURRENT_DATE),
    actionsTaken varchar(200) NOT NULL,
    staffNo int NOT NULL,
    petNo int NOT NULL,
    FOREIGN KEY (staffNo) REFERENCES Staff(staffNo),
    FOREIGN KEY (petNo) REFERENCES Pet(petNo)
    UNIQUE(examDate,staffNo,petNo)
);
"""
cursor.executescript(createTables)

# Create at least 5 tuples for each relation in your database.

#insert values into clinic table
clinic1 = (21,'North Clinic','789 road',6789012345)
clinic2 = (22,'South Clinic','123 lane',7890123456)
clinic3 = (23,'East Clinic','456 lane',8901234567)
clinic4 = (24,'West Clinic','789 lane',9012345678)
clinic5 = (25,'Central Clinic','123 way',9876543210)
 
clinic_list=[clinic1,clinic2,clinic3,clinic4,clinic5]

for clinic in clinic_list:
    cursor.execute("INSERT INTO Clinic VALUES (?,?,?,?)",clinic)

clinicTable = """
 SELECT * FROM Clinic
 """ 
tableCursor = cursor.execute(clinicTable)
print("\nClinic Table:")
current_df = pd.DataFrame(tableCursor.fetchall(), columns=[row[0] for row in tableCursor.description])
print(current_df.to_string())

#insert values into staff member table
staff1 = (11,'Alice','123 street',1234567890,'2000-01-01','Veterinarian',100000,21,21,)
staff2 = (12,'Bob','456 street',2345678901,'2000-02-02','Nurse',90000,22,22,)
staff3 = (13,'Carol','789 street',3456789012,'2000-03-03','Receptionist',75000,23,23,)
staff4 = (14,'Emma','123 road',4567890123,'2000-04-04','Maintenance',70000,22,None)
staff5 = (15,'Kate','456 road',5678901234,'2000-05-05','Groomer',80000,25,None)

staff_list=[staff1,staff2,staff3,staff4,staff5]

for staff in staff_list:
    cursor.execute("INSERT INTO Staff VALUES (?,?,?,?,?,?,?,?,?)",staff)
 
staffMemberTable = """
 SELECT * FROM Staff
 """
tableCursor = cursor.execute(staffMemberTable)
print("\nStaff Member Table:")
current_df = pd.DataFrame(tableCursor.fetchall(), columns=[row[0] for row in tableCursor.description])
print(current_df.to_string())

#insert values into owner table
owner1 = (31,'Jon','456 way',8765432109)
owner2 = (32,'Jane','789 way',7654321098)
owner3 = (33,'Rick','123 ave',6543210987)
owner4 = (34,'Katie','456 ave',5432109876)
owner5 = (35,'Mel','789 ave',4321098765)
 
owner_list = [owner1,owner2,owner3,owner4,owner5]

for owner in owner_list:
    cursor.execute("INSERT INTO Owner VALUES (?,?,?,?)",owner)
 
ownerTable = """
 SELECT * FROM Owner
 """
tableCursor = cursor.execute(ownerTable)
print("\nOwner Table:")
current_df = pd.DataFrame(tableCursor.fetchall(), columns=[row[0] for row in tableCursor.description])
print(current_df.to_string())

#insert values into pet table
pet1 = (41,'Frank','2020-01-01','Cat','Domestic','Gray',21,31)
pet2 = (42,'Winnie','2020-02-02','Dog','Wheaten','Brown',22,32)
pet3 = (43,'Juno','2020-03-03','Reptile','Lizard','Multi.',23,33)
pet4 = (44,'Maggie','2020-04-04','Cat','Domestic','Multi.',23,33)
pet5 = (45,'Beau','2020-05-05','Bird','Parakeet','Green',22,35)

pet_list = [pet1,pet2,pet3,pet4,pet5]

for pet in pet_list:
    cursor.execute("INSERT INTO Pet VALUES (?,?,?,?,?,?,?,?)",pet)
 
petTable = """
 SELECT * FROM Pet
 """
tableCursor = cursor.execute(petTable)
print("\nPet Table:")
current_df = pd.DataFrame(tableCursor.fetchall(), columns=[row[0] for row in tableCursor.description])
print(current_df.to_string())
 
#insert values into examination table
exam1 = (51,'Limping','Checked for fracture','2024-01-01','Ordered imaging',11,42)
exam2 = (52,'Annual Check-Up','General Examination','2024-02-02','No issues found',12,41)
exam3 = (53,'Vaccine','Annual vaccines given','2024-03-03','Updated vaccine records',12,44)
exam4 = (54,'Injury','Cleaned wound and bandaged','2024-03-03','Prescribed antibiotics',11,44)
exam5 = (55,'Limping','Checked for sprain','2024-04-04','Ordered imaging',12,41)

exam_list = [exam1,exam2,exam3,exam4,exam5]

for exam in exam_list:
    cursor.execute("INSERT INTO Examination VALUES (?,?,?,?,?,?,?)",exam)
 
examTable = """
 SELECT * FROM Examination
 """
tableCursor = cursor.execute(examTable)
print("\nExamination Table:")
current_df = pd.DataFrame(tableCursor.fetchall(), columns=[row[0] for row in tableCursor.description])
print(current_df.to_string())

# Develop the 5 SQL queries that correspond to 2c using embedded SQL

#List all details of all Pets registered to a Clinic, given Clinic phone number 7890123456
print("\nAll details of all Pets registered to a Clinic, given Clinic phone number 7890123456")
tableCursor = cursor.execute("SELECT p.*, c.cPhone FROM Pet p, Clinic c WHERE p.clinicNo = c.clinicNo AND c.cPhone = 7890123456")
current_df = pd.DataFrame(tableCursor.fetchall(), columns=[row[0] for row in tableCursor.description])
print(current_df.to_string())

#Find how many Examinations a Pet has received, given pet number 44
print("\nFind how many examinations the pet has received, given pet number 44")
tableCursor = cursor.execute("SELECT COUNT(*) AS examinationCount FROM Examination e WHERE e.petNo = 44")
current_df = pd.DataFrame(tableCursor.fetchall(), columns=[row[0] for row in tableCursor.description])
print(current_df.to_string())

#List all Pets owned by an Owner, given owner number 33
print("\nAll Pets owned by an Owner, given Ownber number 33")
tableCursor = cursor.execute("SELECT p.petNo, p.pName, p.species, p.breed, p.color, p.ownerNo FROM Pet p WHERE p.ownerNo= 33")
current_df = pd.DataFrame(tableCursor.fetchall(), columns=[row[0] for row in tableCursor.description])
print(current_df.to_string())

#Find the names of Staff Members that manage a clinic
print("\nFind the names of Staff Members that manage a clinic")
tableCursor = cursor.execute("SELECT sName FROM Staff s WHERE s.clinicManaged is NOT NULL")
current_df = pd.DataFrame(tableCursor.fetchall(), columns=[row[0] for row in tableCursor.description])
print(current_df.to_string())

#Show the examNo, exam date, petNo, clinicNo, and clinic name of all examinations conducted at a Clinic, given clinicNo 21
print("\nShow examNo, exam date, petNo, pet name, clinicNo, and clinic name of all examinations conducted at a Clinic, given clinicNo 21")
tableCursor = cursor.execute("SELECT e.examNo,e.examDate,p.petNo,p.pName,c.clinicNo,c.cName FROM Examination e, Pet p, Clinic c WHERE c.clinicNo = 21 AND c.clinicNo = p.clinicNo AND p.petNo = e.petNo")
current_df = pd.DataFrame(tableCursor.fetchall(), columns=[row[0] for row in tableCursor.description])
print(current_df.to_string())

#Update the oAddress of an Owner, given owner number 35
print("\nUpdate the oAddress of an Owner, given owner number 35")
print("Previous address:")
tableCursor = cursor.execute("SELECT o.ownerNo, o.oAddress FROM Owner o WHERE o.ownerNo = 35")
current_df = pd.DataFrame(tableCursor.fetchall(), columns=[row[0] for row in tableCursor.description])
print(current_df.to_string())
cursor.execute("UPDATE Owner SET oAddress = '111 new street' WHERE ownerNo = 35")
print("New address:")
tableCursor = cursor.execute("SELECT o.ownerNo, o.oAddress FROM Owner o WHERE o.ownerNo = 35")
current_df = pd.DataFrame(tableCursor.fetchall(), columns=[row[0] for row in tableCursor.description])
print(current_df.to_string())


# Commit any changes to the database
db_connect.commit()
# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()