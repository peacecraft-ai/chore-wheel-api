import psycopg
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
conn = psycopg.connect("host=localhost dbname=chore_wheel user=wheel password=wheel port=5432")
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
            user_id
        from
            tuser
        where
            username = %s""",
        (username,))
    return cur.fetchone()
