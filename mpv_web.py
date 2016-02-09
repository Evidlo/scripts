from bottle import route, run, get, post, request
import subprocess

from bottle import static_file

@get('/')
@post('/')
def root():
    print request.forms.get('a')
    with open('/tmp/mpv','w',0) as mpv:
        if request.forms.get('a') == '||':
            mpv.write('pause\n')
        if request.forms.get('a') == 'next':
            mpv.write('playlist_next\n')
        if request.forms.get('a') == 'prev':
            mpv.write('playlist_prev\n')
        if request.forms.get('a') == 'stop':
            mpv.write('stop\n')

    return '''
    <!DOCTYPE html>
    <html>
    <body>
    <form action="/" method="post">
    <input name="a" type="submit" value="prev">
    <input name="a" type="submit" value="||">
    <input name="a" type="submit" value="next">
    <br>
    <input name="a" type="submit" value="stop">
    </form>
    </body>
    </html>
   '''



run(host='0.0.0.0',port=80)
