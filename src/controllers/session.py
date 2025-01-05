from datetime import datetime

from models.session import Session
from models.user import User


class SessionController:
    def is_active(self, session_id: str) -> bool:
        session = Session.objects(id=session_id, expire_time__gt=datetime.now()).first()
        return session is not None

    def create_session(self, user: User) -> Session:
        session = Session(user=user)
        session.save()
        return session

    def get_user(self, session_id: str) -> User:
        session = Session.objects(id=session_id).first()
        user = session.user
        return user
