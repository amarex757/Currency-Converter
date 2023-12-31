from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = 'your keys'
# 

#example from the website docs
#use it to understand how I did it
@app.route('/docs', methods=['GET'])
def docs():
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo'
    r = requests.get(url)
    data = r.json()
    print(data)
    return data	

if __name__ == "__main__":
	app.run(debug=True)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		try:
			amount = request.form['amount']
			amount = float(amount)
			
			# in order to display in decimals
			# try to get the request from the html
			convert_from = request.form['convert_from']
			convert_to = request.form['convert_to']
			
			# linking the API
			# adding convert_from and convert_to
			url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={convert_from}&to_currency={convert_to}&apikey={API_KEY}'
			
            # making use of python requests to get the Api
			response = requests.get(url).json()
			
            # getting the particular API property
			# like the exchange rate
			Exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
			Exchange_rate = float(Exchange_rate) #inorder to display in decimals
			
            #multiplying the exchange rate by the amount
			result = Exchange_rate * amount
			
            #getting other responses 
			convert_from_code = response['Realtime Currency Exchange Rate']['1. From_Currency Code']
			convert_from_name = response['Realtime Currency Exchange Rate']['2. From_Currency Name']
			convert_to_code = response['Realtime Currency Exchange Rate']['3. To_Currency Code']
			convert_to_name = response['Realtime Currency Exchange Rate']['4. To_Currency Name']
			updated_time = response['Realtime Currency Exchange Rate']['6. Last Refreshed']
			return render_template('home.html',
						            result=round(result, 2), 
						            amount=amount,
						            convert_from_code=convert_from_code, 
						            convert_from_name=convert_from_name,
						            convert_to_code=convert_to_code, 
						            convert_to_name=convert_to_name, 
						            updated_time=updated_time)
		
        # if the request failed

		except Exception as e:
			return f"<h1> Bad request : {e} </h1>"
             
	else:
		return render_template('home.html')