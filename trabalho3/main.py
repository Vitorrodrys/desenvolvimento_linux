
import crud
import models

def main():

    test = crud.crud_game_developer.create(
        models.GameDeveloper(
            name="teste"
        )
    )
    print(test)


main()