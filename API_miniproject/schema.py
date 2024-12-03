from pydantic import BaseModel, Field
from datetime import datetime



class Name(BaseModel):
    """Schema for customer name info."""
    title: str
    first: str
    last: str

class Street(BaseModel):
    """Nested schema for street name and number."""
    
    number: int
    name: str
    
class Location(BaseModel):
    """Schema for address information."""
    
    street: Street
    city: str
    state: str
    country: str
    postcode: str|int

class DOB(BaseModel):
    """Schema for birthdate."""
    date: datetime
    age: int
    
class Picture(BaseModel):
    """Schema for picture of the customer."""
    large: str | None
    medium: str | None
    thumbnail: str | None
    
class Results(BaseModel):
    """
    Structure of the JSON object provided by the RandomUser API.
    
    This only includes the fields we want, there are additional fields I'm not using
    
    """
    
    gender: str
    name: Name
    location: Location
    email: str
    dob: DOB
    picture: Picture

class APIResponse(BaseModel):
    results: list[Results]