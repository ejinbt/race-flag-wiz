import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor
from functools import partial
import yaml
import threading
from client import udp_client,change_color


class MainApp(tk.Tk):
    def __init__(self):
        self.ip,self.port = self.config_reader()
        tk.Tk.__init__(self)
        self.canvas = tk.Canvas(self)
        self.ip_label=tk.Label(text="Enter your Wiz Ip")
        self.ip_entry=tk.Entry(self)
        self.ip_entry.insert(0,self.ip)
        self.port_label=tk.Label(text="Enter your wiz port")
        self.port_entry=tk.Entry(self)
        self.port_entry.insert(0,self.port)
        self.radio = tk.StringVar()
        self.game_label=tk.Label(text="Choose the game")
        self.game_radio_btn=ttk.Radiobutton(self,text="ACC",value="Assetto Corsa Competizione",variable=self.radio)
        self.game_radio_bt2=ttk.Radiobutton(self,text="AC",value="Assetto Corsa",variable=self.radio)
        self.button=tk.Button(self,text="Submit",command=self.on_button)
        self.start_button=tk.Button(self,text='Start',command=self.background_process)
        self.ip_label.pack(fill=tk.X,pady=10,padx=20) 
        self.ip_entry.pack(fill=tk.X,pady=10,padx=40)
        self.port_label.pack(fill=tk.X,pady=10,padx=20)
        self.port_entry.pack(fill=tk.X,pady=10,padx=40)
        self.game_label.pack(fill=tk.X,pady=10)
        self.game_radio_btn.pack()
        self.button.pack(fill=tk.X,pady=10,padx=60)
        self.start_button.pack()
        
    def on_button(self):

        stream = open("config.yaml","r")
        data = yaml.safe_load(stream)
        if not data['ip'] or data['port']:
            self.ip = self.ip_entry.get()
            self.port = self.port_entry.get()
            self.game = self.radio
            data['ip'] = str(self.ip)
            data['port'] = int(self.port)
            with open('config.yaml','w') as file:
                file.write(yaml.dump(data,default_flow_style=False))
    
    def execute(self):
        print("I am here")
        ip,port=self.config_reader()
        json_message = change_color(1)
        udp_client(ip,port,json_message)

    def background_process(self):
        t1=threading.Thread(target=self.execute)
        print("I am started !!")
        t1.start()


    def config_reader(self):
        with open('config.yaml','r') as file:
            prime_service = yaml.safe_load(file)
            ip = prime_service['ip']
            port = prime_service['port']

            return str(port),int(port)
    
    def read_config(self,file):
        with open('config.yaml','r') as file:
            config_yaml = yaml.safe_load(file)
            
    
