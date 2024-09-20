class XYZ:
    def f1(self):
        try:
            a = int(input("Enter value of a: "))
        except Exception as e:
            print("Enter a value only in int")
        else:
            print(a)
        finally:
            print("FINALLY : Anyhow I will be printed")


x = XYZ()
x.f1()