from Flask import Flask, request, session, render_template, redirect, send_from_directory

app = Flask(__name__)
app.secret_key = 'secret'  

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/add', methods=['POST'])
def add_to_cart():
    product = request.form['product']
    price = request.form['price']

    item = {'product': product, 'price': price}

    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append(item)
    session.modified = True
    return redirect('/cart')

@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    return render_template('cart.html', cart=cart)

@app.route('/remove/<int:index>')
def remove_item(index):
    cart = session.get('cart', [])
    if 0 <= index < len(cart):
        cart.pop(index)
        session.modified = True
    return redirect('/cart')

if __name__ == '__main__':
    app.run(debug=True)