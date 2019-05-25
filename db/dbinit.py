import sqlite3

con = sqlite3.connect('post.db')  # Warning: This file is created in the current directory
con.execute("CREATE TABLE posts (id INTEGER PRIMARY KEY,text TEXT,img_file_name TEXT,star_count INTEGER default 0);")
con.commit()
