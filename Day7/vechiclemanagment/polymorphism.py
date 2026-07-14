class Overloadingdemo:
    def show_details(self,*args):
        if len(args) ==1:
            print(f"Car Brand: {args[0]}")
        elif len(args) ==2:
            print(f"Car Brand: {args[0]},Model: {args[1]}")
        elif len(args)==3:
            print(f"Car Brand:{args[0]},Model: {args[1]}, Year: {args[2]}")
        else:
            print("Invalid no of arguments.Please provide 1to 3 arguments")

def Overloading_demo():
    demo=Overloadingdemo()
    demo.show_details("Toyoto")
    demo.show_details("Honda")
    demo.show_details("testle","2000",123456789)