import psycopg
from psycopg.rows import dict_row
from passlib.context import CryptContext
import settings as s

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
conn = psycopg.connect(
    f"host={s.DB_HOST} dbname=chore_wheel user=wheel password=wheel port=5432",
    row_factory=dict_row)

conn.autocommit = True
cur = conn.cursor()

#user
def create_user(username, password):
    cur.execute("""
        insert into tuser
            (username, password)
        values
            (%s, %s)""",
        (username, pwd_context.hash(password))
    )

def get_user_with_username(username):
    cur.execute("""
        select
            user_id,
            password
        from
            tuser
        where
            username = %s""",
        (username,))
    return cur.fetchone()
