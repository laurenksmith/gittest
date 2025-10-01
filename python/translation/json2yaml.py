import json
import os
import sys
import yaml

print("sysargsv: ", sys.argv)

# Valid JSON:

{
  "name": "John Doe",
  "age": 30,
  "isStudent": False,
  "courses": ["Python", "DevOps"],
  "address": {
    "street": "123 Main St",
    "city": "Anytown"
  }
}

sys.argv = ["json2yaml.py", "original.json", "translation.yaml"]

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")

# 1. Convert the JSON to YAML - use yaml library

yaml_string = yaml.dump(source_content)

# 2. Save the YAML into a new file with the name for it received as an argument
# 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
if len(sys.argv) > 2:
    target_file = sys.argv[2]


# 2.2 Check the target file doesn't already exist

    if os.path.exists(target_file):
        print("ERROR: " + target_file + " already exists.")
        exit(1)
# 2.3 If previous conditions not met, then save YAML file

    with open(target_file, "w") as f:
        f.write(yaml_string)

"""
You need to find a way to convert the JSON object to a YAML object and then save that YAML in a new target YAML file (name of YAML file is specified as an argument by the user)

We will talk through it on xxx so be ready to present your solution!

Hints: * The method you need may involve “dumping” * Before you can import yaml, you may need to install the pyyaml module with this command: pip install pyyaml
"""