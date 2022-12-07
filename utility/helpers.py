from api import app, db, abort


@app.errorhandler(404)
def not_found(e):
    response = {'status': 404, 'error': e.description}
    return response, 404


def get_object_or_404(model: db.Model, object_id: int):
    object = model.query.get(object_id)
    if object is None:
        abort(404, description=f"Author with id={object_id} not found")
    return object
