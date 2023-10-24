import re

# p = re.compile(“^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
p = re.compile("^[a-zA-Z0-9-.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
emails = [
    "python.dojang@e-xample.com",
    "@example.com",
    "python@example",
    "python+kr@example.com",
    "python-dojang@example.co.kr",
    "python_10@example.info",
]
for email in emails:
    print(p.match(email) != None, end=" ")
