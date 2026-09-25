from sqlalchemy import String,Date, ForeignKey
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.enums import Role
from sqlalchemy import Enum as ENUMSql
from app.database import Base

class User(Base):
    __tablename__="users"
    id: Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str]=mapped_column(String(100))
    phone: Mapped[str]=mapped_column(String(15))
    date_of_baptism: Mapped[date|None]=mapped_column(Date, nullable=True)
    user_roles=relationship("UserRole", back_populates='user')
    group_id: Mapped[int| None]=mapped_column(ForeignKey("groups.id", use_alter=True, name="fk_users_group"), nullable=True)
    service_assignment_approved_by=relationship("ServiceAssignment", back_populates='approved_by_user', foreign_keys='ServiceAssignment.approved_by')
    service_assignments=relationship("ServiceAssignment",foreign_keys="ServiceAssignment.user_id", back_populates="user")
    reports=relationship("Report", back_populates="user")
    overseer_group=relationship("Group", foreign_keys="Group.overseer_id", back_populates="overseer")
    group=relationship("Group", foreign_keys=[group_id], back_populates="members")
