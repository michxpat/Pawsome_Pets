# Pawsome_Pets
This is the final project for CSC423 with professor Vanessa Aguiar. We were tasked to work in pairs in the Design, development and implementation of a relational
database. I worked with Madeline Bluestone on this project.

# Case Study: Pawsome Pets

A company called Pawsome Pets runs multiple clinics. The company would like for their data
to be stored in a database. The following description was obtained during the analysis phase:
“Each of the Pawsome Pets clinics has several staff members and a member of staff manages
at most one clinic (not all staff manage clinics). Each clinic has a unique clinic number
(clinicNo) and each member of staff has a unique staff number (staffNo). Additionally, the
company would like to store each clinic’s name, address and telephone number, as well as the
staff’s name, address, telephone number, DOB, position and salary.
When a pet owner contacts a clinic, the owner’s pet is registered with the clinic. An owner can
own one or more pets, but a pet can only be registered at one clinic. Each owner has a unique
owner number (ownerNo), a name, an address and a telephone number. Each pet has a unique
pet number (petNo), name, DOB, animal species, breed and color.
When the pet comes to the clinic, it undergoes an examination by a member of the consulting
staff. The database should store the following information for each examination: chief
complaint (i.e., the main cause for the visit), description (i.e., what was done during the
examination), date seen and actions taken (e.g., a treatment was prescribed, tests were
ordered). A unique examination number (examNo) is assigned to each examination.”

# Part 1: Conceptual Model
Develop a conceptual data model reflecting the following requirements: 
- a. Identify the main entity types.
- b. Identify the main relationship types between the entity types identified in "a".
- c. Determine the multiplicity constraints for each relationship identified in "b".
- d. Identify attributes and associate them with entity or relationship types.
- e. Determine candidate and primary key attributes for each (strong) entity type.
- f. Generate the E-R diagram for the conceptual level (no FKs as attributes).

# Part 2: Logical Model
Develop a logical data model based on the following requirements: 
- a. Derive relations from the conceptual model.
- b. Validate the logical model using normalization to 3NF.
- c. Validate the logical model against 5 user transactions. (Note: These will be then implemented in 3c).
- d. Define integrity constraints:
  - i. Primary key constraints.
  - ii. Referential integrity/Foreign key constraints.
  - iii. Alternate key constraints (if any).
  - iv. Required data.
  - v. Attribute domain constraints.
  - vi. General constraints (if any).
- e. Generate the E-R diagram for the  logical level (contains FKs as attributes).

# Part 3: Implementation
Translate the logical data model for the DBMS. 
- a. Develop SQL code to create the entire database schema, reflecting the constraints identified in previous steps.
- b. Create at least 5 tuples for each relation in your database.
- c. Develop the 5 SQL queries that correspond to 2c using embedded SQL.

