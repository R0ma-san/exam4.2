import psycopg2
import config as c


conn = psycopg2.connect(dbname=c.dbname, user=c.user, password=c.password)
cur = conn.cursor()


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(25) UNIQUE, password VARCHAR(20), posts INT)")
        cur.execute(f"INSERT INTO users (name, password) VALUES ('{str(name)}', '{str(password)}')")
     
    def all(self):
        cur.execute("SELECT * FROM users ")
        for i in cur:
            print(i)
        cur.execute(f"SELECT * FROM {self.name}")
        for i in cur:
            print(i)
            
    def get(self, a):
        cur.execute(f"SELECT * FROM users WHERE {str(a)}")
        for i in cur:
            print(i)
    
    def filter(self, a):
        cur.execute(f"SELECT * FROM users ORDER BY {str(a)}")
        for i in cur:
            print(i)

class Post:
    def __init__(self, user, post):
        self.user_name = user.name
        self.post = post
        cur.execute(f"CREATE TABLE IF NOT EXISTS {self.user_name} (id SERIAL PRIMARY KEY, post TEXT)")
        cur.execute(f"INSERT INTO {self.user_name} (post) VALUES ('{post}')")
        cur.execute(f"SELECT COUNT(*) FROM {self.user_name}")
        for i in cur:
            for j in i:
                p = j
        cur.execute(F"UPDATE users SET posts = {p} WHERE  name = '{self.user_name}'")

user1 = User('Ramazan', 1234567890)
p11 = Post(user1, 'grefw  bsfewewvfdafwB BG')
p12 = Post(user1, 'e')
user2 = User('Max', 123131)
user3 = User('Alex', 3223412)
p21 = Post(user2, 'grefw  bsfewewvfdafwB BG')
p22 = Post(user2, 'grefw  bsfewewvfdafwB BG')
p23 = Post(user2, 'grefw  bsfewewvfdafwB BG')
p31 = Post(user3, 'grefw  bsfewewvfdafwB BG')

# user1.all()
# user1.get('id=2')
# user1.filter('name')

cur.close()
conn.close()