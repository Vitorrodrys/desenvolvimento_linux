import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(title="Layout com Gtk.Box", application=app)
        self.set_title("Biblioteca de Jogos")
        self.set_default_size(800, 600)

        # Criar um container horizontal
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_child(vbox)


        # Adicionar botões
        button1 = Gtk.Button(label="Botão 1")
        button1.connect("clicked", self.on_button1_clicked)
        vbox.append(button1)

        button2 = Gtk.Button(label="Botão 2")
        button2.connect("clicked", self.on_button2_clicked)
        vbox.append(button2)

    def on_button1_clicked(self, button):
        print("Botão 1 clicado!")

    def on_button2_clicked(self, button):
        print("Botão 2 clicado!")

class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.exemplo.gtk4")

    def do_activate(self):
        win = MainWindow(self)
        win.present()

if __name__ == "__main__":
    app = MyApplication()
    app.run()