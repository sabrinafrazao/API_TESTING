from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})


data_path = r'C:\Users\sabri\Desktop\API_TESTING\API\resources\Relatorio_cadop.csv'

try:
    providers_df = pd.read_csv(data_path, sep=';', encoding='utf-8', dtype=str)
    providers_df = providers_df.fillna('')  
except Exception as e:
    print(f"Error loading file: {e}")
    providers_df = pd.DataFrame() 

@app.route('/search', methods=['GET'])
def search_providers():

    """Search operators by term (q) in main fields"""

    try:
        search_term = request.args.get('q', '').lower().strip()
        
        if not search_term or providers_df.empty:
            return jsonify([])
        
      
        search_columns = ['Razao_Social', 'Nome_Fantasia', 'Cidade', 'UF', 'CNPJ']
        

        search_mask = pd.concat([providers_df[col].str.lower().str.contains(search_term, na=False) 
                         for col in search_columns], axis=1).any(axis=1)
        
        results = providers_df[search_mask].head(50).to_dict('records')
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
