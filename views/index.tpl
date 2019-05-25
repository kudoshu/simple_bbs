<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Sample</title>
        <link href="/css/main.css" media="screen" rel="stylesheet" type="text/css">
    </head>
    <body>
        <div class="container">
            <h1>Simple BBS</h1>
            <div class="submit">
                <form method="post" id="ex-form" arction="/" enctype="multipart/form-data">
                    <div class="form-text">
                        <textarea rows="10" cols="30" name="ex_text" id="ex_text"></textarea>
                    </div>
                    <div class="form-file">
                        <input type="file" name="file">
                    </div>
                    <div class="form-submit">
                        <input type="submit" name="submit" value="submit">
                    </div>
                </form>
            </div>

            %for post in posts:
            <div class="post">
                <div class="post-text">
                {{post[1]}}
                </div>
                <div clss="post-image">
                    <img src="/uploads/{{post[2]}}" alt="{{post[2]}}" class="ex-image">
                </div>
                <div class="tools">
                    <span class="add-star" data-post-id="{{post[0]}}">
                        {{post[3]}}
                    </span>
                </div>
            </div>
            %end
        </div>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="/js/main.js"></script>
    </body>
</html>
