from bottle import route, run, template, request
from pytube import YouTube


@route('/')
def index():
    url = request.query['url']
    try:
        yt = YouTube(url=url)
        extension = 'mp4'
        video = yt.filter(extension)[0]
        return video.url
    except ValueError:
        return "ValueError"
    except AttributeError:
        return "AttributeError"
    except IndexError:
        return "IndexError"
    return "Error"


run(host='0.0.0.0', port=8082)
