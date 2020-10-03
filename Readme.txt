User API using Django Rest Framework.
Features:-
1.Register user with all required fields.(POST request) Json structure below. URL:http://127.0.0.1:8000/register/
2.Login user with Email,Password with Knox Token authentication.(POST request) URL:http://127.0.0.1:8000/login/ 
3.Retrieve own details with Knox Token(GET request) URL:http://127.0.0.1:8000/detail/

    Json
  {
      "email": "user1@django.com",
      "contact": "9999988888",
      "profile": {
          "name": "user1",
          "company_name": "django",
          "address": {
              "street": "street",
              "city": "city",
              "state": "state",
              "pin_code": "123456"
          },
          "age": 30
      }
  }
  
4.Partial update own details with Knox Token(PUT request) URL:http://127.0.0.1:8000/update/
5.Logout user with Knox Token URL:http://127.0.0.1:8000/logout/ 
6.Project API CRUD features..................retrieve and update using project id.