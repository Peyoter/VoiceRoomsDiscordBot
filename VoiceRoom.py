from sqlalchemy import *


class VoiceRoomModel:

    def __init__(self):
        self.table_name = 'voice_rooms'
        self.engine = create_engine('sqlite:///bot.db')
        self.connect = self.engine.connect()
        self.meta = MetaData()
        self.table = Table(self.table_name, self.meta,
                           Column('id', Integer, primary_key=True),
                           Column('discord_user_id', Integer, nullable=False),
                           Column('discord_guild_id', Integer, nullable=False),
                           Column('discord_room_id', Integer, nullable=False, unique=True),
                           )

    def createTable(self):
        if self.engine.dialect.has_table(self.connect, self.table_name):
            self.table.drop(self.engine)

        self.table.create(self.engine)
        return

    def insert(self, discord_user_id, discord_guild_id, discord_room_id):
        query = insert(self.table).values(
            discord_user_id=discord_user_id,
            discord_guild_id=discord_guild_id,
            discord_room_id=discord_room_id)
        self.connect.execute(query)
        return

    def getUserRoomsByUserId(self, userId):
        query = select(self.table).where(self.table.columns.discord_user_id == userId)
        return self.connect.execute(query).all()

    def removeRoom(self, discord_guild_id, discord_room_id):
        query = delete(self.table).where(self.table.columns.discord_room_id == discord_room_id).where(
            self.table.columns.discord_guild_id == discord_guild_id)
        return self.connect.execute(query)


roomObj = VoiceRoomModel()
