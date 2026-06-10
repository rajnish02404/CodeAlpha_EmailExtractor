import re

# Open the text file
file = open("data.txt", "r")
content = file.read()
file.close()

# Find email addresses
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

# Save emails to another file
output = open("emails.txt", "w")

for email in emails:
    output.write(email + "\n")

output.close()

print("Email addresses extracted successfully!")

print("\nFound Emails:")
for email in emails:
    print(email)