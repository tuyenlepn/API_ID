import sqlite3

#lay hinh anh
def get_images(query):
    connect = sqlite3.connect("data/database_idcard.db")
    data = connect.execute(query).fetchall()
    connect.close()

    return data

if __name__ == "__main__":
    get_images("SELECT * FROM hinh_anh")