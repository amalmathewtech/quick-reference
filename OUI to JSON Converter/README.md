# OUI to JSON Converter
 This script converts a text file containing Organizationally Unique Identifier (OUI) information to a JSON format. The text file is sourced from the IEEE standards website, which can be found [here](https://standards-oui.ieee.org/oui/oui.txt).


This script processes an OUI text file and converts it into a JSON file. It extracts relevant information such as the OUI, company ID, organization, and address, organizing this data into a structured JSON format.

## Usage
* Download the OUI text file from IEEE and save it as oui.txt.
* Place the oui.txt file in the same directory as the script.
* Run the script using Python.
* The output JSON will be saved as `mac-vendors.json`  in the same directory.
## Dependencies
Python 3.x

## Example Output

```
{
    "00-00-00": {
        "company_id": "000000",
        "Organization": "Xerox Corporation",
        "Address": "MS 105-50C 800 Phillips Road Webster NY 14580 US"
    },
    ...
}


```
