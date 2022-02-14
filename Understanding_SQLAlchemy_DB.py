# required imports
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template

# import to create our database model
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

# importing our custom form
from forms import CustomerForm

# import to create our base class
# base class stores a catalog of classes and mapped tables in the Declarative system
from sqlalchemy.ext.declarative import declarative_base

# *******************************Seting up the database*********************************************
# creating database
# create_engine() function is called to set up an engine object which is subsequently used to
# perform SQL operations.The function has two arguments, one is the name of the database and
# other is an echo parameter when set to True will generate the activity log.
engine = create_engine("sqlite:///sales.db", echo=True)

# The declarative_base() function is used to create base class
Base = declarative_base()

# create our customer model for database


class Customers(Base):
    __tablename__ = "Customers"

    sno = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    address = Column(String(500), nullable=False)
    email = Column(String(200), nullable=False)


Base.metadata.create_all(engine)

# A session object is the handle to database. Session class is defined using sessionmaker()
Session = sessionmaker(bind=engine)

# The session object is then set up using its default constructor
session = Session()

# *******************************Seting up our app************************************************

# create the flast instance
app = Flask(__name__)
app.config['SECRET_KEY'] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'


# *******************************Api to handle the home page**************************************
# create route to home
@app.route('/')
def home_page():
    return render_template('home.html')

# create route for customer list

# *******************************Api to handle the customers**************************************
@app.route('/customers')
def customer():
    # adding objects to the database
    c1 = Customers(name="Neeraj Shankar", address=" Indore, Madhya Pradesh",
                   email="iamneerajshankar@outlook.com")
    session.add(c1)

    # To add multiple records, we used the add_all() method of the session class.
    session.add_all([
        Customers(name='Rahul Yadav', address='Indore,Madhya Pradesh',
                  email='rahul.test@gmail.com'),
        Customers(name='Praveen Shankar', address='Sector 40, Noida',
                  email='praveen.test@gmail.com'),
        Customers(name='Chetan Mandloi', address='Budhwar Peth, Pune', email='chetan.test@gmail.com')]

    )
    session.commit()
    customer_list = session.query(Customers).all()
    return render_template('customers.html', customer_list=customer_list)


@app.route('/customer/add', methods=['GET', 'POST'])
def add_customer():
    form = CustomerForm()
    return render_template("add-customer.html", form=form)


# *******************************Configuration Settngs to run app*********************************
# driver code
if __name__ == "__main__":
    app.run(debug=True, port=8000)
