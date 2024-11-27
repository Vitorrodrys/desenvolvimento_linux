from gi.repository import Gtk
from gi.repository import GObject

import crud
import models

from .default_configs import HEIGTH, WIDTH


class RegisterWindow(Gtk.Window):
    __gsignals__ = {
        "game-added": (GObject.SignalFlags.RUN_FIRST, None, ())
    }
    def __mount_combobox_gamedeveloper(self):
        game_developer_combo = Gtk.ComboBoxText()
        game_developers = crud.crud_game_developer.get_all()
        for developer in game_developers:
            game_developer_combo.append(str(developer.id), developer.name)
        game_developer_combo.set_active(0)
        return game_developer_combo

    def __mount_combobox_genre(self):
        game_genre_combo = Gtk.ComboBoxText()
        for index, genre in enumerate(models.GameGenre):
            game_genre_combo.append(str(index), str(genre))
        game_genre_combo.set_active(0)
        return game_genre_combo

    def __mount_combobox_platform(self):
        platform_combo = Gtk.ComboBoxText()
        platforms = crud.crud_platform.get_all()
        for platform in platforms:
            platform_combo.append(str(platform.id), platform.name)
        platform_combo.set_active(0)
        return platform_combo

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
        self.__gamename_entry = entry

        # Game Description
        entry = Gtk.Entry()
        entry.set_placeholder_text("Descrição do jogo")
        vbox.append(entry)
        self.__gamedescription_entry = entry

        # Game priece
        entry = Gtk.Entry()
        entry.set_placeholder_text("Preço do jogo")
        vbox.append(entry)
        self.__gameprice_entry = entry

        # game developer combo box
        game_developer_combo = self.__mount_combobox_gamedeveloper()
        vbox.append(game_developer_combo)
        self.__gamedeveloper_combo = game_developer_combo

        # platform combo box
        platform_combo = self.__mount_combobox_platform()
        vbox.append(platform_combo)
        self.__platform_combo = platform_combo

        # game genre combo box
        game_genre_combo = self.__mount_combobox_genre()
        vbox.append(game_genre_combo)
        self.__gamegenre_combo = game_genre_combo

        # Botão de salvar
        button_save = Gtk.Button(label="Salvar")
        button_save.connect("clicked", self.on_save_clicked)
        vbox.append(button_save)

    def on_save_clicked(self, button):
        name = self.__gamename_entry.get_text()
        description = self.__gamedescription_entry.get_text()
        price = float(self.__gameprice_entry.get_text())
        developer_id = int(self.__gamedeveloper_combo.get_active_id())
        platform_id = int(self.__platform_combo.get_active_id())
        genre = models.GameGenre(self.__gamegenre_combo.get_active_text())
        game = models.Game(
            name=name,
            description=description,
            price=price,
            game_developer_id=developer_id,
            genre=genre,
            platform_id=platform_id,
        )
        crud.crud_game.create(game)
        self.emit("game-added")
        self.destroy()
