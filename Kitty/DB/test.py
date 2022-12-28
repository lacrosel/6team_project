c.execute("CREATE TABLE IF NOT EXISTS REVIEW '(상가번호 text ,리뷰 text,평점 text)")
c.execute(f"INSERT INTO REVIEW VALUES ({},{},{})")
c.execute(f"SELECT * FROM REVIEW WHERE 상가번호 = '{}'")
c.execute(f"DELETE FROM 테이블명 WHERE 상가번호 = '{}'")
# 데이터 삽입 방법 2
c.execute("INSERT INTO table1(id, name, birthday) \
    VALUES(?,?,?)", \
    (2, 'KIM', '1990-00-00'))