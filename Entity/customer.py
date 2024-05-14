from Exception.exceptions import InvalidDataException

class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__address = address

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        try:
            if not self.is_valid_email(value):
                raise InvalidDataException("Invalid email address format.")
        except InvalidDataException as e:
            print(e)
        else:
            self.__Email = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value
    
    def is_valid_email(self, email):
        if "@" in email and "." in email:
            return True
        else:
            return False