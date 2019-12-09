class Pacco:
    ORDINATO, SPEDITO, RICEVUTO = [0, 1, 2]
    pvt_strings = ["ordinato", "spedito", "ricevuto"]

    def __init__(self):
        self._state = Pacco.ORDINATO

    def stampaStato(self):
        print("Il pacco si trova nello stato {}".format(self.pvt_strings[self._state]))

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, newValue):
        if 0 <= newValue <= 2:
            self._state = newValue
        elif newValue == -1:
            print("Il pacco è già stato ordinato")
        elif newValue == 3:
            print("Il pacco è già stato ricevuto")

    def next(self):
        self.state += 1

    def prec(self):
        self.state -= 1


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
