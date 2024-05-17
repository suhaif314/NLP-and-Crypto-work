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
  
    filtered_tokens = [word.lower() for word, tag in tagged_tokens if word.isalnum() and word.lower() not in stop_words]

    sbst = SnowballStemmer('english')
    stemmed_tokens = [sbst.stem(word) for word in filtered_tokens]
 
    select_column = ''
    from_table = ''
    where_clause = []

    if 'grid' in stemmed_tokens:
        from_table = 'grid_details'
    else:
        from_table = 'rf_stats'
    
    if 'grid' in stemmed_tokens:
        select_column = 'grid_name'
    elif 'signal' in stemmed_tokens and 'strength' in stemmed_tokens:
        select_column = 'system_signal'
    elif 'snr' in stemmed_tokens:
        select_column = 'system_snr'
    elif 'blockage' in stemmed_tokens:
        select_column = 'is_in_blockage'
    else:
        select_column = 'ship_name'  
    
    for i in range(len(stemmed_tokens)):
        if stemmed_tokens[i] == 'more' and i + 1 < len(stemmed_tokens):
            if stemmed_tokens[i + 1].isdigit():
                where_clause.append({'column': 'grid_ram', 'relation': '>', 'value': int(stemmed_tokens[i + 1])})
        
        elif stemmed_tokens[i] == 'uptime' and i + 2 < len(stemmed_tokens):
            if stemmed_tokens[i + 1] == 'of' and stemmed_tokens[i + 2].isdigit():
                where_clause.append({'column': 'grid_uptime', 'relation': '>', 'value': int(stemmed_tokens[i + 2]) * 60})
        
        elif stemmed_tokens[i] == 'signal' and stemmed_tokens[i + 1] == 'strength':
            if 'ship' in stemmed_tokens:
                ship_index = stemmed_tokens.index('ship')
                if ship_index + 2 < len(stemmed_tokens) and stemmed_tokens[ship_index + 2].isdigit():
                    where_clause.append({'column': 'ship_name', 'relation': '=', 'value': stemmed_tokens[ship_index + 2]})

        elif stemmed_tokens[i] == 'in' and 'blockage' in stemmed_tokens:
            if 'ship' in stemmed_tokens:
                ship_index = stemmed_tokens.index('ship')
                if stemmed_tokens[ship_index + 2].isdigit():
                    where_clause.append({'column': 'ship_name', 'relation': '=', 'value': stemmed_tokens[ship_index + 2]})
            where_clause.append({'column': 'is_in_blockage', 'relation': '=', 'value': '1'})
        
        elif 'grid' in stemmed_tokens and 'grid_uptime' in stemmed_tokens:
            select_column = 'ship_name'
            if 'more' in stemmed_tokens and 'than' in stemmed_tokens:
                more_index = stemmed_tokens.index('more')
                than_index = stemmed_tokens.index('than')
                if more_index + 1 < len(stemmed_tokens) and than_index + 1 < len(stemmed_tokens) and stemmed_tokens[more_index + 1].isdigit():
                    where_clause.append({'column': 'grid_ram', 'relation': '<', 'value': int(stemmed_tokens[more_index + 1])})
                    where_clause.append({'column': 'grid_uptime', 'relation': '>', 'value': 6 * 60})
        
        elif 'system' in stemmed_tokens and 'in' in stemmed_tokens and 'blockage' in stemmed_tokens:
            select_column = 'system'
            if 'ship' in stemmed_tokens:
                ship_index = stemmed_tokens.index('ship')
                if ship_index + 1 < len(stemmed_tokens):
                    where_clause.append({'column': 'ship_name', 'relation': '=', 'value': stemmed_tokens[ship_index + 1]})
            where_clause.append({'column': 'is_in_blockage', 'relation': '=', 'value': '1'})

        elif 'blockage' in stemmed_tokens and stemmed_tokens[0] == 'name':
            select_column = 'ship_name'
            where_clause.append({'column': 'is_in_blockage', 'relation': '=', 'value': '1'})
            where_clause.append({'column': 'ship_name', 'relation': 'LIKE', 'value': stemmed_tokens[-1][0] + '%g'}) 

        elif 'signal' in stemmed_tokens and 'strength' in stemmed_tokens:
            select_column = 'system_signal_strength'
            if 'ship' in stemmed_tokens:
                ship_index = stemmed_tokens.index('ship')
                if ship_index + 2 < len(stemmed_tokens):
                    where_clause.append({'column': 'ship_name', 'relation': '=', 'value': stemmed_tokens[ship_index + 2]})

        elif 'sound' in stemmed_tokens and 'noise' in stemmed_tokens and 'ratio' in stemmed_tokens and 'of' in stemmed_tokens:
            select_column = 'ship_name'
            if '50' in stemmed_tokens:
                where_clause.append({'column': 'system_snr', 'relation': '=', 'value': '50'})

        elif 'snr' in stemmed_tokens and 'system' in stemmed_tokens:
            select_column = 'system_snr'
            if 'ship' in stemmed_tokens:
                ship_index = stemmed_tokens.index('ship')
                if ship_index + 2 < len(stemmed_tokens):
                    where_clause.append({'column': 'ship_name', 'relation': '=', 'value': stemmed_tokens[ship_index + 2]})
            if 'theta' in stemmed_tokens and 'SCPC_1' in stemmed_tokens:
                pass

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
