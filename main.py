import socket


def getInput():
    return input("[L/R]: ")


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(("wpilib.local", 6001))
    s.sendall(getInput())
    payload = s.recv(1024)

    print(payload)
