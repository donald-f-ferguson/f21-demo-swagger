import connexion
import six

from swagger_server.models.address import Address  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def add_user(body=None):  # noqa: E501
    """creates a user

    Obvious # noqa: E501

    :param body: User to add, except for ID. Application set ID.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_user_address(user_id, body=None):  # noqa: E501
    """Creates the address for the user.

    Obvious # noqa: E501

    :param user_id: ID of the user to update.
    :type user_id: str
    :param body: Address information.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Address.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(user_id):  # noqa: E501
    """Deletes a user by ID

    Deletes a user. # noqa: E501

    :param user_id: ID of the user to delete.
    :type user_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_user_address(user_id):  # noqa: E501
    """Deletes a user&#x27;s address

    Obvious # noqa: E501

    :param user_id: ID of the user to delete.
    :type user_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_user(user_id):  # noqa: E501
    """Gets a user by ID

    Gets a user. # noqa: E501

    :param user_id: ID of the user to get.
    :type user_id: str

    :rtype: User
    """
    return 'do some magic!'


def get_user_address(user_id):  # noqa: E501
    """Gets a user&#x27;s address.

    Obvious # noqa: E501

    :param user_id: ID of the user whose address to get.
    :type user_id: str

    :rtype: List[User]
    """
    return 'do some magic!'


def get_users(search_string=None):  # noqa: E501
    """Resource for creating, reading, updating, etc. users.

    By passing in the appropriate options, you can search for and retrieve information about users.   # noqa: E501

    :param search_string: Optional query string in standard format.
    :type search_string: str

    :rtype: List[User]
    """
    return 'do some magic!'


def update_user(user_id, body=None):  # noqa: E501
    """Updates a user

    Updates a user. Cannot change ID. # noqa: E501

    :param user_id: ID of the user to update.
    :type user_id: str
    :param body: User to update, except for ID. Application set ID.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_user_address(user_id, body=None):  # noqa: E501
    """Updates a user&#x27;s address

    Obvious. # noqa: E501

    :param user_id: ID of the user whose address to update.
    :type user_id: str
    :param body: User to update, except for ID. Application set ID.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
