import gi
from board import Board
import threading
import time

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk



ROWS = 16
COLUMNS = 16
class GridApp(Gtk.ApplicationWindow):
        
    def __init__(self, app):
        super().__init__(application=app, title="Jogo da Vida")  # Definindo o título aqui
        self.set_default_size(400, 400)
        self.board = Board(COLUMNS, COLUMNS)

        # Criação do grid
        grid = Gtk.Grid()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_child(vbox)
        vbox.append(grid)

        # Loop para criar o grid 16x16
        for row in range(ROWS):
            for col in range(COLUMNS):
                button = Gtk.Button()
                button.add_css_class("grid-button")  # Classe CSS para o botão
                button.row = row  # Adiciona a linha como atributo
                button.col = col  # Adiciona a coluna como atributo
                button.connect("clicked", self.on_button_clicked)
                grid.attach(button, col, row, 1, 1)

        # Adicionando o botão "Gerar"
        hboxBotoes = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.append(hboxBotoes)
        hboxBotoes.set_margin_top(10)

        buttonGerar = Gtk.Button(label="Gerar")
        buttonGerar.connect("clicked", self.on_buttonGerar_clicked)
        hboxBotoes.append(buttonGerar)

        buttonGerarAuto = Gtk.Button(label="Gerar Auto")
        buttonGerarAuto.connect("clicked", self.on_buttonGerarAuto_clicked)
        hboxBotoes.append(buttonGerarAuto)

        buttonLimpar = Gtk.Button(label="Limpar")
        buttonLimpar.connect("clicked", self.on_buttonLimpar_clicked)
        hboxBotoes.append(buttonLimpar)

        self.grid = grid

    def on_button_clicked(self, button):
        row = button.row
        col = button.col

        self.board.swap_value(row, col)

        if "selected" in button.get_css_classes():
            button.remove_css_class("selected")
        else:
            button.add_css_class("selected")

    def on_buttonGerar_clicked(self, button):
        self.atualizaMatriz(button=button)
    
    def on_buttonLimpar_clicked(self, button):
        self.board.clear()
        self.atualizaMatriz(button=button)
    
    def on_buttonGerarAuto_clicked(self, button):
        while True:
            time.sleep(1)
            self.atualizaMatriz(button=button)


    def atualizaMatriz(self, button):
        self.board.step()
        matriz = self.board.get_board_matrix()

        grid = self.grid
        for row in range(ROWS):
            for col in range(COLUMNS):
                button = grid.get_child_at(col, row)  # Recupera o botão específico da célula
                if matriz[row][col]:
                    if "selected" not in button.get_css_classes():
                        button.add_css_class("selected")  # Adiciona a classe "selected" se o valor for True
                else:
                    if "selected" in button.get_css_classes():
                        button.remove_css_class("selected")  # Remove a classe "selected" se o valor for False



# Estilo CSS para controlar a cor
style_provider = Gtk.CssProvider()
style_provider.load_from_data(b"""
    .grid-button {
        min-width: 20px;
        min-height: 20px;
        border: 1px solid #ccc;
        background: #000;
    }
    .grid-button.selected {
        background: #f0f0f0;
        color: white;
    }
""")

# Aplica o estilo CSS
Gtk.StyleContext.add_provider_for_display(
    Gdk.Display.get_default(),
    style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_USER,
)

# Inicializa a aplicação
class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.gridapp")

    def do_activate(self):
        window = GridApp(self)  # Passando a instância da aplicação
        window.present()

app = MyApp()
app.run()
