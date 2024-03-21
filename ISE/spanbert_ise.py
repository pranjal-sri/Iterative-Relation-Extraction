from SpanBERT.spanbert import SpanBERT
from .base_ise import BaseISE
from .utils import RELATIONS_DICT

class SpanBertISE(BaseISE):
    def __init__(self, GOOGLE_API_KEY, ENGINE_ID, GEMINI_ID):
        super().__init__(GOOGLE_API_KEY, ENGINE_ID, GEMINI_ID)
        self.spb = SpanBERT("./SpanBERT/pretrained_spanbert")

    def get_query_from_bank(self, query_bank):
        # Returns the query with maximum confidence from the query bank
        if len(query_bank) == 0: return None
        max_conf = float('-inf')
        q_max = None
        
        for q, conf in query_bank.items():
            if conf>max_conf:
                q_max = q
                max_conf = conf

        query_bank.pop(q_max) 
        return q_max    

    def filter_entityblocks(self, entity_blocks, relation_instruction):
        # Recives a list of candidate entities and filters them
        relation_preds = self.spb.predict(entity_blocks)
        n_extracted_relations = 0
        n_accepted_relations = 0
        ACCEPT, REJECT, DUPLICATE = 0, 1 ,2  
        for candidate, relation_prediction in zip(entity_blocks, relation_preds):
            relation, conf = relation_prediction
            if self.match_relation(relation, relation_instruction):
                STATE = REJECT
                n_extracted_relations += 1 

                sub, obj =  candidate['subj'][0], candidate['obj'][0]
                if conf >= self.conf_threshold:
                    if (sub, obj) in self.X:
                        if self.X[(sub, obj)] >= conf: STATE = DUPLICATE
                        else: STATE = ACCEPT
                        self.X[(sub, obj)] = max(self.X[sub, obj], conf)
                    else:
                        self.X[(sub, obj)] = conf
                        STATE = ACCEPT
                    q_cand = sub+ ' '+obj
                    q_cand = q_cand.lower()
                    if q_cand in self.query_bank:
                        self.query_bank[q_cand] = max(self.query_bank[q_cand], conf)
                    else:
                        if q_cand not in self.used_queries: self.query_bank[q_cand] = conf

                self.level_log('=== Extracted Relation ===', level =2) 
                self.level_log(f'Input tokens: {candidate["tokens"]}', level = 2)
                self.level_log(f'Output Confidence: {conf} ; Subject: {sub} ; Object: {obj} ;', level = 2)
                if STATE == REJECT:
                    self.level_log('Confidence is lower than threshold confidence. Ignoring this.', level = 2)
                elif STATE == DUPLICATE:
                    self.level_log('Duplicate with lower confidence than existing record. Ignoring this.', level = 2)
                else:
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
        self.level_log(f"Method       = spanbert")
        self.level_log(f"Relation     = {RELATIONS_DICT[relation_instruction]}")
        self.level_log(f"Threshold    = {threshold}")
        self.level_log(f"Query        = {seed_query}")
        self.level_log(f"# of Tuples  = {num_tuples}")
        self.level_log("Loading necessary libraries; This should take a minute or so ...)")
    
    def log_relations(self, relations, iterations):
        self.level_log(f"================== ALL RELATIONS for per:employee_of ( {len(relations)} ) =================")
        rel_list = [(k, v) for k, v in relations.items()]
        sorted_rel_list = sorted(rel_list, key= lambda x: -x[1])
        sorted_relations = {k: v for k, v in sorted_rel_list}

        for (subject, obj), confidence in sorted_relations.items():
            self.level_log(f"Confidence: {confidence:.8f}\t| Subject: {subject}\t| Object: {obj}")
        self.level_log(f"Total # of iterations = {iterations}")

    def ise(self, seed_query, k, relation_instruction, conf_threshold):
        self.print_start(relation_instruction, conf_threshold, seed_query, k)
        self.X = dict()
        self.query_bank = {seed_query.lower(): 100}
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

        self.log_relations(self.X, iteration)
        
