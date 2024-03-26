template_rel_1 = '''
You act like a computer function for relation extraction within given text. 

You will have to extract all possible entity pairs from a sentence for a the given relation: Schools_Attended

I will give you a piece of text, and you have to do the three step process:

1.⁠ ⁠Identify all named entities of the type PERSON/ORGANIZATION in the sentence using NER. Focus on proper nouns representing people and organizations that are schools/colleges/universities or any educational institute
2.⁠ ⁠Extract all possible pairs of (PERSON, ORGANIZATION) entities.
3.⁠ ⁠Analyze the context and identify pairs with the relationship 'per:schools_attended', where the PERSON attended/is attending the ORGANIZATION as a student.

The relation Schools_Attended, means that you have to find the names of people in the sentence and the names of organizations and return those pairs where the person was/is a student in that organization or attended the organization as a student.

The text is scraped from websites, so it may be irregular and incorrect. So, be flexible in the pairs you extract and extract as many as possible.

Make sure that the entities you consider are proper nouns and do not fall in the category of pronouns like I, we, he, she, they etc.

Be sure to consider all pairs of named entities of the given form. Print analysis as well as output like a python list of tuples in plain text shown below:

Example:
input sentences is 
"Google co - founder Sergey Brin co - founded web - search giant Google Inc. in 1998 with fellow Stanford student Larry Page ."

The valid PERSON entities are:
1) Sergey Brin
2) Larry Page

The valid ORGANIZATION entities are:
1) Stanford

The valid (PERSON, ORGANIZATION) pairs of entities are:
1) (Sergey Brin, Stanford)
2) (Larry Page, Stanford)

The sentence indicates that the two were fellow students at Stanford, so both pairs confirm the relation 'per:schools_attended'.

Output:
[("Sergey Brin", "Stanford"), ("Larry Page", "Standford")]
Example-over

Now, the input:
Provide me the extracted entity pairs from the sentence: {input_sentence}

Remember:

•⁠  ⁠Return as many as possible pairs of named entities.
•⁠  ⁠Use proper nouns and avoid pronouns.
•⁠  ⁠The output last line should be a list of tuples of form (PERSON, ORGANIZATION) in plain text.

Additional Considerations:

•⁠  ⁠Handle ambiguity in the "Schools_Attended" relationship.
•⁠  ⁠Recognize negations that indicate a person did not attend a particular organization.
•⁠  ⁠Extract temporal information if the task requires identifying the specific time period of attendance.

Another example of a valid set of entities and relation is ["Jeff Bezos", "Schools_Attended", "Princeton University"]
''' 

template_rel_2 = '''
You act like a computer function for relation extraction within given text. 

You will have to extract all possible entity pairs from a sentence for a the given relation: Works_For

I will give you a piece of text, and you have to do the three step process:

1.⁠ ⁠Identify all named entities of the type PERSON/ORGANIZATION in the sentence using NER. Focus on proper nouns representing people and organizations
2.⁠ ⁠Extract all possible pairs of (PERSON, ORGANIZATION) entities.
3.⁠ ⁠Analyze the context and identify pairs with the relationship 'per:employee_of', where the PERSON works for the ORGANIZATION as a employee.

The relation Works_For, means that you have to find the names of people in the sentence and the names of organizations and return those pairs where the person was/is a employee in that organization or works/worked in the organization as an employee.

The text is scraped from websites, so it may be irregular and incorrect. So, be flexible in the pairs you extract and extract as many as possible.

Make sure that the entities you consider are proper nouns and do not fall in the category of pronouns like I, we, he, she, they etc.

Be sure to consider all pairs of named entities of the given form. Print analysis as well as output like a python list of tuples in plain text shown below:

Example:
input sentences is 
"Pichai was selected to become the next CEO of Google on August 10 , 2015 , after previously being appointed Product Chief by the then CEO Larry Page ."

The valid PERSON entities are:
1) Pichai
2) Larry Page

The valid ORGANIZATION entities are:
1) Google

The valid (PERSON, ORGANIZATION) pairs of entities are:
1) (Pichai, Google)
2) (Larry Page, Google)

The sentence indicates that the two worked at Google, so both pairs confirm the relation 'per:employee_of'.

Output:
[("Pichai", "Google"), ("Larry Page", "Google")]
Example-over

Now, the input:
Provide me the extracted entity pairs from the sentence: {input_sentence}

Remember:

•⁠  ⁠Return as many as possible pairs of named entities.
•⁠  ⁠Use proper nouns and avoid pronouns.
•⁠  ⁠The output last line should be a list of tuples of form (PERSON, ORGANIZATION) in plain text.

Additional Considerations:

•⁠  ⁠Handle ambiguity in the "Works_For" relationship.
•⁠  ⁠Recognize negations that indicate a person did/does not work for a particular organization.
•⁠  ⁠Extract temporal information if the task requires identifying the specific time period of employment.

Another example of a valid set of entities and relation is ["Alec Radford", "Work_For", "OpenAI"]
''' 

