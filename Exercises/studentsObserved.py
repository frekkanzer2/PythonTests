import collections
import datetime
import sys
import time
import copy

Exam = collections.namedtuple("Exam", "name cfu")


def main():
    historyView = HistoryView()
    liveView = LiveView()
    student = LaureaT_Student()
    student.observers_add(historyView, liveView)
    print("Lo studente sta per superare analisi matematica")
    student.add_grade(Exam("analisi matematica", 9), 28)
    time.sleep(0.5)
    print("Lo studente sta per superare asistemi operativi")
    student.add_grade(Exam("sistemi operativi", 6), 20)
    time.sleep(1)
    print("Lo studente sta per superare la prova di Inglese")
    student.english_r = True

    for grades, flag, timestamp in historyView.data:
        print("Esami: {}, Inglese: {}, Data: {}".format(grades,
                                                        "non superato" if flag is False else "superato",
                                                        timestamp), file=sys.stdout)


class Observer:

    def __init__(self):
        self.listOfListeners = list()

    def observers_add(self, *listeners):
        if len(listeners) > 0:
            for listener in listeners:
                self.listOfListeners.append(listener)
            self.notify()

    def notify(self):
        if len(self.listOfListeners) > 0:
            for listener in self.listOfListeners:
                listener.update(self)


class LaureaT_Student(Observer):
    _total_cfu = 0
    _english_r = False

    def __init__(self):
        super().__init__()
        self._grades = dict()
        self.total_cfu = 0
        self.english_r = False
        self._eng_changed = False

    @property
    def total_cfu(self):
        return self._total_cfu

    @total_cfu.setter
    def total_cfu(self, newValue):
        self._total_cfu = newValue

    @property
    def english_r(self):
        return self._english_r

    @english_r.setter
    def english_r(self, newValue: bool):
        if self.english_r is False and newValue is True:
            self._english_r = newValue
            self._eng_changed = True
            self.notify()

    def add_grade(self, exam: Exam, rate: int):
        self.total_cfu += exam.cfu
        self._grades[exam.name] = rate
        self.notify()





class HistoryView:
    def __init__(self):
        self.data = []  # Add here triples when LaureaT_Student changes status
        # Triples are like (dict of exams, english boolean, change state date)

    def update(self, student):
        if student.total_cfu > 0:
            self.data.append((copy.deepcopy(student._grades), student.english_r, datetime.datetime.today()))


class LiveView:
    # change of state -> print

    def update(self, student):
        if student.total_cfu > 0:
            if student._eng_changed is True:
                student._eng_changed = False
                print("Cambio stato: lo studente ha appena superato la prova di inglese")
            else:
                print("Cambio stato: lo studente ha superato un nuovo esame")
                print("Cambio stato: il numero di CFU è {}".format(student.total_cfu))


if __name__ == "__main__":
    main()

"""Il programma stampa:

Lo studente sta per superare analisi matematica
Cambio stato: lo studente ha superato un nuovo esame
Cambio stato: il numero di CFU e` :  9 

Lo studente sta per superare asistemi operativi
Cambio stato: lo studente ha superato un nuovo esame
Cambio stato: il numero di CFU e` :  15 

Lo studente sta per superare la prova di Inglese
Cambio stato: lo studente ha appena superato la prova di Inglese

Esami: {}, Inglese: non superato, Data: 2019-12-10 10:54:41.413786
Esami: {'analisi matematica': 28}, Inglese: non superato, Data: 2019-12-10 10:54:41.474924
Esami: {'analisi matematica': 28}, Inglese: non superato, Data: 2019-12-10 10:54:41.658306
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: non superato, Data: 2019-12-10 10:54:41.707940
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: non superato, Data: 2019-12-10 10:54:41.908861
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: superato, Data: 2019-12-10 10:54:41.959334

"""
