def prefixCount(names, queries):
    result = []
    
    for q in queries:
        count = 0
        
        for name in names:
            if name.startswith(q) and len(name) > len(q):
                count += 1
        
        result.append(count)
    
    return result
