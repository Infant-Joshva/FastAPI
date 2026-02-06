##### JWT - Json Web Token:



* There are 2 purpose with these JWT.
* One is **Authentication** and another one **Authorization** 



**Authentication:**

* Used to check the user is valid user with their credential 



**Authorization:**

* To check the user is eligible to preform this operation, like restriction one



**Session VS JWT:**

* Session is used as server side and if your are going to so a small application it is ok but

if you are going to build a large application with REST API or Mobile apps or React app or Angular Application it wont suitable.



**Format:**

* It is a string format but it maintain the structure
* **Structure** : Header->Payload->Signature
* **Header:** it will contains the details like type of the Token and what Algorithm is used
* **Payload:** User data, like user\_id, user\_expiry and user\_role
* **Signature:** It will contains only the encoded information like who is going to receive 



**Note: Every JWT will contains these 3 things**

