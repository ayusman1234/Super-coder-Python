#!/usr/bin/env python
# coding: utf-8

# In[8]:


def check_type(type):
    vehicle_type=['TwoWheeler', 'FourWheeler']
    if type not in vehicle_type:
            return 0
    return 1
class Vehicle:
    def __init__(self):
        self.__vehicle_cost=None
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__premium_amount=None
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def set_vehicle_type(self,vehicle_type):
        if check_type(vehicle_type):
            self.__vehicle_type=vehicle_type
        else:
            return "invalid Vehicle DETAILS"4rew
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type    
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
    def get_premium_amount(self):
        return self.__premium_amount
    def calculate_premium(self):
        if self.__vehicle_type=="TwoWheeler":
            self.__premium_amount=self.__vehicle_cost*2/100
        elif self.__vehicle_type=="FourWheeler":
            self.__premium_amount=self.__vehicle_cost*6/100
        else:
            print("Invalid Vehicle Type")
    def display_vehicle_details(self):
        print(self.__vehicle_type, self.__vehicle_cost, int(self.__premium_amount))
v1 = Vehicle()
v1.set_vehicle_type(input())
v1.set_vehicle_cost(int(input()))
v1.calculate_premium()
v1.display_vehicle_details()


# In[4]:


class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
    def set_marks(self,marks):
        self.__marks=marks
    def set_age(self,age):
        self.__age=age
    def set_student_id(self,student_id):
        self.__student_id=student_id    
    def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    def validate_age(self):
        return self.__age > 20
    def validate_marks(self):
        return 0<=self.__marks<=100    
    def check_qualification(self):
        return self.validate_marks() and self.validate_age() and self.__marks>=65
    class Student:
        dic={1001:25575.0,1002:15500.0}
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
        self.__course_id=None
        self.__fees=None
        def choose_course(self,course_id):
            if course_id in self.dic.keys():
            self.__course_id=course_id
            self.__fees=self.dic[course_id]
            if self.__marks>85:
                self.__fees=self.dic[course_id]-self.dic[course_id]*25/100
                return True
        else:
            return False       
    def set_student_id(self,student_id):
        self.__student_id=student_id    
    def set_marks(self,marks):
        self.__marks=marks
    def set_age(self,age):
        self.__age=age
        def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    def get_course_id(self):
        return self.__course_id
    def get_fees(self):
        return self.__fees
    def validate_age(self):
        return self.__age > 20
    def validate_marks(self):
        return 0<=self.__marks<=100
    def check_qualification(self):
        return self.validate_marks() and self.validate_age() and self.__marks>=65
    maddy=Student()
maddy.set_student_id(1001)
maddy.set_age(21)
maddy.set_marks(65)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")    


# In[24]:


class Student:
    def __init__ (self):
            self.__student_id=None
            self.__age=None
            self.__marks=0
            self.__course_id=None
            self.__fees=None           
    def set_student_id(self, student_id):
            self.__student_id = student_id
    def get_student_id(self):
        return self.__student_id
    def set_age(self, age):
            self.__age = age
    def get_age(self):
        return self.__age       
    def set_marks(self, marks):
            self.__marks =marks
    def get_marks(self):
        return self.__marks        
    def get_course_id(self):
        return self.__course_id
    def get_fees(self):
        return self.__fees        
    def validate_marks(self):
             if(self.__marks>=0 and self.__marks<=100):
                return True
            else:
                return False       
    def validate_age(self):
            if(self.__age>20):
                return True
            else:
                return False                 
    def check_qualification(self):
            if(self.__age>20 and self.__marks>=65 and self.validate_marks()):
                return True
            else:
                return False       
    def choose_course(self,course_id):
        if(self.check_qualification() and (course_id==1001 or course_id==1002)):
            self.__course_id=course_id
            if(course_id==1001):
                self.__fees=25575.0
            elif(course_id==1002):
                self.__fees=15500.0
            if(self.__marks>85):
                self.__fees=self.__fees-(self.__fees*25/100)
            return True
        return False    
maddy=Student()
maddy.set_student_id(1001)
maddy.set_age(21)
maddy.set_marks(84)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")


# In[25]:


