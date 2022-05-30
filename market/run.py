from market import app,db

from market.models import User, Item

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Item=Item)

if __name__ == '__main__':
    app.run(debug=True)