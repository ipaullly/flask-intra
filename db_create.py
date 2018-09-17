from app import db
from models import BlogPost

#create the database
db.create_all()

#insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("postgres", "we sey up a local postgres server"))
#commit the changes
db.session.commit()