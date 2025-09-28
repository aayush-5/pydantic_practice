from pydantic import BaseModel, model_validator, Field, EmailStr
from typing import List, Dict, Annotated

class Employee(BaseModel):
    name : Annotated[str, Field(max_length=50, description="Name of the Employee")]
    age : Annotated[int, Field(gt=0, lt=100)]
    email: str
    contact_details: Dict[str, str]
    employee_id : str

    @model_validator(mode='after')
    def validate_employee(cls, model):
        domain_name = model.email.split('@')[-1]

        if domain_name == 'mahindra.com' and model.employee_id.startswith("MMFSL"):
            return model
        else:
            raise ValueError("Not a Mahindra employee")


def update_employee_details(employee:Employee):
    print(employee.name)
    print(employee.age)
    print(employee.email)
    print(employee.contact_details)
    print(employee.employee_id)
    print("Details of the employee updated")

employee_info={'name': 'Aayush', 'email':'aayush@mahindra.com', 'age':27, 'contact_details':{'phone':'9560101745', 'emergency':'9837212525'}, 'employee_id':'MMFSL27055116'}

employee_1 = Employee(**employee_info)

update_employee_details(employee_1)
