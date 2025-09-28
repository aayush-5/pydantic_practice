from pydantic import BaseModel, EmailStr, computed_field
from typing import  Dict, List

class Employee(BaseModel):

    name : str
    email : EmailStr
    age : int
    employee_id : str

    @computed_field
    @property
    def sap_code_generator(self)-> str:
        sap_code = self.employee_id.split('L')[-1]
        return sap_code


def update_employee_details(employee:Employee):
    print(employee.name)
    print(employee.age)
    print(employee.email)
    print(employee.sap_code_generator)
    print(employee.employee_id)
    print("Details of the employee updated")

employee_info={'name': 'Aayush', 'email':'aayush@mahindra.com', 'age':27, 'contact_details':{'phone':'9560101745', 'emergency':'9837212525'}, 'employee_id':'MMFSL27055116'}

employee_1 = Employee(**employee_info)

update_employee_details(employee_1)
