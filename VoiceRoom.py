from sqlalchemy import *


class VoiceRoomModel:

    def __init__(self):
        self.table_name = 'voice_rooms'
        self.engine = create_engine('sqlite:///bot.db')
        self.connect = self.engine.connect()
        self.meta = MetaData()
        self.table = Table(self.table_name, self.meta,
                           Column('id', Integer, primary_key=True),
                           Column('user_discord_id', Integer, nullable=False),
                           Column('room_discord_id', Integer, nullable=False),
                           )

    def createTable(self):
        if self.engine.dialect.has_table(self.connect, self.table_name):
            self.table.drop(self.engine)

        self.table.create(self.engine)
        return

    def insert(self, user_discord_id, room_discord_id):
        query = insert(self.table).values(user_discord_id=user_discord_id, room_discord_id=room_discord_id)
        self.connect.execute(query)
        return

    def getUserRoomsByUserId(self, userId):
        query = select(self.table).where(self.table.columns.user_discord_id == userId)
        return self.connect.execute(query).all()

    def delete(self):
        self.table.delete().where(self.table.columns.user_discord_id == 1)


roomObj = VoiceRoomModel()
