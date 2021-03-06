"""
This module represents directory abstraction in Unicheck.
"""

from .response import UnicheckMainException
from .response import UnicheckDirectoryResponse


class Directory(object):
    """ Representation of directory abstract in Unicheck """

    def __init__(self, oauth_session, server):
        self.oauth_session = oauth_session
        self.server = server

    def create(self, name, parent_id=0):
        """
        Create directory in library

        :param name: Directory name (max length 64), string
        :param parent_id: Parent ID for new directory, 0 is for root directory (default)
        :return: UnicheckDirectoryResponse
        """
        resp = self.oauth_session.post(self.server + '/api/v2/directory/create', data={'name': name, 'parent_id': parent_id})
        return UnicheckDirectoryResponse(resp)

    def delete(self, id):
        """
        Delete directory in library

        :param id: directory id for deleting,
                   You can not delete root directory with ID 0
        :return: UnicheckDirectoryResponse
        """
        resp = self.oauth_session.post(self.server + '/api/v2/directory/delete', data={'id': id})
        return UnicheckDirectoryResponse(resp)

    def get(self, id, list=False):
        """
        Get directory info from library

        :param id: directory id in library, int
        :param list: Include list in response (default: 0), Allowed values: boolean
        :return: UnicheckDirectoryResponse
        """
        resp = self.oauth_session.get(self.server + '/api/v2/directory/get?id=%s?list=%s' % (id, int(list)))
        return UnicheckDirectoryResponse(resp)
