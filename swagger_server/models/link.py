# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Link(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, rel: str=None, href: str=None):  # noqa: E501
        """Link - a model defined in Swagger

        :param rel: The rel of this Link.  # noqa: E501
        :type rel: str
        :param href: The href of this Link.  # noqa: E501
        :type href: str
        """
        self.swagger_types = {
            'rel': str,
            'href': str
        }

        self.attribute_map = {
            'rel': 'rel',
            'href': 'href'
        }
        self._rel = rel
        self._href = href

    @classmethod
    def from_dict(cls, dikt) -> 'Link':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Link of this Link.  # noqa: E501
        :rtype: Link
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rel(self) -> str:
        """Gets the rel of this Link.


        :return: The rel of this Link.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel: str):
        """Sets the rel of this Link.


        :param rel: The rel of this Link.
        :type rel: str
        """
        if rel is None:
            raise ValueError("Invalid value for `rel`, must not be `None`")  # noqa: E501

        self._rel = rel

    @property
    def href(self) -> str:
        """Gets the href of this Link.


        :return: The href of this Link.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href: str):
        """Sets the href of this Link.


        :param href: The href of this Link.
        :type href: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href
