# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.sources_for_sid import SourcesForSid
from cohesity_management_sdk.models.principal import Principal
from cohesity_management_sdk.models.user import User
from cohesity_management_sdk.models.new_s_3_secret_access_key import NewS3SecretAccessKey
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException

class PrincipalsController(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(PrincipalsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def list_sources_for_principals(self,
                                    sids=None):
        """Does a GET request to /public/principals/protectionSources.

        From the passed in list principals (specified by SIDs),
        return the list of Protection Sources objects and View names that
        each
        principal has permission to access.

        Args:
            sids (list of string, optional): Specifies a list of security
                identifiers (SIDs) that specify user or group principals.

        Returns:
            list of SourcesForSid: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_sources_for_principals called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for list_sources_for_principals.')
            _url_path = '/public/principals/protectionSources'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'sids': sids
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for list_sources_for_principals.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for list_sources_for_principals.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'list_sources_for_principals')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for list_sources_for_principals.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, SourcesForSid.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def update_sources_for_principals(self,
                                      body):
        """Does a PUT request to /public/principals/protectionSources.

        Specify the security identifier (SID) of the principal to grant
        access
        permissions for.

        Args:
            body (UpdateSourcesForPrincipalsParams): Request to set access
                permissions to Protection Sources and Views for a principal.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_sources_for_principals called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for update_sources_for_principals.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_sources_for_principals.')
            _url_path = '/public/principals/protectionSources'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_sources_for_principals.')
            _headers = {
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_sources_for_principals.')
            _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'update_sources_for_principals')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_sources_for_principals.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def search_principals(self,
                          domain=None,
                          object_class=None,
                          search=None,
                          sids=None,
                          include_computers=None):
        """Does a GET request to /public/principals/searchPrincipals.

        Optionally limit the search results by specifying security identifiers
        (SIDs),
        an object class (user or group) or a substring.
        You can specify SIDs or a substring but not both.

        Args:
            domain (string, optional): Specifies the domain name of the
                principals to search. If specified the principals in that
                domain are searched. Domain could be an Active Directory
                domain joined by the Cluster or any one of the trusted domains
                of the Active Directory domain or the LOCAL domain. If not
                specified, all the domains are searched.
            object_class (ObjectClassSearchPrincipalsEnum, optional):
                Optionally filter by a principal object class such as 'kGroup'
                or 'kUser'. If 'kGroup' is specified, only group principals
                are returned. If 'kUser' is specified, only user principals
                are returned. If not specified, both group and user principals
                are returned. 'kUser' specifies a user object class. 'kGroup'
                specifies a group object class. 'kComputer' specifies a
                computer object class. 'kWellKnownPrincipal' specifies a well
                known principal.
            search (string, optional): Optionally filter by matching a
                substring. Only principals in the with a name or
                sAMAccountName that matches part or all of the specified
                substring are returned. If specified, a 'sids' parameter
                should not be specified.
            sids (list of string, optional): Optionally filter by a list of
                security identifiers (SIDs) found in the specified domain.
                Only principals matching the specified SIDs are returned. If
                specified, a 'search' parameter should not be specified.
            include_computers (bool, optional): Specifies if Computer/GMSA
                accounts need to be included in this search.

        Returns:
            list of Principal: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('search_principals called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for search_principals.')
            _url_path = '/public/principals/searchPrincipals'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'domain': domain,
                'objectClass': object_class,
                'search': search,
                'sids': sids,
                'includeComputers': include_computers
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for search_principals.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for search_principals.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'search_principals')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for search_principals.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, Principal.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_session_user(self):
        """Does a GET request to /public/sessionUser.

        Get the information of the logged in user.

        Returns:
            User: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_session_user called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_session_user.')
            _url_path = '/public/sessionUser'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_session_user.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_session_user.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_session_user')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_session_user.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, User.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def delete_users(self,
                     body=None):
        """Does a DELETE request to /public/users.

        Only users from the same domain can be deleted by a single request.
        If the Cohesity user was created for an Active Directory user, the
        referenced
        principal user on the Active Directory domain is NOT deleted.
        Only the user on the Cohesity Cluster is deleted.
        Returns Success if the specified users are deleted.

        Args:
            body (UserDeleteParameters, optional): Request to delete one or
                more users on the Cohesity Cluster.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_users called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_users.')
            _url_path = '/public/users'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for delete_users.')
            _headers = {
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for delete_users.')
            _request = self.http_client.delete(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'delete_users')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_users.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_users(self,
                  tenant_ids=None,
                  all_under_hierarchy=None,
                  usernames=None,
                  email_addresses=None,
                  domain=None,
                  partial_match=None):
        """Does a GET request to /public/users.

        If no parameters are specified, all users currently on the Cohesity
        Cluster
        are returned. Specifying parameters filters the results that are
        returned.

        Args:
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.
            usernames (list of string, optional): Optionally specify a list of
                usernames to filter by. All users containing username will be
                returned.
            email_addresses (list of string, optional): Optionally specify a
                list of email addresses to filter by.
            domain (string, optional): Optionally specify a domain to filter
                by. If no domain is specified, all users on the Cohesity
                Cluster are searched. If a domain is specified, only users on
                the Cohesity Cluster associated with that domain are
                searched.
            partial_match (bool, optional): Optionally specify whether to
                enable partial match. If set, all users with name containing
                Usernames will be returned. If set to false, only users with
                exact the same name as Usernames will be returned. By default
                this parameter is set to true.

        Returns:
            list of User: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_users called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_users.')
            _url_path = '/public/users'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy,
                'usernames': usernames,
                'emailAddresses': email_addresses,
                'domain': domain,
                'partialMatch': partial_match
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_users.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_users.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_users')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_users.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, User.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_user(self,
                    body=None):
        """Does a POST request to /public/users.

        If an Active Directory domain is specified, a new user is added to
        the
        Cohesity Cluster for the specified Active Directory user principal.
        If the LOCAL domain is specified, a new user is created directly in
        the default LOCAL domain on the Cohesity Cluster.
        Returns the created or added user.

        Args:
            body (UserParameters, optional): Request to add or create a new
                user.

        Returns:
            User: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_user called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_user.')
            _url_path = '/public/users'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_user.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_user.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_user')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_user.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, User.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def update_user(self,
                    body=None):
        """Does a PUT request to /public/users.

        Returns the user that was updated on the Cohesity Cluster.

        Args:
            body (UserParameters, optional): Request to update an existing
                user.

        Returns:
            User: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_user called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for update_user.')
            _url_path = '/public/users'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_user.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_user.')
            _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'update_user')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_user.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, User.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_user_privileges(self):
        """Does a GET request to /public/users/privileges.

        List the privileges of the session user.

        Returns:
            list of string: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_user_privileges called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_user_privileges.')
            _url_path = '/public/users/privileges'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_user_privileges.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_user_privileges.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_user_privileges')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_user_privileges.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_reset_s_3_secret_key(self,
                                    body=None):
        """Does a POST request to /public/users/s3SecretKey.

        Returns the new key that was generated.

        Args:
            body (ResetS3SecretKeyParameters, optional): Request to reset the
                S3 secret access key for the specified Cohesity user.

        Returns:
            NewS3SecretAccessKey: Response from the API. New S3 Secret Access
                Key.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_reset_s_3_secret_key called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_reset_s_3_secret_key.')
            _url_path = '/public/users/s3SecretKey'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_reset_s_3_secret_key.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_reset_s_3_secret_key.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_reset_s_3_secret_key')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_reset_s_3_secret_key.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, NewS3SecretAccessKey.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
