import json, os

def load_data(path):
    with open(path, "r") as f:
        return json.load(f)

def write_data(data: dict, path):
    with open(path, "w") as f:
        json.dump(data, f)

# if __name__ == "__main__":
    # a = load_data(os.path.join("data", "main_content.json"))
    # a["1"]["name"] = "BOOMER"
    # write_data(a, os.path.join("data", "main_content.json"))
