from ClassesModules.Adapter import Adapter


class Lavoratore:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Il lavoratore {}".format(self.nome)

    def lavora(self, workType: str):
        return "lavora come {}".format(workType)


class Commesso:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Il commesso {}".format(self.nome)

    def vende(self, sellType: str):
        return "vende {}".format(sellType)


class Cuoco:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Il cuoco {}".format(self.nome)

    def cucina(self, cookType: str):
        return "cucina {}".format(cookType)


class Musicista:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Il musicista {}".format(self.nome)

    def suona(self, toolType):
        return "suona {}".format(toolType)


myCommesso = Commesso("Paolo")
myMusicista = Musicista("Veronica")
myCuoco = Cuoco("Antonio")
adapterList = list()
adapterList.append(Adapter(myCommesso, dict(lavora=myCommesso.vende("un abito"))))
adapterList.append(Adapter(myMusicista, dict(lavora=myMusicista.suona("il violino"))))
adapterList.append(Adapter(myCuoco, dict(lavora=myCuoco.cucina("la pasta"))))
for element in adapterList:
    print("{} {}".format(element.__str__(), element.lavora))
