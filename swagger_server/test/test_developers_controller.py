# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.address import Address  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_add_user(self):
        """Test case for add_user

        creates a user
        """
        body = User()
        response = self.client.open(
            '/donff2/F21User/1.0.0/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_user_address(self):
        """Test case for create_user_address

        Creates the address for the user.
        """
        body = Address()
        response = self.client.open(
            '/donff2/F21User/1.0.0/users/{userId}/address'.format(user_id='user_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        Deletes a user by ID
        """
        response = self.client.open(
            '/donff2/F21User/1.0.0/users/{userId}'.format(user_id='user_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user_address(self):
        """Test case for delete_user_address

        Deletes a user's address
        """
        response = self.client.open(
            '/donff2/F21User/1.0.0/users/{userId}/address'.format(user_id='user_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        Gets a user by ID
        """
        response = self.client.open(
            '/donff2/F21User/1.0.0/users/{userId}'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_address(self):
        """Test case for get_user_address

        Gets a user's address.
        """
        response = self.client.open(
            '/donff2/F21User/1.0.0/users/{userId}/address'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users(self):
        """Test case for get_users

        Resource for creating, reading, updating, etc. users.
        """
        query_string = [('search_string', 'search_string_example')]
        response = self.client.open(
            '/donff2/F21User/1.0.0/users',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        Updates a user
        """
        body = User()
        response = self.client.open(
            '/donff2/F21User/1.0.0/users/{userId}'.format(user_id='user_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user_address(self):
        """Test case for update_user_address

        Updates a user's address
        """
        body = User()
        response = self.client.open(
            '/donff2/F21User/1.0.0/users/{userId}/address'.format(user_id='user_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
