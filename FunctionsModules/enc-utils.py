import base64


def str_to_base64(str_input: str, encode_type="ascii"):
    toReturn = base64.b64encode(bytes(str_input, encode_type))
    toReturn = str(toReturn)
    reformattedReturn = toReturn[2:len(toReturn) - 1]
    return reformattedReturn


def base64_to_str(str_encoded: str, decode_type="ascii"):
    str_encoded = bytes(str_encoded, decode_type)
    str_decoded = base64.b64decode(str_encoded)
    str_decoded = str(str_decoded)
    strToReturn = str_decoded[2:len(str_decoded) - 1]
    return strToReturn
