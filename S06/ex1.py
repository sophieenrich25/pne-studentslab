class Seq:
    def __init__(self, strbases):
        bases = ["A", "T", "G", "C"]
        for base in strbases:
            if base not in bases:
                self.strbases = "ERROR"
                print("Incorrect sequence!")
                return
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")


