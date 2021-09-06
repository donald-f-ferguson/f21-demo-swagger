# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.links import Links  # noqa: F401,E501
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, email: str=None, name_last: str=None, name_first: str=None, created_data: datetime=None, links: Links=None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: str
        :param email: The email of this User.  # noqa: E501
        :type email: str
        :param name_last: The name_last of this User.  # noqa: E501
        :type name_last: str
        :param name_first: The name_first of this User.  # noqa: E501
        :type name_first: str
        :param created_data: The created_data of this User.  # noqa: E501
        :type created_data: datetime
        :param links: The links of this User.  # noqa: E501
        :type links: Links
        """
        self.swagger_types = {
            'id': str,
            'email': str,
            'name_last': str,
            'name_first': str,
            'created_data': datetime,
            'links': Links
        }

        self.attribute_map = {
            'id': 'id',
            'email': 'email',
            'name_last': 'nameLast',
            'name_first': 'nameFirst',
            'created_data': 'createdData',
            'links': 'links'
        }
        self._id = id
        self._email = email
        self._name_last = name_last
        self._name_first = name_first
        self._created_data = created_data
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email(self) -> str:
        """Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this User.


        :param email: The email of this User.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def name_last(self) -> str:
        """Gets the name_last of this User.


        :return: The name_last of this User.
        :rtype: str
        """
        return self._name_last

    @name_last.setter
    def name_last(self, name_last: str):
        """Sets the name_last of this User.


        :param name_last: The name_last of this User.
        :type name_last: str
        """
        if name_last is None:
            raise ValueError("Invalid value for `name_last`, must not be `None`")  # noqa: E501

        self._name_last = name_last

    @property
    def name_first(self) -> str:
        """Gets the name_first of this User.


        :return: The name_first of this User.
        :rtype: str
        """
        return self._name_first

    @name_first.setter
    def name_first(self, name_first: str):
        """Sets the name_first of this User.


        :param name_first: The name_first of this User.
        :type name_first: str
        """
        if name_first is None:
            raise ValueError("Invalid value for `name_first`, must not be `None`")  # noqa: E501

        self._name_first = name_first

    @property
    def created_data(self) -> datetime:
        """Gets the created_data of this User.


        :return: The created_data of this User.
        :rtype: datetime
        """
        return self._created_data

    @created_data.setter
    def created_data(self, created_data: datetime):
        """Sets the created_data of this User.


        :param created_data: The created_data of this User.
        :type created_data: datetime
        """

        self._created_data = created_data

    @property
    def links(self) -> Links:
        """Gets the links of this User.


        :return: The links of this User.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links: Links):
        """Sets the links of this User.


        :param links: The links of this User.
        :type links: Links
        """

        self._links = links
