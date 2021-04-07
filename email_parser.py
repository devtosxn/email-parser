import re
def email_parser(email):
  pattern = re.compile(r'[a-z][a-zA-Z0-9+]+[a-zA-Z0-9]@[a-z][a-zA-Z0-9]+\.com', re.IGNORECASE)
  match = pattern.findall(email)
  if email in match:
    split_index = email.index('@')
    username = email[:split_index]
    domain  = email[split_index+1:]
    return {
      'username': username, 
      'domain' : domain
      }

  else:
    return None
