
```python
import grequests 
with open("C:\\path\\urls.txt") as werewolves: 
    array = [row.strip() for row in werewolves]

params = {'a':'b', 'c':'d'}
rs = [grequests.post(u, data=params) for u in array]
for r in grequests.imap(rs, size=16) 
    print(r.status_code)
```