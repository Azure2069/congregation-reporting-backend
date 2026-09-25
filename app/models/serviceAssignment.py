from sqlalchemy import String, Date, ForeignKey, DateTime
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.models.enums import ServiceType
from sqlalchemy import Enum as SQLEnum
from datetime import date, datetime

class ServiceAssignment(Base):
    __tablename__="service_assignments"
    id: Mapped[int]=mapped_column(primary_key=True)
    user_id: Mapped[int]=mapped_column(ForeignKey("users.id"))
    service_type: Mapped[ServiceType]=mapped_column(SQLEnum(ServiceType))
    start_date:Mapped[date]=mapped_column(Date)
    end_date: Mapped[date | None]=mapped_column(Date, nullable=True)
    approved_by: Mapped[int]=mapped_column(ForeignKey("users.id"))
    created_at:Mapped[datetime]=mapped_column(DateTime)
    approved_by_user=relationship('User', foreign_keys=[approved_by], back_populates='service_assignment_approved_by')
    user=relationship("User", foreign_keys=[user_id] ,back_populates="service_assignments")

