import json

res = []

with open("data.json") as f:
    data = json.load(f)
    
    # stack = list(data)
    stack = list(reversed(data))  # start reversed so first node is processed first
    
    while stack:
        node = stack.pop()
        if "leaves" in node:
            res.extend(node["leaves"])
        elif "branches" in node:
            # stack.extend(node["branches"])
            # Push branches in reverse so original order is preserved
            stack.extend(reversed(node["branches"]))
        
    print(res)