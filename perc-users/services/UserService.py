import bson
from utils import utils
import requests
from settings import settings

ORDER_BY_FIELDS_MAP = {
    "name": "name",
    "city": "address.city",
    "company_name": "company.name",
}

"""_summary_
    Service to create the user
Returns:
    _type_: payload
"""
def CreateUser(name, username, email):
    return 201, name, username, email, "User created success"


"""_summary_
    Get users from api users
Returns:
    _type_: payload
"""
def GetAllUser():
    
    url = settings.USER_API_URL
    try:
        # do Get request
        response = requests.get(url)
        if response.status_code == 200:
            # Convert to json
            users = response.json()
            return 200, users
        else:
            print(f"Error: {response.status_code} - {response.reason}")
    except requests.exceptions.RequestException as e:
        return 500, f"Error request: {e}"

"""_summary_
    Filter user depending parameters
Returns:
    _type_: payload
"""    
def SearchUsers(request):
    url = settings.USER_API_URL
    try:
        response = requests.get(url)
        users_data = response.json()
        
        # Filter
        filtered_users = [
            user
            for user in users_data
            if (not request.name or request.name.lower() in user["name"].lower())
            and (not request.city or request.city.lower() in user["address"]["city"].lower())
            and (
                not request.company_name
                or request.company_name.lower() in user["company"]["name"].lower()
            )
        ]
        
        # Sort
        if request.order_by:
            # Get real field based on the map
            order_by_field = ORDER_BY_FIELDS_MAP.get(request.order_by)
            if order_by_field:
                # Acces to nidade value
                def get_nested_value(d, key):
                    keys = key.split(".")
                    for k in keys:
                        d = d.get(k, None)
                        if d is None:
                            break
                    return d

                # Sort using the value of field anidade
                filtered_users.sort(
                    key=lambda u: get_nested_value(u, order_by_field),
                    reverse=request.desc if hasattr(request, "desc") else False,
                )
            
        return 200, filtered_users
    except requests.exceptions.RequestException as e:
        return 500, f"Error request: {e}"