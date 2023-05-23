import tkinter as tk


class IceCream:
    def __init__(self, name, flavors):
        self.name = name
        self.flavors = flavors

    def describe(self):
        print(f"Добро пожаловать в сладкий мир {self.name}!")
        print(f"Доступные виды мороженного: {', '.join(self.flavors)}")


ice_cream = IceCream("Выберите мороженное", ["Ванильное", "Шоколадное", "Клубничное"])

window = tk.Tk()
window.title("Сладкий мир")

name_label = tk.Label(window, text=ice_cream.name, font=("Arial", 24))
name_label.pack()

flavors_label = tk.Label(window, text=f"Доступные виды мороженного: {', '.join(ice_cream.flavors)}", font=("Arial", 18))
flavors_label.pack()

window.mainloop()