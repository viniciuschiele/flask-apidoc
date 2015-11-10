from flask import Flask
from flask_apidoc import ApiDoc

app = Flask(__name__)
doc = ApiDoc(app=app)


@app.route('/users', methods=['POST'])
def add_user():
    """
    @api {post} /user Adds a new User
    @apiVersion 1.0.0
    @apiName add_user
    @apiGroup User

    @apiParam {String}      username        The user's username.
    @apiParam {String}      first_name      The first name of the User.
    @apiParam {String}      last_name       the last name of the User.
    @apiParam {Object}      profile         The profile data
    @apiParam {Number}      profile.age     The user's age.
    @apiParam {String}      profile.image   The user's avatar-image.

    @apiSuccess {Number}    id              The new user id.
    """
    return


@app.route('/users/<id>')
def get_user(id):
    """
    @api {get} /users/:id Gets an user
    @apiVersion 1.0.0
    @apiName get_user
    @apiGroup User

    @apiDescription Gets an user for the given id.

    @apiExample Example usage:
    curl -i http://localhost/users/4711

    @apiParam {Number}      id              The user's i

    @apiSuccess {Number}    id              The user's id.
    @apiSuccess {String}    username        The user's username.
    @apiSuccess {String}    first_name      The first name of the User.
    @apiSuccess {String}    last_name       The last name of the User.
    @apiSuccess {Object}    profile         The profile data
    @apiSuccess {Number}    profile.age     The user's age.
    @apiSuccess {String}    profile.image   The user's avatar-image.

    @apiError UserNotFound      The <code>id</code> of the User was not found.
    """
    return


@app.route('/users')
def get_users():
    """
    @api {get} /users/:id Gets all the users
    @apiVersion 1.0.0
    @apiName get_users
    @apiGroup User

    @apiExample Example usage:
    curl -i http://localhost/users

    @apiSuccess {Object}    users                 The user data
    @apiSuccess {Number}    users.id              The user's id.
    @apiSuccess {String}    users.username        The user's username.
    @apiSuccess {String}    users.first_name      The first name of the User.
    @apiSuccess {String}    users.last_name       The last name of the User.
    @apiSuccess {Object}    users.profile         The profile data
    @apiSuccess {Number}    users.profile.age     The user's age.
    @apiSuccess {String}    users.profile.image   The user's avatar-image.
    """
    return


@app.route('/users/<id>', methods=['POST'])
def update_user():
    """
    @api {post} /users/:id Updates a user
    @apiVersion 1.0.0
    @apiName update_user
    @apiGroup User

    @apiParam {Number}    id              The user's id
    @apiParam {String}    first_name      The first name of the User.
    @apiParam {String}    last_name       The last name of the User.
    """
    return
