import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USERS_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_ANSWERS_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_FORM_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERAL_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_FAVORITE_ANIME_TABLE_QUERY)

        try:
            self.connection.execute(sql_queries.ALTER_USER_TABLE)
            self.connection.execute(sql_queries.ALTER_USER_V2_TABLE)
        except sqlite3.OperationalError:
            pass


    def sql_insert_users(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name, None, None)
        )
        self.connection.commit()


    def sql_insert_answer(self, username, users_phone):
        self.cursor.execute(
            sql_queries.INSERT_ANSWER_QUERY,
            (None, username, users_phone)
        )
        self.connection.commit()

    def sql_delete_answer(self, username):
        self.cursor.execute(
            sql_queries.DELETE_ANSWER_QUERY,(username,)
        )
        self.connection.commit()

    def sql_insert_ban_user(self, telegram_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER_QUERY,
            (None, telegram_id, 1)
        )
        self.connection.commit()

    def sql_select_ban_user(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "count": row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY,
            (telegram_id,)
        ).fetchone()

    def sql_update_ban_user_count(self, telegram_id):
        self.cursor.execute(sql_queries.UPDATE_BAN_USER_COUNT_QUERY,(telegram_id,))
        self.connection.commit()

    def sql_insert_user_form_register(self, telegram_id, nickname, bio, geo, gender, age, photo):
        self.cursor.execute(
            sql_queries.INSERT_USER_FORM_QUERY,
            (None, telegram_id, nickname, bio, geo, gender, age, photo,)
        )
        self.connection.commit()

    def sql_select_all_users(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4]
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_USERS_QUERY).fetchall()

    def sql_select_all_ban_users(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "count": row[2]
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_BAN_USERS_QUERY).fetchall()

    def sql_select_user_form(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "geo": row[4],
            "gender": row[5],
            "age": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_QUERY,
            (telegram_id,)
        ).fetchone()

    def sql_select_all_user_form(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "geo": row[4],
            "gender": row[5],
            "age": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_USER_FORM_QUERY
        ).fetchall()

    def sql_insert_like(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker,)
        )
        self.connection.commit()

    def sql_select_filter_user_form(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "geo": row[4],
            "gender": row[5],
            "age": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.FILTER_LEFT_JOIN_USER_FORM_LIKE_QUERY,
            (tg_id, tg_id,)
        ).fetchall()

    def sql_select_user(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4]
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY).fetchone()

    def sql_delete_user_form(self, telegram_id):
        self.cursor.execute(
            sql_queries.DELETE_USER_FORM_QUERY,(telegram_id,)
        )
        self.connection.commit()

    def sql_select_balance_count_referral(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "balance": row[0],
            "count": row[1],
        }
        return self.cursor.execute(
            sql_queries.DOUBLE_SELECT_REFERRAL_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_update_reference_link(self, link, owner):
        self.cursor.execute(
            sql_queries.UPDATE_REFERENCE_LINK_QUERY,
            (link, owner,)
        )
        self.connection.commit()

    def sql_select_users_link(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "link": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_LINK_QUERY,
            (telegram_id,)
        ).fetchone()

    def sql_select_user_by_link(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            "tg_id": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchone()

    def sql_update_balance(self, tg_id):
        print(tg_id)
        self.cursor.execute(
            sql_queries.UPDATE_USER_BALANCE_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def sql_insert_referral(self, owner, referral, first_name):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_QUERY,
            (None, owner, referral, first_name)
        )
        self.connection.commit()

    def sql_select_referals_by_owner_user(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "first_name": row[0]
        }
        return self.cursor.execute(
            sql_queries.SELECT_REFERALS_BY_OWNER_USER,
            (telegram_id,)
        ).fetchall()

    def sql_insert_favorite_anime(self, telegram_id, first_name, name_anime):
        self.cursor.execute(
            sql_queries.INSERT_FAVORITE_ANIME_QUERY,
            (None, telegram_id, first_name, name_anime)
        )
        self.connection.commit()