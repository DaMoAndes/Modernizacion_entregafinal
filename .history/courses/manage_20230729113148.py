from flask.cli import FlaskGroup

from src.CoursesApp import app
from src.modelos import db

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
