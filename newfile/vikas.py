class vik:

    def __init__(self,name , age) -> None:
        self.name=name
        self.age=age
    
    def dis(self):
        print(self.name,self.age )


l=vik('vikas',22)

l.dis()