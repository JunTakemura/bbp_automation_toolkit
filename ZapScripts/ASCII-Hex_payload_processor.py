# Convert payload to hex
def process(payload):
    encoded = "".join("{:02x}".format(ord(c)) for c in payload)
    return encoded
