from app.database.models import async_session, User, Reminder
from sqlalchemy import select, update

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()
            return False
        return True if user.user_name else False
    
async def update_user(tg_id, name):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(user_name=name))

        await session.commit()

async def timezone_check(tg_id):
    async with async_session() as session:
        timezone = await session.scalar(select(User.timezone).where(User.tg_id == tg_id))

    return timezone is None

async def timezone_update(tg_id, new_timezone):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id==tg_id).values(timezone=new_timezone))

        await session.commit()




async def get_title():
    pass