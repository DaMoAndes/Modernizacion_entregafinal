import sys
sys.path.insert(0, '~/Modernizacion_entregafinal/courses/src')

from flask.cli import FlaskGroup

from CoursesApp import app
from modelos import db

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
