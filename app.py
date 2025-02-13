from flask import Flask, jsonify, request
import pandas as pd
app = Flask(__name__)
merged_data = pd.read_csv('merged_data_clean.csv')
if 'year' in merged_data.columns:
    merged_data.drop(columns=['year'], inplace=True)

@app.route('/data', methods=['GET'])
def get_country_data():
    country = request.args.get('country', default=None, type=str)
    if country:
        result = merged_data[merged_data['country'].str.lower() == country.lower()]
        if not result.empty:
            return jsonify(result.to_dict(orient='records')[0])
        else:
            return jsonify({"error": "Country not found"}), 404
    else:
        # If no country specified, return data for all countries
        all_countries = merged_data.to_dict(orient='records')
        return jsonify(all_countries)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
