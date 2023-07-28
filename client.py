import socket
import json

ACC_FLAGS = [(0,"#22fc00"),(1,"#2600fc"),(2,"#ecff17"),(3,"000000"),(4,"#ffffff"),(5,"#03dffc"),(6,"penalty"),(7,"#28fc03"),(8,"#fc6f03")]


def udp_client(ipaddr,port,message):
    UDP_client_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    UDP_client_socket.sendto(message,(ipaddr,port))
    
    
def find_device():
    message = '{"method":"getPilot","params":{}}'

def change_color(flag):
    flag,color_code= ACC_FLAGS[flag]
    rgb = hex_to_rgb(hex=color_code)
    message = '{"id":1,"method":"setPilot","params":{"r":0,"g":0,"b":0}}'
    json_message=json.loads(message)
    json_message["params"]["r"]=rgb[0]
    json_message["params"]["g"]=rgb[1]
    json_message["params"]["b"]=rgb[2]
    return bytes(json.dumps(json_message),'utf-8')
def hex_to_rgb(hex):
    h = hex.lstrip("#")
    return tuple(int(h[i:i+2],16) for i in (0,2,4))
