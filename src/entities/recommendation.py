class Recommendation:
    """ Class that represents a single reading recommendation. """

    def __init__(self, title, link):
        """ Class constructor. Creates a new reading recommendation.
        Attributes:
            _title: [String] Title of the recommendation.
            _link: [String] Link to the source of the recommendation.
        """

        self._title = title
        self._link  = link

    ## Get
    def get_title(self):
        return self._title

    def get_link(self):
        return self._link

    ## Set
    def set_title(self, title):
        """ Sets the title.
        Args:
            title: [String] The title to be set.
        """

        self._title = title

    def set_link(self, link):
        """ Sets the link.
        Args:
            link: [String] The link to be set.
        """

        self._link = link
