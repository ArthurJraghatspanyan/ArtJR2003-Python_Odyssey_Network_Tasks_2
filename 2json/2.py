import yaml
import json


if __name__ == "__main__":
    with open("data.yaml") as yml:
        data = yaml.load(yml, Loader=yaml.FullLoader)

    with open("data.json", "w") as jsn:
        json.dump(data, jsn, indent=2)

    print("File successfully converted and data saved as JSON fiile")

    with open("data.json", 'r') as f:
        data_jsn = f.read()


    print(data_jsn)