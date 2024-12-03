# Learning & Development Project: Requesting data from an API with Python.
_Elise Kanber, DS1, Nov 2024._
<br>
**Steps:**
- Use the [randomuser](https://randomuser.me/) API for our fake use case.
- We want this to be our "customer" API. 
- Build a class that has a method `get_customers`
- Add in a parameter where you can choose how many customers to select/generate e.g. `n=100`. 
- Call the API (`get` request)
- Use pydantic for validation.
- Transform the output as a pandas dataframe.
- Time to complete: should take ~2 days.

**Tips:** 
- Read the documentation of the API to help you.
- [This](https://www.geeksforgeeks.org/how-to-make-api-calls-using-python/) website was useful on how to make an API call with python.






**Notes:**
I don't use main.py, this was another way to run things. Instead, to run this, I run `customers.py`, which calls `schema.py` for the pydantic schemas that validate the result received from the API.
The output gives me a csv file with the customer data I requested.

To ask about/figure out: Unsure on how to request gender=female and how many customers, AND set the seed so we get the same people everytime. It seems that setting the seed then ignores the gender filter.
