# from pydantic import BaseModel ,ValidationError

# # define a class model

# class User (BaseModel):
#     id:int
#     email:str
 
#     name:str
#     age:int | None =None


# # Valid data

# userdata = {"id":1, "email":"usman@gmail.com" , "password":123 ,"name":"usman" , "age":19}    

# user= User(**userdata)
# print(user)

# # # Invalid Data:

# try:
#     invaliduser = User(id="not_init",email="bobgmail.com" , name="bob")
# except ValidationError as e:
#     print(e)    


# Nested Model

from pydantic import BaseModel , EmailStr

# Define A Nested Model

class Address(BaseModel):
    street:str
    zipcode:int
    city:str


class WithAdress(BaseModel):
    id:int
    name:str
    email:EmailStr
    addresses: list[Address]



# User data with Nested Model
userData = {
    "id":1,
    "name":"Usman",
    "email":"usman@gmail.com",
    "addresses":[
        {"street":"123" , "zipcode":123 , "city":"karachi"}
        ],

}

user = WithAdress.model_validate(userData)
print(user.model_dump())

