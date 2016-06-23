from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover_codes.unwrap_args,
            'python-3': cover_codes.unwrap_args,
            'js-node': cover_codes.js_unwrap_args
        },
        checker=checkers.float_comparison(2),
        function_name={
            "python": "checkio",
            "js": "boxProbability"
        }
    ).on_ready)
