from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String, ForeignKey
from app.database import Base
from app.models.enums import Role
from sqlalchemy import Enum as SQLEnum

class UserRole(Base):
    __tablename__="user_roles"
    id: Mapped[int]=mapped_column(primary_key=True)
    user_id: Mapped[int]=mapped_column(ForeignKey("users.id"))
    role: Mapped[Role]=mapped_column(SQLEnum(Role))

    user=relationship("User", back_populates="user_roles")