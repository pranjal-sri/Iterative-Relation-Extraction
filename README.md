# Project: Information Extraction System

## Team Members:

- Pranjal Srivastava (ps3392)
- Shreyas Chatterjee (sc5290)

## Submitted Files:

- `project2.py`: Main entry point script for the Information Extraction System.
- `ISE/spanbert_ise.py`: Python script for information extraction using SpanBERT model.
- `ISE/gemini_ise.py`: Python script for information extraction using Google Gemini API.
- `ISE/base_ise.py`: Python script containing the base class for information extraction system.
- `ISE/utils.py`: Python script containing utility functions and constants used in information extraction.
- `README.txt`: This README file.
- `QueryManager/__init__.py` : Initialization file for the QueryManager package.
- `QueryManager/query_manager.py`: Python script containing the QueryManager class for querying search results.
- `requirements.txt` : Mentions all the libraries and packages that need to be installed

## Folder Structure:

- Main Folder - Iterative Relation Extraction
    - ISE Folder
        - __init__.py
        - base_ise.py
        - gemini_ise.py
        - spanbert_ise.py
        - utils.py
    - Query Manager Folder
        - __init__.py
        - query_manager.py
    - SpanBERT Folder (imported)
    - project2.py (main file)
    - README.md
    - requirements.txt

## Running the Program:

To run the program, follow these steps:

1. Set up the system like mentioned in the project description (python environment and apt-get package error)
2. Make sure that the environment is activated and navigate to inside the main folder
2. Install the required libraries and dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. When inside the main folder run the following-
    ```bash
    git clone https://github.com/larakaracasu/SpanBERT
    cd SpanBERT
    pip3 install -r requirements.txt
    bash download_finetuned.sh
    ```
4. In SpanBERT/spanbert.py, change the imports to 'from SpanBERT.pytorch_pretrained_bert.modeling' and 'from SpanBERT.pytorch_pretrained_bert.tokenization', i.e., the code should look like-
    ```bash
    #from transformers import AutoTokenizer, AutoModel, BertForSequenceClassification
    from SpanBERT.pytorch_pretrained_bert.modeling import BertForSequenceClassification
    from SpanBERT.pytorch_pretrained_bert.tokenization import BertTokenizer
    ```
6. Execute the main entry point script `project2.py` using Python:
    ```bash
    python3 project2.py [-spanbert|-gemini] <google api key> <google engine id> <google gemini api key> <r> <t> <q> <k>
    ```

## External Libraries Used:

- `spaCy`: Used for natural language processing tasks such as tokenization, part-of-speech tagging, and entity recognition.
- `requests`: Used for making HTTP requests to fetch webpage content.
- `beautifulsoup4`: Used for parsing HTML content fetched from webpages.
- `re`: Used for regular expression operations.
- `ast`: Used for parsing Gemini API output string to extract related entities.
- `google.generativeai`: Used for accessing the Google Gemini API.

## Internal Design:

- `project2.py`: Main entry point for the Information Extraction System. Orchestrates the execution of SpanBERT and Gemini information extraction scripts. It parses the arugements that are passed when we run the main file.
- `ISE/utils.py`: Contains variables and dictionaries which contain information about relations and the corresponding entities. These have been made to refer to whenver needed.
- `ISE/base_ise.py`: Contains the base class `BaseISE` for information extraction system. This file basically provides a base template for both spanbert based extraction and gemini based extraction. It has 4 completely defined functions - match_relation, process_url, download_text_from_url and process_sentence. The functions ise and filter_entity_blocks have been kept undefined here because spanbert and gemini need slightly different versions of the same.
- `ISE/spanbert_ise.py`: Implements information extraction using the SpanBERT model. It contains a class `SpanBertISE` which inherits from `BaseISE`.
- `ISE/gemini_ise.py`: Implements information extraction using the Google Gemini API. It contains a class `GeminiISE` which inherits from `BaseISE`.
- `QueryManager/query_manager.py`: Python script containing the QueryManager class for querying the url and obtain the search results.

## Step 3 Description:

Step 3 involves designing and implementing the information extraction process using two approaches: SpanBERT model and Google Gemini API. The SpanBERT approach utilizes a pre-trained BERT model for extracting relations from text, while the Gemini approach uses the Google Gemini API for natural language processing tasks.

#### Base Information Extraction Class (`base_ise.py`):

- `BaseISE` Class: Processes urls and creates a base template for both spanbert and gemini based extractions.
- `process_sentence`: Takes sentence and relation as input. Uses the relation and utils.py to get the entity of interest. Then uses the spacy_help_fucntions to create entity pairs. It finds the candidate pairs which match the entities of interest dscription and filters them accoridng to the requiements. It also keeps track of the extracted and accepted relations from the url.
- `download_text_from_url`: Takes url as a input and used BeautifulSoup to parse and url and extract the text. It is here that the 10000 character filter is applies to the text.
- `level_log`: Logs info and is used to maintian the appropriate printing format.
- `process_url`: Makes the right calls to the functions to download the text, extract the sentences using spacy. It also maintains the printing format and initialzations required for each url that is being processed.

#### SpanBERT Information Extraction (`spanbert_ise.py`):

- `SpanBertISE` Class: Implements information extraction using the SpanBERT model.
- `get_query_from_bank`: Retrieves the query with maximum confidence from the query bank for different iterations.
- `filter_entityblocks`: Filters candidate entity blocks based on relation predictions from SpanBERT.
- `print_start`: Prints information about the start of the extraction process for each iteration. Used to maintian the appropriate printing format.
- `log_relations`: Logs extracted relations and iterations. Used to maintian the appropriate printing format.
- `ise`: Executes the information extraction process using SpanBERT. It keeps track of the queries, runs the query to obtains urls, processes the urls and runs the iterations.

#### Google Gemini API Information Extraction (`gemini_ise.py`):

- `GeminiISE` Class: Implements information extraction using the Google Gemini API.
- `generate_prompt_template`: Generates prompt templates for Gemini API based on relation instruction.
- `parse_gemini_output`: Parses Gemini API output to extract related entities.
- `get_gemini_completion`: Fetches completion from Gemini API based on prompt.
- `filter_entityblocks`: Filters candidate entity blocks based on Gemini API output.
- `print_start`: Prints information about the start of the extraction process.
- `get_query_from_bank`: Retrieves the query from the query bank.
- `log_relations`: Logs extracted relations and iterations.
- `ise`: Executes the information extraction process using Google Gemini API.

## Google Custom Search Engine API Key and Engine ID:

Pranjal Srivastava
- **API Key:** AIzaSyDuSM_JnE7BUIaW54cgZLIcNgEwm79URsg
- **Engine ID:** 3430a164067404160

Shreyas Chatterjee
- **API Key:** AIzaSyBdyvstyytiLSY0jPXM1FV9JfGmDaoZ3iY
- **Engine ID:** 91edb5a90f6c44a6a

## Additional Information:

The setup has to be same for it to run end to end.

### Details about Query Manager Class from Project 1 (`QueryManager/query_manager.py`):

- `QueryManager` Class: Implements querying of search results using the Google Custom Search Engine API.
- `__init__`: Initializes the QueryManager object with required parameters such as API key, engine ID, and number of results.
- `__repr__`: Provides a string representation of the QueryManager object.
- `query`: Executes a query to retrieve search results based on the specified query string.
- `__verify_results`: Verifies the integrity of search results to ensure they meet the required conditions.
- `__parse_results`: Parses the search results and extracts relevant information such as URLs, titles, and snippets.