class Bambino:
    PRIMOANNO, SECONDOANNO, TERZOANNO, DIPLOMATO = [1, 2, 3, 4]

    def __init__(self):
        self.status = Bambino.PRIMOANNO

    def succ(self):
        if self.status == Bambino.PRIMOANNO:
            self.status = Bambino.SECONDOANNO
        elif self.status == Bambino.SECONDOANNO:
            self.status = Bambino.TERZOANNO
        elif self.status == Bambino.TERZOANNO:
            self.status = Bambino.DIPLOMATO

    def pred(self):
        if self.status == Bambino.SECONDOANNO:
            self.status = Bambino.PRIMOANNO
        elif self.status == Bambino.TERZOANNO:
            self.status = Bambino.SECONDOANNO

    def salta_anno(self):
        if self.status == Bambino.PRIMOANNO:
            self.status = Bambino.TERZOANNO
        elif self.status == Bambino.SECONDOANNO:
            self.status = Bambino.DIPLOMATO

    def stampaStato(self):
        if self.status == Bambino.PRIMOANNO:
            print("Il bambino si è iscritto")
        elif self.status == Bambino.SECONDOANNO:
            print("Il bambino è al secondo anno")
        elif self.status == Bambino.TERZOANNO:
            print("Il bambino è al terzo anno")
        elif self.status == Bambino.DIPLOMATO:
            print("Il bambino si è diplomato ed ora è un vero womo")


def main():
    bambino = Bambino()
    bambino.stampaStato()
    bambino.pred()
    bambino.succ()
    bambino.stampaStato()
    bambino.succ()
    bambino.stampaStato()
    bambino.salta_anno()
    bambino.succ()
    bambino.stampaStato()
    bambino.succ()


if __name__ == "__main__":
    main()
