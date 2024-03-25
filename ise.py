from ISE.spanbert_ise import SpanBertISE
from ISE.gemini_ise import GeminiISE
import sys

def parse_arguments():
    args = sys.argv[1:]
    if len(args) != 8:
        print("Usage: python3 project2.py [-spanbert|-gemini] <google api key> <google engine id> <google gemini api key> <r> <t> <q> <k>")
        sys.exit(1)

    mode = args[0]
    if mode not in ["-spanbert", "-gemini"]:
        print("Please specify either -spanbert or -gemini")
        sys.exit(1) 

    google_api_key = args[1]
    google_engine_id = args[2]
    gemini_api_key = args[3]
    
    try:
        r = int(args[4])
        t = float(args[5])
        q = args[6]
        k = int(args[7])
    except ValueError:
        print("Error: r and k must be integers, t must be a float, and q must be a string.")
        sys.exit(1)

    return mode, google_api_key, google_engine_id, gemini_api_key, r, t, q, k


def main():
    mode, google_api_key, google_engine_id, gemini_api_key, r, t, q, k = parse_arguments()
    # print("Mode:", mode)
    # print("Google API Key:", google_api_key)
    # print("Google Engine ID:", google_engine_id)
    # print("Google Gemini API Key:", gemini_api_key)
    # print("Relation Instruction:", r)
    # print("Threshold:", t)
    # print("Query:", q)
    # print("K:", k)
    # import pdb; pdb.set_trace();
    f = open(f'out_gemini_rel_{r}.log', 'w')
    original_out = sys.stdout
    sys.stdout = f

    if mode == '-spanbert':
        ise = SpanBertISE(google_api_key, google_engine_id, gemini_api_key)
    else:
        ise = GeminiISE(google_api_key, google_engine_id, gemini_api_key)
    
    ise.ise(q, k, r, t)
    
    sys.stdout = original_out
    
if __name__ == "__main__":
    main()
