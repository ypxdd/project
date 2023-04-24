from flask import Flask, render_template, request, redirect, url_for, session
from Forms import CreateUserForm, CreateCustomerForm, LoginForm
import shelve, User, Customer
from datetime import date

app = Flask(__name__)
app.secret_key = 'Welcome'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/homeBuyer')
def home_buyer():
    return render_template('homeBuyer.html')

@app.route('/homeSeller')
def home_seller():
    return render_template('homeSeller.html')


@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data,
                         create_user_form.email.data, create_user_form.address1.data,
                         create_user_form.address2.data, create_user_form.gender.data,
                         create_user_form.membership.data, create_user_form.password.data, create_user_form.confirm_password.data,"Active",create_user_form.phone_number.data )
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        db.close()

        return redirect(url_for('retrieve_staffs'))
    return render_template('createUser.html', form=create_user_form)

@app.route('/createCustomer', methods=['GET', 'POST'])
def create_customer():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'c')

        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")
        customer = Customer.Customer(create_customer_form.first_name.data, create_customer_form.last_name.data,
                                     create_customer_form.gender.data, create_customer_form.email.data,
                                     create_customer_form.address1.data, create_customer_form.address2.data,
                                     create_customer_form.password.data, create_customer_form.confirm_password.data, 'Active', create_customer_form.phone_number.data)
##        customers_dict[customer.get_customer_id()] = customer
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        db.close()
        if create_customer_form.address2.data == 'S':
            return redirect(url_for('home_seller'))
        elif create_customer_form.address2.data == 'B':
            return redirect(url_for('home_buyer'))
        else:
            return redirect(url_for('home'))
    return render_template('createCustomer.html', form=create_customer_form)

@app.route('/retrieveStaffs')
def retrieve_staffs():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrieveStaffs.html', count=len(users_list), users_list=users_list)

@app.route('/retrieveCustomers')
def retrieve_customers():
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()

    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        customers_list.append(customer)

    return render_template('retrieveCustomers.html', count=len(customers_list), customers_list=customers_list)

