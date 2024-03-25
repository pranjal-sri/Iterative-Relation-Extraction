
import google.generativeai as genai
import ast

from .base_ise import BaseISE
from .utils import RELATIONS_DICT, RELEVANT_ENTITIES
from .prompt_templates import PROMPT_TEMPLATES

def generate_prompt_template(relation_instruction):
    template = PROMPT_TEMPLATES[relation_instruction]
    return template

def parse_gemini_output(output):
    # print("OUTPUT:" + output)
    output_line = output.strip(" \n").split('\n')[-1]
    # print("OUTPUT_LINE:"+output_line)

    try:
        tuple_list = ast.literal_eval(output_line.strip())
        return tuple_list
    except: 
        return []
    



class GeminiISE(BaseISE):
    def __init__(self, GOOGLE_API_KEY, ENGINE_ID, GEMINI_ID):
        super().__init__(GOOGLE_API_KEY, ENGINE_ID, GEMINI_ID) 
        genai.configure(api_key=GEMINI_ID)
        self.sentences_sent_to_gem = []


    def get_gemini_completion(self, prompt, max_tokens = 1000, temperature = 2, top_p = 0.4, top_k=32):

        # Initialize a generative model
        model = genai.GenerativeModel('gemini-pro')

        # Configure the model with your desired parameters
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k
        )

        # Generate a response
        response = model.generate_content(prompt, generation_config=generation_config)

        return response.text

    def filter_entityblocks(self, entity_blocks, relation_instruction, sentence):
        self.sentences_sent_to_gem.append(sentence)
        prompt = generate_prompt_template(relation_instruction).format(input_sentence = sentence)
        # Receives a list of candidate entities and filters them
        gemini_output = self.get_gemini_completion(prompt)
        related_entities = parse_gemini_output(gemini_output)
        
        n_extracted_relations = 0
        n_accepted_relations = 0
        ACCEPT, DUPLICATE = 0, 1 
        for candidate in related_entities:
            n_extracted_relations +=1

            sub, obj = candidate
            if (sub, obj) in self.X: 
                 STATE = DUPLICATE
            else: 
                STATE = ACCEPT
                self.X.add((sub, obj))

            q_cand = sub+ ' '+obj
            q_cand = q_cand.lower()
            if q_cand not in self.used_queries: self.query_bank.add(q_cand)

            self.level_log('=== Extracted Relation ===', level =2) 
            self.level_log(f'Sentence: {sentence}', level = 2)
            # self.level_log(f'Prompt: {prompt}')
            self.level_log(f'Subject: {sub} ; Object: {obj} ;', level = 2)
            if STATE == DUPLICATE:
                self.level_log('Duplicate. Ignoring this.', level = 2)
            elif STATE == ACCEPT:
                n_accepted_relations += 1
                self.level_log('Adding to set of extracted relations', level = 2)
            self.level_log('================\n', level = 2)
        return n_extracted_relations, n_accepted_relations

    def print_start(self, relation_instruction, threshold, seed_query, num_tuples):
        # 
        self.level_log("\n\n____")
        self.level_log("Parameters:")
        self.level_log(f"Client key   = {self.GOOGLE_API_KEY}")
        self.level_log(f"Engine key   = {self.ENGINE_ID}")
        self.level_log(f"Gemini key   = {self.GEMINI_ID}")
        self.level_log(f"Method       = gemini")
        self.level_log(f"Relation     = {RELATIONS_DICT[relation_instruction]}")
        self.level_log(f"Threshold    = {threshold}")
        self.level_log(f"Query        = {seed_query}")
        self.level_log(f"# of Tuples  = {num_tuples}")
        self.level_log("Loading necessary libraries; This should take a minute or so ...)")
    
    def get_query_from_bank(self, query_bank):
        if len(query_bank) == 0:
            return None
        return query_bank.pop()
        

    def log_relations(self, relation_instruction,
                      relations, iterations):
        relation_name = RELATIONS_DICT[relation_instruction]
        self.level_log(f"================== ALL RELATIONS for {relation_name} ( {len(relations)} ) =================")

        for (subject, obj) in relations:
            self.level_log(f"Subject: {subject}\t| Object: {obj}")
        self.level_log(f"Total # of iterations = {iterations}")

    def ise(self, seed_query, k, relation_instruction, conf_threshold):
        # import pdb; pdb.set_trace()
        self.print_start(relation_instruction, conf_threshold, seed_query, k)
        self.X = set()
        self.query_bank = set([seed_query.lower(),])
        self.used_queries = set()
        self.conf_threshold = conf_threshold
        iteration = 0
        while len(self.X)<k:
            iteration += 1
            q = self.get_query_from_bank(self.query_bank) 
            if q is None:
                print('ISE has "stalled" before retrieving k high-confidence tuples')
                self.log_relations(self.X)
               
            self.level_log(f'=========== Iteration: {iteration} - Query: {q} ===========')
            self.used_queries.add(q) 
            res = self.qm.query(q)
            urls = [result_item['URL'] for result_item in res]
            for i, url in enumerate(urls):
                self.level_log(f'URL ({i+1} / {len(urls)}): {url}')
                self.process_url(url, relation_instruction)

                if len(self.X)>= k: break

            self.log_relations(relation_instruction,  self.X, iteration)

        with open(f'gemini_sentences_rel_{relation_instruction}.txt', 'w') as f_g:
            for sent in self.sentences_sent_to_gem:
                print(str(sent), file=f_g)
        
