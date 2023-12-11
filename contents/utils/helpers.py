from errors import IPInvalid, PORTInvalid


def validateIP(ip):
    splitip = ip.split(".")

    if len(splitip) != 4:
        raise IPInvalid

    for i in splitip:
        if not i.isdigit():
            raise IPInvalid
    return True


def validatePORT(port):
    if not port.isdigit():
        return PORTInvalid

    if not port.isnumeric():
        return PORTInvalid
    '''
    #! I don't know why, but these 
    #! if statements don't catch anything
    if int(port) <= 0:
        return PORTInvalid

    if int(port) > 65535:
        return PORTInvalid
    '''
    return True
