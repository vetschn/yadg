import pytest
from tests.utils import (
    datagram_from_input,
    standard_datagram_test,
    pars_datagram_test,
    datadir,
)


@pytest.mark.parametrize(
    "input, ts",
    [
        (
            {  # ts0 - rtf parser, supplied date
                "case": "Cp_100mA_1mindelay.rtf",
                "parameters": {"date": "2021-09-17"},
            },
            {
                "nsteps": 1,
                "step": 0,
                "nrows": 110,
                "point": 0,
                "pars": {"Temp": {"sigma": 0.1, "value": 27.4, "unit": "Deg C"}},
            },
        ),
        (
            {  # ts1 - default sep parser, date from fn
                "case": "20211011_DryCal_out.csv"
            },
            {
                "nsteps": 1,
                "step": 0,
                "nrows": 29,
                "point": 0,
                "pars": {"Temp": {"sigma": 0.1, "value": 24.3, "unit": "Deg C"}},
            },
        ),
        (
            {  # ts2 - default sep parser, date from fn, sigma from length
                "case": "2021-10-11_DryCal_out.txt",
                "parameters": {},
            },
            {
                "nsteps": 1,
                "step": 0,
                "nrows": 29,
                "point": 28,
                "pars": {"Pressure": {"sigma": 0.001, "value": 971.0, "unit": "mBar"}},
            },
        ),
        (
            {  # ts3 - default sep parser, date from fn, calfile parser
                "case": "2021-10-11_DryCal_out.txt",
                "parameters": {"calfile": "drycal.json"},
            },
            {
                "nsteps": 1,
                "step": 0,
                "nrows": 29,
                "point": 28,
                "pars": {
                    "T": {"sigma": 0.1, "value": 299.25, "unit": "K", "raw": False},
                    "p": {"sigma": 100, "value": 97100.0, "unit": "Pa", "raw": False},
                },
            },
        ),
    ],
)
def test_datagram_from_drycal(input, ts, datadir):
    ret = datagram_from_input(input, "drycal", datadir)
    standard_datagram_test(ret, ts)
    pars_datagram_test(ret, ts)