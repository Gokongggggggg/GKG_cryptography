import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

bytes = bytes.fromhex(hex_string)

result = base64.b64encode(bytes)

print(result)