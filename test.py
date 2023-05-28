class int_iter:
    def __new__(cls,number, *args, **kwarg):
        remain = 0
        reverse = 0
        while number!= 0:
            remain = number%10 
            reverse = reverse*10 + remain
            number //=10
        number = reverse
        obj = super().__new__(cls, *args, **kwarg)
        obj.number = reverse
        return obj

    def __iter__(self):
        self.n = 0
        return self
        
    def __next__(self):
        remain = 0
        if self.number != 0:
            remain = self.number%10 
            self.number //=10
            return remain
        else:
            raise StopIteration

if __name__ == "__main__":

    print("*"*10)
    a = int_iter(8765135)
    for i in a:
        print(i**2)
    