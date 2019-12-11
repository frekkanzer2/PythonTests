class Pacco:
    ORDINATO, SPEDITO, RICEVUTO = [0, 1, 2]

    def _nextdenied(self):
        print("Il pacco è già stato ricevuto")

    def _precdenied(self):
        print("Il pacco è già stato ordinato")

    def __init__(self):
        self.status = Pacco.ORDINATO

    def _succ(self):
        self.status += 1

    def _prec(self):
        self.status -= 1

    @property
    def status(self):
        if self.prec != self._prec:
            return Pacco.ORDINATO
        elif self.next != self._succ:
            return Pacco.RICEVUTO
        else:
            return Pacco.SPEDITO

    @status.setter
    def status(self, newStatus):
        if newStatus == Pacco.ORDINATO:
            self.next = self._succ
            self.prec = self._precdenied
        if newStatus == Pacco.SPEDITO:
            self.next = self._succ
            self.prec = self._prec
        if newStatus == Pacco.RICEVUTO:
            self.next = self._nextdenied
            self.prec = self._prec

    def stampaStato(self):
        if self.prec == self._precdenied:
            print("Il pacco è stato ordinato ma non ancora spedito")
        elif self.next == self._nextdenied:
            print("Il pacco è stato ricevuto")
        else:
            print("Il pacco è stato spedito ma non ancora ricevuto")


def main():
    print("\nCreo il pacco")
    pacco = Pacco()
    pacco.stampaStato()
    print("\nInoltro il pacco all'ufficio postale")
    pacco.next()
    pacco.stampaStato()
    print("\nConsegno il pacco al destinatario")
    pacco.next()
    pacco.stampaStato()
    print("\nProvo a passare ad uno stato successivo")
    pacco.next()
    pacco.stampaStato()


if __name__ == "__main__":
    main()

"""Il  programma deve stampare:
Creo il pacco
Il pacco e` stato ordinato ma non ancora spedito

Inoltro il pacco all'ufficio postale
Il pacco e` stato spedito ma non ancora ricevuto

Consegno il pacco al destinatario
Il pacco e` stato ricevuto 

Provo a passare ad uno stato successivo
Il pacco e` gia` stato ricevuto
Il pacco e` stato ricevuto 
"""
