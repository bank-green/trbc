import json


def parse_line(line):
    parts = line.split()
    trbc_str = parts[-1].strip()
    permid = int(parts[-2].strip())

    field = " ".join(parts[0:-2]).strip()

    classification = ""
    if len(trbc_str) == 2:
        classification = "Economic Sector"
    elif len(trbc_str) == 4:
        classification = "Business Sector"
    elif len(trbc_str) == 6:
        classification = "Industry Group"
    elif len(trbc_str) == 8:
        classification = "Industry"
    elif len(trbc_str) == 10:
        classification = "Activity"

    return {
        "field": field,
        "classification": classification,
        "trbc": int(trbc_str),
        "permId": permid,
    }


def build_json_structure(lines):
    root = {}

    for line in lines:
        node = parse_line(line.strip())
        trbc_str = str(node["trbc"])

        economic_sector_trbc = int(trbc_str[0:2])
        business_sector_trbc = int(trbc_str[2:4]) if len(trbc_str) >= 4 else ""
        industry_group_trbc = int(trbc_str[4:6]) if len(trbc_str) >= 6 else ""
        industry_trbc = int(trbc_str[6:8]) if len(trbc_str) >= 8 else ""
        activity_trbc = int(trbc_str[8:10]) if len(trbc_str) >= 10 else ""

        if len(trbc_str) == 2:
            root[economic_sector_trbc] = node
        elif len(trbc_str) == 4:
            root[economic_sector_trbc][business_sector_trbc] = node
        elif len(trbc_str) == 6:
            root[economic_sector_trbc][business_sector_trbc][industry_group_trbc] = node
        elif len(trbc_str) == 8:
            root[economic_sector_trbc][business_sector_trbc][industry_group_trbc][
                industry_trbc
            ] = node
        elif len(trbc_str) == 10:
            root[economic_sector_trbc][business_sector_trbc][industry_group_trbc][
                industry_trbc
            ][activity_trbc] = node

    return root


with open("./copy-paste.txt", encoding="utf-8", errors="ignore") as f:
    text = f.read()

lines = text.split("\n")
mydict = build_json_structure(lines)
formatted_json = json.dumps(mydict, indent=2)

with open("./trbc.json", "w") as json_file:
    json_file.write(formatted_json)
