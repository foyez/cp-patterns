import json

res = []

with open("data.json") as f:
    data = json.load(f)
    
    def read_leaves(nodes):
        for n in nodes:
            if "leaves" in n:
                res.extend(n["leaves"])
            elif "branches" in n:
                read_leaves(n["branches"])
    
    read_leaves(data)
    print(res)