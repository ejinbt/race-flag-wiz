from ui import MainApp
from client import hex_to_rgb,udp_client,change_color
import socket
from pyaccsharedmemory import accSharedMemory
import os
import yaml
import threading





asm = accSharedMemory()
sm = asm.read_shared_memory()
ACC_FLAGS = [(0,"#22fc00"),(1,"#2600fc"),(2,"#ecff17"),(3,"000000"),(4,"#ffffff"),(5,"#03dffc"),(6,"penalty"),(7,"#28fc03"),(8,"#fc6f03")]




def test():
    ip = "192.168.68.107"
    port = 38899
    json_message = change_color(5)
    print(json_message)
    udp_client(ip,port,json_message)


def main():
 
    App = MainApp()
    App.geometry("700x500")
    App.mainloop()
    '''
    while True:
        if sm is not None:
            json_message = change_color(sm.Static.ACC_FLAG_TYPE)
            udp_client(ip,port,json_message)
    '''
    # asm.close()

if __name__ == "__main__":
    main()
