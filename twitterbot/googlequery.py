import os

key = "AIzaSyARfjNvudANJwXrc2k6_8xQUOWHg-c319Q"
url = "https://maps.googleapis.com/maps/api/geocode/json?key="+key+"&"

def query_google(_type, data):
    return os.system("curl \"" + url + _type + "=" + data + "\"")

def coords_to_address(coords):
    _type = "latlng"
    query_google(_type, coords)

def address_to_coords(address):
    _type = "address"
    query_google(_type, address)

print(coords_to_address('40.714224,-73.961452'))
print(address_to_coords("Madrid"))
