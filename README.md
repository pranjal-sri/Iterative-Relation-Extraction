# Project: Information Extraction System

## Team Members:

- Your Name (Your Columbia UNI)
- Teammate's Name (Teammate's Columbia UNI)

## Submitted Files:

- `ise.py`: Main entry point script for the Information Extraction System.
- `spanbert_ise.py`: Python script for information extraction using SpanBERT model.
- `gemini_ise.py`: Python script for information extraction using Google Gemini API.
- `base_ise.py`: Python script containing the base class for information extraction system.
- `utils.py`: Python script containing utility functions and constants used in information extraction.
- `prompt_templates.py`: Python script containing prompt templates for Gemini API.
- `README.txt`: This README file.
- `QueryManager/__init__.py` : Initialization file for the QueryManager package.
- `QueryManager/query_manager.py`: Python script containing the QueryManager class for querying search results.

## Running the Program:

To run the program, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required libraries and dependencies:
    ```bash
    pip install spacy requests beautifulsoup4
    ```
3. Set up a Google Custom Search Engine and obtain the JSON API Key and Engine ID.
4. Clone the project repository to your local machine.
5. Replace the placeholders `GOOGLE_API_KEY` and `ENGINE_ID` in the scripts `spanbert_ise.py` and `gemini_ise.py` with your actual Google API Key and Engine ID.
6. Execute the main entry point script `ise.py` using Python:
    ```bash
    python ise.py
    ```

## External Libraries Used:

- `spaCy`: Used for natural language processing tasks such as tokenization, part-of-speech tagging, and entity recognition.
- `requests`: Used for making HTTP requests to fetch webpage content.
- `beautifulsoup4`: Used for parsing HTML content fetched from webpages.
- `re`: Used for regular expression operations.
- `ast`: Used for parsing Gemini API output string to extract related entities.
- `google.generativeai`: Used for accessing the Google Gemini API.

## Internal Design:

- `ise.py`: Main entry point for the Information Extraction System. Orchestrates the execution of SpanBERT and Gemini information extraction scripts.
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
- `filter_entityblocks`: Filters candidate entity blocks based on relation predictions from SpanBERT.
- `print_start`: Prints information about the start of the extraction process.
- `log_relations`: Logs extracted relations and iterations.
- `ise`: Executes the information extraction process using SpanBERT.

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

### Base Information Extraction Class (`base_ise.py`):

- `BaseISE` Class: Contains the base class for information extraction system.
- `process_sentence`: Processes a sentence to find matching entities for extraction.
- `level_log`: Logs messages with indentation based on log level.
- `download_text_from_url`: Downloads text content from a given URL.
- `process_url`: Processes a URL by downloading text and processing sentences.
- `match_relation`: Matches predicted relation with predefined relation templates.
- `ise`: Abstract method for executing the information extraction process.
- `filter_entityblocks`: Abstract method for filtering entity blocks.

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