import pymysql


def delete_user(username):
    conn = pymysql.connect(host="192.168.249.129", user="root", password="123456", db="tpshop3.0", port=3306)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tp_users WHERE mobile = %s", username)
    conn.commit()
    cursor.close()
    conn.close()
