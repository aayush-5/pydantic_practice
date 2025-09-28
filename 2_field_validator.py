from pydantic import BaseModel, EmailStr, AnyUrl, field_validator, Field
from typing import List, Dict, Optional, Annotated

class Employee(BaseModel):
    name: str
    email: EmailStr
    age:int
    contact_details:str

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domain = ['mahindra.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError("Not a valid domain person")

        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('contact_details')
    @classmethod
    def number_validator(cls,value):
        if len(value) != 10:
            raise ValueError("Incorrect Number")
        return value

    @field_validator('age')
    @classmethod
    def validate_age(cls, value):
        if value<0 or value>100:
            raise ValueError("Not the required age of Employee")
        return value

    

def update_employee_details(employee:Employee):
    print(employee.name)
    print(employee.age)
    print(employee.email)
    print(employee.contact_details)
    print("Details of the employee updated")

employee_info={'name': 'Aayush', 'email':'aayush@mahindra.com', 'age':27, 'contact_details':'9560101745'}

employee_1 = Employee(**employee_info)

update_employee_details(employee_1)
