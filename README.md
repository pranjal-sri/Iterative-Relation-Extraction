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

- `project2.py`: Main entry point for the Information Extraction System. Orchestrates the execution of SpanBERT and Gemini information extraction scripts.
- `spanbert_ise.py`: Implements information extraction using the SpanBERT model. It contains a class `SpanBertISE` which inherits from `BaseISE`.
- `gemini_ise.py`: Implements information extraction using the Google Gemini API. It contains a class `GeminiISE` which inherits from `BaseISE`.
- `base_ise.py`: Contains the base class `BaseISE` for information extraction system.
- `utils.py`: Contains utility functions and constants such as `RELATIONS_DICT`, `RELEVANT_ENTITIES`, and `RELATIONS_INTERNAL_REP`.
- `prompt_templates.py`: Contains prompt templates for generating prompts to be used with Google Gemini API.

## Step 3 Description:

Step 3 involves designing and implementing the information extraction process using two approaches: SpanBERT model and Google Gemini API. The SpanBERT approach utilizes a pre-trained BERT model for extracting relations from text, while the Gemini approach uses the Google Gemini API for natural language processing tasks.

#### SpanBERT Information Extraction (`spanbert_ise.py`):

- `SpanBertISE` Class: Implements information extraction using the SpanBERT model.
- `get_query_from_bank`: Retrieves the query with maximum confidence from the query bank.
- `filter_sentence`: Filters candidate entity blocks of a sentence based on relation predictions from SpanBERT.
- `print_start`: Prints information about the start of the extraction process.
- `log_relations`: Logs extracted relations and iterations.
- `ise`: Executes the information extraction process using SpanBERT.

#### Google Gemini API Information Extraction (`gemini_ise.py`):

- `GeminiISE` Class: Implements information extraction using the Google Gemini API.
- `generate_prompt_template`: Generates prompt templates for Gemini API based on relation instruction.
- `parse_gemini_output`: Parses Gemini API output to extract related entities.
- `get_gemini_completion`: Fetches completion from Gemini API based on prompt.
- `filter_sentence`: Filters candidate sentences based on Gemini API output.
- `print_start`: Prints information about the start of the extraction process.
- `get_query_from_bank`: Retrieves the query from the query bank.
- `log_relations`: Logs extracted relations and iterations.
- `ise`: Executes the information extraction process using Google Gemini API.

### Base Information Extraction Class (`base_ise.py`):

- `BaseISE` Class: Contains the base class for information extraction system.
- `process_sentence`: Processes a sentence to find matching entities for extraction.
- `level_log`: Logs messages with indentation based on log level.
- `download_text_from_url`: Downloads text content from a given URL.
- `process_url`: Processes a URL by downloading text and processing sentences.
- `match_relation`: Matches predicted relation with predefined relation templates.
- `ise`: Abstract method for executing the information extraction process.
- `filter_sentence`: Abstract method for filtering entity blocks.

## Query Manager Class (`QueryManager/query_manager.py`):

- `QueryManager` Class: Implements querying of search results using the Google Custom Search Engine API.
- `__init__`: Initializes the QueryManager object with required parameters such as API key, engine ID, and number of results.
- `query`: Executes a query to retrieve search results based on the specified query string.
- `__verify_results`: Verifies the integrity of search results to ensure they meet the required conditions.
- `__parse_results`: Parses the search results and extracts relevant information such as URLs, titles, and snippets.
- `__extract_text_from_url`: Extracts text content from a given URL using web scraping techniques.
- `__repr__`: Provides a string representation of the QueryManager object.

## Google Custom Search Engine API Key and Engine ID:

- API Key: `[Your Google Custom Search Engine JSON API Key]`
- Engine ID: `[Your Google Custom Search Engine ID]`

## Additional Information:

The project is designed to extract information from web pages based on predefined relations such as `Schools_Attended`, `Work_For`, `Live_In`, and `Top_Member_Employees`. SpanBERT is used for contextualized representation learning, while Google Gemini API is utilized for generating prompts and extracting relations. The project is designed to run on a Google Cloud VM with appropriate memory and configurations.The `QueryManager` class satisfies the conditions mentioned in the project description by providing a robust mechanism for querying search results, verifying their integrity, and extracting relevant information from them.