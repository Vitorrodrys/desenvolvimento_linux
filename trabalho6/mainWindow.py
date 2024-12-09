import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk

class GridApp(Gtk.Application):
    def __init__(self):
        super().__init__()

    def do_activate(self):
        # Configura a janela principal
        window = Gtk.ApplicationWindow(application=self)
        window.set_title("Grid 16x16")
        window.set_default_size(400, 400)
        # window.set_margin_top(10)
        # window.set_margin_bottom(10)
        # window.set_margin_start(10)
        # window.set_margin_end(10)

        # Criação do grid
        grid = Gtk.Grid()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        window.set_child(vbox)
        vbox.append(grid)

        # Loop para criar o grid 16x16
        for row in range(16):
            for col in range(16):
                button = Gtk.Button()
                button.add_css_class("grid-button")  # Classe CSS para o botão
                button.connect("clicked", self.on_button_clicked)
                grid.attach(button, col, row, 1, 1)

        hboxBotao = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.append(hboxBotao)

        hboxBotao.set_margin_top(10)

        buttonGerar = Gtk.Button(label="Gerar")
        buttonGerar.connect("clicked", self.on_buttonGerar_clicked)
        hboxBotao.append(buttonGerar)

        # Exibe a janela
        window.show()

    def on_button_clicked(self, button):
        # Alterna entre cores para indicar seleção
        if "selected" in button.get_css_classes():
            button.remove_css_class("selected")
        else:
            button.add_css_class("selected")

    def on_buttonGerar_clicked(self, button):
        pass


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
app = GridApp()
app.run()
