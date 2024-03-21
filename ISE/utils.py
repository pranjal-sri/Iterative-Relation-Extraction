RELATIONS_DICT = {1:'Schools_Attended', 2: 'Work_For', 3: 'Live_In', 4: 'Top_Member_Employees'}

# Schools_Attended: Subject: PERSON, Object: ORGANIZATION
# Work_For: Subject: PERSON, Object: ORGANIZATION
# Live_In: Subject: PERSON, Object: one of LOCATION, CITY, STATE_OR_PROVINCE, or COUNTRY
# Top_Member_Employees: Subject: ORGANIZATION, Object: PERSON
RELEVANT_ENTITIES = {1: ('PERSON', 'ORGANIZATION'), 
                   2: ('PERSON', 'ORGANIZATION'), 
                   3: ('PERSON', 'LOCATION', 'CITY', 'COUNTRY', 'STATE_OR_PROVINCE'),  
                   4: ('ORGANIZATION', 'PERSON')}

RELATIONS_INTERNAL_REP = {1: 'per:schools_attended', 
                   2: 'per:employee_of', 
                   3: 'per:cities_of_residence',  
                   4: 'org:top_members/employees'}
                   