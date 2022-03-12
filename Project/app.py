from flask import Flask, render_template, request, url_for, session, redirect

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        if request.form['signup'] == 'Sign up':
            return render_template('signup.html')

    else:
        print('get')
        return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/client_profile_management', methods=["POST", "GET"])
def client_profile_management():
    if request.method == "POST":
        fname = request.form['fname']
        address1 = request.form['address1']
        address2 = request.form['address2']
        city = request.form['city']
        state = request.form.get('state')
        zipcode = request.form['zipcode']
    
        # print(fname, address1, address2, city, state, zipcode)

        return render_template('client_profile_mgmt.html')

    else:
        return render_template('client_profile_mgmt.html')



@app.route('/fuel_quote_form', methods=["POST", "GET"])
def fuel_quote_form():
    if request.method == "POST":
        gallons_requested = request.form['gallons_requested']
        delivery_address = request.form['delivery_address']
        delivery_date = request.form['delivery_date']
        price_per_gallon = request.form['price_per_gallon']
        total_amount = request.form['total_amount']
    
        # print(gallons_requested, delivery_address, delivery_date)
        # print(price_per_gallon, total_amount)

        return render_template('fuel_quote_form.html')

    else:
        return render_template('fuel_quote_form.html')



@app.route('/fuel_quote_history')
def fuel_quote_history():
    return render_template('fuel_quote_history.html')


if __name__ == "__main__":
    app.run(debug=True)
