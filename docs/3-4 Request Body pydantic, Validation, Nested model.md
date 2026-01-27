##### Request Body:



* Used to send structured data to the server or DB..



##### Pydantic model:



* Used to validation, for example if we ask for the phone number with length of 10, if a user forget to it wont accept.
* **Optional:** method is used to, if we asked any values from user, but few values in mandatory and few are **optional.** on that time we can use this optional method to avoid error on without giving that optional values



##### Serialization:



* This is used to store the data in different format by default it stores as json format, but with the help of this we can store that on different format.



##### Documentation:



* Used to prepare documentation and generate something with that documentation



------



##### Validation:



* With the help of **Field** we can validate the user to minimum and maximum length of string and **Greater than** and **Less than** of the **Int** values.
* And we can use the **Regex method** to set the default values like set a pattern to user.





##### Nested Model:



* Using a same model with the additional of new class refer code for better understanding
