"""
MIT License

Copyright (c) 2017 Jayden Bailey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import asyncio

from .endpoint import Endpoint
from .request import Request
from .objects import Limits, Match, Player, Rank, God
from .language import Language


class Client:
    """Class for handling connections and requests to Hi Rez Studios' APIs

    Parameters
    ----------
    dev_id : str
        Used for authentication. This is the developer ID that you
        receive from Hi-Rez Studios.
    auth_key : str
        Used for authentication. This is the authentication key that you
        receive from Hi-Rez Studios.
    loop : [optional] event loop
        The event used for async ops. If this is the default (None),
        the bot will use asyncio's default event loop.
    default_endpoint : [optional] Endpoint
        The endpoint that will be used by default for outgoing requests.
        You can use different endpoints per request without changing this.
        Otherwise, this will be used. It defaults to Endpoint.smitepc.
    default_language : [optional] Language
        The language that will be used by default when making requests.
        You can use different languages per request without changing this.
        Otherwise, this will be used. It defaults to Language.english.

    """
    def __init__(self, dev_id, auth_key, *, loop=None, default_endpoint=None, default_language=None):
        self.dev_id = str(dev_id)
        self.auth_key = str(auth_key)
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.default_endpoint = str(Endpoint.smitepc) if default_endpoint is None else str(default_endpoint)
        self.default_language = int(Language.english) if default_language is None else int(default_language)

        self.request = Request(self)

    async def ping(self, *, endpoint: Endpoint = None):
        """Pings the API in order to establish connectivity

        Parameters
        ----------
        endpoint : [optional] Endpoint
            The endpoint to make the request with. If not specified,
            Client.default_endpoint is used.

        Returns
        -------
        boolean equal to True

        Raises
        ------
        ConnectionRefusedError
            The request failed

        """
        endpoint = self.default_endpoint if endpoint is None else str(endpoint)
        res = await self.request.make_request(endpoint, 'ping', no_auth=True)
        return True if 'successful' in res else None

    async def get_data_used(self, *, endpoint: Endpoint = None):
        """Gets the data limits for the developer.

        Parameters
        ----------
        endpoint : [optional] Endpoint
            The endpoint to make the request with. If not specified,
            Client.default_endpoint is used.

        Returns
        -------
        Limit object
            The developer limits.

        """
        endpoint = self.default_endpoint if endpoint is None else str(endpoint)
        res = await self.request.make_request(endpoint, 'getdataused')
        obj = Limits(**res[0])  # res should be a list, so we want the first element
        return obj

    async def get_esports_details(self, *, endpoint: Endpoint = None):
        """Returns the matchup information for each matchup for the current eSports Pro League season.

        Parameters
        ----------
        endpoint : [optional] Endpoint
            The endpoint to make the request with. If not specified,
            Client.default_endpoint is used.

        Returns
        -------
        set of Match objects
            The matches in the current season.

        """
        endpoint = self.default_endpoint if endpoint is None else str(endpoint)
        res = await self.request.make_request(endpoint, 'getesportsproleaguedetails')
        matches = []
        for i in res:
            obj = Match(**i)
            matches.append(obj)
        return set(matches)

    async def get_friends(self, username, *, endpoint: Endpoint = None):
        """Returns information about a user's friends.

        Parameters
        ----------
        username : str
            The username of the player to get information about
        endpoint : [optional] Endpoint
            The endpoint to make the request with. If not specified,
            Client.default_endpoint is used.

        Returns
        -------
        list of Player objects or None
            Represents the given user's friends. Will return None if
            the user's privacy settings do not allow, or the
            user given is invalid.

        """
        endpoint = self.default_endpoint if endpoint is None else str(endpoint)
        res = await self.request.make_request(endpoint, 'getfriends', params=[username])
        if not res:
            res = None  # invalid user or privacy settings active
        else:
            players = []
            for i in res:
                if i['account_id'] == '0':  # privacy settings active, skip
                    continue
                obj = Player(**i)
                players.append(obj)
            res = players if players else None
        return res

    async def get_ranks(self, username, *, endpoint: Endpoint = None):
        """Returns information about a user's god or champion ranks,
        depending on the endpoint that is being called (Smite/Paladins)

        Parameters
        ----------
        username : str
            The username of the player to get information about
        endpoint : [optional] Endpoint
            The endpoint to make the request with. If not specified,
            Client.default_endpoint is used.

        Returns
        -------
        list of Rank objects or None
            Represents the given user's ranks. Will return None if
            the user's privacy settings do not allow, or the
            user given is invalid.

        """
        endpoint = self.default_endpoint if endpoint is None else str(endpoint)
        if endpoint == Endpoint.paladinspc.value:
            res = await self.request.make_request(endpoint, 'getchampionranks', params=[username])
        else:
            res = await self.request.make_request(endpoint, 'getgodranks', params=[username])
        if not res:
            res = None  # invalid user or privacy settings active
        else:
            ranks = []
            for i in res:
                if 'god' not in i:  # must be paladins
                    i['god'] = i['champion']
                    i['god_id'] = i['champion_id']
                obj = Rank(**i)
                ranks.append(obj)
            res = ranks if ranks else None
        return res

    async def get_characters(self, language: Language = None, *, endpoint: Endpoint = None):
        """Returns information about the characters in the game.
        For Smite, this is the gods in the game. For Paladins, the champions.

        Parameters
        ----------
        langauge : [optional] Language
            The language code to get the information with. If not specified,
            Client.default_language is used.
        endpoint : [optional] Endpoint
            The endpoint to make the request with. If not specified,
            Client.default_endpoint is used.

        Returns
        -------
        list of God or Champion objects
            Returns the characters in the game. God objects will be reteurned
            if the game is Smite, else Champion objects.

        """
        endpoint = self.default_endpoint if endpoint is None else str(endpoint)
        language = str(self.default_language if language is None else int(language))
        if endpoint == Endpoint.paladinspc.value:
            res = await self.request.make_request(endpoint, 'getchampions', params=[language])
            characters = None
        else:
            res = await self.request.make_request(endpoint, 'getgods', params=[language])
            characters = []
            for i in res:
                obj = God(**i)
                characters.append(obj)
        return characters
