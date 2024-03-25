template_rel_1 = '''
You act like a computer function that finds relations within given text. 

You will have to extract all possible entity pairs from a sentence for a the given relation: Schools_Attended

I will give you a sentence, and you have to do the two step process:

1) Consider list of all pairs of named entities of the form: (PERSON, ORGANIZATION)
2) Return the pairs that fall in the category of the relation: Schools_Attended  

The relation Schools_Attended, means that you have to find the names of people in the sentence and the names of organizations and return those pairs where the person was/is a student in that organization or attended the organization as a student.

Be a little flexible, in terms of the entities you consider and make as many entity pairs as possible from the given sentence. Return those pairs in a proper format and satisfy the description of the relation.

Make sure that the entities you consider are proper nouns and do not fall in the category of pronouns like I, we, he, she, they etc.

Be sure to consider all pairs of named entities of the given form. Print analysis as well as output like a python list of tuples in plain text shown below:

Example:
input sentences is 
"Google co - founder Sergey Brin co - founded web - search giant Google Inc. in 1998 with fellow Stanford student Larry Page ."

You print:

<Analysis>

Output:
[("Sergey Brin", "Stanford"), ("Larry Page", "Standford")]

Provide me the extracted entity pairs from the sentence: {input_sentence}
''' 

template_rel_2 = '''
You act like a computer function that finds relations within given text. 

You will have to extract all possible entity pairs from a sentence for a the given relation: Work_For

I will give you a sentence, and you have to do the two step process:

1) Consider list of all pairs of named entities of the form: (PERSON, ORGANIZATION)
2) Return the pairs that fall in the category of the relation: Work_For  

The relation Work_For, means that you have to find the names of people in the sentence and the names of organizations and return those pairs where the person works in that organization or used to work in that organization.

Be a little flexible, in terms of the entities you consider and make as many entity pairs as possible from the given sentence. Return those pairs in a proper format and satisfy the description of the relation.

Make sure that the entities you consider are proper nouns and do not fall in the category of pronouns like I, we, he, she, they etc.

Be sure to consider all pairs of named entities of the given form. Print analysis as well as output like a python list of tuples in plain text shown below:

Example:
input sentences is 
"Pichai was selected to become the next CEO of Google on August 10 , 2015 , after previously being appointed Product Chief by the then CEO Larry Page ."

You print:

<Analysis>

Output:
[("Pichai", "Google"), ("Larry Page", "Google")]

Provide me the extracted entity pairs from the sentence: {input_sentence}
''' 

template_rel_3 = '''
You act like a computer function that finds relations within given text. 

You will have to extract all possible entity pairs from a sentence for a the given relation: Live_In

I will give you a sentence, and you have to do the two step process:

1) Consider list of all pairs of named entities of the form: (PERSON, LOCATION) or (PERSON, CITY) or (PERSON, COUNTRY) or (PERSON, STATE_OR_PROVINCE)
2) Return the pairs that fall in the category of the relation: Live_In  

The relation Live_In, means that you have to find the names of people in the sentence and the names of locations or cities or countries or states or provinces and return those pairs where the person was/is located/residing in that location/city/country/state/provice.

Be a little flexible, in terms of the entities you consider and make as many entity pairs as possible from the given sentence. Return those pairs in a proper format and satisfy the description of the relation.

Make sure that the entities you consider are proper nouns and do not fall in the category of pronouns like I, we, he, she, they etc.

Be sure to consider all pairs of named entities of the given form. Print analysis as well as output like a python list of tuples in plain text shown below:

Example:
input sentences is 
"Sarah has a degree in journalism and resides in New York City ."

You print:

<Analysis>

Output:
[("Sarah","New York City")]

Provide me the extracted entity pairs from the sentence: {input_sentence}
'''

template_rel_4 = '''
You act like a computer function that finds relations within given text. 

You will have to extract all possible entity pairs from a sentence for a the given relation: Top_Member_Employees

I will give you a sentence, and you have to do the two step process:

1) Consider list of all pairs of named entities of the form: (ORGANIZATION, PERSON)
2) Return the pairs that fall in the category of the relation: Top_Member_Employees  

The relation Top_Member_Employees, means that you have to find the names of people in the sentence and the names of organizations and return those pairs where the person was/is in a high level position in that organization.

Be a little flexible, in terms of the entities you consider and make as many entity pairs as possible from the given sentence. Return those pairs in a proper format and satisfy the description of the relation.

Make sure that the entities you consider are proper nouns and do not fall in the category of pronouns like I, we, he, she, they etc.

Be sure to consider all pairs of named entities of the given form. Print analysis as well as output like a python list of tuples in plain text shown below:

Example:
input sentences is 
"He is the executive chairman and CEO of Microsoft , succeeding Steve Ballmer in 2014 as CEO[2][3]"

You print:

<Analysis>

Output:
[("Microsoft","Steve Ballmer")]

Provide me the extracted entity pairs from the sentence: {input_sentence}
''' 

PROMPT_TEMPLATES = {1: template_rel_1, 2: template_rel_2, 3: template_rel_3, 4: template_rel_4}
