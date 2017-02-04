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


class HrpObject:
    """Represents a generic HiRezPy object

    Attributes
    ----------
    message : str or None
        The message returned from the API request
    """
    def __init__(self, **kwargs):
        self.message = kwargs.get('ret_msg', None)


class Limits(HrpObject):
    """Represents developer usage limits.

    You should not make these manually.

    Attributes
    ----------
    total_requests : int
        The total requests that have been made to the API today
    session_cap : int
        The total amount of sessions permitted today
    active_sessions : int
        The total amount of active sessions
    request_limit : int
        The total amount of requests permitted today
    total_sessions : int
        The total sessions that have been created today
    concurrent_sessions : int
        The amount of concurrent sessions permitted today
    session_time_limit : int
        The amount of time sessions last for, in minutes

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total_requests = kwargs.get('Total_Requests_Today')
        self.session_cap = kwargs.get('Session_Cap')
        self.active_sessions = kwargs.get('Active_Sessions')
        self.request_limit = kwargs.get('Request_Limit_Daily')
        self.total_sessions = kwargs.get('Total_Sessions_Today')
        self.concurrent_sessions = kwargs.get('Concurrent_Sessions')
        self.session_time_limit = kwargs.get('Session_Time_Limit')

    def sessions_left(self):
        """Returns the amount of sessions left that can be created today"""
        rem = self.session_cap - self.total_sessions
        if rem < 0:
            rem = 0
        return rem

    def requests_left(self):
        """Returns the amount of requests left that can be made today"""
        rem = self.request_limit - self.total_requests
        if rem < 0:
            rem = 0
        return rem
