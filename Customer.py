import User

class Customer:
    count_id = 0

    def __init__(self, first_name, last_name, gender, email, address1, address2, password, confirm_password, status, phone_number):
        Customer.count_id += 1
        self.__customer_id = Customer.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__address1 = address1
        self.__address2 = address2
        self.__gender = gender
        self.__password = password
        self.__confirm_password = confirm_password
        self.__status = status
        self.__phone_number = phone_number


    # accessor methods
    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender

    def get_address1(self):
        return self.__address1

    def get_address2(self):
        return self.__address2

    def get_password(self):
        return self.__password

    def get_confirm_password(self):
        return self.__confirm_password

    def get_status(self):
        return self.__status

    def get_phone_number(self):
        return self.__phone_number


    # mutator methods
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_gender(self, gender):
        self.__gender = gender

    def set_address1(self, address1):
        self.__address1 = address1

    def set_address2(self, address2):
        self.__address2 = address2

    def set_password(self, password):
        self.__password = password

    def set_confirm_password(self, confirm_password):
        self.__confirm_password = confirm_password

    def set_status(self, status):
        self.__status = status

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number






