import nltk
from nltk import pos_tag
from nltk import word_tokenize
from nltk.stem import SnowballStemmer

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
stop_words.remove('more')

def process_query(input_text):
    tokens = nltk.word_tokenize(input_text)
    tagged_tokens = nltk.pos_tag(tokens)
    
    # Filter out stopwords and non-alphanumeric tokens
    filtered_tokens = [word.lower() for word, tag in tagged_tokens if word.isalnum() and word.lower() not in stop_words]
    
    # Stemming the tokens
    sbst = SnowballStemmer('english')
    stemmed_tokens = [sbst.stem(word) for word in filtered_tokens]
    
    # Initialize variables
    select_column = ''
    from_table = ''
    where_clause = []
    
    # Determine from_table based on the input query
    if 'grid' in stemmed_tokens:
        from_table = 'grid_details'
    else:
        from_table = 'rf_stats'
    
    if stemmed_tokens[0] == 'ship' or stemmed_tokens[1] =='ship':
        select_column = 'ship_name'
    elif stemmed_tokens[0] == 'system':
        select_column = 'system'
    elif stemmed_tokens[0] == 'grid':
        select_column = 'grid_name'
    elif stemmed_tokens[0] == 'signal':
        select_column = 'system_signal'
    elif  stemmed_tokens[0] == 'snr':
        select_column = 'system_snr'
    elif stemmed_tokens[0] == 'blockage ':
        select_column = 'is_in_blockage'


    # Generate where_clause based on the input query
    for i in range(len(stemmed_tokens)):
        if stemmed_tokens[i] == 'more' and i + 1 < len(stemmed_tokens):
            if stemmed_tokens[i + 1].isdigit():
                where_clause.append({'column': 'grid_ram', 'relation': '>', 'value': int(stemmed_tokens[i + 1])})
        
        elif stemmed_tokens[i] == 'uptime' and i + 2 < len(stemmed_tokens):
            if stemmed_tokens[i + 1] == 'of' and stemmed_tokens[i + 2].isdigit():
                where_clause.append({'column': 'grid_uptime', 'relation': '>', 'value': int(stemmed_tokens[i + 2]) * 60})
        
        elif stemmed_tokens[i] == 'signal' and stemmed_tokens[i + 1] == 'strength':
            select_column = 'system_signal'
            from_table = 'rf_stats'
            if 'ship' in stemmed_tokens:
                ship_index = stemmed_tokens.index('ship')
                if stemmed_tokens[ship_index + 2].isdigit():
                    where_clause.append({'column': 'ship_name', 'relation': '=', 'value': stemmed_tokens[ship_index + 2]})
        
        # Add conditions for other test cases here
    
    # Generate output dictionary
    output = {
        'select_column': select_column,
        'from_table': from_table,
        'where': where_clause
    }
    
    return output

# Test the function with sample inputs
test_cases = [
    "Which ships have a grid with more than 50 gb ram?",
    "Which grid in nebula has more than 60gb ram?",
    "What are the grid versions currently active on the ship eta?",
    "When was grid hub1_LD5 updated on the ship gamma?",
    "Which ships have a grid consuming less than 20 gb memory but has an uptime of more than 6 hours?",
    "Which system is in the blockage on ship umbra?",
    "Name of the ship which is in blockage and has the first letter as ‘g’?",
    "What are the signal strength on the ship ‘mu’?",
    "Which ships have a sound to noise ratio of 50?",
    "Snr of SCPC_1 system in theta ship ?"
]

for query in test_cases:
    output = process_query(query)
    print(f"Input: {query}")
    print("Output:", output)
    print()
