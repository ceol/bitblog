from flaskext.script import Manager
from bitblog import app

manager = Manager(app)

@manager.command
def initdb():
    from bitblog.database import init_db
    init_db()

if __name__ == "__main__":
    manager.run()