@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_email(update_user_form.email.data)
        user.set_phone_number(update_user_form.phone_number)
        user.set_password(update_user_form.password)
        user.set_confirm_password(update_user_form.confirm_password)
        user.set_address1(update_user_form.address1.data)
        user.set_address2(update_user_form.address2.data)
        user.set_gender(update_user_form.gender.data)
        user.set_membership(update_user_form.membership.data)
        user.set_status(update_user_form.status.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_staffs'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.email.data = user.get_email()
        update_user_form.phone_number.data = user.get_phone_number()
        update_user_form.password.data = user.get_password()
        update_user_form.confirm_password.data = user.get_confirm_password()
        update_user_form.address1.data = user.get_address1()
        update_user_form.address2.data = user.get_address2()
        update_user_form.gender.data = user.get_gender()
        update_user_form.membership.data = user.get_membership()
        update_user_form.status.data = user.get_status

        return render_template('updateUser.html', form=update_user_form)

@app.route('/updateCustomer/<int:id>/', methods=['GET', 'POST'])
def update_customer(id):
    update_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and update_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']

        customer = customers_dict.get(id)
        customer.set_first_name(update_customer_form.first_name.data)
        customer.set_last_name(update_customer_form.last_name.data)
        customer.set_gender(update_customer_form.gender.data)
        customer.set_email(update_customer_form.email.data)
        customer.set_phone_number(update_customer_form.phone_number.data)
        customer.set_password(update_customer_form.password.data)
        customer.set_confirm_password(update_customer_form.confirm_password.data)
        customer.set_address1(update_customer_form.address1.data)
        customer.set_address2(update_customer_form.address2.data)
        customer.set_status(update_customer_form.status.data)
        db['Customers'] = customers_dict
        db.close()

        return redirect(url_for('login'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        update_customer_form.first_name.data = customer.get_first_name()
        update_customer_form.last_name.data = customer.get_last_name()
        update_customer_form.gender.data = customer.get_gender()
        update_customer_form.email.data = customer.get_email()
        update_customer_form.phone_number.data = customer.get_phone_number()
        update_customer_form.password.data = customer.get_password()
        update_customer_form.confirm_password.data = customer.get_confirm_password()
        update_customer_form.address1.data = customer.get_address1()
        update_customer_form.address2.data = customer.get_address2()
        update_customer_form.status.data = customer.get_status()

        return render_template('updateCustomer.html', form=update_customer_form)

@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()

    return redirect(url_for('retrieve_staffs'))

@app.route('/deleteCustomer/<int:id>', methods=['POST'])
def delete_customer(id):
    customers_dict = {}
    db = shelve.open('customer.db', 'w')
    customers_dict = db['Customers']
    customers_dict.pop(id)

    db['Customers'] = customers_dict
    db.close()

    return redirect(url_for('retrieve_customers'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    # customers_dict = {}
    users_dict = {}
    error = None
    if login_form.email.data == "admin@gmail.com" and login_form.password.data == "admin123":
        return redirect(url_for('homeStaff'))
    elif login_form.password.data == "":
        error = 'Forgot Password? Instructions sent to ' + login_form.email.data + '.'
    else:
        db = shelve.open('customer.db', 'r')
        customer_dict = db['Customers']
        print(db)
        db.close()
        # db = shelve.open('user.db', 'r')
        # user_dict = db['Users']
        # print(db)
        # db.close()
        # print("Checkpoint 1")
        # print(len(customer_dict))
        # print(type(customer_dict))
        # print(customer_dict.values())
        cust_list = list(customer_dict.values())

        for cus in cust_list:
            print(type(cus))
            print(cus.get_email())
            print(cus.get_address2())
            if cus.get_email() == login_form.email.data:
                if cus.get_password() == login_form.password.data:
                    if cus.get_status() == "Active":
                        print("Checkpoint 3")
                        session['Customer'] = cus.get_customer_id()
                        session['name'] = cus.get_first_name()
                        if cus.get_address2() == "B":
                            print("Hello")
                            return redirect(url_for('home_buyer'))
                        elif cus.get_address2() == "S":
                            print("Hi")
                            return redirect(url_for('home_seller'))
                error = "Invalid Credentials. Please try again."
                return render_template('login.html', form=login_form, error=error)
        #redirect('login.html')
        #return render_template('login.html', form=login_form, error=error)

    return render_template('login.html', form=login_form, error=error)


    # for email in customers_dict:
    #     print("Checkpoint 2")
    #     customer = customer_dict.get(email)
    #     if customer.get_email() == login_form.email.data:
    #         if customer.get_password() == login_form.password.data:
    #             if customer.get_status() == "Active":
    #                 print("Checkpoint 3")
    #                 session['Customer'] = customer.get_customer_id()
    #                 session['name'] = customer.get_first_name()
    #                 if customer.get_address2() == "Buyer":
    #                     print("Hello")
    #                     return redirect(url_for('homeBuyer'))
    #                 elif customer.get_address2() == "Seller":
    #                     print("Hi")
    #                     return redirect(url_for('homeSeller'))
     # for email in customers_dict:
     #    customer = customer_dict.get(email)
     #    if customer.get_email() == login_form.email.data and customer.get_password() == login_form.password.data and customer.get_status() == "Active" and
     #        session['Customer'] = customer.get_customer_id()
     #        session['name'] = customer.get_first_name()
     #        return redirect(url_for('homeSeller'))

    # for email in users_dict:
    #     print("Checkpoint user 2")
    #     user = user_dict.get(email)
    #     if user.get_email() == login_form.email.data and user.get_password() == login_form.password.data and user.get_status() == "Active":
    #         session['User'] = user.get_user_id()
    #         session['name'] = user.get_first_name(), user.get_last_name()
    #         return redirect(url_for('homeStaff'))
    #     else:
    #          redirect('login.html')
    # return render_template('login.html',form=login_form)




@app.route('/homeStaff')
def homeStaff():
    return render_template('homeStaff.html')

if __name__ == '__main__':
    app.run()


