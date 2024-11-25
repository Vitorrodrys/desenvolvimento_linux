import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(title="Layout com Gtk.Box", application=app)

        # Criar um container horizontal
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.set_child(hbox)

        # Adicionar botões
        button1 = Gtk.Button(label="Botão 1")
        button1.connect("clicked", self.on_button1_clicked)
        hbox.append(button1)

        button2 = Gtk.Button(label="Botão 2")
        button2.connect("clicked", self.on_button2_clicked)
        hbox.append(button2)

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