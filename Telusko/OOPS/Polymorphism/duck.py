
class VsCode:

    

    def execute(self):
        print("Compiling")
        print("Running")
        print("Autocomplete")
        print("Extensions")
  
        

class MyEditor :
    def execute(self):
        print("Compiling")
        print("Running")


class Laptop:
    def code(self,ide):
        ide.execute()

ide = VsCode()

lap = Laptop()
lap.code(ide)

