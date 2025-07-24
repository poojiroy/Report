from flask import Flask, request, jsonify
from app.weather import get_weather_data

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400

    data = get_weather_data(city)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
