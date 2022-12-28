import sqlite3


# DB 생성 (오토 커밋)
conn = sqlite3.connect("Shop2.db", isolation_level=None)
# 커서 획득
c = conn.cursor()
# # 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
# c.execute("CREATE TABLE IF NOT EXISTS table1 \
#     (id integer PRIMARY KEY, name text, birthday text)")

# 데이터 삽입 방법 1
# c.execute("INSERT INTO table1 \
#     VALUES(1, 'LEE', '1987-00-00')")
# 데이터 삽입 방법 2
c.execute("INSERT INTO table1(id, name, birthday) \
    VALUES(?,?,?)", \
    (2, 'KIM', '1990-00-00'))
test_tuple = (
    (3, 'PARK', '1991-00-00'),
    (4, 'CHOI', '1999-00-00'),
    (5, 'JUNG', '1989-00-00')
)
c.executemany("INSERT INTO table1(id, name, birthday) VALUES(?,?,?)", test_tuple)
c.execute("SELECT * FROM table1")
print(c.fetchone())
print(c.fetchone())
print(c.fetchall())
c.execute("SELECT * FROM table1")
print(c.fetchall())
# 방법 1
c.execute("SELECT * FROM table1")
for row in c.fetchall():
    print(row)
# 방법 2 ################### 이걸로 리스트를 만듬  방법 1은 튜플로 만들어지더라 ~
for row in c.execute("SELECT * FROM table1 ORDER BY id ASC"):
    print(row)

# 방법 1
param1 = (1,)
c.execute('SELECT * FROM table1 WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall())
# 방법 2
param2 = 1
c.execute("SELECT * FROM table1 WHERE id='%s'" % param2)  # %s %d %f
print('param2', c.fetchone())
print('param2', c.fetchall())
# 방법 3
c.execute("SELECT * FROM table1 WHERE id=:Id", {"Id": 1})
print('param3', c.fetchone())
print('param3', c.fetchall())
# 방법 4
param4 = (1, 4)
c.execute('SELECT * FROM table1 WHERE id IN(?,?)', param4)
print('param4', c.fetchall())
# 방법 5
c.execute("SELECT * FROM table1 WHERE id In('%d','%d')" % (1, 4))
print('param5', c.fetchall())
# 방법 6
c.execute("SELECT * FROM table1 WHERE id=:id1 OR id=:id2", {"id1": 1, "id2": 4})
print('param6', c.fetchall())





# 방법 1
c.execute("UPDATE table1 SET name=? WHERE id=?", ('NEW1', 1))
# 방법 2
c.execute("UPDATE table1 SET name=:name WHERE id=:id", {"name": 'NEW2', 'id': 3})
# 방법 3
c.execute("UPDATE table1 SET name='%s' WHERE id='%s'" % ('NEW3', 5))
# 확인
for row in c.execute('SELECT * FROM table1'):
    print(row)
# 방법 1
c.execute("DELETE FROM table1 WHERE id=?", (1,))
# 방법 2
c.execute("DELETE FROM table1 WHERE id=:id", {'id': 3})
# 방법 3
c.execute("DELETE FROM table1 WHERE id='%s'" % 5)
# 확인
for row in c.execute('SELECT * FROM table1'):
    print(row)
# 방법 2
print(conn.execute("DELETE FROM table1").rowcount)
with conn:
    with open('dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Completed.')