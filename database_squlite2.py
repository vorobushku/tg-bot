import sqlite3

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS magicball(id INTEGER, name TEXT)"""
    cursor.execute(query)

def mbfun(emp_id, name):
    try:
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        sqlite_mbfun_query = """INSERT INTO magicball
                                  (id, name) VALUES (?, ?)"""
        data_tuple1 = (emp_id, name)
        cursor.execute(sqlite_mbfun_query, data_tuple1)
        db.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if db:
            db.close()
            print("Соединение с SQLite закрыто")

mbfun(1, "Бесспорно")
mbfun(2, "Предрешено")
mbfun(3, "Никаких сомнений")
mbfun(4, "Определённо, да")
mbfun(5, "Можешь быть уверен в этом")
mbfun(6, "Мне кажется — «да»")
mbfun(7, "Вероятнее всего")
mbfun(8, "Хорошие перспективы")
mbfun(9, "Знаки говорят — «да»")
mbfun(10, "Да")
mbfun(11, "Пока не ясно, попробуй снова")
mbfun(12, "Спроси позже")
mbfun(13, "Лучше не рассказывать")
mbfun(14, "Сейчас нельзя предсказать")
mbfun(15, "Сконцентрируйся и спроси опять")
mbfun(16, "Даже не думай")
mbfun(17, "Мой ответ — «нет»")
mbfun(18, "По моим данным — «нет»")
mbfun(19, "Перспективы не очень хорошие")
mbfun(20, "Весьма сомнительно")