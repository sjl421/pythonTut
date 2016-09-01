import base64

print base64.b64encode('binary\x00string')

print base64.b64decode('YmluYXJ5AHN0cmluZw==')