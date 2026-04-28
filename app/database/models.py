from sqlalchemy.ext.asyncio import (create_async_engine, async_sessionmaker,
                                    AsyncAttrs)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import (BigInteger, String, 
                        ForeignKey, func, DateTime,
                        Boolean)


from datetime import datetime


engine = create_async_engine(url="sqlite+aiosqlite:///database.db", 
                             echo=True)


async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    user_name: Mapped[str] = mapped_column(String(32), nullable=True)
    timezone: Mapped[str] = mapped_column(String(31), default=None, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        server_default=func.now()
    )

class Reminder(Base):
    __tablename__ = 'reminders'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), 
                                         nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    is_sent: Mapped[bool] = mapped_column(Boolean,
                                          default=False, 
                                          nullable=False)
    remind_at: Mapped[datetime] = mapped_column(DateTime, 
                                                nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        server_default=func.now()
    )


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)