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
        #vbox.set_halign(Gtk.Align.CENTER)  # Centralizar os elementos verticalmente

        hboxBusca = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        vbox.append(hboxBusca)
        hboxBusca.set_halign(Gtk.Align.CENTER)
        hboxBusca.set_margin_bottom(15)

        entry = Gtk.Entry()
        entry.set_placeholder_text("Pesquisar jogos...")
        hboxBusca.append(entry)

        buttonBuscar = Gtk.Button(label="Buscar")
        buttonBuscar.connect("clicked", self.on_buttonBuscar_clicked)
        hboxBusca.append(buttonBuscar)

        hboxMainContent = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        vbox.append(hboxMainContent)

        # Caixa com a lista de jogos dentro de uma área rolável
        vboxJogos = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scroll.set_child(vboxJogos)
        scroll.set_vexpand(True)  # Permitir que a área rolável cresça verticalmente
        scroll.set_size_request(350, 50)
        hboxMainContent.append(scroll)

        # Adicionar itens de exemplo à lista de jogos
        for i in range(20):  # Exemplo com 20 jogos
            jogo_label = Gtk.Label(label=f"Jogo {i + 1}")
            vboxJogos.append(jogo_label)


        # Botões CRUD
        vboxCRUDButtons = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        hboxMainContent.append(vboxCRUDButtons)

        # Botões de exemplo
        buttonAdicionar = Gtk.Button(label="Adicionar")
        vboxCRUDButtons.append(buttonAdicionar)

        buttonRemover = Gtk.Button(label="Remover")
        vboxCRUDButtons.append(buttonRemover)


        # # Adicionar botões
        # button1 = Gtk.Button(label="Botão 1")
        # button1.connect("clicked", self.on_button1_clicked)
        # vbox.append(button1)

        # button2 = Gtk.Button(label="Botão 2")
        # button2.connect("clicked", self.on_button2_clicked)
        # vbox.append(button2)

    def on_button1_clicked(self, button):
        print("Botão 1 clicado!")

    def on_button2_clicked(self, button):
        print("Botão 2 clicado!")

    def on_buttonBuscar_clicked(self, button):
        print("Busca realizada!")

class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.exemplo.gtk4")

    def do_activate(self):
        win = MainWindow(self)
        win.present()

if __name__ == "__main__":
    app = MyApplication()
    app.run()