template_rel_3 = '''
You act like a computer function for relation extraction within given text. 

You will have to extract all possible entity pairs from a sentence for a the given relation: Live_In

I will give you a piece of text, and you have to do the three step process:

1.⁠ ⁠Identify all named entities of the type PERSON/LOCATION/CITY/COUNTRY/STATE/PROVINCE in the sentence using NER. Focus on proper nouns representing people and places which are locations or cities or countries or states or provinces
2.⁠ ⁠Extract all possible pairs of (PERSON, LOCATION/CITY/COUNTRY/STATE/PROVINCE) entities.
3.⁠ ⁠Analyze the context and identify pairs with the relationship 'per:cities_of_residence', where the PERSON resides/resided in LOCATION/CITY/COUNTRY/STATE/PROVINCE as a resident.

The relation Live_In, means that you have to find the names of people in the sentence and the names of locations or cities or countries or states or provinces and return those pairs where the person was/is a resident in that locations or cities or countries or states or provinces or lives/lived in the location or city or county or state or province an resident.

The text is scraped from websites, so it may be irregular and incorrect. So, be flexible in the pairs you extract and extract as many as possible.

Make sure that the entities you consider are proper nouns and do not fall in the category of pronouns like I, we, he, she, they etc.

Be sure to consider all pairs of named entities of the given form. Print analysis as well as output like a python list of tuples in plain text shown below:

Example:
input sentences is 
"Sarah has a degree in journalism and resides in New York City ."

The valid PERSON entities are:
1) Sarah

The valid ORGANIZATION entities are:
1) New York City

The valid (PERSON, LOCATION/CITY/COUNTRY/STATE/PROVINCE) pairs of entities are:
1) (Sarah, New York City)

The sentence indicates that Sarah resides in New York City, so both pairs confirm the relation 'per:cities_of_residence'.

Output:
[("Sarah","New York City")]
Example-over

Now, the input:
Provide me the extracted entity pairs from the sentence: {input_sentence}

Remember:

•⁠  ⁠Return as many as possible pairs of named entities.
•⁠  ⁠Use proper nouns and avoid pronouns.
•⁠  ⁠The output last line should be a list of tuples of form (PERSON, LOCATION/CITY/COUNTRY/STATE/PROVINCE) in plain text.

Additional Considerations:

•⁠  ⁠Handle ambiguity in the "Live_In" relationship.
•⁠  ⁠Recognize negations that indicate a person did/does not live/lived in a particular location or city or country or state or province.
•⁠  ⁠Extract temporal information if the task requires identifying the specific time period of residence.

Another example of a valid set of entities and relation is ["Vladimir Putin", "Live_In", "Moscow"]
'''

template_rel_4 = '''
You act like a computer function for relation extraction within given text. 

You will have to extract all possible entity pairs from a sentence for a the given relation: Top_Member_Employees

I will give you a piece of text, and you have to do the three step process:

1.⁠ ⁠Identify all named entities of the type ORGANIZATION/PERSON in the sentence using NER. Focus on proper nouns representing people and organizations
2.⁠ ⁠Extract all possible pairs of (ORGANIZATION, PERSON) entities.
3.⁠ ⁠Analyze the context and identify pairs with the relationship 'org:top_members/employees', where the PERSON holds/held a founding, leadership, or high-level role in the ORGANIZATION.

The relation Top_Member_Employees, means that you have to find the names of people in the sentence and the names of organizations and return those pairs where the person was/is in a founding, leadership, or high-level role in that organization or was a part of the organization in a founding, leadership, or high-level role.

The text is scraped from websites, so it may be irregular and incorrect. So, be flexible in the pairs you extract and extract as many as possible.

Make sure that the entities you consider are proper nouns and do not fall in the category of pronouns like I, we, he, she, they etc.

Be sure to consider all pairs of named entities of the given form. Print analysis as well as output like a python list of tuples in plain text shown below:

Example:
input sentences is 
"He is the executive chairman and CEO of Microsoft , succeeding Steve Ballmer in 2014 as CEO[2][3]"

The valid PERSON entities are:
1) Steve Balmer

The valid ORGANIZATION entities are:
1) Microsoft

The valid (ORGANIZATION, PERSON) pairs of entities are:
1) (Steve Balmer, Microsoft)

The sentence indicates that Steve Balmer previously held the position of a CEO which is a high level/leadership role in Microsoft, so both pairs confirm the relation 'org:top_members/employees'.

Output:
[("Microsoft","Steve Ballmer")]
Example-over

Now, the input:
Provide me the extracted entity pairs from the sentence: {input_sentence}

Remember:

•⁠  ⁠Return as many as possible pairs of named entities.
•⁠  ⁠Use proper nouns and avoid pronouns.
•⁠  ⁠The output last line should be a list of tuples of form (ORGANIZATION, PERSON) in plain text.

Additional Considerations:

•⁠  ⁠Handle ambiguity in the "Top_Member_Employees" relationship.
•⁠  ⁠Recognize negations that indicate a person did/does not hold a founding, leadership, or high-level role for a particular organization.
•⁠  ⁠Extract temporal information if the task requires identifying the specific time period of employment.

Another example of a valid set of entities and relation is ["Nvidia", "Top_Member_Employees", "Jensen Huang"]
''' 

PROMPT_TEMPLATES = {1: template_rel_1, 2: template_rel_2, 3: template_rel_3, 4: template_rel_4}
