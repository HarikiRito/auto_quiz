from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS

from api.seach import google_search_get

app = FlaskAPI(__name__)
CORS(app)

notes = {
    0: 'do the shopping',
    1: 'build the codez',
    2: 'paint the door',
}


def note_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        'text': notes[key]
    }


@app.route("/search", methods=['GET', 'POST'])
def notes_list():
    """
    List or create notes.
    """
    if request.method == 'POST':
        q: str = request.data.get('q')
        a: str = request.data.get('a')
        result = google_search_get(q, a)
        return {
            'count': result,
            'count_appear': 'c'
        }

    # request.method == 'GET'
    return {'count': 'b', 'count_appear': 'c'}


@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail(key):
    """
    Retrieve, update or delete note instances.
    """
    if request.method == 'PUT':
        note = str(request.data.get('text', ''))
        notes[key] = note
        return note_repr(key)

    elif request.method == 'DELETE':
        notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in notes:
        raise exceptions.NotFound()
    return note_repr(key)


if __name__ == "__main__":
    app.run(port=8888, debug=True, passthrough_errors=True)
