from flask import Flask
from flask import render_template
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/about_us")
def about_us():
    return render_template('about_us.html')

order_information = {
    "order_number": 1,
    "order_items": ["Margherita", "Pepperoni"],
    "total_price": 10.00 
}

@app.route("/register")
def register():
    return render_template('register.html', **order_information)

@app.route("/reviews")
def reviews():
    return render_template('reviews.html')

@app.route("/kitchen")
def kitchenPage():
    data_list = []
    orderNumber=[]

    with open('orders.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for receipt in reader:
            orderNumber.extend(receipt)

    with open('bake.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data_list.extend(row)
    
    return render_template('kitchenScreen.html',
                           lista = data_list, orderNumber = orderNumber)


@app.route("/customer")
def customerPage():

    processingOrders=[]
    readyOrders=[]

    with open('preparing.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            processingOrders.extend(row)

  
    with open('ready.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            readyOrders.extend(row)

    return render_template('customerScreen.html',
                           processingOrders = processingOrders,
                           readyOrders = readyOrders)
