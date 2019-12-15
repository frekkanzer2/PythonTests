class FW:
    """
    FW memorizza la parte comune dello stato in SharedState

    """

    def __init__(self, sharedState: str):
        self.sharedState = sharedState

    """op aggiunge un oggetto oggetto al file  prendendo tutta la parte condivisa dell'auto da sharedState e il resto dal
    parametro itsOwnState"""

    def op(self, itsOwnState: list, tipo: type, file):
        # itsOwnState contains the following list: [targa, proprietario]
        # tipo contains Automobile
        concatenatedState = self.sharedState + itsOwnState
        print("Il nuovo oggetto di tipo {} è {}".format(tipo, concatenatedState))
        report = open(file, "w")
        report.write("Il nuovo oggetto di tipo {} e' {}\n".format(tipo, concatenatedState))
        report.flush()
        report.close()


class FWFactory:
    """
    Questa classe crea oggetti FW: ne crea uno nuovo se non esiste, altrimenti resituisce uno preesistente
    """

    def __init__(self, listOfStatus: list):
        self._fwDict = dict()
        for status in listOfStatus:
            self.get_FW(status)

    # get_statusKey ritorna la key dello stato passato come argomento
    def get_statusKey(self, arg_status: list) -> str:
        return "_".join(sorted(arg_status))

    def get_FW(self, shared_state: list) -> FW:
        """
        restituisce un FW con un certo stato o ne crea uno nuovo
        """
        if self.get_statusKey(shared_state) in self._fwDict.keys():
            print("Returning an existent FW")
            return self._fwDict[self.get_statusKey(shared_state)]
        else:
            print("Creating a new FW")
            self._fwDict[self.get_statusKey(shared_state)] = FW(shared_state)
            return self._fwDict[self.get_statusKey(shared_state)]

    def list_FWs(self):
        """ stampa numero oggetti FW's e gli stati degli FW's"""
        print("There are {} FWs".format(len(self._fwDict)))
        for value in self._fwDict.values():
            print(" | ".join(value.sharedState))


class automobile:
    def __init__(self, state: list):
        self._state = state

    def state(self):
        return self._state


def add_car(factory: FWFactory, targa: str, proprietario: str, marca: str, modello: str, colore: str):
    print("\n\nClient: Aggiungo un'automobile.")
    fw = factory.get_FW([marca, modello, colore])

    fw.op([targa, proprietario], automobile, "automobili.txt")


if __name__ == "__main__":
    """
    The client code usually creates a bunch of pre-populated flyweights in the
    initialization stage of the application.
    """

    factory = FWFactory([
        ["Chevrolet", "Camaro2018", "rosa"],
        ["Mercedes Benz", "C300", "nera"],
        ["Mercedes Benz", "C500", "rossa"],
        ["BMW", "M5", "rossa"],
        ["BMW", "X6", "bianca"],
    ])

    factory.list_FWs()

    add_car(
        factory, "DE123AT", "Bob Bab", "BMW", "M5", "rossa")

    add_car(
        factory, "AR324SD", "Mike Smith", "BMW", "X1", "rossa")

    print("\n")

    factory.list_FWs()

"""Il programma stampa :

FWFactory: ho  5 oggetti FW: 
Camaro2018_Chevrolet_rosa
C300_Mercedes Benz_nera
C500_Mercedes Benz_rossa
BMW_M5_rossa
BMW_X6_bianca


Client: Aggiungo un automobile.
FWFactory:  uso un FW esistente.
Il nuovo oggetto di tipo <class '__main__.automobile'> e` ['BMW', 'M5', 'rossa', 'DE123AT', 'Bob Bab']:


Client: Aggiungo un automobile.
FWFactory: non trovo un FW, ne creo uno nuovo.
Il nuovo oggetto di tipo <class '__main__.automobile'> e` ['BMW', 'X1', 'rossa', 'AR324SD', 'Mike Smith']:


FWFactory: ho  6 oggetti FW: 
Camaro2018_Chevrolet_rosa
C300_Mercedes Benz_nera
C500_Mercedes Benz_rossa
BMW_M5_rossa
BMW_X6_bianca
BMW_X1_rossa

"""