class Student:
    def __init__ (self):
            self.__student_id=None
            self.__age=None
            self.__marks=0
            self.__course_id=None
            self.__fees=None
            
    def set_student_id(self, student_id):
            self.__student_id = student_id
    def get_student_id(self):
        return self.__student_id
    
    def set_age(self, age):
            self.__age = age
    def get_age(self):
        return self.__age   
    
    def set_marks(self, marks):
            self.__marks =marks
    def get_marks(self):
        return self.__marks
        
    def get_course_id(self):
        return self.__course_id
    def get_fees(self):
        return self.__fees
        
    def validate_marks(self):
             if(self.__marks>=0 and self.__marks<=100):
                 return True
             else:
                 return False   
    
    def validate_age(self):
            if(self.__age>20):
                 return True
            else:
                 return False
                 
    def check_qualification(self):
            if(self.__age>20 and self.__marks>=65 and self.validate_marks()):
                 return True
            else:
                 return False
        
    def choose_course(self,course_id):
        if(self.check_qualification() and (course_id==1001 or course_id==1002)):
            self.__course_id=course_id
            if(course_id==1001):
                self.__fees=25575.0
            elif(course_id==1002):
                self.__fees=15500.0
            if(self.__marks>85):
                self.__fees=self.__fees-(self.__fees*25/100)
            return True
        return False
    
maddy=Student()
maddy.set_student_id(1001)
maddy.set_age(21)
maddy.set_marks(84)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")


# In[1]:


class Customer:
    def __init__(self, customer_name, quantity):
        self.__customer_name = customer_name
        self.__quantity = quantity

    def get_customer_name(self):
        return self.__customer_name

    def get_quantity(self):
        return self.__quantity

    def validate_quantity(self):
        if self.__quantity >= 1 and self.__quantity <= 5:
            return True
        return False
class Pizzaservice:
    counter = 100
    def __init__(self, customer, pizza_type, additional_topping=False):
        self.__service_id = None
        self.__customer = customer
        self.__pizza_type = pizza_type
        self.__additional_topping = additional_topping
        self.pizza_cost = None
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in ["small", "medium"]:
            return True
        return False
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            Pizzaservice.counter += 1
            if self.__pizza_type.lower() == "small":
                self.pizza_cost = 150 * self.__customer.get_quantity()
                if self.__additional_topping == True:
                    self.pizza_cost += 35 * self.__customer.get_quantity()
                self.__service_id = "S" + str(Pizzaservice.counter)
            if self.__pizza_type.lower() == "medium":
                self.pizza_cost = 200 * self.__customer.get_quantity()
                if self.__additional_topping == True:
                    self.pizza_cost += 50 * self.__customer.get_quantity()
                self.__service_id = "M" + str(Pizzaservice.counter)
        else:
            self.pizza_cost = -1
    def get_service_id(self):
        return self.__service_id
    def get_customer(self):
        return self.__customer
    def get_pizza_type(self):
        return self.__pizza_type
    def get_additional_topping(self):
        return self.__additional_topping
class Doordelivery(Pizzaservice):
    def __init__(self, customer, pizza_type, additional_topping, distance_in_kms):
        super().__init__(customer, pizza_type, additional_topping)
        self.__delivery_charge = None
        self.__distance_in_kms = distance_in_kms
    def validate_distance_in_kms(self):
        if self.__distance_in_kms >= 1 and self.__distance_in_kms <= 10:
            return True
        return False
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            if self.pizza_cost != -1:
                if self.__distance_in_kms <= 5:
                    self.__delivery_charge = self.__distance_in_kms * 5
                else:
                    self.__delivery_charge = 25 + (self.__distance_in_kms - 5) * 7
                self.pizza_cost += self.__delivery_charge
        else:
            self.pizza_cost = -1
    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance_in_kms(self):
        return self.__distance_in_kms
c=Customer("Ayusman",4)
p=Pizzaservice("Ayusman","medium",False)
d=Doordelivery("Ayusman","medium",False,5)
print("Customer name:",c.get_customer_name())
print("Quantity is:",c.get_quantity())
print("valid quantity:",c.validate_quantity())
print("valid pizza type:",p.validate_pizza_type())
print("valid distance in kms:",d.validate_distance_in_kms())  


# In[ ]:





# In[ ]:




