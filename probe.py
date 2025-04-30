class Animal:
    def breathe(self):
        print("Inhale, exhale!")

class Fish(Animal):
    def breathe(self):
        print("doing this underwater.")

    def swim(self):
        print("moving in water!")

    def show_status(self):
        super().breathe()

nemo = Fish()
nemo.show_status()