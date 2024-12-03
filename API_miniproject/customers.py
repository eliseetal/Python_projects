import requests
from schema import APIResponse
from pydantic import ValidationError
import pandas as pd


class CustomersClient:
    """
    Client to make requests to the RandomUser API.
    
    Docs for the API can be found at https://randomuser.me/documentation
    """
    
    def __init__(self)-> None:
        self.ncustomers = 10
    
    def _get_customers(self, ncustomers):
        # url = f'https://randomuser.me/api/?results={ncustomers}&gender=female&seed=abc'
        url = f'https://randomuser.me/api/?results={ncustomers}&gender=female'


        try:
            # Make a GET request to the API endpoint
            response = requests.get(url)
            
            if response.status_code == 200:
                customers = response.json()  # Raw JSON response
                # print(customers)
                
                # Validate and return the structured Pydantic model
                return APIResponse(**customers) # ** works with a dictionary, * for keyword expansion
            else:
                print('Error:', response.status_code)
                return None  # I don't really need these lines, I could just do response = requests.get(url) and then if it fails it fails. If it's not clear from the error message why it's failing, then you can create a custom exception for example, and do a try: except: 
        
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            return None
    
    def _convert_to_df(self, customers:APIResponse) -> pd.DataFrame:
        """Convert customers to dataframe."""
        records = []
        
        for customer in customers.results:
            record = {
                "gender": customer.gender,
                "title": customer.name.title,
                "first_name": customer.name.first,
                "last_name": customer.name.last,
                "street": customer.location.street.name,
                "door_number": customer.location.street.number,
                "city": customer.location.city,
                "state": customer.location.state,
                "country": customer.location.country,
                "postcode": customer.location.postcode,
                "email": customer.email,
                "date_of_birth": customer.dob.date,
                "age": customer.dob.age,
                "picture_url": customer.picture.large
            }
            records.append(record)
        
        df = pd.DataFrame(records)
        return df
    
    def _save_to_csv(self, df: pd.DataFrame) -> None:
        df.to_csv("customers.csv", index=False)
        
    
    def main(self):
        customers = self._get_customers(self.ncustomers)
    
        if customers:
            # print(customers)
            print(customers.results[0])
        #     first_user = customers['results'][0]
        #     print('First User Name:', f"{first_user['name']['first']} {first_user['name']['last']}")
        else:
            print('Failed to fetch posts from API.')
        
        df = self._convert_to_df(customers)
        # print(df.head())
        
        self._save_to_csv(df)

if __name__ == '__main__':
    CustomersClient = CustomersClient()
    customers = CustomersClient._get_customers(ncustomers=10)
    df = CustomersClient._convert_to_df(customers)
    CustomersClient._save_to_csv(df)
    print(df.head(10))
    # CustomersClient.main()
    
    
