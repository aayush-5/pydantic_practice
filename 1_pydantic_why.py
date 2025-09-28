from pydantic import BaseModel, EmailStr, Field, AnyUrl
from typing import List, Annotated, Dict

class Employee(BaseModel):
    name: Annotated[str, Field(max_length=50, description="Name of the Employee", examples=["Aayush", "Rajat"])]
    email: EmailStr
    linkedinURL: AnyUrl
    age: Annotated[int, Field(gt=0, lt=100)]
    employeed_id:Annotated[str,Field(max_length=10, description="Unique Employee ID", examples=["27055110"])]
    contact_Details:Dict[str, str]


def update_employee_data(employee: Employee):
    print(employee.name)
    print(employee.age)
    print(employee.email)
    print(employee.linkedinURL)
    print(employee.employeed_id)
    print(employee.contact_Details)
    print("Details of the employee updated")

employee_info={'name': 'Aayush', 'email':'aayush@gmail.com', 'age':27, 'linkedinURL':'http://linkedin.com/345', 'employeed_id':'2701125', 'contact_Details':{'phone':'45212586'}}

employee_1 = Employee(**employee_info)

update_employee_data(employee_1)