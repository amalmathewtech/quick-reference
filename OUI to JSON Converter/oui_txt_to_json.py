
import re
import json


# The text file is sourced from the IEEE standards website
# link : https://standards-oui.ieee.org/oui/oui.txt
# Read the text file
with open('oui.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize variables
result = {}
current_oui = None
address_lines = []

# Iterate over lines
for line in lines:
    # Match OUI/MA-L
    match_oui = re.match(r'^([0-9A-Fa-f]{2}[:-]){2}([0-9A-Fa-f]{2})\s+', line)
    if match_oui:
        if current_oui:
            result[current_oui]["Address"] = " ".join(address_lines)
            address_lines = []
        current_oui = match_oui.group().strip()
        result[current_oui] = {}
    else:
        # Match company_id and Address
        match_data = re.match(r'^\s*([0-9A-Fa-f]{6})\s+\(base 16\)\s+(.+)$', line)
        if match_data and current_oui:
            company_id, organization_address = match_data.groups()
            organization, *address_parts = organization_address.split('\n')
            result[current_oui]["company_id"] = company_id.strip()
            result[current_oui]["Organization"] = organization.strip()
            address_lines.extend([part.strip() for part in address_parts])
        else:
            match_address = re.match(r'^\t+(.+)$', line)
            if match_address and current_oui:
                address_lines.append(match_address.group(1).strip())

# Add the last address
if current_oui:
    result[current_oui]["Address"] = " ".join(address_lines)

# Convert result to JSON
json_result = json.dumps(result, indent=4)
print(json_result)

# Write JSON to a file
with open('mac-vendors.json', 'w') as output_file:
    output_file.write(json_result)