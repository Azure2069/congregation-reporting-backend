from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date,ForeignKey, DateTime, UniqueConstraint
from datetime import date, datetime
from app.database import Base
from app.models.enums import ServiceType, Status
from sqlalchemy import Enum as SQLEnum
from typing import Optional

class Report(Base):
    __tablename__="reports"
    id: Mapped[int]=mapped_column(primary_key=True)
    user_id: Mapped[int]=mapped_column(ForeignKey("users.id"))
    reporting_month: Mapped[date]=mapped_column(Date)
    service_type: Mapped[ServiceType]=mapped_column(SQLEnum(ServiceType))
    hours: Mapped[int | None]=mapped_column(nullable=True)
    bible_studies: Mapped[int]
    participated: Mapped[bool]
    status: Mapped[Status]=mapped_column(SQLEnum(Status))
    submitted_at: Mapped[datetime]=mapped_column(DateTime)
    original_submission_time: Mapped[datetime]=mapped_column(DateTime)
    user=relationship("User", back_populates="reports")

    __table_args__=(
        UniqueConstraint("user_id",
                         'reporting_month',
                         name='uq_user_reporting_month'),
    )
    #alembic revision --autogenerate -m "create initial tables"