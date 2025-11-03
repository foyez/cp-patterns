from collections import deque
import json

res = []

with open("data.json") as f:
    data = json.load(f)
    
    q = deque(data)
    
    while q:
        node = q.popleft()
        if "leaves" in node:
            res.extend(node["leaves"])
        elif "branches" in node:
            q.extend(node["branches"])
    
    print(res)