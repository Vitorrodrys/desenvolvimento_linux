import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

import crud
import models

from .default_configs import HEIGTH, WIDTH
from .register_window import RegisterWindow
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(title="Biblioteca de Jogos", application=app)
        self.set_default_size(HEIGTH, WIDTH)

        # Criar um container vertical
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_child(vbox)

        # Barra de busca
        hboxBusca = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        vbox.append(hboxBusca)
        hboxBusca.set_halign(Gtk.Align.CENTER)
        hboxBusca.set_margin_bottom(10)
        hboxBusca.set_margin_top(10)

        entry = Gtk.Entry()
        entry.set_placeholder_text("Pesquisar jogos...")
        hboxBusca.append(entry)
        self.entry = entry

        buttonBuscar = Gtk.Button(label="Buscar")
        buttonBuscar.connect("clicked", self.on_buttonBuscar_clicked)
        hboxBusca.append(buttonBuscar)

        # Área principal
        hboxMainContent = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        vbox.append(hboxMainContent)

        # Lista de jogos em uma área rolável
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
        listbox.connect("row-activated", self.on_row_selected)
        self.listbox = listbox

        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scroll.set_child(listbox)
        scroll.set_vexpand(True)
        scroll.set_size_request(390, 50)
        hboxMainContent.append(scroll)
        hboxMainContent.set_margin_start(10)
        hboxMainContent.set_margin_end(10)
        hboxMainContent.set_margin_bottom(10)


        # Botões CRUD e área de texto
        vboxCRUDButtons = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        hboxMainContent.append(vboxCRUDButtons)
        

        buttonAdicionar = Gtk.Button(label="Adicionar")
        buttonAdicionar.connect("clicked", self.on_buttonAdicionar_clicked)
        vboxCRUDButtons.append(buttonAdicionar)

        buttonRemover = Gtk.Button(label="Remover")
        vboxCRUDButtons.append(buttonRemover)

        # Caixa de texto para informações do jogo
        scroll_text = Gtk.ScrolledWindow()
        scroll_text.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scroll_text.set_vexpand(True)  # Permitir que a área cresça verticalmente
        scroll_text.set_size_request(390, 100)  # Tamanho inicial da área de texto

        self.textview = Gtk.TextView()  # Armazenar como atributo para uso posterior
        self.textview.set_editable(False)  # Tornar somente leitura
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)  # Quebra automática de linha
        scroll_text.set_child(self.textview)
        vboxCRUDButtons.append(scroll_text)

        

    def on_buttonAdicionar_clicked(self, button):
        new_window = RegisterWindow()
        new_window.present()
        
    def on_buttonBuscar_clicked(self, button):
        child = self.listbox.get_first_child()
        while child is not None:
            next_child = child.get_next_sibling()  # Obter o próximo antes de remover
            self.listbox.remove(child)  # Remover o filho atual
            child = next_child
        
        entryText = self.entry.get_text()
        games = crud.crud_game.get_by_name(entryText)
        # Adicionar itens de exemplo à lista de jogos
        for game in games:  # Exemplo com 20 jogos
            row = Gtk.ListBoxRow()
            label = Gtk.Label(label=game.name, xalign=0)
            row.set_child(label)
            self.listbox.append(row)

    def do_activate(self):
        win = MainWindow(self)
        win.present()
        win.on_load()

    def on_load(self):
        games = crud.crud_game.get_all()
        # Adicionar itens de exemplo à lista de jogos
        for game in games:  # Exemplo com 20 jogos
            row = Gtk.ListBoxRow()
            label = Gtk.Label(label=game.name, xalign=0)
            row.set_child(label)
            self.listbox.append(row)


    def on_row_selected(self, listbox, row):
        # Obter o texto do item selecionado
        label = row.get_child()
        texto = f"Informações do jogo selecionado:\n\n{label.get_text()}"

        # Atualizar o conteúdo da TextView
        buffer = self.textview.get_buffer()
        buffer.set_text(texto)

class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.exemplo.gtk4")

    def do_activate(self):
        win = MainWindow(self)
        win.present()
        win.on_load()
