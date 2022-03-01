# pylint: disable=no-member
from app import db

class Recommendation(db.Model):
    """ Class that represents a single reading recommendation. """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable = False)
    link = db.Column(db.String(80), nullable = False)
    media = db.Column(db.String(80), nullable = True)
    author = db.Column(db.String(80), nullable = True)
    description = db.Column(db.String(80), nullable = True)
    isbn = db.Column(db.String(80), nullable = True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), nullable=False)
    user_account = db.relationship('User_account', backref=db.backref('recommendations', lazy=True))

    '''
    def __init__(self, title, link):
        """ Class constructor. Creates a new reading recommendation.
        Attributes:
            _title: [String] Title of the recommendation.
            _link: [String] Link to the source of the recommendation.
        """

        self._title = title
        self._link = link
        self._media = None
        self._author = None
        self._description = None
        self._isbn = None
    '''

    def get_title(self):
        """ Gets the title of the recommendation."""

        return self.title

    def get_link(self):
        """ Gets the link to the recommendation."""

        return self.link

    def get_media(self):
        """ Gets the media type of the recommendation."""

        return self.media

    def get_author(self):
        """ Gets the author of the recommendation."""

        return self.author

    def get_description(self):
        """ Gets the description of the recommendation."""

        return self.description

    def get_isbn(self):
        """ Gets the isbn of the recommendation."""

        return self.isbn

    def set_title(self, title):
        """ Sets the title.
        Args:
            title: [String] The title to be set.
        """

        self.title = title

    def set_link(self, link):
        """ Sets the link.
        Args:
            link: [String] The link to be set.
        """

        self.link = link

    def set_media(self, media):
        """ Sets the media type.
        Args:
            media: [String] The media type to be set.
        """

        self.media = media

    def set_author(self, author):
        """ Sets the author.
        Args:
            author: [String] The author to be set.
        """

        self.author = author

    def set_description(self, description):
        """ Sets the description.
        Args:
            description: [String] The description to be set.
        """

        self.description = description

    def set_isbn(self, isbn):
        """ Sets the isbn.
        Args:
            isbn: [String] The isbn to be set.
        """

        self.isbn = isbn
