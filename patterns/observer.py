class Subject:
    def __init__(self):
        self.observer = []
    def add_observer(self, observer):
        if observer not in self.observer:
            self.observer.append(observer)
    def remove_observer(self,observer):
        self.observer.remove(observer)
    def notify(self, message):
        for observer in self.observer:
            observer.update(message)
        
class observer:
    def update(self):
        pass
class ConcreteObserver(observer):
    def update(self,message):
        print(f"[Received Message]: {message}")
subject = Subject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()
observer3 = ConcreteObserver()
subject.add_observer(observer1)
subject.add_observer(observer2)
subject.add_observer(observer3)
subject.notify("ipsom lorum")


        