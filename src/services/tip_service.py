from entities.user import User_account
from repositories.tip_repository import TipRepository

class TipService:
    """Tip Service """

    def __init__(self):
        self.user = User_account
        self.tips = TipRepository
