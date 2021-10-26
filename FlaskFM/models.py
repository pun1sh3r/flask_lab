from app import app, db


# the User model: each user has a username, and a playlist_id foreign key referring
# to the user's Playlist
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))

    # representation method
    def __repr__(self):
        return "{}".format(self.username)

# create the Song model here + add a nice representation method
class Song(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80),index=True)
    artist = db.Column(db.String(80),index=True)
    n = db.Column(db.Integer)

    # representation method
    def __repr__(self):
        return "{} by {} ".format(self.title, self.artist )

# create the Playlist model here + add a nice representation method
class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.relationship('Item', backref='playlist',lazy='dynamic')


# create the Item model here + add a nice representation method
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer,db.ForeignKey('song.id'))
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))


