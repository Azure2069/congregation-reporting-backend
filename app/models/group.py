from sqlalchemy import String, Date,ForeignKey,UniqueConstraint
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship


class Group(Base):
    __tablename__="groups"
    id:Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str]=mapped_column(String(100))
    overseer_id: Mapped[int]=mapped_column(ForeignKey("users.id", use_alter=True, name="fk_group_overseer"), unique=True,)
    members=relationship("User", foreign_keys="User.group_id", back_populates="group")
    overseer=relationship("User", foreign_keys="Group.overseer_id", back_populates="overseer_group")
    
    
