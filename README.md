# AutoSort

> Flask Server to process text and return sorted versions

## Getting Started

```sh

# Setting up virtual environment for local development
virtualenv -p python3 venv

# Activate the virtual environment
./venv/Scripts/activate

# Install dependencies
pip3 install -r requirements.txt

# Set flask environment variables
set FLASK_APP=main.py
set FLASK_ENV=development

# Run flask server locally
flask run

```

## Endpoints 

- ### `POST /sortedText`
    - Request Parameters
        - text : The text to be sorted
    - Sample Request
        
        ```HTTP
        Recommended client: Advanced REST Client
        POST /sortedText HTTP/1.1
        Host: localhost:5000
        Content-Type: application/json

        {
            "text": "samsung,'OEM Samsung Washing Machine Pulsator Washplate Cap Shipped With\r\nWA48J7700AW, WA48J7700AW\/A2, WA48J7700AW\/AA',20916,samsung,'OEM Samsung\r\nChrome Washing Machine Washplate Pulsator Cap Shipped With WA52M7750AV,\r\nWA52M7750AV\/A4, WA52M7750AW, WA52M7750AW\/A4',13000,samsung, 'SAMSUNG\r\nWashing Machine Spring Hanger, DC61-01257M', 22970,samsung,'Samsung DC97-17022B\r\nAssy Detergent',32959,samsung,'Samsung DC66-00470A DAMPER\r\nSHOCK',29981,saumsung,'DC64-00519D Samsung Washing Machine Door Lock Washer Dryer\r\nDishwashe -MP#GH4498 349Y49HBRG9109150',52000,samsung,'Samsung DC97-16991A\r\nAssembly Filter',91995\r\n",
            
        }
        ```
    - Response
        - sorted_text_json: The sorted versions of the text corpus sent in the request
    - Sample Response
        ```json
        {
            "0": "samsung,'Samsung DC97-16991A Assembly Filter',91995 ",
            "1": "saumsung,'DC64-00519D Samsung Washing Machine Door Lock Washer Dryer Dishwashe -MP#GH4498 349Y49HBRG9109150',52000",
            "2": "samsung,'Samsung DC97-17022B Assy Detergent',32959",
            "3": "samsung,'Samsung DC66-00470A DAMPER SHOCK',29981",
            "4": "samsung, 'SAMSUNG Washing Machine Spring Hanger, DC61-01257M', 22970",
            "5": "samsung,'OEM Samsung Washing Machine Pulsator Washplate Cap Shipped With WA48J7700AW, WA48J7700AW/A2, WA48J7700AW/AA',20916",
            "6": "samsung,'OEM Samsung Chrome Washing Machine Washplate Pulsator Cap Shipped With WA52M7750AV, WA52M7750AV/A4, WA52M7750AW, WA52M7750AW/A4',13000"
        }
        ```
