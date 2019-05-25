from bottle import Bottle, run, static_file, template, request, redirect
import sqlite3
import uuid

app = Bottle()


@app.route('/')
def index():
    conn = sqlite3.connect('./db/post.db')
    c = conn.cursor()
    c.execute('SELECT * FROM posts ORDER BY id DESC')
    posts = c.fetchall()
    c.close()
    return template('index', posts=posts)


@app.route('/', method='POST')
def index_post():
    file = request.files.get('file')

    if file is not None:
        if "jpeg" in file.content_type:
            ext = ".jpg"
        elif "png" in file.content_type:
            ext = ".png"
        else:
            return "JPEG or PNG only.<br><a href='/'>Back to top</a>"

        filename = str(uuid.uuid4()) + ext
        file.save('./static/uploads/' + filename)

        ex_text = request.forms.get('ex_text')
        conn = sqlite3.connect('./db/post.db')
        c = conn.cursor()
        c.execute('INSERT INTO posts (text, img_file_name) VALUES (?,?)', (ex_text, filename))
        conn.commit()
        c.close()
    else:
        return "File does not exist.<br><a href='/'>Back to top</a>"

    redirect('/')


@app.route('/star')
def add_star():
    post_id = int(request.params.post_id)
    conn = sqlite3.connect('./db/post.db')
    c = conn.cursor()
    c.execute('SELECT star_count FROM posts WHERE id = (?)', (post_id,))
    post = c.fetchone()
    if post is None:
        return "error"
    else:
        new_star_count = post[0] + 1
        c.execute('UPDATE posts SET star_count = (?) WHERE id = (?)', (new_star_count, post_id))
        conn.commit()
        c.close()
        response = {"star_count": new_star_count}
        return response


@app.route('/<filename:path>')
def static_file_(filename):
    return static_file(filename, root='./static')


run(app, host='0.0.0.0', port=8080, reloader=True, debug=True)
