
def countX(_string):
    results = {}
    lst = _string.lower() .split(" ") 
    count= 0
    for  i in lst:
        count = lst.count(i)
        results[i] = count

    return results

result = countX("Captain America is captain of America")

print(result)

result1 = countX("Alex is alEx and he is going to alex land")

print(result1)