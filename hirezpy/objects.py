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
from datetime import datetime


class HrpObject:
    """Represents a generic HiRezPy object

    Attributes
    ----------
    ret_msg : str or None
        The message returned from the API request
    as_json: dict or list
        The request as JSON, if you prefer

    """
    def __init__(self, **kwargs):
        self.ret_msg = kwargs.get('ret_msg', None)
        self.as_json = kwargs


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

    @property
    def sessions_left(self):
        """Returns the amount of sessions left that can be created today as int"""
        rem = self.session_cap - self.total_sessions
        if rem < 0:
            rem = 0
        return rem

    @property
    def requests_left(self):
        """Returns the amount of requests left that can be made today as int"""
        rem = self.request_limit - self.total_requests
        if rem < 0:
            rem = 0
        return rem


class Match(HrpObject):
    """Represents an eSports match.

    You should not make these manually.

    Attributes
    ----------
    id : int
        The match ID. This is unique, and will always be different to another match.
    number : int
        The match number
    status : str
        The status of the match
    region : str
        The region of the match
    tournament_name : str
        The name of the tournament that the match is involved in
    map_instance_id : int
        The map instance ID
    date : datetime or str
        The date and time of the match. Only returns a str if the date and time can't be parsed
        correctly by datetime.strptime, which should not happen
    away_team_id : int
        The ID of the away team
    away_team_name : str
        The name of the away team
    away_team_tag : str
        The clan tag of the away team
    home_team_id : int
        The ID of the home team
    home_team_name : str
        The name of the home team
    home_team_tag : str
        The clan tag of the home team

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = int(kwargs.get('matchup_id'))
        self.number = int(kwargs.get('match_number'))
        self.status = kwargs.get('match_status')
        self.region = kwargs.get('region')
        self.tournament = kwargs.get('tournament_name')
        self.map_instance_id = int(kwargs.get('map_instance_id'))

        date = kwargs.get('match_date')
        try:
            date = datetime.strptime(date, '%-m/%-d/%Y %-I:%M:%S %p')
        except ValueError:  # couldn't parse date and time
            pass
        self.date = date

        self.away_team_id = int(kwargs.get('away_team_clan_id'))
        self.home_team_id = int(kwargs.get('home_team_clan_id'))
        self.away_team_name = kwargs.get('away_team_name')
        self.home_team_name = kwargs.get('home_team_name')
        self.away_team_tag = kwargs.get('away_team_tagname')
        self.home_team_tag = kwargs.get('home_team_tagname')

    def __str__(self):
        return "<Match {}/{}/{}>".format(self.id, self.home_team_name, self.away_team_name)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id


class Player(HrpObject):
    """Represents a player.

    You should not make these manually.

    Attributes
    ----------
    id : int
        The player's account ID. This is the ID of a player's
        Hi-Rez account
    player_id : int
        The player's ID, based on the game that you are checking
        against
    avatar_url : str
        The player's avatar image URL. Could be an empty string
        if the user is using the default avatar.
    username : str
        The player's username

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = int(kwargs.get('account_id'))
        self.player_id = int(kwargs.get('player_id'))
        self.avatar_url = kwargs.get('avatar_url')
        self.username = kwargs.get('name')

    def __str__(self):
        return "<Player {}>".format(self.id)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id
