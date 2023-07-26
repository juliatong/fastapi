from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
import datetime as _dt
import decimal
import connect
from typing_extensions import Annotated
from sqlalchemy.orm import registry
from sqlalchemy import String


str_255 = Annotated[str, 255]

class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            str_255: String(255),
        }
    )

class Record(Base):
    __tablename__ = 'ohlc_history'
    UNIX:Mapped[_dt.datetime] = mapped_column(nullable=False, default=_dt.datetime.utcnow, primary_key=True)
    SYMBOL:Mapped[str_255] = mapped_column(nullable=False, primary_key=True)
    OPEN:Mapped[decimal.Decimal] = mapped_column(nullable=False)
    CLOSE:Mapped[decimal.Decimal] = mapped_column(nullable=False)
    HIGH:Mapped[decimal.Decimal] = mapped_column(nullable=False)
    LOW:Mapped[decimal.Decimal]  = mapped_column(nullable=False)
    
