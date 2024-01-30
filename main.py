
class LinkedList:
    def __init__(self):
        self.head = None

    def vloz(self, prvok):
        if self.head is None:
            self.head = prvok
        else:
            aktualny = self.head
            while aktualny.next:
                aktualny = aktualny.next
            aktualny.next = prvok

    def vypis(self):
        aktualny = self.head
        print(aktualny.data)
        while aktualny.next:
            aktualny = aktualny.next
            print(aktualny.data)

    def zmaz(self):
        aktualny=self.head
        while aktualny.next:
            aktualny=aktualny.next
            aktualny.next=prvok

    def obsahuje(self,meno):
        aktualny=self.head
        if aktualny==None:
            return False
        if aktualny.data==meno:
            return True
        while aktualny.next:
            aktualny=aktualny.next
            if aktualny.data==meno:
                return True
        return False



class Prvok:
    def __init__(self, data):
        self.data = data
        self.next = None

mojLinked = LinkedList()
# prvok1 = Prvok("Milan")
# mojLinked.vloz(prvok1)
# prvok2 = Prvok("Jozo")
# mojLinked.vloz(prvok2)
# prvok3 = Prvok("Fero")
# mojLinked.vloz(prvok3)
# mojLinked.vypis()
# prvok4=Prvok("Marek")
# mojLinked.vloz(prvok4)
mojLinked.obsahuje("Milan")
print(mojLinked.obsahuje("Milan"))
print("test")
