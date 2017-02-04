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
from .objects import Limits


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

    """
    def __init__(self, dev_id, auth_key, *, loop=None, default_endpoint=None):
        self.dev_id = str(dev_id)
        self.auth_key = str(auth_key)
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.default_endpoint = str(Endpoint.smitepc) if default_endpoint is None else str(default_endpoint)

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

        """
        endpoint = self.default_endpoint if endpoint is None else str(endpoint)
        res = await self.request.make_request(endpoint, 'getdataused')
        obj = Limits(**res[0])  # res should be a list, so we want the first element
        return obj
