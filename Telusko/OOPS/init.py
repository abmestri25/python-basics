class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("Configuration is",self.cpu,"processor and",self.ram,"RAM")

# Create object
comp = Computer("i3","8GB")

comp.config()
        