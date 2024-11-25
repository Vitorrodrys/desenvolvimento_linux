from gi.repository import Gtk

from .default_configs import HEIGTH, WIDTH

class RegisterWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Cadastro de Jogo")
        self.set_default_size(HEIGTH, WIDTH)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_child(vbox)

        label = Gtk.Label(label="Preencha as informações do jogo:")
        vbox.append(label)

        # Entrada de texto para o nome do jogo
        entry = Gtk.Entry()
        entry.set_placeholder_text("Nome do jogo")
        vbox.append(entry)

        # Botão de salvar
        button_save = Gtk.Button(label="Salvar")
        button_save.connect("clicked", self.on_save_clicked)
        vbox.append(button_save)

    def on_save_clicked(self, button):
        print("Jogo salvo!")
        self.destroy()
