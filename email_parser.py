import re
def email_parser(email):
  pattern = re.compile(r'[a-z][a-zA-Z0-9+]+[a-zA-Z0-9]@[a-z][a-zA-Z0-9]+\.com', re.IGNORECASE)
  match = pattern.findall(email)
