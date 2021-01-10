import socket
import sys

stack = []
top = -1


def append():
    global top
    stack.append(input("enter Link: "))
    top += 1


def display():
    global top
    if top < 0:
        print("Stack Underflow")
    else:
        i = top
        while i > -1:
            print(stack[i])
            i -= 1


def pop():
    global top
    stack.pop(top)
    top -= 1


def startcheck():
    global top
    port = 80
    i = top
    while i > -1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            host_ip = socket.gethostbyname(stack[i].strip())
        except socket.gaierror:
            print("there was an error resolving the host")
        try:
            s.settimeout(30)
            s.connect((host_ip, port))
            print(stack[i], "is online")
        except TimeoutError:
            print(stack[i], "seems to be offline.")
        s.detach()
        i -= 1


if __name__ == "__main__":
    while True:
        d = {1: "append", 2: "display", 3: "pop",
             4: "startcheck", 5: "sys.exit"}
        print("\n", d, "\n")
        x = int(input("Enter your choice: "))
        for k, v in d.items():
            if x == k:
                eval(f"{v}()")
