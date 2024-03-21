from .utils import RELATIONS_DICT, RELEVANT_ENTITIES, RELATIONS_INTERNAL_REP
from QueryManager import QueryManager
import spacy
from SpanBERT.spacy_help_functions import create_entity_pairs

from bs4 import BeautifulSoup
import re
import requests
import requests.exceptions as rexceptions

class BaseISE:
    def __init__(self, GOOGLE_API_KEY, ENGINE_ID, GEMINI_ID):
        self.GOOGLE_API_KEY = GOOGLE_API_KEY
        self.ENGINE_ID = ENGINE_ID
        self.GEMINI_ID = GEMINI_ID
        self.qm = QueryManager(GOOGLE_API_KEY, ENGINE_ID)
        self.nlp = spacy.load("en_core_web_lg")  
        self.url_stats = {'sentences_with_annotations': 0, 'candidate_relations':0,  'accepted_relations': 0}
        self.o = 'output.log'

    def process_sentence(self, sentence, relation_instruction):
        # Processes a sentence to find all matching entities. The list of these matching entities is sent to 
        # `filter_entityblocks(self, entity_blocks, relation_instruction):`

        entities_of_interest = list(RELEVANT_ENTITIES[relation_instruction])
        entity_pairs = create_entity_pairs(sentence, entities_of_interest)

        candidates = []
        for candidate in entity_pairs:
            tokens, e1, e2 = candidate
            if e1[1] == entities_of_interest[0] and e2[1] == entities_of_interest[1]:
                candidates.append({"tokens": tokens, "subj": e1, "obj": e2})
            if e2[1] == entities_of_interest[0] and e1[1] == entities_of_interest[1]: 
                candidates.append({"tokens": tokens, "subj": e2, "obj": e1})
            
        if len(candidates) == 0:
            return
        
        n_extracted_relations, n_accepted_relations = self.filter_entityblocks(candidates, relation_instruction)
        if n_extracted_relations>0: self.url_stats['sentences_with_annotations'] += 1
        self.url_stats['candidate_relations'] += n_extracted_relations
        self.url_stats['accepted_relations'] += n_accepted_relations

    
    def level_log(self, message, level =0, mode = 'a'):
        indent = ['\t'] * level
        indent = ''.join(indent)
        # with open(, mode) as f: 
        print(f"{indent}{message}") 

    def download_text_from_url(self, url):
        try:
            self.level_log('Fetching text from url...', level = 1)
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                text = soup.get_text()
                text = re.sub(r'\n+', '\n', text)
                text = re.sub(r'\t+', '\t', text)
                if text is not None and len(text)>10000:
                    self.level_log(f'trimming webpage length from {len(text)} to 10000', level = 1)
                    text = text[:10000]
                self.level_log(f'Webpage length (num characters): {len(text)}', level= 1)
                return text
            else:
                self.level_log(f"Failed to retrieve content from URL: {url}. Status code: {response.status_code}", level = 1)
                return None
        except Exception as e:
            self.level_log(f"An error occurred while extracting text from URL: {url}", 1)
            self.level_log(f"Error details: {str(e)}", 1)
            return None
    
    def process_url(self, url, relation_instruction):
        text = self.download_text_from_url(url)
        if text is None:
            self.level_log('Skipping the URL as no text was extracted', level = 1)
            return
        
        self.level_log('Annotating the webpage using spacy ...', level = 1)
        doc = self.nlp(text)
        sentences = list(doc.sents)
        self.level_log(f'Extracted {len(sentences)} sentences. Processing each sentence one by one to check for presence of right pair of named entity types; if so, will run the second pipeline ...', level = 1)
        
        for i, sentence in enumerate(sentences):
            if((i+1)%5 == 0): self.level_log(f'Processed {i+1} / {len(sentences)} sentences', level = 1)
            self.process_sentence(sentence, relation_instruction)
        
        self.level_log('\n')
        self.level_log(f'Extracted annotations for  {self.url_stats["sentences_with_annotations"]}  out of total  {len(sentences)}  sentences', level = 1)
        self.level_log(f'Relations extracted from this website: {self.url_stats["accepted_relations"]} (Overall: {self.url_stats["candidate_relations"]})', level = 1)
        self.level_log('\n')
        self.url_stats["sentences_with_annotations"] = 0
        self.url_stats["relations_extracted"] = 0
        self.url_stats["candidate_relations"] = 0

    def match_relation(self, predicted_relation, relation_instruction):
        match_template = RELATIONS_INTERNAL_REP[relation_instruction]
        if type(match_template) is str:
            match_template = [match_template,]
        
        if predicted_relation in match_template:
            return True
        else:
            return False

    def ise(self, seed_query, k, relation_instruction, conf_threshold):
        raise NotImplementedError

    def filter_entityblocks(self, entity_blocks, relation_instruction):
        raise NotImplementedError