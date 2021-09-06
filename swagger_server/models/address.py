# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Address(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, street_number: str=None, street_name1: str=None, street_name2: str=None, city_name: str=None, region_name: str=None, postal_code: str=None, country_name: str=None):  # noqa: E501
        """Address - a model defined in Swagger

        :param street_number: The street_number of this Address.  # noqa: E501
        :type street_number: str
        :param street_name1: The street_name1 of this Address.  # noqa: E501
        :type street_name1: str
        :param street_name2: The street_name2 of this Address.  # noqa: E501
        :type street_name2: str
        :param city_name: The city_name of this Address.  # noqa: E501
        :type city_name: str
        :param region_name: The region_name of this Address.  # noqa: E501
        :type region_name: str
        :param postal_code: The postal_code of this Address.  # noqa: E501
        :type postal_code: str
        :param country_name: The country_name of this Address.  # noqa: E501
        :type country_name: str
        """
        self.swagger_types = {
            'street_number': str,
            'street_name1': str,
            'street_name2': str,
            'city_name': str,
            'region_name': str,
            'postal_code': str,
            'country_name': str
        }

        self.attribute_map = {
            'street_number': 'streetNumber',
            'street_name1': 'streetName1',
            'street_name2': 'streetName2',
            'city_name': 'cityName',
            'region_name': 'regionName',
            'postal_code': 'postalCode',
            'country_name': 'countryName'
        }
        self._street_number = street_number
        self._street_name1 = street_name1
        self._street_name2 = street_name2
        self._city_name = city_name
        self._region_name = region_name
        self._postal_code = postal_code
        self._country_name = country_name

    @classmethod
    def from_dict(cls, dikt) -> 'Address':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Address of this Address.  # noqa: E501
        :rtype: Address
        """
        return util.deserialize_model(dikt, cls)

    @property
    def street_number(self) -> str:
        """Gets the street_number of this Address.


        :return: The street_number of this Address.
        :rtype: str
        """
        return self._street_number

    @street_number.setter
    def street_number(self, street_number: str):
        """Sets the street_number of this Address.


        :param street_number: The street_number of this Address.
        :type street_number: str
        """
        if street_number is None:
            raise ValueError("Invalid value for `street_number`, must not be `None`")  # noqa: E501

        self._street_number = street_number

    @property
    def street_name1(self) -> str:
        """Gets the street_name1 of this Address.


        :return: The street_name1 of this Address.
        :rtype: str
        """
        return self._street_name1

    @street_name1.setter
    def street_name1(self, street_name1: str):
        """Sets the street_name1 of this Address.


        :param street_name1: The street_name1 of this Address.
        :type street_name1: str
        """
        if street_name1 is None:
            raise ValueError("Invalid value for `street_name1`, must not be `None`")  # noqa: E501

        self._street_name1 = street_name1

    @property
    def street_name2(self) -> str:
        """Gets the street_name2 of this Address.


        :return: The street_name2 of this Address.
        :rtype: str
        """
        return self._street_name2

    @street_name2.setter
    def street_name2(self, street_name2: str):
        """Sets the street_name2 of this Address.


        :param street_name2: The street_name2 of this Address.
        :type street_name2: str
        """
        if street_name2 is None:
            raise ValueError("Invalid value for `street_name2`, must not be `None`")  # noqa: E501

        self._street_name2 = street_name2

    @property
    def city_name(self) -> str:
        """Gets the city_name of this Address.


        :return: The city_name of this Address.
        :rtype: str
        """
        return self._city_name

    @city_name.setter
    def city_name(self, city_name: str):
        """Sets the city_name of this Address.


        :param city_name: The city_name of this Address.
        :type city_name: str
        """
        if city_name is None:
            raise ValueError("Invalid value for `city_name`, must not be `None`")  # noqa: E501

        self._city_name = city_name

    @property
    def region_name(self) -> str:
        """Gets the region_name of this Address.


        :return: The region_name of this Address.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name: str):
        """Sets the region_name of this Address.


        :param region_name: The region_name of this Address.
        :type region_name: str
        """
        if region_name is None:
            raise ValueError("Invalid value for `region_name`, must not be `None`")  # noqa: E501

        self._region_name = region_name

    @property
    def postal_code(self) -> str:
        """Gets the postal_code of this Address.


        :return: The postal_code of this Address.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code: str):
        """Sets the postal_code of this Address.


        :param postal_code: The postal_code of this Address.
        :type postal_code: str
        """
        if postal_code is None:
            raise ValueError("Invalid value for `postal_code`, must not be `None`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def country_name(self) -> str:
        """Gets the country_name of this Address.


        :return: The country_name of this Address.
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name: str):
        """Sets the country_name of this Address.


        :param country_name: The country_name of this Address.
        :type country_name: str
        """

        self._country_name = country_name